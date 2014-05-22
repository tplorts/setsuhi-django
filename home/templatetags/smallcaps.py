from django import template
from django.template.defaultfilters import stringfilter
from django.utils.safestring import mark_safe
import re

register = template.Library()
 
@register.filter(is_safe=True)
@stringfilter
def smallcaps(text):
    return re.sub(r'([a-z]+)', 
                  r'<span class="smallcaps">\1</span>', 
                  text)
