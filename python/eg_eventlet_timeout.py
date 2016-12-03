import eventlet
import time




with eventlet.Timeout(1, False):
    while(True) :
        print(112)
        pass

print("fin")