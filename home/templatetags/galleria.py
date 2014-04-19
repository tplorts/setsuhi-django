# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django import template
import urllib2
import json
from setsuhi import settings


register = template.Library()


class G:
    def __init__(self, info, base_url=None):
        self.titles = info["titles"]
        self.briefs = info["briefs"]
        if base_url:
            self.main_image_url = base_url + info["main"]
        else:
            self.main_image_url = info["main"]
        self.big_image_url = None
        self.thumbnail_image_url = None
    def main_url(self):
        return self.main_image_url
    def thumbnail_url(self):
        if self.thumbnail_image_url:
            return self.thumbnail_image_url
        return self.main_image_url
    def big_url(self):
        if self.big_image_url:
            return self.big_image_url
        return self.main_image_url



@register.inclusion_tag('tags/galleria.html', takes_context=True)
def galleria( context, galleria_id, image_folder ):
    context["galleria_id"] = galleria_id
    
    if not image_folder.endswith('/'):
        image_folder += '/'
    base_url = settings.S3_BUCKET_URL + "static/media/images/" + image_folder    
    jsonurl = urllib2.urlopen( base_url + "info.json" )
    jsoninfo = json.load( jsonurl )
    context["galleria_items"] = [G(json_item, base_url) for json_item in jsoninfo]
    
    return context
