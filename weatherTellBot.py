import tweepy
import pyowm
import time
import datetime
 
def tweet_Update():
    # Consumer keys and access tokens, used for OAuth from twitter
    consumer_key = 'GL9tcAonfq02uVO9P4HmkzZKo'
    consumer_secret = '2mAEKL51npVgpat2jm3uk0s13udQOd9G4FxY2drNTTgNMi0Ot3'
    access_token = '200545877-7YdSwAA3kYSs9wiLzFre5MsrV9fZvP3kg3yphyDF'
    access_token_secret = 'xUz3W6rFrm0AeVaXA9UNpFScAF8LfaHJayV6ZXS6v4Fut'
     
    # OAuth twitter process, using the keys and tokens
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
     
    # Creation of the actual interface, using authentication
    api = tweepy.API(auth)

    #api from openweathermap.org
    owm = pyowm.OWM("bc2ab34b16719508a9ba53b2ffbaa4f8")
    obs = owm.weather_at_place('Cape Coast,GH')
    w = obs.get_weather()
    temp = w.get_temperature('celsius')
    
    # time taken
    localtime = datetime.datetime.now()
    message = "Weather Update from Cape Coast "+str(localtime) +" :\n"+"The Temp is: " + str(temp['temp']) + " and The Humidity is: " + str(w.get_humidity())
    
    #weather message to update twitter
    api.update_status(message)

# updates twitter every hour 
while True:
    tweet_Update()
    time.sleep(3600)
