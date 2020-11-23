def dosya_al():
    liste = []
    liste2=[]
    satir = file.readline()
    while satir != "":
        satir = satir[:-1]
        liste.append(satir.split(" "))
        liste2.append(satir.split(" "))
        satir = file.readline()

    tablo(0, 0, 0, liste,liste2)


def tablo(islem_kodu, sec_sutun, sec_satir, liste,liste2):
    for i in range(len(liste)):
        for x in range(len(liste)):
            if islem_kodu == "D" and sec_satir == i + 1 and sec_sutun == x + 1:
                liste2[i][x] = "{}{}{}".format("(", liste[i][x], ")")

            elif islem_kodu == "B" and sec_satir == i + 1 and sec_sutun == x + 1:
                liste2[i][x] = "{}{}{}".format("-", "X", "-")

                if x==0:
                    if liste2[i][x]==liste2[i][x+1]:
                        liste2[i][x] = "{}{}{}".format("-", liste[i][x], "-")
                        print("Boş kareler, yatay ya da dikey olarak birbirlerine komşu olamazlar.Tekrar giriniz.")

                        oyun(liste, liste2)
                elif x<len(liste)-1 :
                    if liste2[i][x]== liste2[i][x-1] or liste2[i][x]==liste2[i][x+1]:
                        print("Boş kareler, yatay ya da dikey olarak birbirlerine komşu olamazlar.Tekrar giriniz.")
                        liste2[i][x] = "{}{}{}".format("-", liste[i][x], "-")
                        oyun(liste, liste2)
                else:
                    if liste2[i][x]==liste2[i][x-1] or liste2[i][x]==liste2[i+1][x]:
                        print("Boş kareler, yatay ya da dikey olarak birbirlerine komşu olamazlar.Tekrar giriniz.")
                        liste2[i][x] = "{}{}{}".format("-", liste[i][x], "-")
                        oyun(liste, liste2)
            elif islem_kodu == "N" and sec_satir == i + 1 and sec_sutun == x + 1:
                liste2[i][x] = "{}{}{}".format("-", liste[i][x], "-")

    print("    ")
    for sutun in range(1, len(liste) + 1):
        if sutun == 1:
            print("   ", sutun, end="   ")
        else:
            print(sutun, end="   ")
    print("\n")

    for i in range(len(liste)):
        print(i+1, end="  ")
        for x in range(len(liste)):
            if islem_kodu == "D" and sec_satir == i + 1 and sec_sutun == x + 1:
                liste2[i][x] = "{}{}{}".format("(", liste[i][x], ")")
                print(liste2[i][x], end=" ")
            elif islem_kodu == "B" and sec_satir == i + 1 and sec_sutun == x + 1:

                liste2[i][x] = "{}{}{}".format("-", "X", "-")
                print(liste2[i][x], end=" ")
            elif islem_kodu == "N" and sec_satir == i + 1 and sec_sutun == x + 1:
                liste2[i][x] = "{}{}{}".format("-", liste[i][x], "-")
                print(liste2[i][x], end=" ")
            else:
                if liste2[i][x]!=liste[i][x]:
                    print(liste2[i][x],end=" ")
                else:
                    print("{}{}{}".format("-", liste2[i][x], "-"), end=" ")
        print(end="\n")


    print(liste2)




    return oyun(liste,liste2)


def oyun(liste,liste2):
    while True:
        degisiklik = input("Satır numarasını,sütun numarasını ve "
                           "işlem kodunu(B:Boş,D:Dolu,N:Normal/İşaretsiz) aralarında boşluk bırakarak giriniz:")
        liste_degisiklik = []
        liste_degisiklik.append(degisiklik.split(" "))
        sec_sutun = int(liste_degisiklik[0][1])
        sec_satir = int(liste_degisiklik[0][0])
        islem_kodu = str(liste_degisiklik[0][2])

        tablo(islem_kodu, sec_sutun, sec_satir, liste,liste2)


try:
    file = open("hitori_bulmaca.txt", "r")
except IOError:
    print("Veri Dosyası açılamadı ya da okunamadı!")

dosya_al()


