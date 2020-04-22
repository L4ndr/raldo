import tweepy
from time import sleep

consumer_key = "dJHHerYFLYjq5faGVNwBXdcGH"
api_secret = "Lep6W9zFvjNuAcULxxAeG5SirfBKUDjr3LxXZCjF4QODMQ7eja"

auth = tweepy.OAuthHandler(consumer_key, api_secret)
auth_url = auth.get_authorization_url()
open(auth_url)

verifier = input()
auth.get_access_token(verifier)
api = tweepy.API(auth)

print(f"logged in as {api.me().screen_name}")

def get_followers(screen_name):
    ids = list()
    for page in tweepy.Cursor(api.followers_ids, screen_name=screen_name).pages():
        ids.extend(page)
        sleep(60)
    return ids

input("protect your tweets then press enter")

blockedids = list()

for id in get_followers(api.me().screen_name):
    print(api.get_user(int(id)).screen_name)
    inp = input()
    if inp == "s":
        api.create_block(int(id))
        blockedids.append(int(id))
    else:
        pass

input("unprotect your tweets then press enter")

for id in blockedids:
    api.destroy_block(id)
