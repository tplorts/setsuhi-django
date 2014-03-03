from boto.s3.connection import S3Connection


# These are the credentials for the user 'setsuhi'
cxn = S3Connection('AKIAJZDM7UFOXEZXO4NA', 'bAK78NsqgSvGekyfyjYuI2rJo6jTrZPbhBGoOglk')

bucket = cxn.get_bucket('setsuhi-tokyo')

bucket_url = "http://s3-ap-northeast-1.amazonaws.com/setsuhi-tokyo/"
