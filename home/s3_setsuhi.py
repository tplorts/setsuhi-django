from boto.s3.connection import S3Connection


# These are the credentials for the user 'setsuhi'
cxn = S3Connection('AKIAIQDCJ3TJSVSEJHUQ', '7+zUUT2oiIx6R0KAzQPNSVbBJAUnN99sMB4fxUR4')

bucket = cxn.get_bucket('setsuhi-tokyo')

bucket_url = "http://s3-ap-northeast-1.amazonaws.com/setsuhi-tokyo/"
