import json

file = "c:/tmp/sap_job_test.json"
fp = open(file,encoding="utf-8", errors="surrogateescape")
x = json.load(fp)
print(x)