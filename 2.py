import locale
import operator
import collections
locale.setlocale(locale.LC_ALL, "tr_TR.utf8"),
# -*- coding: utf-8 -*-
def islemSayisi():
    toplamMetin=""
    while True:
        metin = input("İşlem uygulamak istediğiniz metini giriniz :")
        genislik = int(input("Görüntülenmesini istediğiniz satır genişliğini giriniz :"))
        toplamMetin +=metin+"-"
        if genislik >0:
            paragrafDuzenlemece(metin, genislik)
            sozlukIslemleri(metin)
        if genislik==0:
            konumHarf(toplamMetin)
            toplamMetin=toplamMetin.rstrip("-")
            print("TOPLAM İŞLEMLERİ")
            sozlukIslemleri(toplamMetin)
            harfUzayi(toplamMetin)
            break

def sozlukIslemleri(metin):
    kelime=metin.split("-")
    sozluk={}#ALFABETİK SIRAYLA TUTULAN SÖZLÜK
    kelime1=[]
    for t in kelime:
        yeniKelime=""
        for s in t:
            if (s.isupper()==True):
                yeniKelime+=(s.upper())
            else:
                yeniKelime+=(s.upper())
        kelime1.append(yeniKelime)
    kelime1.sort(key=locale.strxfrm)
    for j in kelime1:
        if j in sozluk:
            sozluk[j] += 1
        else:
            sozluk[j] = 1

    print("ALFABETİK SIRAYLA")
    print("KELİMELER           TEKRAR SAYILARI")
    print("-"*19+" "+"-"*15)
    for a,l in sozluk.items(): #ALFABETİK SIRAYLA
        print(f"{a:<15}{l:>10}")

    siraliDict=sorted(sozluk.items(),key=operator.itemgetter(1),reverse=True)
    siraliDict2=collections.OrderedDict(siraliDict) #SAYISINA GÖRE SIRALANMIŞ SÖZLÜK#
    print("TEKRAR SAYISIYLA")
    print("KELİMELER           TEKRAR SAYILARI")
    print("-"*19+" "+"-"*15)
    for a,t in siraliDict2.items(): #KAÇ TANE VARSA
        print(f"{a:<15}{t:>10}")


def konumHarf(toplamMetin): #KUSURSUZ BİR ŞEKİLDE ÇALIŞMAKTADIR
    kelime=toplamMetin.split("-")
    harflereGoreIndeksler=[]
    kelime1=[]
    alfabe=["A","B","C","Ç","D","E",
            "F","G","Ğ","H","I",
            "İ","J","K","L","M",
            "N","O","Ö","P","R",
            "S","Ş","T","U","Ü",
            "V","Y","Z"]
    for t in kelime:
        yeniKelime=""
        for s in t:
            if (s.isupper()==True):
                yeniKelime+=(s.upper())
            else:
                yeniKelime+=(s.upper())
        kelime1.append(yeniKelime)
    for i in range(29):
        harflereGoreKonumlar=[0]*21
        harflereGoreIndeksler.append(harflereGoreKonumlar)
    for t in range(len(kelime1)):
        for x in range(len(alfabe)):
             a=0
             while a<len(kelime1[t]):
                if (kelime1[t][a].find(alfabe[x])!=-1):
                    harflereGoreIndeksler[x][a]+=1
                a+=1
    sayac=0
    for t in harflereGoreIndeksler:
        toplam=0
        for toplamlari in t:
            toplam+=toplamlari
        harflereGoreIndeksler[sayac][20]=toplam
        sayac+=1
    print("Harf 1    2    3    4    5    6    7    8    9   10   11   12   13   14   15   16   17   18   19   20  TOPLAMLARI")
    print("---- ------------------------------------------------------------------------------------------------  ----------")
    for a in range(29):
        print(alfabe[a],end="")
        for b in range(21):
            print(f"{harflereGoreIndeksler[a][b]:>5}",end="")
        print("")

def paragrafDuzenlemece(metin,genislik): #KUSURSUZ BİR ŞEKİLDE ÇALIŞMAKTADIR#
    kelimeler=metin.split("-")
    satirListesi=[]
    satir=""
    satirUzunlugu=0
    for kelime in kelimeler:
        satirUzunlugu+=len(kelime)+1
        satir+=kelime+"-"
        sonSatir=satir
        if (satirUzunlugu>genislik):
            sonKelime=kelime
            satirListesi.append(satir[:len(satir)-len(sonKelime)-2])
            satir=""
            satirUzunlugu=0
            satir+=sonKelime+"-"
            satirUzunlugu+=len(sonKelime)
    satirListesi.append(sonSatir.rstrip("-"))
    satirIkiBoyut=[]
    for t in range(len(satirListesi)):
        satirIkiBoyut.append(satirListesi[t].split("-"))
    for j in range(len(satirIkiBoyut)-1):
        satirKelimeUzunluklari=0
        boslukSayisi=0
        yazdir=""
        sayac=1
        for q in satirIkiBoyut[j]:
            satirKelimeUzunluklari+=len(q)
            boslukSayisi =(genislik - satirKelimeUzunluklari)
            artan=boslukSayisi%(len(satirIkiBoyut[j])-1)
            artan2=artan+1
            kesinKoyulacak=(boslukSayisi-artan)/(len(satirIkiBoyut[j])-1)
        for t in satirIkiBoyut[j]:
            yeniHali=t+"-"*int(kesinKoyulacak)
            if (j%2==0 and artan>0):
                yeniHali=yeniHali+"-"
                yazdir+=yeniHali
                yeniHali=""
                artan-=1
            elif(j%2==1 and artan>0):
                i=len(satirIkiBoyut[j])
                if (sayac >(i)-artan2):
                    yeniHali = yeniHali + "-"
                    artan-=1
                yazdir += yeniHali
                yeniHali = ""
                sayac+=1
            else:
                yazdir+=yeniHali
        print(yazdir.rstrip("-"))
    print(sonSatir.rstrip("-"))


def harfUzayi(metin):
    oku = open("harf_uzayi.txt", "r", encoding="utf-8")
    kelimeler = metin.upper().split("-")
    satir = oku.readline()
    satirListesi = []
    while satir != "":
        satirListesi.append(satir)
        satir = oku.readline()
    for kelime in kelimeler:
        sayac0 = 0
        for satir in satirListesi:
            sayac0 += 1
            for index in range(0, len(satir)):
                if (satir[index] == kelime[0]):
                    if (len(satir) - index >= len(kelime)):  # KENAN DOĞULU
                        lazim = satir[index]
                        for i in range(1, len(satir) - index):
                            lazim += satir[index + i]
                            if (lazim == kelime):
                                print(f"{lazim:<5}{sayac0}{index+1:>5}","DOĞU YÖNÜNDE")
                    if (len(kelime) <= index):  # KENAN BATILI
                        lazim = satir[index]
                        for i in range(index - 1, 0, -1):
                            lazim += satir[i]
                            if (lazim == kelime):
                                print(f"{lazim:<5}{sayac0}{index + 1:>5}", "BATI YÖNÜNDE") ###
                    if (len(satirListesi) - (sayac0 - 1) >= len(kelime)):  # KENAN GÜNEYLİ
                        lazim = satir[index]
                        for i in range(sayac0, len(satirListesi)):
                            lazim += satirListesi[i][index]
                            if (lazim == kelime):
                                print(f"{lazim:<5}{sayac0}{index+1:>5}","GÜNEY YÖNÜNDE")
                    if (sayac0 >= len(kelime)):  # KENAN KUZEYLİ
                        lazim = satir[index]
                        for i in range(sayac0 - 1, 0, -1):
                            lazim += satirListesi[i - 1][index]
                            if (lazim == kelime):
                                print(f"{lazim:<5}{sayac0}{index+1:>5}","KUZEY YÖNÜNDE")
                    if (len(satir) - index >= len(kelime)):  # KENAN GÜNEYDOĞULU
                        lazim = satir[index]
                        j = sayac0 - 1
                        if (len(satirListesi) - j < len(satirListesi) - index):
                            for i in range(1, len(satirListesi) - j):
                                lazim += satirListesi[j + 1][index + i]
                                j += 1
                                if (lazim == kelime):
                                    print(f"{lazim:<5}{sayac0}{index + 1:>5}", "GÜNEYDOĞU YÖNÜNDE")
                        else:
                            for i in range(1, len(satirListesi) - index):
                                lazim += satirListesi[j + 1][index + i]
                                j += 1
                                if (lazim == kelime):
                                    print(f"{lazim:<5}{sayac0}{index + 1:>5}", "GÜNEYDOĞU YÖNÜNDE")
                    if (len(kelime) <= index):  # KENAN GÜNEYBATILI
                        lazim = satir[index]
                        j = sayac0 - 1
                        if (len(satirListesi) - j < index):
                            for i in range(1, len(satirListesi) - j):
                                lazim += satirListesi[j + 1][index - i]
                                j += 1
                                if (lazim == kelime):
                                    print(f"{lazim:<5}{sayac0}{index + 1:>5}", "GÜNEYBATI YÖNÜNDE")
                        else:
                            for i in range(1, index):
                                lazim += satirListesi[j + 1][index - i]
                                j += 1
                                if (lazim == kelime):
                                    print(f"{lazim:<5}{sayac0}{index + 1:>5}", "GÜNEYBATI YÖNÜNDE")
                    if (len(satir) - index >= len(kelime)):  # KENAN KUZEYDOĞULU
                        lazim = satir[index]
                        if (sayac0 - 1 < len(satirListesi) - index):
                            for i in range(1, sayac0):
                                lazim += satirListesi[sayac0 - 1 - i][index + i]
                                if (lazim == kelime):
                                    print(f"{lazim:<5}{sayac0}{index + 1:>5}", "KUZEYDOĞU YÖNÜNDE")
                        else:
                            for i in range(1, len(satirListesi) - index):
                                lazim += satirListesi[sayac0 - 1 - i][index + i]
                                if (lazim == kelime):
                                    print(f"{lazim:<5}{sayac0}{index + 1:>5}", "KUZEYDOĞU YÖNÜNDE")
                    if (len(kelime) <= index + 1):  # KENAN KUZEYBATILI
                        j = sayac0 - 1
                        lazim = satir[index]
                        if (j + 1 < index + 1):
                            for i in range(1, j + 1):
                                lazim += satirListesi[j - i][index - i]
                                if (lazim == kelime):
                                    print(f"{lazim:<5}{sayac0}{index + 1:>5}", "KUZEYBATI YÖNÜNDE")
                        else:
                            j = sayac0 - 1
                            for i in range(1, index + 1):
                                lazim += satirListesi[j - i][index - i]
                                if (lazim == kelime):
                                    print(f"{lazim:<5}{sayac0}{index + 1:>5}", "KUZEYBATI YÖNÜNDE")


islemSayisi()


