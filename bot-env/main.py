import json

with open('conf.json') as  e:
    infos = e.json.load(e)
    TOKEN = infos['toke']
    prefix = infos['prefix']