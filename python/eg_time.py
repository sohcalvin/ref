
import datetime, time

def getYYMMDDHHMISS() :
    ts = time.time()
    st = datetime.datetime.fromtimestamp(ts).strftime('%Y%m%d%H%M%S')
    return st

now = datetime.datetime.now()
now_plus_x_min = now + datetime.timedelta(minutes = 20)

print( "Current hour is {0}".format( now_plus_x_min.hour))
print( "Current min  is {0}".format( now_plus_x_min.minute))

