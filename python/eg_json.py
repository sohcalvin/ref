import json
import os
import re

ss = str({"mongodb":[{"name":"CVR_MONGODB_SAP","label":"mongodb","tags":["mongodb","document"],"plan":"v3.0-container","credentials":{"hostname":"10.0.97.129","ports":{"27017/tcp":"33362","28017/tcp":"33363"},"port":"33362","username":"9sreqnqptt0bacyw","password":"xuqtoybxfxqz1zks","dbname":"79fl5gwwergs3soh","uri":"mongodb://9sreqnqptt0bacyw:xuqtoybxfxqz1zks@10.0.97.129:33362/79fl5gwwergs3soh"}}]})
os.environ['VCAP_SERVICES'] = json.dumps(ss)

vs = os.environ['VCAP_SERVICES']

os.environ['AA'] = '${VCAP_SERVICES}'
os.environ['MONGODB_HOST'] = '${VCAP_SERVICES}'

def envEval(env_name) :
    val = os.environ.get(env_name)
    if(val is None) : return None
    match = re.match(r'^\${(.*)}', val)
    if(match is not None) :
        group1 = str(match.group(1))
        val = os.environ.get(group1)
    try :
        val = eval(val)
        return
    except Exception as e :
        pass
    return val

print(eval('"AA"'))


__import__('os')

