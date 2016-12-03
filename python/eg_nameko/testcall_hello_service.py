from flask import Flask, request
# from flasgger import Swagger
from nameko.standalone.rpc import ClusterRpcProxy
from nameko.rpc import RpcProxy
import base64

CONFIG = {'AMQP_URI': "amqp://localhost:5672"}

def callHello() :
    with ClusterRpcProxy(CONFIG) as cluster_rpc:
        hello5_res = cluster_rpc.hello.hello.call_async( 5)
        print("Finished call to hello5")
        hello10_res = cluster_rpc.hello.hello.call_async(10)
        print("Finished call to hello10")
        print("")

        # do work while waiting
        print("Waiting for hello10 to return")
        res10 = hello10_res.result()
        print("Results from hello10 back = ", res10)

        print("")
        print("Waiting for hello5 to return")
        res5 = hello5_res.result()
        print("Results from hello5 back = ", res5)



res = callHello()
