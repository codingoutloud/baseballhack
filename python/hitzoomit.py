import mechanize
import urllib
import urllib2

browser = mechanize.Browser()
response = browser.open("http://zoom.it/")

values = {'url' : 'https://avatars.githubusercontent.com/u/560657',
          'x' : '35',
          'y' : '8'
          }
data = urllib.urlencode(values)
req = urllib2.Request("http://zoom.it/", data)
response2 = urllib2.urlopen(req)

print response.geturl()
print response.info()
print response.read()
