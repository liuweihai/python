#/usr/bin/env python
#-*- coding:utf-8 -*-
import requests
import json
url = 'https://api.douban.com/v2/movie/search'
parms = dict(q='刘德华')
r = requests.get(url,parms)
print('search Parms:\n',json.dumps(parms,ensure_ascii=False))
print('Search request:\n',json.dumps(r.json(),ensure_ascii=False,indent=4))