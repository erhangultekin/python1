def uretim_verilerini_al(uretim_dosyasi,uretim_toplamlari,gun_sayilari):
    gun_no=uretim_dosyasi.readline()
    while gun_no!="":
        makina_no=int(uretim_dosyasi.readline())
        gunluk_uretim=int(uretim_dosyasi.readline())
        uretim_toplamlari[makina_no-1]+=gunluk_uretim
        gun_sayilari[makina_no-1]+=1
        gun_no=uretim_dosyasi.readline()

try:
    uretim_dosyasi=open("aylik_uretim.txt","r")
    makina_say=int(uretim_dosyasi.readline())
    uretim_toplamlari=[0]*makina_say
    gun_sayilari=[0]*makina_say
    uretim_verilerini_al(uretim_dosyasi,uretim_toplamlari,gun_sayilari)
    uretim_dosyasi.close()
except IOError:
    print("Veri dosyası açılamadı ya da okunamadı!")
else:
    print("Makina No   Aylık Üretim   Üretim Yaptığı Gün Sayısı   Günlük Ortalama")
    print("---------   ------------   -------------------------   ---------------")
    for makina_no in range(makina_say):
        print(format(makina_no+1,"9d"),end="   ")
        print(format(uretim_toplamlari[makina_no],"12d"),end="   ")
        print(format(gun_sayilari[makina_no],"25d"),end="   ")
        if gun_sayilari[makina_no]!=0:
            print(format(uretim_toplamlari[makina_no]/gun_sayilari[makina_no],"15.2f"))
        else:
            print(format(0.00,"15.2f"))

    print("\nFabrikanin aylık üretimi:",sum(uretim_toplamlari))
    max_uretim=max(uretim_toplamlari)
    max_no=uretim_toplamlari.index(max_uretim)+1
    print("Aylık üretimi en yüksek olan makinanın numarası:",max_no)
    print("Aylık üretimi en yüksek olan makinanın aylık üretimi:",max_uretim)
