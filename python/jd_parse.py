import os
from html.parser import HTMLParser
class MLStripper(HTMLParser):
    def __init__(self):
        self.reset()
        self.strict = False
        self.convert_charrefs= True
        self.fed = []
    def handle_data(self, d):
        self.fed.append(d)
    def get_data(self):
        return ''.join(self.fed)

def strip_tags(html):
    s = MLStripper()
    s.feed(html)
    return s.get_data()


fileDir = 'C:/tmp/jobs/'
for file_name in os.listdir(fileDir):
         with open(os.path.join(fileDir, file_name), errors='ignore') as fin:
             # fileContent=strip_tags(fin.read())
             fileContent = fin.read()
             print(strip_tags(fileContent))
             print("-----------------------------------------<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<{0} end ".format(file_name))
            # for line in fin:



