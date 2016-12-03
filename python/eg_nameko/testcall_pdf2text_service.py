# from flask import Flask, request
# from flasgger import Swagger
from nameko.standalone.rpc import ClusterRpcProxy
import base64

CONFIG = {'AMQP_URI': "amqp://localhost:5672"}

def sendPdfBytesForConversionToText() :
    pdfFile = open("sample.pdf", "rb")
    pdfbytes = pdfFile.read()
    with ClusterRpcProxy(CONFIG) as rpc:
        base64_encoded_bytes = base64.b64encode(pdfbytes)
        base64_encoded_str = base64_encoded_bytes.decode("utf-8")
        result = rpc.pdf2text.convert(base64_encoded_str)
    return result

res = sendPdfBytesForConversionToText()
print(res)