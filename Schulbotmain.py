# --------------------------------------------------------------------------------------------------------
#                       Current Bot Version - schulbot_1.0 (release) - 28.11.2020
#               (c) for whoever sees this code - feel free to run, study, share and modify 
# --------------------------------------------------------------------------------------------------------


# DEUTSCH 

# Hallo und willkommen zum Main von unseren RS+/FOS Schulbot! Entwickelt von Admin / Python Team von
# unserem Discord-Server ( einfach den Link kopieren um zu joinen - https://discord.gg/PbyBnKf )



# ENGLISH

# Hey-ho and welcome to the main of our RS+/FOS schoolbot! Developed by admin / python team of our
# discord-server ( just copy the following link to join it - https://discord.gg/PbyBnKf )


# --------------------------------------------------------------------------------------------------------

# Changelog - last correction made by [clurky] :

# updated code structure:

# - added bot decription german/english 
# - renamed pictures variables
# - updated descriptions (german + english everywhere, except this tiny changelog)
# - repositioned some variables and structured them into item groups

# --------------------------------------------------------------------------------------------------------
#                               Vorbereitung für Code | Necessary for code
# --------------------------------------------------------------------------------------------------------

# Bibliotheken | Libraries 

import discord
import random
import requests
from datetime import datetime
from random import randint

# Channels IDs

willkommen_channel_id = Channel-ID
channel_id_rating_person = Channel-ID
channel_id_rating_car = Channel-ID
channel_id_setup_rating = Channel-ID

# Token, Keys

schulbot_token = "Schulbot-Token"
api_key = "API-KEY"

# Zeit | Current time

datetime_now = datetime.now()
time_now = datetime_now.strftime('%H:%M:%S')

# Bild für Wetterbericht | icon for weather command embed

img_weathericon = "https://i.pinimg.com/originals/77/0b/80/770b805d5c99c7931366c2e84e88f251.png"

# Bilder für Befehl Person schlagen :) | pictures for slap command

erstes_schlag = "https://img.gentside.de/article/boxen/nach-diesem-schlag-sieht-er-sterne_8f2b376896a6e50a3561d410322415cf159df13e.jpg"
zweites_schlag = "https://img.gentside.de/article/480/boxen/briggs-kostet-gerade-die-gewaltige-rechte-von-klitschko_907d9b7316d0f81108d5c646bba0cfdb63ff1552.jpg"
drittes_schlag = "https://static.dw.com/image/18071264_303.jpg"
viertes_schlag = "https://resources.stuff.co.nz/content/dam/images/1/l/a/0/t/a/image.related.StuffLandscapeSixteenByNine.710x400.1lzyeu.png/1506715007584.jpg"
fuenftes_schlag = "https://hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/concussion-1568632204.jpg"
sechstes_schlag = "https://www.cnsneurosurgery.com.au/wp-content/uploads/2015/12/concusion-boxing-300x183.jpg"
siebtes_schlag = "https://i.pinimg.com/originals/c6/86/d2/c686d29494fe02fbe3d03e5c5587ab80.jpg"
achtes_schlag = "https://cdn.yepse.com/fc/31303332303835323732_31323033343839393932.jpg?11439921363"
neuntes_schlag = "https://images-na.ssl-images-amazon.com/images/I/81tGLLntS3L.png"
zehntes_schlag = "https://itsinterestingdotcom.files.wordpress.com/2012/04/knockour-pounch.jpg"
elftens_schlag = "https://tenor.com/view/animated-couple-hit-%E6%AE%B4%E3%82%89%E3%82%8C%E3%82%8B-gif-10694370"
zwoelftes_schlag = "https://tenor.com/view/gap-slapped-knock-out-punch-gif-5122019"
dreizentes_schlag = "https://tenor.com/view/spank-tom-and-jerry-tom-puppy-hit-gif-16778355"
vierzentes_schlag = "https://tenor.com/view/punch-in-the-face-gif-14279719"
fuenfzehntes_schlag = "https://tenor.com/view/watch-out-run-you-over-gif-5729865"
sechzentes_schlag = "https://tenor.com/view/kids-falling-hit-sister-fight-siblings-gif-12112871"
achtzentes_schlag = "https://tenor.com/view/hit-punch-fight-face-viewer-gif-7762551"
neunzentes_schlag = "https://tenor.com/view/penguins-hit-gif-5498544"
zwanzigstes_schlag = "https://tenor.com/view/slap-come-here-amanda-bynes-gif-7677089"
einundzwanzigstes_schlag = "https://tenor.com/view/hit-tomandjerry-gif-7447702"
zweiundzwanzigstes_schlag = "https://tenor.com/view/chicas-malas-hit-and-run-bye-dad-bad-girl-gif-9152616"
dreiunzwanzigstes_schlag = "https://tenor.com/view/me-you-heate-gif-6106339"
vierundzwanzigstes_schlag = "https://tenor.com/view/3d-model-romantic-animated-from-the-back-gif-15246717"
fuenfundzwanzigstes_schlag = "https://tenor.com/view/hump-gif-13375503"
sexundzwanzigstes_schlag = "https://tenor.com/view/kill-smack-anime-gif-9955653" # Troll Bild
siebenundzwanzigstes_schlag = "https://tenor.com/view/im-gay-i-am-gay-im-gay-im-a-gay-man-now-gif-14573101"
achtundzwanzigstes_schlag = "https://tenor.com/view/anime-barakamon-knockout-dead-gif-10942590"
neunundzwanzigstes_schlag = "https://tenor.com/view/bite-kill-you-angry-wolf-gif-18227410"
dreisichstes_schlag = "https://tenor.com/view/gay-pride-gif-7223984" # Troll bild

# Bilder für Befehl Roulette | pictures for roulette command

gewonnen_bild = "https://tenor.com/view/win-confetti-celebration-gif-7374480"
verloren_bild = "https://tenor.com/view/alcmaria-av-verloren-lost-gif-18554382"



# !------------------------------------------------------------------------------------------------------!
# <<------------------------------------------     ~(˘▾˘~)    ------------------------------------------>>
# !------------------------------------------------------------------------------------------------------!
#                               Eigentlicher Bot Code | The bot code itself
# !------------------------------------------------------------------------------------------------------!
# <<-----------------------------------------  (ﾉ◕ヮ◕)ﾉ*:･ﾟ✧   ----------------------------------------->>
# !------------------------------------------------------------------------------------------------------!


try:
    class MyClient(discord.Client):


# Einloggen vom Bot | Bot initialization for idle
        
        async def on_ready(self):
            print("Ich habe mich eingeloggt.")

# --------------------------------------------------------------------------------------------------------
#   (Auto)    Befehl - Rolenzuteilung mit Reaktionen für neue Nutzer | Command - role on reaction
# --------------------------------------------------------------------------------------------------------

# Wird am Start im Chat eingezeigt | Shown for new users


            try:
                willkommen_channel = client.get_channel(willkommen_channel_id)

#Zum Löschen der alten Nachrichten
                await willkommen_channel.purge()

                embed_willkommen1 =discord.Embed(title="Willkommen:", description='''**Willkommen auf dem Paul von Denis Realschule Plus und Fachoberschule Server. Bitte reagiere auf einen dieser Nachrichten um Rechte auf dem Server zu bekommen, sowie deiner Klasse zugeordnet zu werden. Dieser Server wird von Schüler der Schule geführt.**''', color=0x11ff00)
                embed_willkommen1.add_field(name="👍 für Member", value ="🐻 für Developer", inline = True)
                embed_willkommen1.add_field(name="🐬 für Streamer", value="-", inline=True)
                willkommen_nachricht1 = await willkommen_channel.send(embed=embed_willkommen1)
                await willkommen_nachricht1.add_reaction('👍')
                await willkommen_nachricht1.add_reaction('🐻')
                await willkommen_nachricht1.add_reaction('🐬')

                embed_willkommen2 = discord.Embed(color=0x11ff00)
                embed_willkommen2.add_field(name="⚔ für Jahrgang 5", value="-", inline=True)
                embed_willkommen2.add_field(name="🎳 für Jahrgan 6", value="💡 für Klasse 7a", inline=True)
                embed_willkommen2.add_field(name="📁 für Klasse 7b", value="🐘 für Klasse 7c", inline=True)
                embed_willkommen2.add_field(name="💼 für Klasse 7d", value="🦉 für Jahrgang 7", inline=True)
                embed_willkommen2.add_field(name="⚡  für Klasse 8a", value="👴 für Klasse 8b", inline=True)
                willkommen_nachricht2 = await willkommen_channel.send(embed=embed_willkommen2)
                await willkommen_nachricht2.add_reaction('⚔')
                await willkommen_nachricht2.add_reaction('🎳')
                await willkommen_nachricht2.add_reaction('💡')
                await willkommen_nachricht2.add_reaction('📁')
                await willkommen_nachricht2.add_reaction('🐘')
                await willkommen_nachricht2.add_reaction('💼')
                await willkommen_nachricht2.add_reaction('🦉')
                await willkommen_nachricht2.add_reaction('⚡')
                await willkommen_nachricht2.add_reaction('👴')

                embed_willkommen3 = discord.Embed(color=0x11ff00)
                embed_willkommen3.add_field(name="👎 für Klasse 8c", value="🌐 für Klasse 8d", inline=True)
                embed_willkommen3.add_field(name="🏈 für Jahrgang 8", value="-", inline=True)
                embed_willkommen3.add_field(name="🏺 für Klasse 9a", value="🍍 für Klasse 9b", inline=True)
                embed_willkommen3.add_field(name="🎣 für Klasse 9c", value="💎 für Klasse 9d", inline=True)
                embed_willkommen3.add_field(name="⚓ für Jahrgang 9", value="📶 für Klasse 10a", inline=True)
                embed_willkommen3.add_field(name="🔥 für Klasse 10b", value="👀 für Klasse 10c", inline=True)
                willkommen_nachricht3=await willkommen_channel.send(embed=embed_willkommen3)
                await willkommen_nachricht3.add_reaction('👎')
                await willkommen_nachricht3.add_reaction('🌐')
                await willkommen_nachricht3.add_reaction('🏈')
                await willkommen_nachricht3.add_reaction('🏺')
                await willkommen_nachricht3.add_reaction('🍍')
                await willkommen_nachricht3.add_reaction('🎣')
                await willkommen_nachricht3.add_reaction('💎')
                await willkommen_nachricht3.add_reaction('⚓')
                await willkommen_nachricht3.add_reaction('📶')
                await willkommen_nachricht3.add_reaction('🔥')
                await willkommen_nachricht3.add_reaction('👀')


                embed_willkommen4 = discord.Embed(color=0x11ff00)
                embed_willkommen4.add_field(name="💙 für Klasse 10d", value="❗ für Jahrgang 10", inline=True)
                embed_willkommen4.add_field(name="🏝 für Klasse 11a", value="👽 für Klasse 11b", inline=True)
                embed_willkommen4.add_field(name="⛏ für Jahrgang 11", value="🚗 für Klasse 12a", inline=True)
                embed_willkommen4.add_field(name="🥑 für Klasse 12b", value="🦄 für Jahrgang 12", inline=True)
                embed_willkommen4.add_field(name="✈ für Realschule Plus", value="🛁 für FOS", inline=True)
                willkommen_nachricht4=await willkommen_channel.send(embed=embed_willkommen4)
                await willkommen_nachricht4.add_reaction('💙')
                await willkommen_nachricht4.add_reaction('❗')
                await willkommen_nachricht4.add_reaction('🏝')
                await willkommen_nachricht4.add_reaction('👽')
                await willkommen_nachricht4.add_reaction('⛏')
                await willkommen_nachricht4.add_reaction('🚗')
                await willkommen_nachricht4.add_reaction('🥑')
                await willkommen_nachricht4.add_reaction('🦄')
                await willkommen_nachricht4.add_reaction('✈')
                await willkommen_nachricht4.add_reaction('🛁')


            except Exception as error_willkommen:
                print("Fehler bei der Willkommensnachricht: ")
                print(error_willkommen)

# Wenn eine Reaktion gibt, Rolenzuteilung | Role events on user reaction

        async def on_reaction_add(self, reaction, user):
            reaction_von_channel = reaction.message.channel.id
            if reaction_von_channel == willkommen_channel_id:
                a= discord.utils.get(user.guild.roles, name="Member")
                f= discord.utils.get(user.guild.roles, name="Jahrgang 5")
                k= discord.utils.get(user.guild.roles, name="Jahrgang 6")
                l= discord.utils.get(user.guild.roles, name="Klasse 7a")
                m= discord.utils.get(user.guild.roles, name="Klasse 7b")
                n= discord.utils.get(user.guild.roles, name="Klasse 7c")
                o= discord.utils.get(user.guild.roles, name="Klasse 7d")
                p= discord.utils.get(user.guild.roles, name="Jahrgang 7")
                q= discord.utils.get(user.guild.roles, name="Klasse 8a")
                r= discord.utils.get(user.guild.roles, name="Klasse 8b")
                s= discord.utils.get(user.guild.roles, name="Klasse 8c")
                t= discord.utils.get(user.guild.roles, name="Klasse 8d")
                u= discord.utils.get(user.guild.roles, name="Jahrgang 8")
                v= discord.utils.get(user.guild.roles, name="Klasse 9a")
                w= discord.utils.get(user.guild.roles, name="Klasse 9b")
                x= discord.utils.get(user.guild.roles, name="Klasse 9c")
                y= discord.utils.get(user.guild.roles, name="Klasse 9d")
                z= discord.utils.get(user.guild.roles, name="Jahrgang 9")
                ab= discord.utils.get(user.guild.roles, name="Klasse 10a")
                bb= discord.utils.get(user.guild.roles, name="Klasse 10b")
                cb= discord.utils.get(user.guild.roles, name="Klasse 10c")
                db= discord.utils.get(user.guild.roles, name="Klasse 10d")
                eb= discord.utils.get(user.guild.roles, name="Jahrgang 10")
                fb= discord.utils.get(user.guild.roles, name="Klasse 11a")
                gb= discord.utils.get(user.guild.roles, name="Klasse 11b")
                hb= discord.utils.get(user.guild.roles, name="Jahrgang 11")
                ib= discord.utils.get(user.guild.roles, name="Klasse 12a")
                jb= discord.utils.get(user.guild.roles, name="Klasse 12b")
                kb= discord.utils.get(user.guild.roles, name="Jahrgang 12")
                lb= discord.utils.get(user.guild.roles, name="Realschule Plus-Schifferstadt")
                mb= discord.utils.get(user.guild.roles, name="FOS-Schifferstadt")
                nb= discord.utils.get(user.guild.roles, name="Streamer")
                pb= discord.utils.get(user.guild.roles, name="Developer")

    # Rolenprüfung | Role checking

                if  user == client.user:
                    pass
                elif str(reaction.emoji) == "👍":
                    await user.add_roles(a)
                elif str(reaction.emoji) == "⚔":
                    await user.add_roles(f)
                elif str(reaction.emoji) == "🎳":
                    await user.add_roles(k)
                elif str(reaction.emoji) == "💡":
                    await user.add_roles(l)
                elif str(reaction.emoji) == "📁":
                    await user.add_roles(m)
                elif str(reaction.emoji) == "🐘":
                    await user.add_roles(n)
                elif str(reaction.emoji) == "💼":
                    await user.add_roles(o)
                elif str(reaction.emoji) == "🦉":
                    await user.add_roles(p)
                elif str(reaction.emoji) == "⚡":
                    await user.add_roles(q)
                elif str(reaction.emoji) == "👴":
                    await user.add_roles(r)
                elif str(reaction.emoji) == "👎":
                    await user.add_roles(s)
                elif str(reaction.emoji) == "🌐":
                    await user.add_roles(t)
                elif str(reaction.emoji) == "🏈":
                    await user.add_roles(u)
                elif str(reaction.emoji) == "🏺":
                    await user.add_roles(v)
                elif str(reaction.emoji) == "🍍":
                    await user.add_roles(w)
                elif str(reaction.emoji) == "🎣":
                    await user.add_roles(x)
                elif str(reaction.emoji) == "💎":
                    await user.add_roles(y)
                elif str(reaction.emoji) == "⚓":
                    await user.add_roles(z)
                elif str(reaction.emoji) == "📶":
                    await user.add_roles(ab)
                elif str(reaction.emoji) == "🔥":
                    await user.add_roles(bb)
                elif str(reaction.emoji) == "👀":
                    await user.add_roles(cb)
                elif str(reaction.emoji) == "💙":
                    await user.add_roles(db)
                elif str(reaction.emoji) == "❗":
                    await user.add_roles(eb)
                elif str(reaction.emoji) == "🏝":
                    await user.add_roles(fb)
                elif str(reaction.emoji) == "👽":
                    await user.add_roles(gb)
                elif str(reaction.emoji) == "⛏":
                    await user.add_roles(hb)
                elif str(reaction.emoji) == "🚗":
                    await user.add_roles(ib)
                elif str(reaction.emoji) == "🥑":
                    await user.add_roles(jb)
                elif str(reaction.emoji) == "🦄":
                    await user.add_roles(kb)
                elif str(reaction.emoji) == "✈":
                    await user.add_roles(lb)
                elif str(reaction.emoji) == "🛁":
                    await user.add_roles(mb)
                elif str(reaction.emoji) == "🐬":
                    await user.add_roles(nb)
                elif str(reaction.emoji) == "🐻":
                    await user.add_roles(pb)

# --------------------------------------------------------------------------------------------------------
#                           Befehl - Hilfe für Befehlsliste | Command - help
# --------------------------------------------------------------------------------------------------------
         
# Damit der Bot nicht auf seine Nachrichten reagiert | Bot should ignore his own messages

        async def on_message(self, message):
            if message.author == client.user:
                return

            elif message.content == "$help": #color=0x11ff00 17 255
                embed_help=discord.Embed(title="Du kannst folgende dreckige Dinge mit mir anstellen:", color = 0x11ff00)
                embed_help.add_field(name="hello bot:",value ="Frage nach Bot",inline=True)
                embed_help.add_field(name="$playgame:",value ="Beschreibung von Roulette",inline=True)
                embed_help.add_field(name="$playroulette (Variable):",value ="Start einer Roulett runde", inline = True)
                embed_help.add_field(name="$plscontactme:",value ="Private Kontakt aufnahme", inline = True)
                embed_help.add_field(name="$wetter (ort):",value ="Abfrage des Wetters", inline = True)
                embed_help.add_field(name="$wetter2 (ort):", value ="Ausführliche abfrage", inline = True)
                embed_help.add_field(name="$slap(person):", value ="Um jemanden zu Schlagen", inline = True)
                await message.channel.send(embed=embed_help)
# --------------------------------------------------------------------------------------------------------
#                       Abfrage ob der Bot Aktiv ist | Checking if bot is okay
# --------------------------------------------------------------------------------------------------------

            elif message.content.startswith("hello bot"):
                embed_aktiv = discord.Embed(title="Ich bin aktiv!", color = 0x11ff00)
                await message.channel.send(embed=embed_aktiv)

# --------------------------------------------------------------------------------------------------------
#                               Befehl - Person Schlagen | Command - slap person
# --------------------------------------------------------------------------------------------------------

            elif message.content.startswith("$slap "):
                
                try:

                    geschlagene_person = message.content.split(' ')[1]
                    schlag_liste = [erstes_schlag, zweites_schlag, drittes_schlag, viertes_schlag, fuenftes_schlag, sechstes_schlag,
                                    siebtes_schlag, achtes_schlag, neuntes_schlag, zehntes_schlag, elftens_schlag, zwoelftes_schlag,
                                    dreizentes_schlag, vierzentes_schlag, fuenfzehntes_schlag, sechzentes_schlag, achtzentes_schlag,
                                    neunzentes_schlag, zwanzigstes_schlag, einundzwanzigstes_schlag, zweiundzwanzigstes_schlag, dreiunzwanzigstes_schlag,
                                    vierundzwanzigstes_schlag, fuenfundzwanzigstes_schlag, sexundzwanzigstes_schlag, siebenundzwanzigstes_schlag, achtundzwanzigstes_schlag,
                                    neunundzwanzigstes_schlag, dreisichstes_schlag]
                    schlag = schlag_liste[randint(0, 29)]
                    await message.channel.send(f"UFFF, {geschlagene_person} wurde geschlagen!")
                    await message.channel.send(schlag)


                    
                except Exception as error_schlag:
                    print("Fehler beim Schlagen")
                    print(error_schlag)
                    embed_fataler_error = discord.Embed(title="Fataler Error ",description="Leider ist ein Fataler Fehler Aufgetreten, bitte kontaktiere sofort einen Admin!",color=0xf50505)
                    embed_fataler_error.set_thumbnail(url="https://www.aufkleberdealer.de/images/www.aufkleberdealer.de/product/84184_autoaufkleber-totenkopf-skull_1.jpg")
                    await message.channel.send(embed=embed_fataler_error)

# --------------------------------------------------------------------------------------------------------
#                       Befehl - Spielliste | Command - games list
# --------------------------------------------------------------------------------------------------------
                    
            elif message.content.startswith("$playgame"):
                embed_roulette_regeln = discord.Embed(title="Spiel Roulette:", color = 0x11ff00)
                embed_roulette_regeln.add_field(name="Für Roulette:", value ="$playroulette (BID) eigeben, wobei BID steht für:", inline= False)
                embed_roulette_regeln.add_field(name="balck", value="- $roulette black", inline=False)
                embed_roulette_regeln.add_field(name="red", value="- $roulette red", inline=False)
                embed_roulette_regeln.add_field(name="number", value="- $roulette 0-36", inline=False)
                await message.channel.send(embed=embed_roulette_regeln)

# --------------------------------------------------------------------------------------------------------
#                       Befehl - Privaterkontakt | Command - plscontactme
# --------------------------------------------------------------------------------------------------------

            elif message.content.startswith("$plscontactme"):
                embed_contact = discord.Embed(title="Hier bin ich, was kann ich für dich tun?", color = 0x11ff00)
                await message.author.send(embed=embed_contact)

# --------------------------------------------------------------------------------------------------------
#                           Befehl - Wetterabfrage | Command - weather
# --------------------------------------------------------------------------------------------------------

            elif message.content.startswith("$wetter "):
                
                try:
                    datetime_now = datetime.now()
                    time_now = datetime_now.strftime('%H:%M:%S')
                    City = message.content.split(' ')[1]
                    url = f'https://api.openweathermap.org/data/2.5/weather?q={City}&appid={api_key}&units=metric'
                    data = requests.get(url).json()

                    temperatur = data['main']['temp']
                    feuchtigkeit = data['main']['humidity']

                    embed_weathern = discord.Embed(color=0x00eaff)
                    embed_weathern.set_author(name=f"{City}", icon_url=img_weathericon)
                    embed_weathern.add_field(name="**Temparatur**", value=f"{temperatur}°C")
                    embed_weathern.add_field(name="**Luftfeuchtigkeit**", value=f"{feuchtigkeit}%")
                    embed_weathern.set_footer(text=f"{time_now}")

                    await message.channel.send(embed=embed_weathern)

                #Rückgabe von Error
                except Exception as errorwetter:
                    print("Error Wetter:")
                    print(errorwetter)
                    embed_error = discord.Embed(title="Error",description="Leider ist ein Fehler Aufgetreten, bitte kontrolliere deine Eingabe oder kontaktiere einen Admin!",color=0xf50505)
                    embed_error.set_thumbnail(url="https://www.padtinc.com/blog/wp-content/uploads/2020/09/plc-errors.jpg")
                    await message.channel.send(embed=embed_error)

            elif message.content.startswith("$wetter2 "):

                try:
                    datetime_now = datetime.now()
                    time_now = datetime_now.strftime('%H:%M:%S')
                    City = message.content.split(' ')[1]
                    url = f'https://api.openweathermap.org/data/2.5/weather?q={City}&appid={api_key}&units=metric'
                    data = requests.get(url).json()

                    temperatur = data['main']['temp']
                    feuchtigkeit = data['main']['humidity']
                    feel_temperatur = data['main']['feels_like']
                    temperatur_minimum= data['main']['temp_min']
                    temperatur_maximum= data['main']['temp_max']
                    luft_druck= data['main']['pressure']
                    sichtweite = data['visibility']

                    embed_weathern = discord.Embed(color=0x00eaff)
                    embed_weathern.set_author(name=f"{City}", icon_url=img_weathericon)
                    embed_weathern.add_field(name="**Temparatur**", value=f"{temperatur}°C")
                    embed_weathern.add_field(name="**Gefühlte Temperatur**", value=f"{feel_temperatur}°C")
                    embed_weathern.add_field(name="**Temperatur Minimum**", value=f"{temperatur_minimum}°C")
                    embed_weathern.add_field(name="**Temperatur Maximum**", value=f"{temperatur_maximum}°C")
                    embed_weathern.add_field(name="**Luftfeuchtigkeit**", value=f"{feuchtigkeit}%")
                    embed_weathern.add_field(name="**Luftdruck**", value=f"{luft_druck}bar")
                    embed_weathern.add_field(name="**Sichtweite**", value=f"{sichtweite}m")
                    embed_weathern.set_footer(text=f"{time_now}")

                    await message.channel.send(embed=embed_weathern)

                #rückgabe von Error
                except Exception as errorwetter2:
                    print("Error Wetter:")
                    print(errorwetter2)
                    embed_error=discord.Embed(title="Error",description="Leider ist ein Fehler Aufgetreten, bitte kontrolliere deine Eingabe oder kontaktiere einen Admin!",color=0xf50505)
                    embed_error.set_thumbnail(url="https://www.padtinc.com/blog/wp-content/uploads/2020/09/plc-errors.jpg")
                    await message.channel.send(embed=embed_error)
# --------------------------------------------------------------------------------------------------------
#                       Befehl - Roulette das Spiel | Command - the roullete game
# --------------------------------------------------------------------------------------------------------
                    
            if message.content.startswith("$playroulette "):
                
                bid = message.content.split(' ')[1]
                bid_param = 1
                
                if bid.lower() == "black":
                    bid_param = 2
                elif bid.lower() == "red":
                    bid_param = 3
                else:
                    try:
                        bid_param = int(bid)
                    except:
                        bid_param = 1
                        
                if bid_param == 1:
                    embed_ungueltig = discord.Embed(title="Das ist eine Ungültige Eingabe!", color = 0x11ff00)
                    await message.channel.send(embed=embed_ungueltig)
                    return

                result = random.randint(0,36)
                
                if bid_param == 2:
                    won = result%2 == 0 and not result == 0
                elif bid_param == 3:
                    won = result %2 == 1
                else:
                    won = result == bid_param

                if won:
                    embed_win = discord.Embed(title="$$$ Du hast gewonnen! $$$", color=0x11ff00)
                    await message.channel.send(embed=embed_win)
                    await message.channel.send(gewonnen_bild)
                else:
                    embed_verloren = discord.Embed(title="Du hast leider verloren!", color=0x11ff00)
                    await message.channel.send(embed=embed_verloren)
                    await message.channel.send(verloren_bild)

# --------------------------------------------------------------------------------------------------------
#                       Befehl - Rating  | Command - the rating
# --------------------------------------------------------------------------------------------------------

            message_von_channel = message.channel.id
            if message_von_channel == channel_id_rating_person:
                await message.add_reaction('0️⃣')
                await message.add_reaction('1️⃣')
                await message.add_reaction('2️⃣')
                await message.add_reaction('3️⃣')
                await message.add_reaction('4️⃣')
                await message.add_reaction('5️⃣')
                await message.add_reaction('6️⃣')
                await message.add_reaction('7️⃣')
                await message.add_reaction('8️⃣')
                await message.add_reaction('9️⃣')
                await message.add_reaction('🔟')
                await message.add_reaction('❤')
                await message.add_reaction('🥵')
                await message.add_reaction('😍')
            elif message_von_channel == channel_id_rating_car:
                await message.add_reaction('0️⃣')
                await message.add_reaction('1️⃣')
                await message.add_reaction('2️⃣')
                await message.add_reaction('3️⃣')
                await message.add_reaction('4️⃣')
                await message.add_reaction('5️⃣')
                await message.add_reaction('6️⃣')
                await message.add_reaction('7️⃣')
                await message.add_reaction('8️⃣')
                await message.add_reaction('9️⃣')
                await message.add_reaction('🔟')
                await message.add_reaction('❤')
                await message.add_reaction('🥵')
                await message.add_reaction('😍')
            elif message_von_channel == channel_id_setup_rating:
                await message.add_reaction('0️⃣')
                await message.add_reaction('1️⃣')
                await message.add_reaction('2️⃣')
                await message.add_reaction('3️⃣')
                await message.add_reaction('4️⃣')
                await message.add_reaction('5️⃣')
                await message.add_reaction('6️⃣')
                await message.add_reaction('7️⃣')
                await message.add_reaction('8️⃣')
                await message.add_reaction('9️⃣')
                await message.add_reaction('🔟')
                await message.add_reaction('❤')
                await message.add_reaction('🥵')
                await message.add_reaction('😍')




    client = MyClient()
    client.run(schulbot_token)

except Exception as error1:
    print("Allgemeiner Großer Fehler!")
    print(error1)


# --------------------------------------------------------------------------------------------------------
#                   Zusatz - Hilfe für Entwickler | Extras - help sheet for developers
# --------------------------------------------------------------------------------------------------------

# async def on_message(self, message):
# print(str(message.channel.id))

