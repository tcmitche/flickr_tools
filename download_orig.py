#!/usr/bin/env python
import flickr
import urllib
import ConfigParser
import os

config = ConfigParser.ConfigParser()
config.read('conf')

flickr.API_KEY = config.get('ApiCredentials', 'key')
flickr.API_SECRET = config.get('ApiCredentials', 'secret')

setId = '72157648278345450'
photoDir = 'photos'

if not os.path.exists(photoDir):
    os.makedirs(photoDir)

print('Calling flickr for set: %s' % setId)
photos = flickr.Photoset(setId).getPhotos()

# for p in photos:
p = photos[0]
pUrl = 'https://farm%s.staticflickr.com/%s/%s_%s_o.%s' % (p.farm, p.server, p.id, p.originalsecret, p.originalformat)
f = open('%s/%s.%s' % (photoDir, p.id, p.originalformat), 'wb')
f.write(urllib.urlopen(pUrl).read())
f.close()
