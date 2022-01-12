from random import randint
import discord

def rollen_k(variable, user):
    liste_rollen = ["Member","Jahrgang 5","Jahrgang 6","Klasse 7a","Klasse 7b","Klasse 7c","Klasse 7d","Jahrgang 7",
                    "Klasse 8a","Klasse 8b","Klasse 8c","Klasse 8d","Jahrgang 8","Klasse 9a","Klasse 9b","Klasse 9c",
                    "Klasse 9d","Jahrgang 9","Klasse 10a","Klasse 10b","Klasse 10c","Klasse 10d","Jahrgang 10","Klasse 11a",
                    "Klasse 11b","Jahrgang 11","Klasse 12a","Klasse 12b","Jahrgang 12","Realschule Plus-Schifferstadt",
                    "FOS-Schifferstadt","Streamer","Developer"]
    for x in range(33):
        if variable == x:
            rolle = discord.utils.get(user.guild.roles, name=liste_rollen[x])
            return rolle


def rollen_emojis():
    liste_emojis = ["👍","⚔","🎳","💡","📁","🐘","💼","🦉","⚡","👴","👎","🌐","🏈","🏺",
                    "🍍","🎣","💎","⚓","📶","🔥","👀","💙","❗","🏝","👽","⛏","🚗","🥑",
                    "🦄","✈","🛁","🐬","🐻"]
    return liste_emojis

def schlagen():
    # Bilder für Befehl Person schlagen :) | pictures for slap command
    schlag_liste_bilder = ["https://img.gentside.de/article/boxen/nach-diesem-schlag-sieht-er-sterne_8f2b376896a6e50a3561d410322415cf159df13e.jpg",
                 "https://img.gentside.de/article/480/boxen/briggs-kostet-gerade-die-gewaltige-rechte-von-klitschko_907d9b7316d0f81108d5c646bba0cfdb63ff1552.jpg"
    ,"https://static.dw.com/image/18071264_303.jpg","https://resources.stuff.co.nz/content/dam/images/1/l/a/0/t/a/image.related.StuffLandscapeSixteenByNine.710x400.1lzyeu.png/1506715007584.jpg",
    "https://hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/concussion-1568632204.jpg",
    "https://www.cnsneurosurgery.com.au/wp-content/uploads/2015/12/concusion-boxing-300x183.jpg",
    "https://i.pinimg.com/originals/c6/86/d2/c686d29494fe02fbe3d03e5c5587ab80.jpg","https://cdn.yepse.com/fc/31303332303835323732_31323033343839393932.jpg?11439921363","https://images-na.ssl-images-amazon.com/images/I/81tGLLntS3L.png",
    "https://itsinterestingdotcom.files.wordpress.com/2012/04/knockour-pounch.jpg",
    "https://tenor.com/view/animated-couple-hit-%E6%AE%B4%E3%82%89%E3%82%8C%E3%82%8B-gif-10694370","https://tenor.com/view/gap-slapped-knock-out-punch-gif-5122019","https://tenor.com/view/spank-tom-and-jerry-tom-puppy-hit-gif-16778355",
    "https://tenor.com/view/punch-in-the-face-gif-14279719","https://tenor.com/view/watch-out-run-you-over-gif-5729865","https://tenor.com/view/kids-falling-hit-sister-fight-siblings-gif-12112871",
    "https://tenor.com/view/hit-punch-fight-face-viewer-gif-7762551","https://tenor.com/view/penguins-hit-gif-5498544","https://tenor.com/view/slap-come-here-amanda-bynes-gif-7677089",
    "https://tenor.com/view/hit-tomandjerry-gif-7447702","https://tenor.com/view/chicas-malas-hit-and-run-bye-dad-bad-girl-gif-9152616","https://tenor.com/view/me-you-heate-gif-6106339",
    "https://tenor.com/view/3d-model-romantic-animated-from-the-back-gif-15246717","https://tenor.com/view/hump-gif-13375503","https://tenor.com/view/kill-smack-anime-gif-9955653",
    "https://tenor.com/view/im-gay-i-am-gay-im-gay-im-a-gay-man-now-gif-14573101","https://tenor.com/view/anime-barakamon-knockout-dead-gif-10942590",
    "https://tenor.com/view/bite-kill-you-angry-wolf-gif-18227410","https://tenor.com/view/gay-pride-gif-7223984"]
#troll bild -> 30, 26
    bild = schlag_liste_bilder[randint(0, 29)]
    return bild

def reaction_to_pictures():
    reactions = ['0️⃣','1️⃣','2️⃣','3️⃣','4️⃣','5️⃣','6️⃣','7️⃣','8️⃣','9️⃣','🔟','❤','🥵','😍']
    return reactions

def channel_ids(channel):
    # Channels IDs
    channel_namen = ["willkommen_channel_id","channel_id_rating_person",
    "channel_id_rating_car","channel_id_setup_rating"]
    channel_ids = [channel_ids ...]

    for x in range(4):
        if channel == channel_namen[x]:
            return channel_ids[x]
