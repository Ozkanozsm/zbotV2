def mesajiayir(anamesaj):
    mesajlistesi = list(anamesaj)
    del mesajlistesi[0]
    return "".join(mesajlistesi).lower().split()


def zamanhesapla(eski, yeni):
    # zbot'un ilk hâlinden alındı
    zamanfarki = yeni - eski
    uptsaniye = round(zamanfarki.total_seconds())
    uptdakika = uptsaniye // 60
    uptsaat = uptdakika // 60
    uptgun = uptsaat // 24
    if uptsaniye // 60 < 1:
        return "{} saniye".format(uptsaniye)
    elif uptdakika // 60 < 1:
        upksaniye = uptsaniye % 60
        return "{} dakika, {} saniye".format(uptdakika, upksaniye)
    elif uptsaat // 24 < 1:
        upksaniye = uptsaniye % 60
        upkdakika = uptdakika % 60
        return "{} saat, {} dakika, {} saniye".format(uptsaat, upkdakika, upksaniye)
    else:
        upksaniye = uptsaniye % 60
        upkdakika = uptdakika % 60
        upksaat = uptsaat % 24
        return "{} gün, {} saat, {} dakika, {} saniye".format(uptgun, upksaat, upkdakika, upksaniye)


def idbolucu(metin):
    idsonhal = "".join("".join(metin.split("<@")).split(">"))
    if idsonhal.startswith("!"):
        idsonhal = "".join(idsonhal.split("!"))
    return int(idsonhal)


mesajlara_karsilik = {
    "sa": "as",
    "deneme": ":white_check_mark:"
}
