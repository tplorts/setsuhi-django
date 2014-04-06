# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import json
from django import template
from home import models


register = template.Library()


class GalleriaImage:
    def __init__(self):
        self.image = None
        self.thumb = None
        self.big = None
        self.title = None
        self.description = None

    def __init__(self, sakuhin):
        self.image = sakuhin.main_image_url
        self.thumb = sakuhin.thumb_image_url
        self.big = sakuhin.large_image_url
        self.title = sakuhin.title
        self.description = sakuhin.brief

class GalleriaEncoder(json.JSONEncoder):
    def default(self, o):
        return o.__dict__   


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

    context["sakuhin_group_name"] = sakuhin_group
    context["galleria_items"] = items
    return context



@register.simple_tag()
def sakuhin_galleria_data( *args, **kwargs ):
    if not "group" in kwargs:
        return "[]"
    group_name = kwargs["group"]
    try:
        group = models.SakuhinGroup.objects.get( name=group_name )
    except Exception:
        return "[]"
    items = group.sakuhin_set.all()
    gitems = [GalleriaImage(x) for x in items]
    gJSON = json.dumps(gitems, cls=GalleriaEncoder)
    return gJSON
