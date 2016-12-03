
import re

def removeExtension(filename) :
    a = filename.split(".")
    if(len(a) == 1) : return filename
    return ".".join(a[:-1])
# print(removeExtension("abcdef"))
# print(removeExtension("abcdef gida asdf"))
# print(removeExtension("abcdef.tXtasd"))
# print(removeExtension("abcdef.sdf.sdf"))

def removeExtensionUsingRegex(filename) :
    return re.sub(r'\.(?!.*\.).*$', '', filename)

# print(removeExtensionUsingRegex("apple orange"))
# print(removeExtensionUsingRegex("apple orange.txt"))
# print(removeExtensionUsingRegex("apple orange.txt.pdf"))
# print(removeExtensionUsingRegex("apple orange.txt.doc.pdf"))

def regLookAhead(str):
    return re.sub(r'111(?!.*bbb)', '-', str)

# print(regLookAhead('aaa111xxbbb111ccc') )

def reSubstitute() :
    s = 'abc_def.txt.pDf\ndef.txt'
    n = re.sub(r'\..*$', '', s,flags=re.IGNORECASE|re.MULTILINE)
    print(s)
    print("----------")
    print(n)




def reSubstitueCaptureGroup() :
     content = "APPLE\nCOMMENT THIS\n  COMMENT with space\nORANGE"
     print("Before: \n" , content)
     content = re.sub(r'^(\s*COMM.*)$', r'##\1', content,flags=re.IGNORECASE|re.MULTILINE)
     print("\n----\nAfter: \n" , content)

# reSubstitueCaptureGroup()

# driver = "Chrome ( \"../chromedriver.exe\" ) "
# driver = re.sub(r'\"',"'",driver)
# ss = re.split(r'\s*\(\s*\'|\'\s*\)\s*',driver)
# print(ss)


def cfApi() :
    s = "API endpoint: https://api.cf.sapaws.hana.ondemand.com (API version: 2.59.0)"
    ss = s.split(r' ')
    for f in ss :
        if(f.startswith("https")) :
            domain = re.sub(r'^https:\/\/api.cf.','',f)
            return domain
    return None
cfApi()





