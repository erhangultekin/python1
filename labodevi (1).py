madde_sayisi=int(input("Madde sayısını giriniz:"))
baska_katilimci="e"
ogrenim_durumu_sayisi={}
puan_yazim={"01-10":1,"11-20":2,"21-30":3,"31-40":4,"41-50":5,"51-60":6,"61-70":7,"71-80":8,"81-90":9,"91-100":10}
puan_dagilimi=[]

def veri_al(baska_katilimci,):
    while baska_katilimci=="e" or baska_katilimci=="E":
        ogrenim_durumu=input("Öğrenim durumunuzu giriniz:")
        madde_int = 0
        for madde_no in range(1, int(madde_sayisi)+1):
            puan = int(input("Soru için puanınızı giriniz:"))
            while puan > 100 or puan < 0:
                puan = int(input("Puanınız geçersiz.Yeniden puanınızı giriniz:"))
            madde_int+=1
            madde = [0]*10
            puan_dagilimi.append(madde)
            if puan > 0 and puan < 11:
                puan_dagilimi[madde_int-1][0] += 1
            elif puan > 10 and puan < 21:
                puan_dagilimi[madde_int-1][1] += 1
            elif puan > 20 and puan < 31:
                puan_dagilimi[madde_int-1][2] += 1
            elif puan > 30 and puan < 41:
                puan_dagilimi[madde_int-1][3] += 1
            elif puan > 40 and puan < 51:
                puan_dagilimi[madde_int-1][4] += 1
            elif puan > 50 and puan < 61:
                puan_dagilimi[madde_int-1][5] += 1
            elif puan > 60 and puan < 71:
                puan_dagilimi[madde_int-1][6] += 1
            elif puan > 70 and puan < 81:
                puan_dagilimi[madde_int-1][7] += 1
            elif puan > 80 and puan < 91:
                puan_dagilimi[madde_int-1][8] += 1
            else:
                puan_dagilimi[madde_int-1][9] += 1
        try:
            ogrenim_durumu_sayisi[ogrenim_durumu]+=1
        except KeyError:
            ogrenim_durumu_sayisi[ogrenim_durumu]=1
        baska_katilimci=input("Başka katılımcı var mı?(Evet:e/E)")

def ogrenim_tablo_ciz():
    print("Öğrenim Durumu","\t","Katılımcı Sayısı")
    print("-"*14,"\t","-"*16)

    for ogrenim_durumu in ogrenim_durumu_sayisi:
        print(format(ogrenim_durumu,"7"),format(ogrenim_durumu_sayisi[ogrenim_durumu],"10"))
        print(end="\n")

def madde_puan_tablo_ciz(puan_dagilimi,puan_yazim,madde_sayisi):
    print("Madde No",end="           ")
    for i in puan_yazim:
        print(i,"Puan Arası",end="   \t")
    print(" ")
    print("-"*16,end="\t")
    for i in puan_yazim:
        print("-"*16,end="\t")
    print(" ")

    for x in range(1,madde_sayisi+1):
        print(format(x,"1"),"      ",end="         \t")
        for i in range(1, 11):
            print(format(puan_dagilimi[x - 1][i- 1],"17"),end="")
        print(end="\n")

veri_al(baska_katilimci)
ogrenim_tablo_ciz()
madde_puan_tablo_ciz(puan_dagilimi,puan_yazim,madde_sayisi)