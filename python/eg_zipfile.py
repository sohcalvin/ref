import zipfile



with zipfile.ZipFile('t.zip') as myzip:
    with myzip.open('b.txt') as myfile:
        print(myfile.readline().decode("utf-8"))
        print(myfile.readline().decode("utf-8"))
        print(myfile.readline().decode("utf-8"))
