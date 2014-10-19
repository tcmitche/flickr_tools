#!/usr/bin/env python
import flickr
import urllib
import ConfigParser
import os

config = ConfigParser.ConfigParser()
config.read('conf')

flickr.API_KEY = config.get('ApiCredentials', 'key')
flickr.API_SECRET = config.get('ApiCredentials', 'secret')

setId = config.get('Info', 'set_id')
photoDir = config.get('Info', 'photo_dir')

if not os.path.exists(photoDir):
    os.makedirs(photoDir)

print('Calling flickr for set: %s' % setId)
photos = flickr.Photoset(setId).getPhotos()

for p in photos:
    pUrl = 'https://farm%s.staticflickr.com/%s/%s_%s_o.%s' % (p.farm, p.server, p.id, p.originalsecret, p.originalformat)
    f = open('%s/%s.%s' % (photoDir, p.id, p.originalformat), 'wb')
    print('Getting photo %s...' % pUrl)
    f.write(urllib.urlopen(pUrl).read())
    print('done!')
    f.close()
