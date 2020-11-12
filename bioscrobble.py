from time import sleep
import webbrowser

import tweepy
twitter_consumer_key = ""
twitter_api_secret = ""

import pylast
# pra ter acesso à suas chaves da api do last você precisa se registrar aqui antes: https://www.last.fm/api/account/create
last_api_key = ""
last_api_secret = ""
username = "user" # coloque seu usuário do last aqui
network = pylast.LastFMNetwork(api_key=last_api_key, api_secret=last_api_secret, username=username)
user = pylast.User(username, network)

auth = tweepy.OAuthHandler(twitter_consumer_key, twitter_api_secret)
auth_url = auth.get_authorization_url()
webbrowser.open(auth_url)


# pra poder rodar no nohup eu tive que fazer essa gambiarrinha aqui
# você pega o código que apareceu na janela que abriu e cola num arquivo
# com nome "auth.txt" (sem aspas) dentro do mesmo diretório

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
