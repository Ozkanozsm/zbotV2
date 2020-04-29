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
    # asilmsj, mesajın asıl hali
    yollayan = message.author.name
    print(yollayan + ": " + asilmsj)
    # resim falan atıldığında resim atıldı yazdır
    if message.author == client.user:
        return
    if asilmsj.startswith(prefix):
        icerik = fonklar.mesajiayir(asilmsj)
        ilki = icerik[0]
        print(type(icerik))
        # icerik, tum mesajların list hâli; ilki, ana komut
        if ilki == "açılış":
            print(aciliszamani.strftime("%d.%m.%Y %H:%M:%S"))
        elif ilki == "up":
            suankizaman = datetime.datetime.now()
            fark = fonklar.zamanhesapla(aciliszamani, suankizaman)
            print(fark)
        elif ilki == "çık":
            print("çıktım")
            await client.logout()


client.run(keylerim["token"])
