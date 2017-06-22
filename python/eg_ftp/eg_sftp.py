import paramiko
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

import sys
host = 'lssinh009.sin.sap.corp'                    #hard-coded
port = 22

password = "iownu1.123"                #hard-coded
username = "i319984"                #hard-coded

def sftpGet(host, port, username, password, source_dir, destination_dir) :
    transport = paramiko.Transport((host, port))
    transport.connect(username = username, password = password)
    sftp = paramiko.SFTPClient.from_transport(transport)

    try:
        sftp.chdir(source_dir)
    except Exception as e :
        logger.error({ "message" : "Unable to chdir to '{}' in ftp server".format(source_dir)})
        sftp.close()
        transport.close()
        return False

    return True


    remote_list = sftp.listdir("")
    print(remote_list)
    sftp.close()
    transport.close()

    # sftp.get("/home/i319984/scratch/deletem/a.txt","./g.txt")

target_dir = "/home/i319984/scratch/deletemx/"
sftpGet(host, port, username, password, target_dir, "." )




# path = './THETARGETDIRECTORY/' + sys.argv[1]    #hard-coded
# localpath = sys.argv[1]
# sftp.put(localpath, path)

