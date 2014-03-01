from django import template
from home import s3_setsuhi


register = template.Library()


@register.inclusion_tag('tags/s3photoset.html')
def s3photoset( place ):
    ls = s3_setsuhi.bucket.list(prefix="photographs/"+place, encoding_type="url")
    image_locators = [ s3_setsuhi.bucket_url + photo.key for photo in ls ]
    return {"image_locators": image_locators}
