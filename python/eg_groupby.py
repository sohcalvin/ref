from itertools import groupby
from operator import itemgetter


input_data = [
{'dept': '001', 'sku': 'foo', 'transId': 'uniqueId1', 'qty': 100},
{'dept': '001', 'sku': 'bar', 'transId': 'uniqueId2', 'qty': 200},
{'dept': '001', 'sku': 'foo', 'transId': 'uniqueId3', 'qty': 300},
{'dept': '002', 'sku': 'baz', 'transId': 'uniqueId4', 'qty': 400},
{'dept': '002', 'sku': 'baz', 'transId': 'uniqueId5', 'qty': 500},
{'dept': '002', 'sku': 'qux', 'transId': 'uniqueId6', 'qty': 600},
{'dept': '003', 'sku': 'foo', 'transId': 'uniqueId7', 'qty': 700}
]

grouper = itemgetter("dept", "sku")
result = []
for key, grp in groupby(sorted(input_data, key = grouper), grouper):
    print("================")
    g = list(grp)
    print(g)
    len_or_one = max(len(g), 1)
    sum_g = sum(item["qty"] for item in g)
    mean = float(sum_g) /len_or_one
    print(mean)
    print("--")

# from pprint import pprint
# pprint(result)