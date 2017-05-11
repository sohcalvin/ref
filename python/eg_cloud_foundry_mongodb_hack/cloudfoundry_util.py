import os
import json

def _getUrisFromCloudfoundryEnv(list_of_backing_service_types) :
    env_config = os.environ.get('VCAP_SERVICES')
    uris = {}
    if env_config:
        vcapJsonObj = json.loads(env_config)
        for c in list_of_backing_service_types :
            if(c in vcapJsonObj):
                config_list = vcapJsonObj[c]
                for i in config_list :
                    uri = i['credentials']['uri']
                    mongodb_name = i["name"]
                    uris[mongodb_name] = uri
    return uris

def getMongodbUriFromCloudfoundryEnv() :
    return _getUrisFromCloudfoundryEnv([ 'mongodb', 'user-provided'])

def getRabbitMqUriFromCloudfoundryEnv() :
    return _getUrisFromCloudfoundryEnv(['rabbitmq', 'p-rabbitmq'])
