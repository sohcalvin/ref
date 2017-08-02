import redis

# pool = redis.ConnectionPool(host='localhost', port=6379, db=0)
# r = redis.Redis(connection_pool=pool)
import time
import os
import json

def _getRedisConfigFromCloudfoundryEnv():
    env_config = os.environ.get('VCAP_SERVICES')
    if env_config:
        vcapJsonObj = json.loads(env_config)
        if 'redis' in vcapJsonObj:
            redis_config =vcapJsonObj['redis'][0]['credentials']
            return redis_config
    return None

def getRedis():
    redis_config = _getRedisConfigFromCloudfoundryEnv()
    if redis_config is None:
        return redis.StrictRedis(host='localhost', port=6379, db=0)
    return redis.StrictRedis(host=redis_config["hostname"], port=int(redis_config["port"]), password=redis_config["password"], db=0)


# r = redis.StrictRedis(host='localhost', port=6379, db=0)
r = getRedis()
print("gotten redis")
# with open("small.json", "r") as fp :
with open("disney_model.json", "r") as fp :
    t0 =time.time()
    toload = fp.read()
    t1 = time.time()

    print("Reading time {} secs".format(t1 - t0))

    r.set("disney", toload)
    t2 = time.time()
    print("Saving time {} secs".format(t2-t1) )

    loaded = r.get("disney")
    t3 = time.time()
    print("Loading time {} secs".format(t3 - t2))

