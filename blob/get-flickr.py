import flickrapi
api_key = '652dbd597aa5103e20afe8fdf3b4f42e'
flickr = flickrapi.FlickrAPI(api_key, cache=True)

photos = flickr.photos_search(tags='boston', lat='42.355056', lon='-71.065503', radius='5')

for photo in photos[0]:
    try:
        print photo.attrib['title']
        photoLoc = flickr.photos_geo_getLocation(photo_id=photo.attrib['id'])
        print photoLoc[0][0].attrib['latitude']
        print photoLoc[0][0].attrib['longitude']
        photoSizes = flickr.photos_getSizes(photo_id=photo.attrib['id'])
        print photoSizes[0][1].attrib['source']
    except:
        pass


