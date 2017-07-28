import paramiko
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

import sys
# host = 'demo.wftpserver.com'                    #hard-coded
# port = 2222
#
# password = 'demo-user'                #hard-coded
# username = 'demo-user'                #hard-coded


host = 'ec2-52-77-252-17.ap-southeast-1.compute.amazonaws.com'
port = 22

username = 'csoh'                #hard-coded
password = 'letlrin'                #hard-coded


def create_sftp_client(host, port, username, password, keyfilepath, keyfiletype):
    """
    create_sftp_client(host, port, username, password, keyfilepath, keyfiletype) -> SFTPClient

    Creates a SFTP client connected to the supplied host on the supplied port authenticating as the user with
    supplied username and supplied password or with the private key in a file with the supplied path.
    If a private key is used for authentication, the type of the keyfile needs to be specified as DSA or RSA.
    :rtype: SFTPClient object.
    """
    sftp = None
    key = None
    transport = None
    try:
        if keyfilepath is not None:
            # Get private key used to authenticate user.
            if keyfiletype == 'DSA':
                # The private key is a DSA type key.
                key = paramiko.DSSKey.from_private_key_file(keyfilepath)
            else:
                # The private key is a RSA type key.
                key = paramiko.RSAKey.from_private_key(keyfilepath)

        # Create Transport object using supplied method of authentication.
        transport = paramiko.Transport((host, port))
        transport.connect(None, username, password, key)

        sftp = paramiko.SFTPClient.from_transport(transport)

        return sftp
    except Exception as e:
        print('An error occurred creating SFTP client: %s: %s' % (e.__class__, e))
        if sftp is not None:
            sftp.close()
        if transport is not None:
            transport.close()
        pass



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

target_dir = "/tmp"
sftpGet(host, port, username, password, target_dir, "." )



# keyfile_path = None
#
# sftpclient = create_sftp_client(host, port, username, password, keyfile_path, 'DSAx')
# print(sftpclient)
# dirlist = sftpclient.listdir('.')
# for row in dirlist:
#     print(row)