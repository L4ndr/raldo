from time import sleep
import webbrowser

import tweepy
twitter_consumer_key = ""
twitter_api_secret = ""

import pylast
# in order to get your last.fm api credentials you first need to register here: https://www.last.fm/api/account/create
last_api_key = ""
last_api_secret = ""
username = "user" # replace user with your actual last.fm username
network = pylast.LastFMNetwork(api_key=last_api_key, api_secret=last_api_secret, username=username)
user = pylast.User(username, network)

auth = tweepy.OAuthHandler(twitter_consumer_key, twitter_api_secret)
auth_url = auth.get_authorization_url()
webbrowser.open(auth_url)

# in order to run it in the background you'll need this little workaround while i can't think of anything better.
# you take your auth code in the tab that should have opened up in your default browser and paste
# it into a file named "auth.txt" in the same directory as the one the script is being ran from

sleep(60)
auth.get_access_token(open('auth.txt').read().strip('\n'))
api = tweepy.API(auth)

bio = api.me().description

while True:
    track = user.get_now_playing()
    if track is not None:
        if (len(bio)-8 + len(str(track))) <= 160:
            api.update_profile(description=(bio.replace("%MUSICA%", str(track))))
        elif (len(bio)-8 + len(str(track).split(' - ')[1])) <= 160:
            api.update_profile(description=(bio.replace("%MUSICA%", str(track).split(' - ')[1])))
        else:
            api.update_profile(description=(bio.replace("%MUSICA%", "😎")))
    else:
        api.update_profile(description=(bio.replace("%MUSICA%", "not listening to anything 😴")))
    sleep(100)
