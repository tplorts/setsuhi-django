from __future__ import unicode_literals
import codecs
import json
import time
from home import phota


dateformat = "%Y-%m-%d"

info = {}
for photumname in phota.names:
    datepart = photumname.split(' ')[0]
    try:
        date = time.strftime( dateformat, time.strptime(datepart, dateformat) )
    except ValueError:
        date = None
    info[photumname] = {
        "folder": photumname,
        "date": date,
        "use": False,
        "cover": None,
    }

infofile = codecs.open("phota.json", "w", encoding="utf-8")
json.dump(info, infofile, indent=2)
infofile.close()
