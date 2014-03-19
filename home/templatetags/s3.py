from django import template
from home import s3_setsuhi


register = template.Library()


@register.simple_tag
def s3_url( key ):
    return s3_setsuhi.bucket_url + key


@register.assignment_tag
def s3_url_list( folder ):
    ls = s3_setsuhi.bucket.list( prefix=folder, encoding_type="url" )
    return [ s3_url(item.key) for item in ls if not item.key.endswith('/') ]


@register.inclusion_tag('tags/s3photoset.html')
def s3photoset( place ):
    ls = s3_setsuhi.bucket.list(prefix="photographs/"+place, encoding_type="url")
    image_locators = [ s3_setsuhi.bucket_url + photo.key for photo in ls ]
    return {"image_locators": image_locators}


@register.inclusion_tag('tags/photocarousel.html', takes_context=True)
def s3_photocarousel( context, carousel_id, folder ):
    context["carousel_id"] = carousel_id
    context["photo_url_list"] = s3_url_list( folder )
    return context
