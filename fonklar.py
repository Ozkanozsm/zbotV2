def mesajiayir(anamesaj):
    mesajlistesi = list(anamesaj)
    del mesajlistesi[0]
    return "".join(mesajlistesi).lower().split()
