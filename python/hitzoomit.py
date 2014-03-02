import mechanize
import urllib
import urllib2
import sys

imageurl = sys.argv[1]

browser = mechanize.Browser()
browser.set_handle_redirect(False)
response = browser.open("http://zoom.it/")

values = {'url' : imageurl,
          'x' : '35',
          'y' : '8'
          }
data = urllib.urlencode(values)
req = urllib2.Request("http://zoom.it/", data)
response2 = urllib2.urlopen(req)

# This is the short url of the deepzoom image
print response2.geturl()
