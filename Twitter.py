from twython import Twython
from Keys import *

twitter = Twython(
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
)

def tweet_image(filename):
    image = open(filename, 'rb')
    response = twitter.upload_media(media=image)
    media_id = [response['media_id']]
    twitter.update_status(media_ids=media_id)