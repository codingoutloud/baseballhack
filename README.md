hackbaseball
============

Baseball Hackathon March 2, 2014

https://github.com/baseballhackday/2014-data-and-resources/wiki/Resources-and-ideas,-2014

http://baseballhackday.tumblr.com/

http://zoom.it

http://www.flickr.com/services/apps/create/noncommercial/?

secret/key
1d1ab74cef2f0916
652dbd597aa5103e20afe8fdf3b4f42e

Example that might help with geo-search in Flickr: http://spanring.eu/blog/2010/02/25/python-flickr-api-geo-search-example/ 
http://graphics.cs.cmu.edu/projects/im2gps/flickr_code.html
https://gist.github.com/jueyang/2431935

Instagram Client ID
725032259a6249f5b6b391c436f6b178

Location based searches of instagram should just need the client ID in the request. Can do GPS coordinates or facebook/foursquare checkin IDs for locations.  http://instagram.com/developer/endpoints/locations/

Get fenway park data from seatgeek including GPS coordinates
http://api.seatgeek.com/2/venues/21

This might explain how to read the meta data from the submitted photo 
http://stackoverflow.com/questions/4764932/in-python-how-do-i-read-the-exif-data-for-an-image

THis is a master list for a given date.  We could use this for the 9/4/13 photo.
http://gd2.mlb.com/components/game/mlb/year_2013/month_09/day_04/master_scoreboard.json
I'm sure we could go for a more dynamic approach easilty by doing http://gd2.mlb.com/components/game/mlb/year_{from-photo}/month_{from-photo}/day_{from-photo}/master_scoreboard.json


Format of zoom.it embedded control - the 5 characters before .js will change with each image:
<script src="http://zoom.it/YcnBL.js?width=auto&height=400px"></script>