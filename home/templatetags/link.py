# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django import template


register = template.Library()


en_url = "http://ja.wikipedia.org/wiki/%E7%B8%81"
sakaiki_url = "http://sakaiki.modalbeats.com/"
jiang_url = "http://jiang-xiaoqing.xii.jp/"
adidas_article = "http://news.adidas.com/GLOBAL/Latest-News/adidas-presents-the-Japanese-federation-kit-for-2014-FIFA-World-Cup-Brazil-/s/006665d3-f880-4b36-b1a1-ee07f37a3805#.UvhZ4j03Srs.link"


# If the display name is in Roman characters, I want the
# English font used.  Even if the link appears in a
# Japanese section.
english_addresses = {
    "Jay Anderson": "http://www.jayandersonbass.com/",
    "Frank Kinbrough": "http://home.earthlink.net/~fkimbrough/",
    "Adam Unsworth": "http://adamunsworth.net/",
    "London Improvisers Orchestra": "http://www.londonimprovisersorchestra.co.uk/",
    "Vasco da Gama": "http://www.amazon.com/s/ref=nb_sb_noss?url=search-alias%3Ddigital-text&field-keywords=magellan+japan+vasco+da+gama",
    "Jiang Xiao-Qing": jiang_url,
    "Fissler": "http://www.fissler.com/",
    "RYONA": "http://ryona.jp",
    "Sakaiki": sakaiki_url,
    "Saideigama": "http://saideigama.com/index_eng.html",
#    "縁 (&ldquo;en&rdquo;)": en_url,
    "article about the jersey": adidas_article,

};
japanese_addresses = {
    "姜小青":  jiang_url,
    "喫茶茶会記": sakaiki_url,
    "茶会記": sakaiki_url,
    "日本代表新ユニフォーム": "http://adidas.jp/jfa/",
    "彩泥窯": "http://saideigama.com/taiken_tepure_syodo_saport.html",
#    "縁": en_url,
#    "〜en〜縁": en_url,
};


# I would rather use the inclusion tag style rather than
# (as it is now) a simple tag but a space is always inserted
# immediately after what is rendered, and that will not do
# for these links..

#@register.inclusion_tag('tags/link.html')
@register.simple_tag
def link( name, lang=None ):
#    if( name not in people ):
#        url = None
#    else:
#        url = people[name]
#    return { 'name': name, 'url': url, 'lang': lang }
    
    if( name in english_addresses ):
        lang = "en"
        addresses = english_addresses
    elif( name in japanese_addresses ):
        lang = "ja"
        addresses = japanese_addresses
    else:
        return name

    a = "<a "
    target = "target=\"_blank\" "
    href = "href=\"" + addresses[name] + "\" "
    _a = "</a>"

    span = "<span "
    if lang == None:
        l = ""
    else:
        l = "lang=\"" + lang + "\" "
    _span = "</span>"

    return a+target+href+'>'+span+l+'>'+name+_span+_a

