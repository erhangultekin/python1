devam="e"
ogrenim_durumu_dict={}
ogrenim_durumu_list=[]
puan_dict={1:"1-10 Puan",2:"11-20 Puan",3:"21-30 Puan",4:"31-40 Puan",5:"41-50 Puan",6:"51-60 Puan",7:"61-70 Puan",8:"71-80 Puan",9:"81-90 Puan",10:"91-100 Puan"}
puan_sayilari = []
madde_sayisi=int(input("Anketteki madde sayisini giriniz:"))

def tablo_ciz(puan_sayilari,madde_sayisi):
    print("Madde No", end="   ")
    for puan_kodu in range(1, 11):
        print(format(puan_dict[puan_kodu], "14"), end="")
    print(end="\n")
    print(format("--------", "10"), end="")
    for puan_kodu in range(1, 11):
        print(format("------------", "14"), end="")
    madde_int = 0
    print(end="\n")
    for madde in range(1, madde_sayisi + 1):
        madde_int += 1
        print(format(madde_int, "3"), "     ", end="")
        for puan_kodu in range(1, 11):
            print(format(puan_sayilari[madde_int - 1][puan_kodu - 1], "8"), "     ", end="")
        print(end="\n")
def tablo_ogrenim_durumu():
    print(format("Öğrenim Durumu", "14"), end="   ")
    print(format("Katılımcı Sayisi", "14"))
    print(format("---------------", "10"), end="  ")
    print(format("---------------", "10"))
    for i in range(1, len(ogrenim_durumu_dict) + 1):
        print(format(ogrenim_durumu_list[i-1],"14"),end="    ")
        print(format(ogrenim_durumu_dict[ogrenim_durumu_list[i-1]], "6"))
def veri_al(devam,puan_sayilari,madde_sayisi):

    while devam=="e" or devam=="E":



        ogrenim_durumu=input("Öğrenim durumunuzu giriniz:")
        ogrenim_durumu_list.append(ogrenim_durumu)
        ogrenim_durumu_dict[ogrenim_durumu]=ogrenim_durumu_dict.get(ogrenim_durumu,0)+1
        madde_int=0
        for madde in range(1,madde_sayisi+1):
            madde_int+=1
            print(madde,". madde için",end="",sep="")
            puan=int(input("verdiğiniz puanı giriniz:"))
            bir_maddenin_puan_sayilari=[0]*10
            puan_sayilari.append(bir_maddenin_puan_sayilari)
            if puan>= 1 and  puan<11:
                puan_sayilari[madde_int-1][0]+=1
            elif puan>=11 and puan<21:
                puan_sayilari[madde_int-1][1]+=1
            elif puan>=21 and puan<31:
                puan_sayilari[madde_int-1][2]+=1
            elif puan>=31 and puan<41:
                puan_sayilari[madde_int-1][3]+=1
            elif puan>=41 and puan<51:
                puan_sayilari[madde_int-1][4]+=1
            elif puan>=51 and puan<61:
                puan_sayilari[madde_int-1][5]+=1
            elif puan>=61 and puan<71:
                puan_sayilari[madde_int-1][6]+=1
            elif puan>=71 and puan<81:
                puan_sayilari[madde_int-1][7]+=1
            elif puan>=81 and puan<91:
                puan_sayilari[madde_int-1][8]+=1
            else:
                puan_sayilari[madde_int-1][9]+=1


        devam = input("Başka katılımcı var mı(E/e)?")

veri_al(devam,puan_sayilari,madde_sayisi)
tablo_ciz(puan_sayilari, madde_sayisi)
tablo_ogrenim_durumu()