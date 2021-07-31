import json
htags = json.load(open('tags/html','r'))
stags = json.load(open('tags/svg','r'))
mtags = json.load(open('tags/math','r'))
blacklist = {}
deepness = 20
fillers = ["aa","bb","cc","GG"]
