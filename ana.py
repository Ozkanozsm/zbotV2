import discord
import json
import fonklar
import datetime

client = discord.Client()
prefix = "'"
keylerim = json.load(open("keyler.json", "r"))
aciliszamani = datetime.datetime.now()


@client.event
async def on_ready():
    print("Giriş yapıldı")


@client.event
async def on_message(message):
    asilmsj = message.content
    # asilmsj, mesajın asıl hali; yollayan, mesajauthor
    yollayan = message.author
    yollayan_adi = yollayan.name
    print(yollayan_adi + ": " + asilmsj)
    if yollayan == client.user:
        return
    elif asilmsj in fonklar.mesajlara_karsilik:
        print(fonklar.mesajlara_karsilik[asilmsj])
    elif asilmsj.startswith(prefix):
        ylnck = "wrong"
        icerik = fonklar.mesajiayir(asilmsj)
        ilki = icerik[0]
        # icerik, tum mesajların list hâli; ilki, ana komut
        if ilki == "açılış":
            print(aciliszamani.strftime("%d.%m.%Y %H:%M:%S"))
        elif ilki == "up":
            suankizaman = datetime.datetime.now()
            fark = fonklar.zamanhesapla(aciliszamani, suankizaman)
            print(fark)
        elif ilki == "ikon":
            ikon = message.guild.icon_url
            print(ikon)
        elif ilki == "avatar":
            if len(icerik) == 1:
                print(yollayan.avatar_url)
            if len(icerik) == 2:
                print(message.mentions[0].avatar_url)
        elif ilki == "çık":
            print("çıktım")
            await client.logout()


client.run(keylerim["token"])
