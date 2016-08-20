import requests as r
import urllib
import json
import sys
import os

# export FLICKR_API_KEY="<api-key>" in .bashrc

flick_rest_url = "https://api.flickr.com/services/rest/"
PER_PAGE = 5
sort_options= ["interestingness-desc", "interestingness-asc", "relevance"] # date-posted-asc/desc, date-taken-asc/desc

args                 = dict() # parameters to pass to flickr rest api
args['method']       = 'flickr.photos.search'
args['sort']         = sort_options[0]
args['safe_search']  = 1
args['content_type'] = 7
args['media']        = 'photos'
args['extras']       = 'url_n'
args['per_page']     = PER_PAGE
args['page']         = 1
args['format']       ='json'
args['jsoncallback'] = 1
args['tag_mode']     = 'all' # any for OR, all for AND

if len(sys.argv) > 1:
    query = sys.argv[1]
    query = query.replace(' ',',')
else:
    query="nile,river"
print "query = '{}'".format(query)
args['tags']         = query
args['api_key']      = os.environ['FLICKR_API_KEY']

o = r.get(flick_rest_url, args)
print "ok = {}, status_code = {}".format(o.ok, o.status_code)

text = o.text[2:-1] # remove round bracket for json parsing
j = json.loads(text)
print json.dumps(j, indent=4, sort_keys=True)

image_urls = [ j['photos']['photo'][i]['url_n'] for i in range(len(j['photos']['photo'])) ]
print "\n".join(image_urls)
