from django import template
from home import s3_setsuhi

register = template.Library()

@register.inclusion_tag('tags/okiphoto.html', takes_context=True)
def okiphoto( context, sourceURL ):
    context["sourceURL"] = s3_setsuhi.bucket_url + sourceURL
    return context
