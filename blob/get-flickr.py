import flickrapi
import requests
import sys
import urllib

api_key = '652dbd597aa5103e20afe8fdf3b4f42e'
flickr = flickrapi.FlickrAPI(api_key, cache=True)

lat = '42.355056'
lon = '-71.065503'
rad = 10
the_date = '2013-08-04'

#photos = flickr.photos_search(tags='boston', lat='42.355056', lon='-71.065503', radius='5')
photos = flickr.photos_search(lat=lat, lon=lon, radius=rad) 
#	min_taken_date=the_date, max_taken_date=the_date)

maxdown = 2

print "starting..."
for photo in photos[0]:
    if maxdown > 0: 
        maxdown = maxdown - 1
        try:
            print photo.attrib['title']
            photoLoc = flickr.photos_geo_getLocation(photo_id=photo.attrib['id'])
            print photoLoc[0][0].attrib['latitude']
            print photoLoc[0][0].attrib['longitude']
            photoSizes = flickr.photos_getSizes(photo_id=photo.attrib['id'])
            url = photoSizes[0][1].attrib['source']
            print "URL => " + url
            d = dir(url)
            print(d)

            down_file(url)
            #download_file(url)
        except:
            print "exception: %s" % sys.exc_info()[0]
            pass
    else:
        #print "-- REACHED MAX DOWNLOADS --"
        sys.exit

def down_file(url):
    print "hello to %s" % url
    urllib.urlretrieve(url)


def download_file(url):
    print "hello to %s" % url
    return
    local_filename = url.split('/')[-1]
    print "saving to " + local_filename
    # NOTE the stream=True parameter
    r = requests.get(url, stream=True)
    with open(local_filename, 'wb') as f:
        for chunk in r.iter_content(chunk_size=1024): 
            print "chunk..."
            if chunk: # filter out keep-alive new chunks
                f.write(chunk)
                f.flush()
    return local_filename

