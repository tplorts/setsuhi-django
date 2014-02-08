from django import template

register = template.Library()

@register.inclusion_tag('tags/okiphoto.html', takes_context=True)
def okiphoto( context, sourceURL ):
    context["sourceURL"] = sourceURL
    return context
