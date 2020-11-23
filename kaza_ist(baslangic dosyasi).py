def kaza_verilerini_al(kaza_dosyasi,tum_kaza_sayilari,tum_hasar_tutarlari):
    il_kodu_str=kaza_dosyasi.readline()
    while il_kodu_str!="":
        il_kodu=int(il_kodu_str)
        kaza_nedeni_kodu=int(kaza_dosyasi.readline())
        hasar_tutari=int(kaza_dosyasi.readline())
        # verileri, kaza sayilari ve hasar tutarlari listelerine isle

        il_kodu_str=kaza_dosyasi.readline()

def tablo_yazdir(iki_boyutlu_liste):
    print("İl Kodu ",end="")
    for kaza_nedeni_kodu in range(1,11):
        print(format(kaza_nedenleri[kaza_nedeni_kodu],"13"),end="")
    print("Toplam")
    print("------- ",end="")
    for kaza_nedeni_kodu in range(1,11):
        print("------------ ",end="")
    print("------")
    # tabloyu, tablonun satir ve sutun toplamlarini yazdir


try:
    kaza_dosyasi=open("kazalar.txt","r")
    kaza_nedenleri={1:"Aşırı Hız", 2:"Kural İhlali", 3:"Dikkatsizlik", 4:"Sollama", 5:"Uykusuzluk", 6:"Acemilik", 7:"Alkol", 8:"Yakın Takip", 9:"Agresiflik", 10:"Diğer"}
    # kaza sayilari ve hasar tutarlari icin 2 adet iki boyutlu liste yarat

    # kaza verilerini dosyadan almak icin ilgili fonksiyonu cagir

    kaza_dosyasi.close()
except IOError:
    print("Veri dosyası açılamadı ya da okunamadı!")
else:
    print("İllere ve Kaza Nedenlerine Göre Yıllık Kaza Sayıları")
    # yillik kaza sayilari tablosunu yazdirmak icin ilgili fonksiyonu cagir

    bir_tus=input()
    print("İllere ve Kaza Nedenlerine Göre Yıllık Hasar Tutarları")
    # yillik hasar tutarlari tablosunu yazdirmak icin ilgili fonksiyonu cagir
