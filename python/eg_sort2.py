files =[
  "t_FULL_20170101010102",
  "t_DELTA_20170101010102",
  "t_FULL_20170101010101",
  "a_FULL_20170101010102",
  "t_DELETE_20170101010101",
  "t_FULL_20170101010103",
  "b_FULL_20170101010102",
]
import re
def importFileSortKeyFunction(x) :
    if re.match(r'.*FULL', x, flags=re.IGNORECASE) :
      s = "+-+a-{0}".format(x)
    elif re.match(r'.*DELTA', x, flags=re.IGNORECASE) :
      s = "+-+b-{0}".format(x)
    else :
      s = "+-+c-{0}".format(x)
    return s


# sorted_cv_list = sorted(array_of_objects, key=lambda x: x['name'], reverse=True)

sorted_cv_list = sorted(files, key=importFileSort, reverse=False)

for i in sorted_cv_list :
  print(i)


from operator import itemgetter, attrgetter