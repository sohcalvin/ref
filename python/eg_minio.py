# Import Minio library.
from minio import Minio
from minio.error import (ResponseError, BucketAlreadyOwnedByYou,
                         BucketAlreadyExists)

minioClient = Minio('127.0.0.1:9000',
                    access_key='asdfasdfa',
                    secret_key='asdfasdfasdf',
                    secure=False)

# Make a bucket with the make_bucket API call.
try:
       minioClient.make_bucket("a.csohbucket")
except BucketAlreadyOwnedByYou as err:
       pass
except BucketAlreadyExists as err:
       pass
except ResponseError as err:
       raise

try:
       print("running")
       # some.log is the filename used server
       # /tmp/t.txt is the file to upload
       minioClient.fput_object('csohbucket', 'some.log', '/tmp/t.txt')
       minioClient.fput_object('csohbucket', 'some2.log', '/tmp/t.txt')
       minioClient.fput_object('a.csohbucket', 'some2.log', '/tmp/t.txt')
except ResponseError as err:
       print(err)