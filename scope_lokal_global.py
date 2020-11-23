global_degisken = 27

def bir_fonksiyon():
    global global_degisken
    global_degisken = global_degisken + 1

def dis_fonksiyon(dis_parametre = 123):
    dis_degisken = global_degisken + dis_parametre

    def ic_fonksiyon(ic_parametre = 0):
        ic_degisken = ic_parametre + dis_degisken + global_degisken
        return ic_degisken

    sonuc = ic_fonksiyon(dis_degisken)
    return sonuc

sonuc  = dis_fonksiyon(7)
print('Sonuç:',sonuc)

bir_fonksiyon()

sonuc  = dis_fonksiyon(7)
print('Sonuç:',sonuc)
