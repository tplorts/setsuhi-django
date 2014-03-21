# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django import template

register = template.Library()

class G:
    def __init__(self, url):
        self.main_image_url = url
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
    def titles(self):
        return {'en': 'The title',
                'ja': 'タイトル'}
    def descriptions(self):
        return {'en': 'The desc',
                'ja': '短い紹介文'}


u = 'http://s3-ap-northeast-1.amazonaws.com/setsuhi-tokyo/static/media/images/shikaku-cover-cropped.jpg'
dummy = [G(u), G(u)]

@register.inclusion_tag('tags/galleria.html', takes_context=True)
def galleria( context, galleria_id ):
    context["galleria_id"] = galleria_id
    context["galleria_items"] = dummy
    return context
