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


import random
import requests
from Verarbeitung import *
from datetime import datetime
from discord.ext import commands
import asyncio

# Token, Keys

schulbot_token = "bot-token"
api_key = "wetter-key"

# Zeit | Current time

datetime_now = datetime.now()
time_now = datetime_now.strftime('%H:%M:%S')

# Bild für Wetterbericht | icon for weather command embed

img_weathericon = "https://i.pinimg.com/originals/77/0b/80/770b805d5c99c7931366c2e84e88f251.png"

# Bilder für Befehl Roulette | pictures for roulette command

gewonnen_bild = "https://tenor.com/view/win-confetti-celebration-gif-7374480"
verloren_bild = "https://tenor.com/view/alcmaria-av-verloren-lost-gif-18554382"

#global variable für einmal ausführung |
ausfuehrung = 0

# !------------------------------------------------------------------------------------------------------!
# <<------------------------------------------     ~(˘▾˘~)    ------------------------------------------>>
# !------------------------------------------------------------------------------------------------------!
#                               Eigentlicher Bot Code | The bot code itself
# !------------------------------------------------------------------------------------------------------!
# <<-----------------------------------------  (ﾉ◕ヮ◕)ﾉ*:･ﾟ✧   ----------------------------------------->>
# !------------------------------------------------------------------------------------------------------!

intents = discord.Intents.default()
client = commands.Bot(
    command_prefix="$",
    help_command=None,
    intents=intents
)


# Einloggen vom Bot | Bot initialization for idle
@client.event
async def on_connect():
        print("[Ich habe mich eingeloggt]...")
        client.loop.create_task(aufgabe())
        #client.loop.create_task(change_status())

# --------------------------------------------------------------------------------------------------------
#   (Auto)    Befehl - Rolenzuteilung mit Reaktionen für neue Nutzer | Command - role on reaction
# --------------------------------------------------------------------------------------------------------

# Wird am Start im Chat angezeigt | Shown for new users

async def aufgabe():
    global ausfuehrung
    if ausfuehrung == 0:
        ausfuehrung = 1
        try:
            willkommen_channel = client.get_channel(channel_informationen_id('willkommen_channel'))
#Zum Löschen der alten Nachrichten
            try:
                await client.wait_until_ready()
                await willkommen_channel.purge()
                
            except:
                print('Fehler beim Löschen')
            embed_willkommen_nachricht =discord.Embed(title="Willkommen:", description='''**Willkommen auf dem Paul von Denis Realschule Plus und Fachoberschule Server. Bitte reagiere auf einen dieser Nachrichten um Rechte auf dem Server zu bekommen, sowie deiner Klasse zugeordnet zu werden. Dieser Server wird von Schüler der Schule geführt.**''', color=0x11ff00)
            await willkommen_channel.send(embed=embed_willkommen_nachricht)


            for x in range(3):
                embed_willkommen_nachricht_rollen = discord.Embed(color=0x11ff00)
                embed_willkommen_nachricht_rollen .add_field(name=message_content()[x][0], value=message_content()[x][1], inline=True)
                embed_willkommen_nachricht_rollen .add_field(name=message_content()[x][2], value=message_content()[x][3], inline=True)
                embed_willkommen_nachricht_rollen .add_field(name=message_content()[x][4], value=message_content()[x][5], inline=True)
                embed_willkommen_nachricht_rollen .add_field(name=message_content()[x][6], value=message_content()[x][7], inline=True)
                embed_willkommen_nachricht_rollen .add_field(name=message_content()[x][8], value=message_content()[x][9], inline=True)
                embed_willkommen_nachricht_rollen .add_field(name=message_content()[x][10], value='-', inline=True)
                embed_willkommen_nachricht_rollen  = await willkommen_channel.send(embed=embed_willkommen_nachricht_rollen )
                await embed_willkommen_nachricht_rollen.add_reaction(message_emoji()[x][0])
                await embed_willkommen_nachricht_rollen.add_reaction(message_emoji()[x][1])
                await embed_willkommen_nachricht_rollen.add_reaction(message_emoji()[x][2])
                await embed_willkommen_nachricht_rollen.add_reaction(message_emoji()[x][3])
                await embed_willkommen_nachricht_rollen.add_reaction(message_emoji()[x][4])
                await embed_willkommen_nachricht_rollen.add_reaction(message_emoji()[x][5])
                await embed_willkommen_nachricht_rollen.add_reaction(message_emoji()[x][6])
                await embed_willkommen_nachricht_rollen.add_reaction(message_emoji()[x][7])
                await embed_willkommen_nachricht_rollen.add_reaction(message_emoji()[x][8])
                await embed_willkommen_nachricht_rollen.add_reaction(message_emoji()[x][9])
                await embed_willkommen_nachricht_rollen.add_reaction(message_emoji()[x][10])

        except Exception as error_willkommen:
            print("Fehler bei der Willkommensnachricht: ")
            print(error_willkommen)

# Wenn eine Reaktion gibt, Rolenzuteilung | Role events on user reaction
@client.event
async def on_reaction_add(reaction, user):
    reaction_von_channel = reaction.message.channel.id
    if reaction_von_channel == channel_id_infomation("willkommen_channel_id"):
# Rolenprüfung | Role checking

        if user == client.user:
            pass
        for x in range(33):
            if str(reaction.emoji) == rollen_emojis()[x]:
                await user.add_roles(rollen_k(x, user))

# --------------------------------------------------------------------------------------------------------
#                           Befehl - Hilfe für Befehlsliste | Command - help
# --------------------------------------------------------------------------------------------------------
         
# Damit der Bot nicht auf seine Nachrichten reagiert | Bot should ignore his own messages
@client.event
async def on_message(message):
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
            schlag = schlagen()
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
    if message_von_channel == channel_id_infomation("channel_id_rating_person"):
        for x in range(13):
            await message.add_reaction(reaction_to_pictures()[x])
    elif message_von_channel == channel_id_infomation("channel_id_rating_car"):
        for x in range(13):
            await message.add_reaction(reaction_to_pictures()[x])
    elif message_von_channel == channel_id_infomation("channel_id_setup_rating"):
        for x in range(13):
            await message.add_reaction(reaction_to_pictures()[x])


async def change_status():
    while True:
        try:
            await client.change_presence(activity=discord.Activity(
                type=discord.ActivityType.playing,
                name="Verarbeitet Informationen!",
                status=discord.Status.online))
            await asyncio.sleep(7.5)
            await client.change_presence(activity=discord.Activity(
                type=discord.ActivityType.listening,
                name="Empfängt neue Informationen!",
                status=discord.Status.do_not_disturb))
            await asyncio.sleep(7.5)
        except:
            pass


client.run(schulbot_token)
