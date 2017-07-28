import logging
import os


from flask import (Flask, request, Response)
from flask_restful import Api
from werkzeug.utils import secure_filename

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)
api = Api(app)


import paramiko

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


host = 'ec2-52-77-252-17.ap-southeast-1.compute.amazonaws.com'
port = 22

username = 'csoh'                #hard-coded
password = 'letlrin'                #hard-coded


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

@app.route('/ftp', methods=['GET'])
def testFtp() :
    target_dir = "/tmp"
    sftpGet(host, port, username, password, target_dir, ".")
    return "Done", 200




if __name__ == '__main__':
    port = int(os.getenv("PORT", 5000))
    logger.info("Running learning-recommender webapp_admin in http")
    app.run(host='0.0.0.0', debug=False, port=port, threaded=True)


