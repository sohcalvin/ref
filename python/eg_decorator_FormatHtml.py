
from functools import wraps
def FormatListDict2HtmlTable(key_name_list):
    def wrapper0(function_to_be_decorated):
        @wraps(function_to_be_decorated)
        def wrapper(*args, **kwargs):
            result = function_to_be_decorated(*args, **kwargs)
            f_result = "<table>"
            for h in key_name_list :
                f_result += "<th>{}</th>".format(h)
            for o in result :
                f_result += "<tr>"
                for h in key_name_list:
                    f_result +=  "<td>{}</td>".format(o.get(h))
                f_result += "</tr>"
            f_result += "</table>"
            return f_result
        return wrapper
    return wrapper0


data = [
    { "owner" : "sap",
      "job_count" : 10,
      "cv_count" : 5
      },
    { "owner" : "red",
      "job_count" : 40,
      "cv_count" : 50
      }

]
@FormatListDict2HtmlTable(["owner", "cv_count"])
def getData(d) :
    return d


print(getData(data))


