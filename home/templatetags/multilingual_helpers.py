from django import template

register = template.Library()


@register.assignment_tag(takes_context=True)
def is_selected_language(context, lang):
    return context["selected_language"] == lang


@register.assignment_tag(takes_context=True)
def class_for_language(context, lang):
    if context["selected_language"] == lang:
        return "ml-on"
    else:
        return "ml-off"

