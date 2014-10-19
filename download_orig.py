#!/usr/bin/env python
import flickr
import urllib
import ConfigParser

config = ConfigParser.ConfigParser()
config.read('conf')

flickr.API_KEY = config.get('ApiCredentials', 'key')
flickr.API_SECRET = config.get('ApiCredentials', 'secret')

setId = '72157648278345450'

print('Calling flickr for set: %s' % setId)
photos = flickr.Photoset(setId).getPhotos()

# for p in photos:
p = photos[0]
print('https://farm%s.staticflickr.com/%s/%s_%s_o.%s' % (p.farm, p.server, p.id, p.originalsecret, p.originalformat))
