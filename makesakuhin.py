# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from home.models import Sakuhin, SakuhinGroup, SakuhinEntry
from home import s3_setsuhi

base_url = s3_setsuhi.bucket_url + "作品/書画/表/"
filelist = ['4127.jpg','4128.jpg','4129.jpg','4133.jpg',
            '4140.jpg','4142.jpg','4143.jpg','4154.jpg',
            '4156.jpg','4158.jpg','4160.jpg','4161.jpg',
            '4162.jpg','4165.jpg','4173.jpg']

g = SakuhinGroup(name='shoga')
g.save()

i=1
for f in filelist:
    s = Sakuhin( main_image_url = base_url + "S/" + f, 
                 thumb_image_url = base_url + "T/" + f,
                 large_image_url = base_url + "L/" + f )
    s.save()

    e = SakuhinEntry( sakuhin=s, group=g, order_index=i )
    e.save()

    i += 1
