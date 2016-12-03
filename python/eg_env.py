
import os
import re

def printEnv() :
    for index, each in enumerate(sorted(os.environ.items())):
                       print(index, each)


# printEnv()

# print(">>>", os.environ.get('HOMEDRIVE') )

def envEval(env_name) :
    val = os.environ.get(env_name)
    if(val is None) : return None
    match = re.match(r'^\${(.*)}', val)
    if(match is not None) :
        group1 = str(match.group(1))
        val = os.environ.get(group1)
    return val



# print(envEval('CSOH') )

def setEnvDriver() :
    cmd_str = os.environ.get("DRIVER")
    if(cmd_str is None) : return None
    # if(re.match(r'^eval *:',cmd_str, flags=re.IGNORECASE)) :
    #     nval = re.sub(r'^eval *:', '', cmd_str,flags=re.IGNORECASE)
    nval = re.sub(r'webdriver','__import__("selenium.webdriver")', cmd_str) # Manually map allowable modules for safety
    return eval("self.driver = "+ nval,{})

import sys
def printPythonPath() :
    for f in (sys.path) :
        print(f)
# printPythonPath()

# SCRIPT_PATH = os.path.dirname(os.path.realpath(__file__))
# print(os.name)
# print(SCRIPT_PATH)

    #
    # export PYTHONPATH
    # python <<EEE
    # import sys
    # for f in (sys.path):
    #   print(f)
    # EEE

# SHELL script dir
# SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"


def setGetEnv() :
    os.environ['TARGET_HOST_URL'] = 'abcdef'
    print(os.getenv('TARGET_HOST_URL'))
    print(os.environ['TARGET_HOST_URL'])
    print(os.environ.__dict__.get('TARGET_HOST_URL'))  # THIS IS None !!!!!!

setGetEnv()