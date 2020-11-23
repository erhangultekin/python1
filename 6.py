aboneTipi=""
toplamSuUcreti=0
toplamAtıkSuUcreti=0
suBirimi = 2.89
atıkSuUcreti = 1.44
suBirimi1 = 3.13
atıkSuUcreti1 =1.56
suBirimi2=6.43
atıkSuUcreti2=3.22
BornovaBedel=13
BuyukSehirBedel=2.54
toplamBornova=0
toplamBelediye=0
liste=["E","e","Y","y","Ş","ş","G","g","S","s"]
KonutTipisayisi=0
isyeriTipisayisi=0
resmidaireTipisayisi=0
organizesanayiTipisayisi=0
hayvansulamaTipisayisi=0
konutSuyu=0
isyeriSuyu=0
resmidaireSuyu=0
organizesanayiSuyu=0
hayvansulamaSuyu=0
KademeBirSuTuketim=0
KademeIkiSuTuketim=0
KademeUcSuTuketim=0
KademeBirHaneSayisi=0
KademeİkiHaneSayisi=0
KademeUcHaneSayisi=0
ellitonAboneHayvan=0
yuzTonveyaBesyuz=0
maksSuTuketimResmi=0
maksResmiAboneNo=0
maksSuTuketimUcretiKonutYok=0
maksKonutYokAboneNo=0
maksKonutYokAboneTipi=""
maksSuTuketimKonutYok=0
toplamES=0
toplamSGS=0
konutlarToplamSuTuketimUcreti=0
isyeriToplamSuTuketimUcreti=0
resmidaireToplamSuTuketimUcreti=0
organizesanayiToplamSuTuketimUcreti=0
hayvanToplamSuTuketimUcreti=0
toplamİZSU=0
toplamKDV=0
while True:
    suTuketimUcreti=0
    atıkSuTuketimUcreti=0
    aboneNo=int(input("Abone numaranızı giriniz :"))
    aboneTipiKodu=int(input("Abone tipi kodunuzu giriniz (1-5 arasında tamsayı) :"))
    while aboneTipiKodu<0 or aboneTipiKodu>5:
        aboneTipiKodu=int(input("Lütfen aralıkta bir değer giriniz :"))
    öncekiSayac=int(input("Önceki sayaç değerini giriniz :"))
    while öncekiSayac<0:
        öncekiSayac=int(input("Önceki sayaç değeriniz 0 dan küçük olamaz. Tekrar giriniz :"))
    simdikiSayac=int(input("Şimdiki sayaç değerini giriniz :"))
    while simdikiSayac<öncekiSayac:
        simdikiSayac=int(input("Şimdiki sayaç değeriniz önceki sayaç değerinizden küçük olamaz"))
    tarih=int(input("Önceki ve şimdi olan sayaçlar arasındaki gün sayısını giriniz :"))
    while tarih<=0:
        tarih=int(input("Lütfen geçerli bir gün sayısı giriniz :"))
    sayacMetreKupFark=simdikiSayac-öncekiSayac
    BirkademeSınırHesapla=(13*(tarih))/30
    IkiKademeSınırHesapla=(20*(tarih))/30
    if (aboneTipiKodu==1):
        aboneTipi="Konut"
        KonutTipisayisi+=1
        haneSayısı=int(input("Hane sayısını giriniz :"))
        while haneSayısı<1:
            haneSayısı=int(input("Lütfen doğru bir hane sayısı giriniz :"))
        if (haneSayısı==1):
            indirimDurumu=input("Yok/Şehit/Gazi/Sporcu/Engelli:(Y/y/Ş/ş/G/g/S/s/E/e karakterleri) uygun olanı seçiniz :")
            while indirimDurumu not in liste:
                indirimDurumu=input("Uygun olanı tekrar giriniz : Yok/Şehit/Gazi/Sporcu/Engelli:(Y/y/Ş/ş/G/g/S/s/E/e karakterleri)")

            if (indirimDurumu=="y") or (indirimDurumu=="Y"):
                if(sayacMetreKupFark<=BirkademeSınırHesapla):
                    suTuketimUcreti=suBirimi*sayacMetreKupFark
                    atıkSuTuketimUcreti=atıkSuUcreti*sayacMetreKupFark
                    KademeBirSuTuketim+=sayacMetreKupFark
                    KademeBirHaneSayisi+=1
                elif(sayacMetreKupFark>BirkademeSınırHesapla) and(sayacMetreKupFark <=IkiKademeSınırHesapla):
                    suTuketimUcreti=(suBirimi*BirkademeSınırHesapla)+(suBirimi1*(sayacMetreKupFark-BirkademeSınırHesapla))
                    atıkSuTuketimUcreti=(atıkSuUcreti*BirkademeSınırHesapla)+(atıkSuUcreti1*(sayacMetreKupFark-BirkademeSınırHesapla))
                    KademeBirSuTuketim+=BirkademeSınırHesapla
                    KademeIkiSuTuketim+=(sayacMetreKupFark-BirkademeSınırHesapla)
                    KademeİkiHaneSayisi+=1
                else:
                    suTuketimUcreti=(suBirimi*BirkademeSınırHesapla)+(suBirimi1*IkiKademeSınırHesapla)+\
                                    (suBirimi2*(sayacMetreKupFark-IkiKademeSınırHesapla))
                    atıkSuTuketimUcreti=(atıkSuUcreti*BirkademeSınırHesapla)+(atıkSuUcreti1*(IkiKademeSınırHesapla))+\
                                        (atıkSuUcreti2*(sayacMetreKupFark-IkiKademeSınırHesapla))
                    KademeBirSuTuketim+=BirkademeSınırHesapla
                    KademeIkiSuTuketim+=(IkiKademeSınırHesapla-BirkademeSınırHesapla)
                    KademeUcSuTuketim+=(sayacMetreKupFark-IkiKademeSınırHesapla)
                    KademeUcHaneSayisi+=1
            elif(indirimDurumu=="e" or indirimDurumu=="E"):
                toplamES+=1
                if (sayacMetreKupFark <= BirkademeSınırHesapla):
                    suTuketimUcreti = (suBirimi/2) * sayacMetreKupFark
                    atıkSuTuketimUcreti = (atıkSuUcreti/2) * sayacMetreKupFark
                    KademeBirSuTuketim += sayacMetreKupFark
                    KademeBirHaneSayisi+=1
                elif (sayacMetreKupFark > BirkademeSınırHesapla) and (sayacMetreKupFark <= IkiKademeSınırHesapla):
                    suTuketimUcreti = ((suBirimi/2) * BirkademeSınırHesapla) + ((
                                suBirimi1/2) *(sayacMetreKupFark - BirkademeSınırHesapla))
                    atıkSuTuketimUcreti = ((atıkSuUcreti/2) * BirkademeSınırHesapla) + ((
                                atıkSuUcreti1/2) * (sayacMetreKupFark - BirkademeSınırHesapla))
                    KademeBirSuTuketim += BirkademeSınırHesapla
                    KademeIkiSuTuketim += (sayacMetreKupFark - BirkademeSınırHesapla)
                    KademeİkiHaneSayisi+=1
                else:
                    suTuketimUcreti = ((suBirimi/2) * BirkademeSınırHesapla) + ((suBirimi1/2) * IkiKademeSınırHesapla) + \
                                      (suBirimi2 * (sayacMetreKupFark - IkiKademeSınırHesapla))
                    atıkSuTuketimUcreti = ((atıkSuUcreti/2) * BirkademeSınırHesapla) + (
                            (atıkSuUcreti1/2) * (IkiKademeSınırHesapla)) + \
                                          (atıkSuUcreti2 * (sayacMetreKupFark - IkiKademeSınırHesapla))
                    KademeBirSuTuketim += BirkademeSınırHesapla
                    KademeIkiSuTuketim += (IkiKademeSınırHesapla - BirkademeSınırHesapla)
                    KademeUcSuTuketim += (sayacMetreKupFark - IkiKademeSınırHesapla)
                    KademeUcHaneSayisi+=1
            else:
                toplamSGS += 1
                if (sayacMetreKupFark <= BirkademeSınırHesapla):
                    suTuketimUcreti = (suBirimi/2) * sayacMetreKupFark
                    atıkSuTuketimUcreti = (atıkSuUcreti/2) * sayacMetreKupFark
                    KademeBirSuTuketim += sayacMetreKupFark
                    KademeBirHaneSayisi+=1
                elif (sayacMetreKupFark > BirkademeSınırHesapla) and (sayacMetreKupFark <= IkiKademeSınırHesapla):
                    suTuketimUcreti = ((suBirimi/2)* BirkademeSınırHesapla) + ((
                        (suBirimi1/2))*(sayacMetreKupFark - BirkademeSınırHesapla))
                    atıkSuTuketimUcreti = ((atıkSuUcreti/2) * BirkademeSınırHesapla)+ (
                            (atıkSuUcreti1/2) * (sayacMetreKupFark - BirkademeSınırHesapla))
                    KademeBirSuTuketim += BirkademeSınırHesapla
                    KademeIkiSuTuketim += (sayacMetreKupFark - BirkademeSınırHesapla)
                    KademeİkiHaneSayisi+=1
                else:
                    suTuketimUcreti = ((suBirimi/2) * BirkademeSınırHesapla) + ((suBirimi1/2) * IkiKademeSınırHesapla) + \
                                      ((suBirimi2/2) * (sayacMetreKupFark - IkiKademeSınırHesapla))
                    atıkSuTuketimUcreti = ((atıkSuUcreti/2) * BirkademeSınırHesapla) + (
                            (atıkSuUcreti1/2) * (IkiKademeSınırHesapla)) + \
                                         ((atıkSuUcreti2/2) * (sayacMetreKupFark - IkiKademeSınırHesapla))
                    KademeBirSuTuketim += BirkademeSınırHesapla
                    KademeIkiSuTuketim += (IkiKademeSınırHesapla - BirkademeSınırHesapla)
                    KademeUcSuTuketim += (sayacMetreKupFark - IkiKademeSınırHesapla)
                    KademeUcHaneSayisi+=1

            borc=suTuketimUcreti+atıkSuTuketimUcreti+BornovaBedel+BuyukSehirBedel
            toplamBornova+=BornovaBedel
            toplamBelediye+=BuyukSehirBedel
        else: #Hane Sayısı >1 durumu

            SehitGaziSporcuSayı=int(input("Şehit,gazi veya sporcu sayısı :"))
            while SehitGaziSporcuSayı<0 or SehitGaziSporcuSayı>haneSayısı:
                SehitGaziSporcuSayı=int(input("Yanlış bir sayı girdiniz tekrar giriniz :"))
            toplamSGS+=SehitGaziSporcuSayı

            engelliSayısı=int(input("Engelli sayısı giriniz :"))
            while engelliSayısı<0 or engelliSayısı>haneSayısı:
                engelliSayısı=int(input("Yanlış bir sayı girdiniz tekrar giriniz :"))
            toplamES+=engelliSayısı
            while engelliSayısı+SehitGaziSporcuSayı>haneSayısı:
                print("Hane sayısını geçtiniz...")
                SehitGaziSporcuSayı = int(input("Şehit,gazi veya sporcu sayısını Tekrar giriniz :"))
                while SehitGaziSporcuSayı < 0 or SehitGaziSporcuSayı > haneSayısı:
                    SehitGaziSporcuSayı = int(input("Yanlış bir sayı girdiniz tekrar giriniz :"))
                engelliSayısı = int(input("Engelli sayısını Tekrar giriniz :"))
                while engelliSayısı < 0 or engelliSayısı > haneSayısı:
                    engelliSayısı = int(input("Yanlış bir sayı girdiniz tekrar giriniz :"))
            ortalama=sayacMetreKupFark/haneSayısı
            for x in range(0,SehitGaziSporcuSayı,1):
                if (ortalama <= BirkademeSınırHesapla):
                    suTuketimUcreti += (suBirimi/2) * ortalama
                    atıkSuTuketimUcreti += (atıkSuUcreti/2) * ortalama
                    KademeBirSuTuketim+=ortalama
                    KademeBirHaneSayisi+=1
                elif (ortalama > BirkademeSınırHesapla) and (ortalama <= IkiKademeSınırHesapla):
                    suTuketimUcreti += ((suBirimi/2)* BirkademeSınırHesapla) + ((
                        (suBirimi1/2))*(ortalama - BirkademeSınırHesapla))
                    atıkSuTuketimUcreti  += ((atıkSuUcreti/2) * BirkademeSınırHesapla)+ (
                            (atıkSuUcreti1/2) * (ortalama - BirkademeSınırHesapla))
                    KademeBirSuTuketim+=BirkademeSınırHesapla
                    KademeIkiSuTuketim+=(ortalama-BirkademeSınırHesapla)
                    KademeİkiHaneSayisi+=1
                else:
                    suTuketimUcreti += ((suBirimi/2) * BirkademeSınırHesapla) + ((suBirimi1/2) * IkiKademeSınırHesapla) + \
                                      ((suBirimi2/2) * (ortalama - IkiKademeSınırHesapla))
                    atıkSuTuketimUcreti += ((atıkSuUcreti/2) * BirkademeSınırHesapla) + (
                            (atıkSuUcreti1/2) * (IkiKademeSınırHesapla)) + \
                                          ((atıkSuUcreti2/2) * (ortalama - IkiKademeSınırHesapla))
                    KademeBirSuTuketim+=BirkademeSınırHesapla
                    KademeIkiSuTuketim+=IkiKademeSınırHesapla
                    KademeUcSuTuketim+=(ortalama-IkiKademeSınırHesapla)
                    KademeUcHaneSayisi+=1
            for j in range(0,engelliSayısı,1):
                if (ortalama <= BirkademeSınırHesapla):
                    suTuketimUcreti += (suBirimi/2) * ortalama
                    atıkSuTuketimUcreti += (atıkSuUcreti/2) * ortalama
                    KademeBirSuTuketim+=ortalama
                    KademeBirHaneSayisi+=1
                elif (ortalama > BirkademeSınırHesapla) and (ortalama <= IkiKademeSınırHesapla):
                    suTuketimUcreti += ((suBirimi/2) * BirkademeSınırHesapla) + ((
                                suBirimi1/2) *(ortalama - BirkademeSınırHesapla))
                    atıkSuTuketimUcreti += ((atıkSuUcreti/2) * BirkademeSınırHesapla) + ((
                                atıkSuUcreti1/2) * (ortalama - BirkademeSınırHesapla))
                    KademeBirSuTuketim += BirkademeSınırHesapla
                    KademeIkiSuTuketim += (ortalama - BirkademeSınırHesapla)
                    KademeİkiHaneSayisi+=1
                else:
                    suTuketimUcreti += ((suBirimi/2) * BirkademeSınırHesapla) + ((suBirimi1/2) * IkiKademeSınırHesapla) + \
                                      (suBirimi2 * (ortalama - IkiKademeSınırHesapla))
                    atıkSuTuketimUcreti += ((atıkSuUcreti/2) * BirkademeSınırHesapla) + (
                            (atıkSuUcreti1/2) * (IkiKademeSınırHesapla)) + \
                                          (atıkSuUcreti2 * (ortalama - IkiKademeSınırHesapla))
                    KademeBirSuTuketim += BirkademeSınırHesapla
                    KademeIkiSuTuketim += IkiKademeSınırHesapla
                    KademeUcSuTuketim += (ortalama - IkiKademeSınırHesapla)
                    KademeUcHaneSayisi+=1

            for q in range (0,haneSayısı-(engelliSayısı+SehitGaziSporcuSayı),1):
                if (ortalama <= BirkademeSınırHesapla):
                    suTuketimUcreti += suBirimi * ortalama
                    atıkSuTuketimUcreti += atıkSuUcreti * ortalama
                    KademeBirSuTuketim+=ortalama
                    KademeBirHaneSayisi+=1
                elif (ortalama > BirkademeSınırHesapla) and (ortalama <= IkiKademeSınırHesapla):
                    suTuketimUcreti += (suBirimi * BirkademeSınırHesapla) + (
                                suBirimi1 * (ortalama - BirkademeSınırHesapla))
                    atıkSuTuketimUcreti += (atıkSuUcreti * BirkademeSınırHesapla) + (
                                atıkSuUcreti1 * (ortalama - BirkademeSınırHesapla))
                    KademeBirSuTuketim += BirkademeSınırHesapla
                    KademeIkiSuTuketim += (ortalama - BirkademeSınırHesapla)
                    KademeİkiHaneSayisi+=1
                else:
                    suTuketimUcreti += (suBirimi * BirkademeSınırHesapla) + (suBirimi1 * IkiKademeSınırHesapla) + \
                                      (suBirimi2 * (ortalama - IkiKademeSınırHesapla))
                    atıkSuTuketimUcreti += (atıkSuUcreti * BirkademeSınırHesapla) + (
                                atıkSuUcreti1 * (IkiKademeSınırHesapla)) + \
                                          (atıkSuUcreti2 * (ortalama - IkiKademeSınırHesapla))
                    KademeBirSuTuketim += BirkademeSınırHesapla
                    KademeIkiSuTuketim += IkiKademeSınırHesapla
                    KademeUcSuTuketim += (ortalama - IkiKademeSınırHesapla)
                    KademeUcHaneSayisi+=1


            borc=(suTuketimUcreti+atıkSuTuketimUcreti)+(BornovaBedel*haneSayısı)+(BuyukSehirBedel*haneSayısı)
            toplamBelediye+=BuyukSehirBedel*haneSayısı
            toplamBornova+=BornovaBedel*haneSayısı
        konutSuyu+=sayacMetreKupFark
        konutlarToplamSuTuketimUcreti+=suTuketimUcreti
    elif(aboneTipiKodu==2):
        haneSayısı=1
        aboneTipi="İşyeri"
        suTuketimUcreti=(sayacMetreKupFark)*(7.38)
        atıkSuTuketimUcreti=(sayacMetreKupFark)*(3.68)
        isyeriTipisayisi+=1
        borc=sayacMetreKupFark*(7.38+3.68)+BornovaBedel+BuyukSehirBedel
        toplamBelediye+=BuyukSehirBedel
        toplamBornova+=BornovaBedel
        isyeriSuyu+=sayacMetreKupFark
        isyeriToplamSuTuketimUcreti+=suTuketimUcreti
    elif(aboneTipiKodu==3):
        haneSayısı=1
        aboneTipi="Resmi Daire"
        suTuketimUcreti=(sayacMetreKupFark)*(4.34)
        atıkSuTuketimUcreti=(sayacMetreKupFark)*(2.16)
        resmidaireTipisayisi+=1
        borc=sayacMetreKupFark*(4.34+2.16)+BornovaBedel+BuyukSehirBedel
        toplamBelediye += BuyukSehirBedel
        toplamBornova += BornovaBedel
        resmidaireSuyu+=sayacMetreKupFark
        resmidaireToplamSuTuketimUcreti += suTuketimUcreti
        if(sayacMetreKupFark>maksSuTuketimResmi):
            maksSuTuketimResmi=sayacMetreKupFark
            maksResmiAboneNo=aboneNo
    elif(aboneTipiKodu==4):
        haneSayısı=1
        aboneTipi="Organize Sanayi"
        suTuketimUcreti=(sayacMetreKupFark)*(5.00)
        atıkSuTuketimUcreti=(sayacMetreKupFark)*(2.50)
        organizesanayiTipisayisi+=1
        borc=sayacMetreKupFark*(5.00+2.50)+BornovaBedel+BuyukSehirBedel
        toplamBelediye += BuyukSehirBedel
        toplamBornova += BornovaBedel
        organizesanayiSuyu+=sayacMetreKupFark
        organizesanayiToplamSuTuketimUcreti+=suTuketimUcreti
    else:
        haneSayısı=1
        aboneTipi="İlçe Tarımsal ve Hayvan Sulama"
        hayvansulamaTipisayisi+=1
        if(sayacMetreKupFark<=BirkademeSınırHesapla):
            suTuketimUcreti=1.45*sayacMetreKupFark
            atıkSuTuketimUcreti=0.72*sayacMetreKupFark
        elif(sayacMetreKupFark>BirkademeSınırHesapla) and (sayacMetreKupFark<=IkiKademeSınırHesapla):
            suTuketimUcreti=1.45*BirkademeSınırHesapla+2.89*(sayacMetreKupFark-BirkademeSınırHesapla)
            atıkSuTuketimUcreti=0.72*BirkademeSınırHesapla+1.44*(sayacMetreKupFark-BirkademeSınırHesapla)
        else:
            suTuketimUcreti=1.45*BirkademeSınırHesapla+2.89*(IkiKademeSınırHesapla-BirkademeSınırHesapla)+\
                6.43*(sayacMetreKupFark-IkiKademeSınırHesapla)
            atıkSuTuketimUcreti=0.72*BirkademeSınırHesapla+1.44*(IkiKademeSınırHesapla-BirkademeSınırHesapla)+\
                3.22*(sayacMetreKupFark-IkiKademeSınırHesapla)

        if(sayacMetreKupFark>=50):
            ellitonAboneHayvan+=1


        borc=suTuketimUcreti+atıkSuTuketimUcreti+BornovaBedel+BuyukSehirBedel
        toplamBelediye += BuyukSehirBedel
        toplamBornova += BornovaBedel
        hayvansulamaSuyu+=sayacMetreKupFark
        hayvanToplamSuTuketimUcreti+=suTuketimUcreti
    if(sayacMetreKupFark>100) or (suTuketimUcreti>500):
        yuzTonveyaBesyuz+=1

    if(aboneTipi!="Konut"):
        if(suTuketimUcreti>maksSuTuketimUcretiKonutYok):
            maksSuTuketimUcretiKonutYok=suTuketimUcreti
            maksKonutYokAboneNo=aboneNo
            maksKonutYokAboneTipi=aboneTipi
            maksSuTuketimKonutYok=sayacMetreKupFark

    toplamSuUcreti+=suTuketimUcreti
    toplamAtıkSuUcreti+=atıkSuTuketimUcreti


    toplamBornova+=0.39*sayacMetreKupFark
    kdv=borc*(8/100)
    borc+=(borc*8/100)+(0.39*sayacMetreKupFark)
    izSu=suTuketimUcreti+atıkSuTuketimUcreti
    toplamİZSU+=izSu
    toplamKDV+=kdv

    print("Dönemlik")
    print("Su tüketim miktarı :" ,format(sayacMetreKupFark,".2f"))
    print("Abone tipi :" ,aboneTipi)
    print("Su tüketim ücreti :",format(suTuketimUcreti,".2f"))
    print("Atık su tüketim ücreti :",format(atıkSuTuketimUcreti,".2f"))
    print("Toplam :",format(suTuketimUcreti+atıkSuTuketimUcreti,".2f"))
    print("ÇTV miktarı :" ,format(0.39*sayacMetreKupFark,".2f"))
    print("Katı atık toplama ücreti :",format(BornovaBedel*haneSayısı,".2f"))
    print("Katı atık bertaraf ücreti :",format(BuyukSehirBedel*haneSayısı,".2f"))
    print("Toplam fatura tutar :",format(borc,".2f"))
    print("Devlete aktarılacak olan KDV miktarı :",format(kdv,".2f"))
    print("İlçe Belediyesine aktarılacak olan tutar :",format((BornovaBedel * haneSayısı)+(0.39*sayacMetreKupFark),".2f"))
    print("Büyükşehir Belediyesine aktarılacak olan tutar :",format(BuyukSehirBedel * haneSayısı,".2f"))
    print("İzsu payı :",format(izSu,".2f"))

    baskaislem=input("Başka işlem var mı? E/e H/h :")
    while baskaislem!="e" and baskaislem!="E" and baskaislem!="H" and baskaislem!="h":
        baskaislem=input("Lütfen işlemi tekrar giriniz E/e H/h :")

    if (baskaislem=="h") or (baskaislem=="H"):
        break
    else:
        continue


toplamSayi=isyeriTipisayisi+KonutTipisayisi+hayvansulamaTipisayisi+organizesanayiTipisayisi+resmidaireTipisayisi
print("Her abone tipi için; abone (hane) sayıları, yüzdeleri ve aylık ortalama su tüketim miktarları ")
print("Konut Tipi :",KonutTipisayisi,format((KonutTipisayisi/toplamSayi)*100,".2f"),format(konutSuyu/KonutTipisayisi,".2f"))
print("İşyeri Tipi :",isyeriTipisayisi,format((isyeriTipisayisi/toplamSayi)*100,".2f"),format(isyeriSuyu/isyeriTipisayisi,".2f"))
print("Organize Sanayi :",organizesanayiTipisayisi,format((organizesanayiTipisayisi/toplamSayi)*100,".2f"),format(organizesanayiSuyu/organizesanayiTipisayisi,".2f"))
print("Resmi Daire :",resmidaireTipisayisi,format((resmidaireTipisayisi/toplamSayi)*100,".2f"),format(organizesanayiSuyu/organizesanayiTipisayisi,".2f"))
print("İlçe Tarımsal ve Hayvan Sulama :",hayvansulamaTipisayisi,format((hayvansulamaTipisayisi/toplamSayi)*100,".2f"),format(hayvansulamaSuyu/hayvansulamaTipisayisi,".2f"))
print(" Aylık su tüketim miktarlarına göre her kademedeki konut tipi abonelerin (hanelerin) sayıları, "
      "konut tipi aboneler içindeki yüzdeleri ve aylık ortalama su tüketim miktarları")
print("Konut Tipi Abonelerin Sayısı 1.Kademe :", KademeBirHaneSayisi)
print("Konut Tipi Abonelerin Sayısı 2.Kademe :", KademeİkiHaneSayisi)
print("Konut Tipi Abonelerin Sayısı 3.Kademe :", KademeUcHaneSayisi)
print("1. Kademe Oranı :",format(KademeBirHaneSayisi/KonutTipisayisi,".2f"))
print("2. Kademe Oranı :",format(KademeİkiHaneSayisi/KonutTipisayisi,".2f"))
print("3. Kademe Oranı :",format(KademeUcHaneSayisi/KonutTipisayisi,".2f"))
print("1. Kademe Ortalama Su Tuketimi :",format(KademeBirSuTuketim/(KademeBirSuTuketim+KademeIkiSuTuketim+KademeUcSuTuketim),".2f"))
print("2. Kademe Ortalama Su Tuketimi :",format(KademeIkiSuTuketim/(KademeBirSuTuketim+KademeIkiSuTuketim+KademeUcSuTuketim),".2f"))
print("3. Kademe Ortalama Su Tuketimi :",format(KademeUcSuTuketim/(KademeBirSuTuketim+KademeIkiSuTuketim+KademeUcSuTuketim),".2f"))
print(" Aylık su tüketim miktarı 50 tondan fazla olan ilçe tarımsal ve hayvan sulama tipi abonelerin sayısı :",ellitonAboneHayvan)
print("Ve İlçe tarımsal ve hayvan sulama tipi aboneler içindeki yüzdesi :",format((ellitonAboneHayvan/hayvansulamaTipisayisi)*100,".2f"))
print("Aylık su tüketim miktarı 100 tondan yüksek veya aylık su tüketim ücreti 500 TL’den yüksek olan abonelerin (hanelerin) sayısı :",yuzTonveyaBesyuz)
print("Şehit, gazi veya devlet sporcusu olan ve engelli olan konut tipi abonelerin (hanelerin) "
      "sayısı :", toplamSGS ,"ve", toplamES)
print("Ve Engelli ,Şehit, Gazi ve Sporcu Toplam Sayısının Konut tipi aboneler (haneler) içindeki yüzdeleri :",format(((toplamSGS+toplamES)/KonutTipisayisi)*100,".2f"))
print("Aylık su tüketim miktarı en yüksek olan resmi daire tipi abonenin abone no’su  :",maksResmiAboneNo)
print("Aylık su tüketim miktarı en yüksek olan resmi daire tipi abonenin su tüketim miktari :",format(maksSuTuketimResmi,".2f"))
print("Aylık su tüketim ücreti en yüksek olan konut tipi dışındaki abonenin abone no’su :",maksKonutYokAboneNo)
print("Abone tipi adı :",maksKonutYokAboneTipi)
print("Aylık su tüketim miktar :",format(maksSuTuketimKonutYok,".2f"))
print("Ödediği aylık su tüketim ücreti :",format(maksSuTuketimUcretiKonutYok,".2f"))
print("Her Abone Tipi İçin Aylık Su Tüketim Miktarları:")
print("Konut İçin :",format(konutSuyu,".2f"))
print("İşyeri İçin :",format(isyeriSuyu,".2f"))
print("Resmi Daire :",format(resmidaireSuyu,".2f"))
print("Organize Sanayi :",format(organizesanayiSuyu,".2f"))
print("İlçe Tarımsal ve Hayvan Sulama :",format(hayvansulamaSuyu,".2f"))
print("Suların Genele Göre Yüzdesi :")
print("Konut Tipinin Bornova Bölgesi İçinde Yüzdesi :",format(konutSuyu/(konutSuyu+isyeriSuyu+resmidaireSuyu+organizesanayiSuyu+hayvansulamaSuyu)*100,".2f"))
print("İşyeri Tipinin Bornova Bölgesi İçinde Yüzdesi :",format(isyeriSuyu/(konutSuyu+isyeriSuyu+resmidaireSuyu+organizesanayiSuyu+hayvansulamaSuyu)*100,".2f"))
print("Resmi Daire Tipinin Bornova Bölgesi İçinde Yüzdesi :",format(resmidaireSuyu/(konutSuyu+isyeriSuyu+resmidaireSuyu+organizesanayiSuyu+hayvansulamaSuyu)*100,".2f"))
print("Organize Sanayi Tipinin Bornova Bölgesi İçinde Yüzdesi :",format(organizesanayiSuyu/(konutSuyu+isyeriSuyu+resmidaireSuyu+organizesanayiSuyu+hayvansulamaSuyu)*100,".2f"))
print("İlçe Tarımsal ve Hayvan Sulama Tipinin Bornova Bölgesi İçinde Yüzdesi :",format(hayvansulamaSuyu/
      (konutSuyu + isyeriSuyu + resmidaireSuyu + organizesanayiSuyu + hayvansulamaSuyu)*100,".2f"))
print("Bornova Bölgesi Toplam Su :",format(konutSuyu+isyeriSuyu+resmidaireSuyu+organizesanayiSuyu+hayvansulamaSuyu,".2f"))
print("Konut İçin Su Tuketim Ücreti :",format(konutlarToplamSuTuketimUcreti,".2f"))
print("İsyeri İçin Su Tuketim Ücreti :",format(isyeriToplamSuTuketimUcreti,".2f"))
print("Resmi Daire İçin Su Tuketim Ücreti :",format(resmidaireToplamSuTuketimUcreti,".2f"))
print("Organize Sanayi İçin Su Tuketim Ücreti :",format(organizesanayiToplamSuTuketimUcreti,".2f"))
print("İlçe Tarımsal ve Hayvan Sulama Su Tüketim Ücreti :",format(hayvanToplamSuTuketimUcreti,".2f"))
print("Toplamları :",format(konutlarToplamSuTuketimUcreti+isyeriToplamSuTuketimUcreti+resmidaireToplamSuTuketimUcreti+organizesanayiToplamSuTuketimUcreti+hayvanToplamSuTuketimUcreti,".2f"))
print("İlgili Dönemde Su Faturalarından Elde Edilen Toplam Tutarlar :")
print("İZSU payı :",format(toplamİZSU,".2f"))
print("İlçe Belediyesinin :",format(toplamBornova,".2f"))
print("Büyük Şehir Belediyesinin :",format(toplamBelediye,".2f"))
print("Devletin aldığı tutar:",format(toplamKDV,".2f"))
