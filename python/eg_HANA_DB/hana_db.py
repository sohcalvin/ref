import pyhdb
import re

def ResultIterator(cursor, arraysize=10):
    while True:
        results = cursor.fetchmany(arraysize)
        if not results:
            break
        for result in results:
            yield result

class HanaDb(object) :
    def __init__(self, host, port, user, password):
        self._connection = pyhdb.connect(
            host=host,
            port=port,
            user=user,
            password=password
        )

    def _cursor(self):
        return self._connection.cursor()


    def describeSchema(self,schema_name, tablename_filter=None) :
        sql = """ 
        SELECT TABLE_NAME, SCHEMA_NAME || '.' || TABLE_NAME as SCHEMA_TABLE_NAME, COLUMN_NAME, POSITION
        FROM    SYS.COLUMNS
        WHERE SCHEMA_NAME = '{}' 
        ORDER BY TABLE_NAME;
        """.format(schema_name)
        cursor = self._cursor()
        cursor.execute(sql)
        result = cursor.fetchall()
        by_table = {}
        for r in result :
            table_name = r[0]
            schema_table_name = r[1]
            if(tablename_filter is not None and not re.match(tablename_filter, table_name, flags=re.IGNORECASE) ):
                continue
            table_col = r[2]
            table_value = by_table.get(schema_table_name)
            if(table_value is None) :
                by_table[schema_table_name] =  set()
                table_value = by_table[schema_table_name]
            table_value.add(table_col)

        for k in by_table.keys() :
            a_set = by_table.get(k)
            by_table[k] = list(a_set)

        return by_table


    def describeTable(self, table_name) :
        sql= "select count(*) as COUNT from {}".format(table_name)
        cursor = self._cursor()
        cursor.execute(sql)
        result = cursor.fetchall()
        row_count = result[0][0]
        cursor = self._cursor()
        cursor.execute("select * from {} limit 1".format(table_name))
        return {
            "table_name" : table_name,
            "row_count" : row_count,
            "column_names" : [ x[0] for x in cursor.description]
        }

    def selectTable(self, table_name, limit=None, proc=None) :
        sql = "select * from {}".format(table_name)
        if (limit is not None):
            sql += " limit {}".format(limit)
        cursor = self._cursor()
        cursor.execute(sql)
        column_names = []
        for d in cursor.description:
            column_names.append(d[0])
        print(column_names)
        for result in ResultIterator(cursor):
            if(proc ==None) :
                print(result)
            else :
                csv =""
                for c in result :
                    csv += str(c) +","
                csv += "\n"
                proc(csv)

    def query(self, sql,limit=None, proc=None) :
        if (limit is not None):
            sql += " limit {}".format(limit)
        cursor = self._cursor()
        cursor.execute(sql)
        column_names = []
        for d in cursor.description:
            column_names.append(d[0])
        print(column_names)
        for result in ResultIterator(cursor):
            if(proc ==None) :
                print(result)
            else :
                csv =""
                for c in result :
                    csv += c +","
                proc(csv)


    def describeAllViews(self, schema_name_filter= None, table_name_filter=None) :
        sql = """ 
            SELECT SCHEMA_NAME, VIEW_NAME
            FROM  VIEWS 
            ORDER BY SCHEMA_NAME;
            """
        cursor = self._cursor()
        cursor.execute(sql)
        result = cursor.fetchall()
        schema_viewlist = {}
        for r in result:
            schema_name = r[0]
            view_name = r[1]
            # print(r)
            # print(schema_name, "=====", view_name)
            if (schema_name_filter is not None and not re.match(schema_name_filter, schema_name, flags=re.IGNORECASE)):
                continue
            if (table_name_filter is not None and not re.match(table_name_filter, view_name, flags=re.IGNORECASE)):
                continue
            view_set = schema_viewlist.get(schema_name)
            if (view_set is None):
                view_set = set()
                schema_viewlist[schema_name] = view_set
            view_set.add(view_name)
        return schema_viewlist





