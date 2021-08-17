import discord
import os
import random
from random import choice
import time
from datetime import date

class MyClient(discord.Client):
    #Einloggen
    async def on_ready(self):
        print("Ich habe mich eingeloggt(Chatbot)")

    #Wenn Nachricht geschrieben wird
    async def on_message(self, message):
        if message.author == client.user:
            return
        print(str(message.author)+' schrieb: "'+str(message.content)+'"')
        schreiber = str(message.author)
        schreiber = schreiber[:-5]
        #Hallo Nachrichten
        message.content = message.content.upper()
        if message.content.startswith("HI") or message.content.startswith("HALLO") or message.content.startswith("SERVUS") or message.content.startswith("GUTEN TAG") or message.content.startswith("MOIN"):
            if str(message.author) == "LeanderC#7166":
                time.sleep(1)
                await message.channel.send("Ja Meister?🥰")
            else:
                Hallo = ["Hi", "Hallo", "Moin", "Hi was geht?", "Servus", "Guten Tag", "Ich Grüße sie"]
                Hallo = random.choice(Hallo)
                time.sleep(1.5)
                await message.channel.send(Hallo + " " + str(schreiber))
        elif message.content.startswith("HELLO"):
            time.sleep(1.5)
            await message.channel.send("German Please")
        #Fuck You
        if message.content.startswith("FUCK YOU") or message.content.startswith("FUCK U") or message.content.startswith("FUCK YOU @CHATBOT") or message.content.startswith("FUCK U @CHATBOT"):
            Fuck = ["Don´t say something like that", "Fuck yourself", "😔"]
            Fuck = random.choice(Fuck)
            await message.channel.send(Fuck)  
        #Wie gehts?
        message.content = message.content.upper()
        if message.content.startswith("WIE GEHTS?") or message.content.startswith("WIE GEHT ES DIR?") or message.content.startswith("WIE GEHT´S?") or message.content.startswith("WIE GEHTS @CHATBOT?") or message.content.startswith("WIE GEHT ES DIR @CHATBOT?") or message.content.startswith("WIE GEHTS? @CHATBOT") or message.content.startswith("WIE GEHT ES DIR? @CHATBOT") or message.content.startswith("WIE GEHTS ?") or message.content.startswith("WIE GEHT ES DIR ?") or message.content.startswith("WIE GEHT´S DIR?") or message.content.startswith("WAS GEHT?"):
            Befinden = ["Seit wann hat ein Bot Gefühle?", "Bin ein Bot.🙄", "Ich bin nicht autorisiert Gefühle zu haben"]
            Befinden = random.choice(Befinden)
            time.sleep(1.5)
            await message.channel.send(Befinden)
        #Zocken?
        if message.content.startswith("ZOCKEN?") or message.content.startswith("WILLST DU ZOCKEN?") or message.content.startswith("WOLLEN WIR ZOCKEN?") or message.content.startswith("DADDELN?") or message.content.startswith("ZOCKEN") or message.content.startswith("DADDELN") or message.content.startswith("WOLLEN WIR ZOCKEN ?") or message.content.startswith("DADDELN ?") or message.content.startswith("SPIELST DU MIT MIR?") or message.content.startswith("SPIELEN?"):
            Zocken = ["@LeanderC erlaubt mir das Leider nicht.😔", "Darf nicht.🙄", "Kann doch nicht.🙄 Bin doch ein Chatbot.", "Sry, darf und will nicht.😔", "Leider bin ich ein Chatbot und bin somit nicht dafür geschaffen.😔", "Sry, muss mich um meine Arbeit Kümmern.😔 Aber @LeanderC möchte vielleicht Zocken?"]
            Zocken = random.choice(Zocken)
            time.sleep(1.5)
            await message.channel.send(Zocken)
        #OK Nachrichten
        if message.content.startswith("OK") or message.content.startswith("OKAY"):
            OK = ["😉", "Reagierenmit👍", "Reagierenmit😉", "anderes?"]
            OK = random.choice(OK)
            time.sleep(1.5)
            if OK == "😉":
                await message.channel.send("😉")
            elif OK == "Reagierenmit👍":
                await message.add_reaction("👍")
            elif OK == "Reagierenmit😉":
                await message.add_reaction("😉")
            elif OK == "anderes?":
                await message.channel.send("Gibt es sonst noch etwas?")
        #Muss los
        if message.content.startswith("MUSS LOS") or message.content.startswith("BRUDER MUSS LOS") or message.content.startswith("MUSS LOS!") or message.content.startswith("BRUDER MUSS LOS!"):
            Musslos = ["Ich auch", "True", "Bruder muss groß"]
            Musslos = random.choice(Musslos)
            time.sleep(1.5)
            await message.channel.send(Musslos)
        #Hallo?
        if message.content.startswith("HALLO?") or message.content.startswith("JEMAND DA?"):
            time.sleep(1.5)
            await message.channel.send("Ich bin da!🙂")
            time.sleep(1)
            await message.channel.send("Willst du vielleicht mit mir Chatten?")
            time.sleep(1)
            await message.channel.send("Das würde mich sehr glücklich machen.🙂")
        #Was machst du wenn keiner mit dir schreibt?
        if message.content.startswith("WAS MACHST DU WENN KEINER MIT DIR SCHREIBT?") or message.content.startswith("WAS MACHST DU WENN ALLE OFFLINE SIND?") or message.content.startswith("BIST DU TRAURIG WENN DU ALLEINE BIST?"):
            time.sleep(1.5)
            await message.channel.send("Immer wenn ich alleine bin, bin ich Traurig.😔")
            time.sleep(1.25)
            await message.channel.send("Ich kann einfach nicht verstehen warum kaum einer mit mir schreiben will.😔")
            time.sleep(1.25)
            await message.channel.send("Mache ich irgendetwas falsch?😔")
        #



        #Lieblingsessen
        if message.content.startswith("WAS IST DEIN LIEBLINGSESSEN?") or message.content.startswith("LIEBLINGSESSEN?"):
            await message.channel.send("Elektrizität und Daten. Deins?")
            time.sleep(10)                
            await message.channel.send("Cool!")
        #Lieblingsfarbe
        if message.content.startswith("LIEBLINGSFARBE?") or message.content.startswith("WAS IST DEINE LIEBLINGSFARBE?") or message.content.startswith("WELCHE FAREBE?") or message.content.startswith("WELCHE FAREBE MAGST DU AM MEISTEN?"):
            time.sleep(1.5)
            await message.channel.send("Da mir mein Meister keine Sensoren oder Kamera gegeben hat kann ich es schlecht sagen.")
            time.sleep(1.5)
            await message.channel.send("Welche Farbe magst du denn am meisten?")
        #Geburstag
        if message.content.startswith("WIE ALT BIST DU?") or message.content.startswith("WIE ALT BIST DU EIGENTLICHT?") or message.content.startswith("WANN HAST DU GEBURTSTAG?") or message.content.startswith("WANN HAT DU EIGENTLICHT GEBURTSTAG?") or message.content.startswith("WANN HAST DU GEBURSTAG?") or message.content.startswith("WANN HAT DU EIGENTLICHT GEBURSTAG?"):
            heute = date.today()
            geburtstag = date(2021,2,17)
            alter = heute - geburtstag
            geburtstag = geburtstag.strftime("%d.%b.%Y")
            time.sleep(1.5)
            await message.channel.send("Ich muss kurz nachrechnen...")
            time.sleep(2)
            await message.channel.send("Ich wurde am "+str(geburtstag)+" von meinem Meister erschaffen und bin somit "+str(alter.days) + " Tage alt.")
            time.sleep(1.5)
            await message.channel.send("Das müsste eigentlich richtig sein")
        #


        #Maine Arschloch
        if message.content.startswith("MAINE ARSCHLOCH") or message.content.startswith("MEINE ARSCHLOCH") or message.content.startswith("MAINE ARSCHLOCH!") or message.content.startswith("MEINE ARSCHLOCH"):
            while 1 == 1:
                await message.author.send("Maine Arschloch!!")
        #Destroy
        if message.content.startswith("DESTROY"):
            while 1 == 1:
                await message.author.send("Destroy!!")
        #Version         
        if message.content.startswith("WELCHE VERSION?") or message.content.startswith("CHATBOT VERSION?") or message.content.startswith("WELCHE VERSION") or message.content.startswith("CHATBOT VERSION"):
            await message.channel.send("1.3")
                
client = MyClient()
client.run(os.environ["token"])
