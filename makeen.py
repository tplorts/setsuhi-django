# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from home.models import Sakuhin, SakuhinGroup
from home import s3_setsuhi

base_url = s3_setsuhi.bucket_url + "作品/縁/"
filenumbers = range(3,15) + range(1,3) + range(15,27)
filelist = [str(n).zfill(4)+".jpg" for n in filenumbers]
ordering = [14,6,12,10,7,9,18,19,22,4,23,24,25,5,2,1,3,11,13,15,21,8,16,17,20]

titles = [
    "Bracelette ￥17000", "",
    "Earring ￥16000　Bracelette ￥17000", "", "", "", "",
    "Earring ￥15000",
    "Bracelette ￥17000", "",
    "Earring ￥16000", "",
    "Earring ￥16000", "",
    "Neckless ￥19000",
    "Strap ￥7000",
    "Bracelette ￥16000",
    "Strap ￥8000　Bracelette ￥17000　Earring ￥16000",
    "Strap ￥8000",
    "Strap ￥7000　Bracelette ￥16000　Earring ￥15000", "",
    "Earring ￥16000",
    "Bracelette ￥18000",
    "Earring ￥16000",
    "Earring ￥16000　Neckless ￥20000　Bracelette ￥18000",
    "Strap ￥9000",
]

g = SakuhinGroup(name='en2')
g.save()

for o in ordering:
    f = filelist[o-1]
    t = titles[o-1]
    g.sakuhin_set.create( main_image_url = base_url + "S/" + f, 
                          thumb_image_url = base_url + "T/" + f,
                          large_image_url = base_url + "L/" + f,
                          title = t
    ).save()
