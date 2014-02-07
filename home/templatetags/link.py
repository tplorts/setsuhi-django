# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django import template


register = template.Library()

people = {
    "Jay Anderson": "http://www.jayandersonbass.com/",
    "Frank Kinbrough": "http://home.earthlink.net/~fkimbrough/",
    "Adam Unsworth": "http://adamunsworth.net/",
    "London Improvisers Orchestra": "http://www.londonimprovisersorchestra.co.uk/",
    "Vasco da Gama": "http://www.amazon.com/s/ref=nb_sb_noss?url=search-alias%3Ddigital-text&field-keywords=magellan+japan+vasco+da+gama",
    "Jiang Xiao-Qing": "http://jiang-xiaoqing.xii.jp/",
    "姜小青":  "http://jiang-xiaoqing.xii.jp/",
    "Fissler": "http://www.fissler.com/",
    "Ryona": "http://ryona.jp",
    "喫茶茶会記": "http://sakaiki.modalbeats.com/",
    "茶会記": "http://sakaiki.modalbeats.com/",
    "Sakaiki": "http://sakaiki.modalbeats.com/",
    "日本代表新ユニフォーム": "http://adidas.jp/jfa/",
    "Saideigama": "http://saideigama.com/index_eng.html",
    "彩泥窯": "http://saideigama.com/",
};

#@register.inclusion_tag('link.html')
@register.simple_tag
def link( name, lang=None ):
#    if( name not in people ):
#        url = None
#    else:
#        url = people[name]
#    return { 'name': name, 'url': url, 'lang': lang }
    if( name not in people ):
        return name
    a = "<a "
    target = "target=\"_blank\" "
    href = "href=\"" + people[name] + "\" "
    _a = "</a>"

    span = "<span "
    if lang == None:
        l = ""
    else:
        l = "lang=\"" + lang + "\" "
    _span = "</span>"

    return a+target+href+'>'+span+l+'>'+name+_span+_a

