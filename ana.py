import discord
import json
import fonklar

client = discord.Client()
prefix = "'"
keylerim = json.load(open("keyler.json", "r"))


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
        if ilki == "çık":
            print("çıktım")
            await client.logout()


client.run(keylerim["token"])
