from nameko.rpc import rpc
import time
class HelloWorldService(object):
    name = 'hello'

    @rpc
    def hello(self, secs):
        time.sleep(secs)
        return "Sleep for {} secs!".format(secs)
