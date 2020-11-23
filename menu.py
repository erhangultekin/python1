# Basit Bir Menu Programi:
#
# Aşağıda arayüzleri ve ne yaptıkları belirtilen fonksiyonlardan oluşan bir program yazınız:
#
# sayi_al(alt_sinir, ust_sinir): kullanıcıdan, parametreler ile belirtilen aralıkta (sınır değerler dahil) bir tamsayı alınmasını sağlar ve bu sayıyı döndürür.
#
# dikdortgen_ciz(dikey_kenar, yatay_kenar): kenar uzunlukları parametreler ile belirtilen dikdörtgeni, ‘*’ karakterini kullanarak ekrana çizer.
#
# faktoriyel(sayi): parametre ile belirtilen sayının faktöriyelini hesaplar ve döndürür.
#
# kombinasyon(n, k): parametreler ile belirtilen C(n,k) kombinasyonunu hesaplar ve döndürür. (   )
#
# menu_goruntule(): ekrana aşağıdaki gibi basit bir menü görüntüler:
# (1) Dikdörtgen çizme
# (2) Faktöriyel hesaplama
# (3) Kombinasyon (C(n,k)) hesaplama
# (0) Çıkış
#
# menu(): bir menü aracılığıyla kullanıcının seçimine göre ilgili işlemlerin yapılmasını sağlar. Burada kullanıcının menü seçimi için [0-3],
# dikdörtgenin dikey kenarı için [1,20], dikdörtgenin yatay kenarı için [1-75], faktoriyeli hesaplacak sayı için [1-10],
# kombinasyonun n değeri için [1-10] ve k değeri için [1-n] aralığında sayılar girmesi sağlanmalıdır. Ayrıca, kullanıcı menü seçimi için 0
# girdiğinde ise çıkmak istediğinden emin olup olmadığı sorulmalı [e/E/h/H], eminse programdan çıkılmalı, değilse tekrar menüye dönülmelidir.

def menu_goruntule(): # parametre almayan ve deger dondurmeyen fonksiyon ornegi
    print("1. Dikdortgen cizme...")
    print("2. Faktoriyel hesaplama...")
    print("3. Kombinasyon (C(n,k)) hesaplama...")
    print("0. Cikis...")

def sayi_al(alt_sinir,ust_sinir): # parametre alan ve deger donduren fonksiyon ornegi
    sayi=int(input())
    while sayi<alt_sinir or sayi>ust_sinir: # sayi dogru girilinceye kadar bekleniyor...
        sayi=int(input("hatali veri girisi, lutfen tekrar giriniz:"))

    return sayi

def dikdortgen_ciz(dikey_kenar, yatay_kenar): # parametre alan ve deger dondurmeyen fonksiyon ornegi
    for i in range(dikey_kenar):
        for j in range(yatay_kenar):
            print('*',end='')
        print('')

def faktoriyel(sayi):
    carpim=1
    for carpan in range(sayi,1,-1):
        carpim=carpim*carpan

    return carpim

def kombinasyon(n,k): # baska bir fonksiyon cagiran fonksiyon ornegi
    return int(faktoriyel(n)/(faktoriyel(k)*faktoriyel(n-k))) # faktoriyel fonksiyonu 3 kez cagriliyor...

def menu():
    cikis='h'
    while cikis=='H' or cikis=='h':
    #while cikis!='E' and cikis!='e': # ustteki satir, bu sekilde de yazilabilir
    #while not (cikis=='E' or cikis=='e'): # ustteki satir, bu sekilde de yazilabilir
        menu_goruntule() # programcinin kendisinin yazdigi fonksiyon cagriliyor...
        print("Seciminizi giriniz [0-3]:",end='') # kutuphane fonksiyonu cagriliyor...
        secim=sayi_al(0,3) # fonksiyon cagriliyor ve dondurdugu deger saklaniyor...

         # kullanicinin istegi yerine getiriliyor...
        if secim==1:
            print("Dikdortgenin dikey kenar uzunlugunu giriniz [1-20]:",end='')
            dikey_kenar=sayi_al(1,20)
            print("Dikdortgenin yatay kenar uzunlugunu giriniz [1-75]:",end='')
            yatay_kenar=sayi_al(1,75)
            dikdortgen_ciz(dikey_kenar,yatay_kenar) # fonksiyon cagriliyor, herhangi bir deger donmuyor...
        elif secim==2:
            print("Faktoriyeli hesaplanacak sayiyi giriniz [1-10]:",end='')
            n=sayi_al(1,10)
            print(n,"!=",faktoriyel(n)) # fonksiyonun dondurdugu deger, baska bir fonksiyona parametre olarak gonderiliyor...
        elif secim==3:
            print("n sayisini giriniz [1-10]:",end='')
            n=sayi_al(1,10)
            print("k sayisini giriniz [1-",n,"]:",end='')
            k=sayi_al(1,n)
            print("C(",n,",",k,")=",kombinasyon(n,k))
        else:
            cikis=input("Cikmak istediginize emin misiniz(e/E/h/H)?:")
            while cikis not in ['e', 'E', 'h', 'H']: # cevap dogru girilinceye kadar bekleniyor...
                cikis=input("hatali veri girisi, lutfen tekrar giriniz:")
    # while sonu

menu()