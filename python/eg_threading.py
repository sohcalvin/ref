import threading
import time

def tp(x) :
    time.sleep(5)
    print("tp says " + str(x))

f = lambda : tp(6)
w = threading.Thread(target=f)
w.setDaemon(False)

print("before start")
w.start()
print("after start")