from instagram.client import InstagramAPI

access_token = "725032259a6249f5b6b391c436f6b178"
api = InstagramAPI(access_token=access_token)
recent_media, next = api.user_recent_media(user_id="userid", count=10)
for media in recent_media:
   print media.caption.text

