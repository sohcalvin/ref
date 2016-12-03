from cvr.util.pdf_transformer import readTextFromPDFFileStream, readHTMLFromPDF

# readTextFromPDFFileStream()

# from os import listdir
#
#
# dir = "c:/tmp/cv/"
# fyles = listdir(dir)
#
# for f in fyles :
#     if(f != 'Luca Fiaschi.pdf') : continue
#     fp = dir + f
#     x = open(fp,'rb')
#     text = readHTMLFromPDF(x)
#     print(text)
#
#
# import os
# os.environ['MONGODB_HOST'] = "ahost"
# os.environ['MONGODB_PORT'] = "123"
# from cvr.database.base_db import BaseDb
# (host, port) = BaseDb.envMongodbHostPort()
# host =   if host is None else var1
# port = port || "345"
# print(host, port)

import os
def envIgnorecase(env_name) :
    val = os.environ.get(env_name)
    if(val is None) :
        keys = os.environ.keys()
        if(keys is not None) :
            env_name_lower = env_name.lower()
            for k in keys :
                if(env_name_lower == k.lower()) :
                    val = os.environ.get(k)
                    if(val is not None) : break

    return val




print(envIgnorecase("homedrive"))
    # val = os.environ.get(env_name)
    # if(val is None) :
    #   http_proxy = os.environ.get('HTTP_PROXY') if (os.environ.get('http_proxy') is None) else os.environ.get('http_proxy')
    #    https_proxy = os.environ.get('HTTPS_PROXY') if (os.environ.get('https_proxy') is None) else os.environ.get('https_proxy')
