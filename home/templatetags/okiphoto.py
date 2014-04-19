from django import template
from setsuhi import settings

register = template.Library()

@register.inclusion_tag('tags/okiphoto.html', takes_context=True)
def okiphoto( context, sourceURL ):
    context["sourceURL"] = settings.S3_BUCKET_URL + sourceURL
    return context
