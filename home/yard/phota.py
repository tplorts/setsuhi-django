from __future__ import unicode_literals
import s3_setsuhi
import urllib2
import json


phota_folder = "photographs/"


class Photum:
    def __init__(self):
        self.folder = None
        self.date = None
        self.cover = None
        self.use = False

    def __init__(self, dictionary):
        self.folder = dictionary['folder']
        self.date = dictionary['date']
        self.cover = dictionary['cover']
        self.use = dictionary['use']

    def cover_url(self):
        return s3_setsuhi.bucket_url + phota_folder + self.folder + "/" + self.cover


if s3_setsuhi.isConnected:
    jsonurl = urllib2.urlopen( s3_setsuhi.bucket_url + "phota.json" )
    jsoninfo = json.load( jsonurl )
    allphota = [Photum(d) for d in jsoninfo.values()]
    photatouse = [p for p in allphota if p.use]

