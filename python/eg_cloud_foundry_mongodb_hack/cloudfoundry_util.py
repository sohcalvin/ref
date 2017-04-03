import os
import json

def getMongodbUriFromCloudfoundryEnv() :
    env_config = os.environ.get('VCAP_SERVICES')
    mongodb_uri = {}
    if env_config:
        vcapJsonObj = json.loads(env_config)

        for c in [ 'mongodb', 'user-provided'] :
            if(c in vcapJsonObj):
                config_list = vcapJsonObj[c]
                for i in config_list :
                    uri = i['credentials']['uri']
                    mongodb_name = i["name"]
                    mongodb_uri[mongodb_name] = uri
                    # mongodb_clients.append(MongoClient(uri).get_default_database())
                break # Only do one
    return mongodb_uri
