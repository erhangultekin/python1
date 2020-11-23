#Problem:
# Kullanıcıdan bir üçgenin kenar uzunluklarını (tamsayı) alan ve
# üçgenin tipini ("üçgen değil", "dik üçgen", "geniş açılı üçgen",
# "dar açılı üçgen" şeklinde) belirleyen bir algoritma ve program yazınız.


#Algoritma:
#kenar1=input()
#kenar2=input()
#kenar3=input()
#
#if kenar1>kenar2 and kenar1>kenar3: #3 sayının en büyüğünü bulma alg
#    uzun_kenar=kenar1
#    kisa_kenar1=kenar2
#    kisa_kenar2=kenar3
#elif kenar2>kenar3:
#    uzun_kenar=kenar2
#    kisa_kenar1=kenar1
#    kisa_kenar2=kenar3
#else:
#    uzun_kenar=kenar3
#    kisa_kenar1=kenar1
#    kisa_kenar2=kenar2
#
#if uzun_kenar>=kisa_kenar1+kisa_kenar2:
#    print("üçgen değil")
#else:
#    uzun_kenar_kare=uzun_kenar*uzun_kenar
#    kisa_kenarlarin_kareler_toplami=kisa_kenar1*kisa_kenar1+kisa_kenar2*kisa_kenar2
#    if uzun_kenar_kare==kisa_kenarlarin_kareler_toplami:
#        print("dik üçgen")
#    elif uzun_kenar_kare>kisa_kenarlarin_kareler_toplami:
#        print("geniş açılı üçgen")
#    else:
#        print("dar açılı üçgen")


#Program:
kenar1=int(input("Üçgenin bir kenarının uzunluğunu giriniz:"))
kenar2=int(input("Üçgenin diğer bir kenarının uzunluğunu giriniz:"))
kenar3=int(input("Üçgenin diğer kenarının uzunluğunu giriniz:"))

if kenar1>kenar2 and kenar1>kenar3: #3 sayının en büyüğünü bulma alg
    uzun_kenar=kenar1
    kisa_kenar1=kenar2
    kisa_kenar2=kenar3
elif kenar2>kenar3:
    uzun_kenar=kenar2
    kisa_kenar1=kenar1
    kisa_kenar2=kenar3
else:
    uzun_kenar=kenar3
    kisa_kenar1=kenar1
    kisa_kenar2=kenar2

if uzun_kenar>=kisa_kenar1+kisa_kenar2:
    print("Girilen sayılar bir üçgen oluşturmuyor!")
else:
    uzun_kenar_kare=uzun_kenar*uzun_kenar
    kisa_kenarlarin_kareler_toplami=kisa_kenar1*kisa_kenar1+kisa_kenar2*kisa_kenar2
    if uzun_kenar_kare==kisa_kenarlarin_kareler_toplami:
        print("Bu üçgen, bir dik üçgendir")
    elif uzun_kenar_kare>kisa_kenarlarin_kareler_toplami:
        print("Bu üçgen, geniş açılı bir üçgendir")
    else:
        print("Bu üçgen, dar açılı bir üçgendir")
