# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django import template
from home import models


register = template.Library()


@register.inclusion_tag('tags/galleria.html', takes_context=True)
def sakuhin_galleria( context, sakuhin_group, *args, **kwargs):
    try:
        group = models.SakuhinGroup.objects.get( name=sakuhin_group )
    except Exception:
        items = None
    else:
        items = group.sakuhin_set.all()

    # Supply a default id unless provided explicitly
    if "id" in kwargs:
        context["galleria_id"] = kwargs["id"]
    else:
        context["galleria_id"] = "galleria-sakuhin-"+sakuhin_group

    # Class is optional
    if "class" in kwargs:
        context["galleria_class"] = kwargs["class"]
    else:
        context["galleria_class"] = ""

    context["galleria_items"] = items    
    return context
