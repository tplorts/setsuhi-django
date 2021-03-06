# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from home.models import Sakuhin, SakuhinGroup, SakuhinEntry
from home import s3_setsuhi

base_url = s3_setsuhi.bucket_url + "作品/縁/"
filenumbers = range(3,15) + range(1,3) + range(15,27)
filelist = [str(n).zfill(4)+".jpg" for n in filenumbers]
ordering = [14,6,12,10,7,9,18,19,22,4,23,24,25,5,2,1,3,11,13,15,21,8,16,17,20]

titles = [
    "Bracelet ￥17000", "",
    "ピアス ￥16000　Bracelet ￥17000", "", "", "", "",
    "ピアス ￥15000",
    "Bracelet ￥17000", "",
    "ピアス ￥16000", "",
    "ピアス ￥16000", "",
    "Necklace ￥19000",
    "Strap ￥7000",
    "Bracelet ￥16000",
    "Strap ￥8000　Bracelet ￥17000　ピアス ￥16000",
    "Strap ￥8000",
    "Strap ￥7000　Bracelet ￥16000　ピアス ￥15000", "",
    "ピアス ￥16000",
    "Bracelet ￥18000",
    "ピアス ￥16000",
    "ピアス ￥16000　Necklace ￥20000　Bracelet ￥18000",
    "Strap ￥9000",
]

g = SakuhinGroup(name='en')
g.save()

i = 1
for o in ordering:
    f = filelist[o-1]
    t = titles[o-1]

    s = Sakuhin( main_image_url = base_url + "S/" + f, 
                 thumb_image_url = base_url + "T/" + f,
                 large_image_url = base_url + "L/" + f,
                 title = t )
    s.save()

    e = SakuhinEntry( sakuhin=s, group=g, order_index=i )
    e.save()

    i += 1
