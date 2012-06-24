# Quick example how to connect to openCPU

import requests
url = "http://public.opencpu.org/R/pub/stats/rnorm/json"
data_params = {'n' : '5'}
print "Connecting to url: %s, with the data_params %s" %(url, data_params)
r = requests.post(url, data=data_params)
#data in the json
print "Status ok: %s, result: %s" %(r.status_code, r.json)

