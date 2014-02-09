from django import template

register = template.Library()

@register.inclusion_tag('tags/photocarousel.html', takes_context=True)
def photocarousel( context, carousel_id, photo_path ):
    context["carousel_id"] = carousel_id
    context["photo_path"] = photo_path
    return context
