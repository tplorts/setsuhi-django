from __future__ import unicode_literals
import s3_setsuhi
import urllib


ls = s3_setsuhi.bucket.list(prefix="photographs/", delimiter="/")

names = [urllib.unquote_plus(x.name.split('/')[1]) for x in ls]
# The first object is the key of the query
names = names[1:]
