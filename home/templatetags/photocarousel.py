from django import template

register = template.Library()

@register.inclusion_tag('tags/photocarousel.html', takes_context=True)
def photocarousel( context, carousel_id, photo_path, quantity ):
    quantity = int( quantity )
    context["carousel_id"] = carousel_id
    context["photo_path"] = photo_path
    context["photos"] = [str(n)+".jpg" for n in range(0, quantity)]
    return context
