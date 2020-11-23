#Problem:
# Kullanıcıdan bir üçgenin önce en uzun kenarının,
# daha sonra kısa kenarlarının uzunluklarını (tamsayı) alan ve
# üçgenin tipini ("üçgen değil", "dik üçgen", "geniş açılı üçgen",
# "dar açılı üçgen" şeklinde) belirleyen bir algoritma ve program yazınız.


#Algoritma:
#uzun_kenar=input()
#kisa_kenar1=input()
#kisa_kenar2=input()
#
#if uzun_kenar>=kisa_kenar1+kisa_kenar2:
#    print("üçgen değil")
#elif uzun_kenar*uzun_kenar==kisa_kenar1*kisa_kenar1+kisa_kenar2*kisa_kenar2:
#    print("dik üçgen")
#elif uzun_kenar*uzun_kenar>kisa_kenar1*kisa_kenar1+kisa_kenar2*kisa_kenar2:
#    print("geniş açılı üçgen")
#else:
#    print("dar açılı üçgen")


#Program:
uzun_kenar=int(input("Üçgenin en uzun kenarının uzunluğunu giriniz:"))
kisa_kenar1=int(input("Üçgenin diğer bir kenarının uzunluğunu giriniz:"))
kisa_kenar2=int(input("Üçgenin diğer kenarının uzunluğunu giriniz:"))

if uzun_kenar>=kisa_kenar1+kisa_kenar2:
    print("Girilen sayılar bir üçgen oluşturmuyor!")
elif uzun_kenar*uzun_kenar==kisa_kenar1*kisa_kenar1+kisa_kenar2*kisa_kenar2:
    print("Bu üçgen, bir dik üçgendir")
elif uzun_kenar*uzun_kenar>kisa_kenar1*kisa_kenar1+kisa_kenar2*kisa_kenar2:
    print("Bu üçgen, geniş açılı bir üçgendir")
else:
    print("Bu üçgen, dar açılı bir üçgendir")
