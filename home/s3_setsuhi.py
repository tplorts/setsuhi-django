from boto.s3.connection import S3Connection
from setsuhi import settings

# These are the credentials for the user 'setsuhi'
cxn = S3Connection('AKIAJZDM7UFOXEZXO4NA', 'bAK78NsqgSvGekyfyjYuI2rJo6jTrZPbhBGoOglk')

bucket = cxn.get_bucket( settings.S3_BUCKET_NAME )
isConnected = True
