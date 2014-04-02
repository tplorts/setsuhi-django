# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from home.models import Sakuhin, SakuhinGroup
from home import s3_setsuhi

base_url = s3_setsuhi.bucket_url + "作品/samples/"
filelist = [str(n+1).zfill(4)+".jpg" for n in range(12)]

g = SakuhinGroup(name='samples')
g.save()

for f in filelist:
    g.sakuhin_set.create( main_image_url = base_url + "S/" + f, 
                          thumb_image_url = base_url + "T/" + f,
                          large_image_url = base_url + "L/" + f
    ).save()
