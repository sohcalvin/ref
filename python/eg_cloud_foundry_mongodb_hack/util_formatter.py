def formatListDict2HtmlTable(key_name_list, list_dict):
    style = """
        <style>
            table, th, td { border: 1px solid black; border-collapse: collapse; }
            th, td {   padding: 5px; }
        </style>
    """
    f_result = "{}<table>".format(style)
    for h in key_name_list:
        f_result += "<th>{}</th>".format(h)
    for o in list_dict:
        f_result += "<tr>"
        for h in key_name_list:
            f_result += "<td>{}</td>".format(o.get(h))
        f_result += "</tr>"
    f_result += "</table>"
    return f_result

