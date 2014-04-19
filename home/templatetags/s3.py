from django import template
import boto
from setsuhi import settings
from home import s3_setsuhi


register = template.Library()


@register.simple_tag
def s3_url( key ):
    return settings.S3_BUCKET_URL + key


@register.assignment_tag
def s3_url_list( folder ):
    if not folder.endswith('/'):
        folder = folder + '/'
    ls = s3_setsuhi.bucket.list( prefix=folder, delimiter='/', encoding_type="url" )
    return [ s3_url(item.key) for item in ls if isinstance(item, boto.s3.key.Key) and not item.key.endswith('/') ]


@register.inclusion_tag('tags/s3photoset.html')
def s3photoset( place ):
    ls = s3_setsuhi.bucket.list(prefix="photographs/"+place, encoding_type="url")
    image_locators = [ settings.S3_BUCKET_URL + photo.key for photo in ls ]
    return {"image_locators": image_locators}


@register.inclusion_tag('tags/photocarousel.html', takes_context=True)
def s3_photocarousel( context, carousel_id, folder ):
    context["carousel_id"] = carousel_id
    context["photo_url_list"] = s3_url_list( folder )
    return context


@register.inclusion_tag('tags/slides.html', takes_context=True)
def s3_slides( context, slides_id, folder ):
    context["slides_id"] = slides_id
    context["photo_url_list"] = s3_url_list( folder )
    return context

