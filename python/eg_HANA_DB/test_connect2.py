from hana_db import HanaDb
import pprint
import pandas.io.sql as psql

pp = pprint.PrettyPrinter(indent=4)

# Connection settings:
db = HanaDb("10.48.145.36", 31074, "SYSTEM", "Initial1!")



# all_tables =  db.describeSchema("LMS_LF_QM13AQP01T03", tablename_filter=None)
# pp.pprint(all_tables)

# print(all_tables.keys())
# print(all_tables.get("DI_LMS_LEARNING_HISTORY"))
# describeSchema("LMS_LF")

# selectTable("LMS_LF_QM13AQP01T03.DI_LMS_LEARNING_ENTITY", limit=3)
# selectTable("LMS_LF_QM13AQP01T03.DI_LMS_CATALOG", limit= None)
# print(describeTable("LMS_LF_QM13AQP01T03.DI_LMS_CATALOG"))

# selectTable("LMS_LF_QM13AQP01T03.DI_LMS_STUDENT", limit=3)

# selectTable("LMS_LF_QM13AQP01T03.DI_LMS_STUDENT", limit=10)
#
# schema_views = db.describeAllViews(schema_name_filter=".*LM.*")
# for k in schema_views.keys() :
#     print(k)
#     print(">>>", schema_views.get(k))

# pp.pprint(db.describeTable("LMS_LF_QM13AQP01T03.DI_LMS_LEARNING_HISTORY"))

# print(db.describeTable("LMS_LF_QM13AQP01T03.DI_LMS_LEARNING_HISTORY"))


# db.selectTable("LMS_LF_QM13AQP01T03.DI_LMS_LEARNING_PLAN", limit=20)


tables = [
"DI_LMS_LEARNING_PLAN"
,"DI_LMS_LEARNING_HISTORY"
,"DI_LMS_CATALOG"
,"DI_LMS_CATALOG_ITEM"
,"DI_LMS_LEARNING_ENTITY"
,"DI_LMS_P2P_RECOMMENDATIONS"
,"DI_LMS_STUDENT"
,"DI_LMS_STUD_ASSGN_PRFL"
,"DI_LMS_STUD_LRN_ITEM_BOOKMARK"
,"DI_LMS_STUD_RATING"
,"DI_LMS_SUBJECT_AREA"
,"DI_LMS_SUBJ_ENTITY" ]
# tables =["DI_LMS_LEARNING_PLAN"]



for t in tables :
    stable = "LMS_LF_QM13AQP01T03.{}".format(t)
    info = db.describeTable(stable)
    f = open("{}.csv".format(t), "w")
    for c in info.get("column_names") :
        f.write(c + ",")
    f.write("\n")

    db.selectTable(stable, limit=None, proc=lambda r : f.write(r))




