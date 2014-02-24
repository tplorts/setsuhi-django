#from __future__ import unicode_literals
from boto.s3.connection import S3Connection
from django import template


register = template.Library()


# These are the credentials for the user 'setsuhi'
cxn = S3Connection('AKIAIQDCJ3TJSVSEJHUQ', '7+zUUT2oiIx6R0KAzQPNSVbBJAUnN99sMB4fxUR4')

bucket = cxn.get_bucket('setsuhi-tokyo')


@register.inclusion_tag('tags/s3photoset.html')
def s3photoset( place ):
    ls = bucket.list(prefix="photographs/"+place, encoding_type="url")
    base = "http://s3-ap-northeast-1.amazonaws.com/setsuhi-tokyo/"
    image_locators = [ base+photo.key for photo in ls ]
    return {"image_locators": image_locators}
