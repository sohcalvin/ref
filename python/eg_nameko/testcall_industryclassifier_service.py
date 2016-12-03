# from flask import Flask, request
# from flasgger import Swagger
from nameko.standalone.rpc import ClusterRpcProxy
import base64

CONFIG = {'AMQP_URI': "amqp://localhost:5672"}

def sendPdfBytesForConversionToText() :
    with ClusterRpcProxy(CONFIG) as rpc:
        result = rpc.industry_classifier.classify("some text")
    return result

res = sendPdfBytesForConversionToText()
print(res)