# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from home.models import Sakuhin, SakuhinGroup, SakuhinEntry
from home.s3_setsuhi import bucket_url

d = {
    'flyer': ('0001.jpg','0002.jpg','0003.jpg','0004.jpg','0005.jpg','0006.jpg','0007.jpg','0008.jpg','0009.jpg','0010.jpg','0011.jpg','0012.jpg','0013.jpg','0014.jpg','0015.jpg','0016.jpg','0017.jpg','0018.jpg','0019.jpg','0020.jpg','0021.jpg','0022.jpg','0023.jpg','0024.jpg','0025.jpg','0026.jpg','0027.jpg','0028.jpg','0029.jpg','0030.jpg','0031.jpg','0032.jpg','0033.jpg','0034.jpg','0035.jpg','0036.jpg','0037.jpg','0038.jpg','0039.jpg','0040.jpg','0041.jpg','0042.jpg','0043.jpg','0044.jpg','0045.jpg','0046.jpg','0047.jpg','0048.jpg','0049.jpg','0050.jpg','0051.jpg','0052.jpg','0053.jpg','0054.jpg','0055.jpg','0056.jpg','0057.jpg','0058.jpg','0059.jpg','0060.jpg','0061.jpg','0062.jpg','0063.jpg','0064.jpg','0065.jpg','0066.jpg','0067.jpg','0068.jpg','0069.jpg','0070.jpg','0071.jpg','0072.jpg','0073.jpg','0074.jpg','0075.jpg','0076.jpg','0077.jpg','0078.jpg','0079.jpg','0080.jpg','0081.jpg','0082.jpg',),
    'futariten': ('0001.jpg','0002.jpg','0003.jpg','0004.jpg','0005.jpg','0006.jpg','0007.jpg','0008.jpg','0009.jpg','0010.jpg','0011.jpg','0012.jpg','0013.jpg','0014.jpg','0015.jpg','0016.jpg','0017.jpg','0018.jpg','0019.jpg','0020.jpg','0021.jpg','0022.jpg','0023.jpg','0024.jpg','0025.jpg','0026.jpg','0027.jpg','0028.jpg','0029.jpg','0030.jpg','0031.jpg','0032.jpg',),
    'goods': ('0001.jpg','0002.jpg','0003.jpg','0004.jpg','0005.jpg','0006.jpg','0007.jpg','0008.jpg',),
    'logo': ('0001.jpg','0002.jpg','0003.jpg','0004.jpg','0005.jpg','0006.jpg','0007.jpg','0008.jpg','0009.jpg','0010.jpg','0011.jpg','0012.jpg','0013.jpg','0014.jpg','0015.jpg','0016.jpg','0017.jpg','0018.jpg','0019.jpg','0020.jpg','0021.jpg','0022.jpg','0023.jpg','0024.jpg','0025.jpg','0026.jpg','0027.jpg','0028.jpg','0029.jpg',),
    'media': ('0001.jpg','0002.jpg','0003.jpg','0004.jpg','0005.jpg','0006.jpg','0007.jpg','0008.jpg','0009.jpg','0010.jpg','0011.jpg','0012.jpg','0013.jpg','0014.jpg','0015.jpg','0016.jpg','0017.jpg','0018.jpg','0019.jpg','0020.jpg','0021.jpg','0022.jpg','0023.jpg','0024.jpg','0025.jpg','0026.jpg','0027.jpg','0028.jpg','0029.jpg',),
    'perform': ('0001.jpg','0002.jpg','0003.jpg','0004.jpg','0005.jpg','0006.jpg','0007.jpg','0008.jpg','0009.jpg','0010.jpg','0011.jpg','0012.jpg','0013.jpg','0014.jpg','0015.jpg','0016.jpg','0017.jpg',),
    'tools': ('0001.jpg','0002.jpg','0003.jpg','0004.jpg','0005.jpg','0006.jpg','0007.jpg','0008.jpg','0009.jpg',),
    'wedding-dress': ('0001.jpg','0002.jpg','0003.jpg','0004.jpg','0005.jpg','0006.jpg','0007.jpg','0008.jpg','0009.jpg','0010.jpg','0011.jpg','0012.jpg','0013.jpg','0014.jpg','0015.jpg','0016.jpg','0017.jpg','0018.jpg','0019.jpg','0020.jpg','0021.jpg','0022.jpg','0023.jpg','0024.jpg',),
    'wedding+name+': ('0001.jpg','0002.jpg','0003.jpg','0004.jpg','0005.jpg','0006.jpg','0007.jpg','0008.jpg','0009.jpg','0010.jpg','0011.jpg','0012.jpg','0013.jpg','0014.jpg','0015.jpg','0016.jpg','0017.jpg','0018.jpg','0019.jpg','0020.jpg','0021.jpg','0022.jpg','0023.jpg','0024.jpg','0025.jpg','0026.jpg','0027.jpg','0028.jpg','0029.jpg','0030.jpg','0031.jpg','0032.jpg','0033.jpg','0034.jpg','0035.jpg','0036.jpg','0037.jpg','0038.jpg','0039.jpg','0040.jpg','0041.jpg','0042.jpg','0043.jpg','0044.jpg','0045.jpg','0046.jpg','0047.jpg','0048.jpg','0049.jpg','0050.jpg','0051.jpg','0052.jpg','0053.jpg','0054.jpg','0055.jpg','0056.jpg','0057.jpg','0058.jpg','0059.jpg','0060.jpg','0061.jpg','0062.jpg','0063.jpg',),
    'work': ('0001.jpg','0002.jpg','0003.jpg','0004.jpg','0005.jpg','0006.jpg','0007.jpg','0008.jpg','0009.jpg','0010.jpg','0011.jpg','0012.jpg','0013.jpg','0014.jpg','0015.jpg','0016.jpg','0017.jpg','0018.jpg','0019.jpg','0020.jpg','0021.jpg','0022.jpg','0023.jpg','0024.jpg','0025.jpg','0026.jpg','0027.jpg','0028.jpg','0029.jpg','0030.jpg','0031.jpg','0032.jpg','0033.jpg','0034.jpg','0035.jpg','0036.jpg','0037.jpg','0038.jpg','0039.jpg','0040.jpg','0041.jpg','0042.jpg','0043.jpg','0044.jpg','0045.jpg','0046.jpg','0047.jpg','0048.jpg',),
    '縁': ('0001.jpg','0002.jpg','0003.jpg','0004.jpg','0005.jpg','0006.jpg','0007.jpg','0008.jpg','0009.jpg','0010.jpg','0011.jpg','0012.jpg','0013.jpg','0014.jpg','0015.jpg','0016.jpg','0017.jpg','0018.jpg','0019.jpg','0020.jpg','0021.jpg','0022.jpg','0023.jpg','0024.jpg','0025.jpg','0026.jpg','0027.jpg','0028.jpg','0029.jpg','0030.jpg','0031.jpg','0032.jpg','0033.jpg','0034.jpg','0035.jpg',),
}

for groupname in d:
    g = SakuhinGroup( name=groupname,
                      title="notitle" )
    g.save()
    u = bucket_url + 'i/' + groupname + '/'
    index = 1
    for i in d[groupname]:
        s = Sakuhin( main_image_url=u+'S/'+i,
                     thumb_image_url=u+'T/'+i,
                     large_image_url=u+'O/'+i )
        s.save()
        e = SakuhinEntry( sakuhin=s,
                          group=g,
                          order_index=index )
        e.save()
        index += 1
    g.save()
