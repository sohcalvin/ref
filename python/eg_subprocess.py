import subprocess, os

def runEchoWithPopen( text_output = False) :
    cmd = "echo this is a subprocess"
    p = subprocess.Popen(cmd.split(), stdout=subprocess.PIPE, universal_newlines=text_output)
    p.wait(timeout= 5) # wait for child to complete and set returncode
    ret = p.returncode
    out = p.stdout.read()
    print("runEchoWithPopen : {0}".format(out))
    print("runEchoWithPopen : {0}".format(ret))

# runEchoWithPopen()
# runEchoWithPopen(text_output=True)

def runCommandWithCheckoutput(cmd, text_output = False) :
    output = subprocess.check_output(cmd.split(), universal_newlines=text_output, timeout=1)
    print("runEchoWithCheckoutput : {0}".format(output))

# runCommandWithCheckoutput("echo abcdef", text_output=True)


def runCall(cmd_str) :
    cmd = cmd_str.split()
    subprocess.call(cmd, shell=False)

os.environ['https_proxy'] = 'http://proxy.sin.sap.corp:8080'
runCall("echo abc")
