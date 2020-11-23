import dikdortgen
import kuvvet

alan,cevre,kare=dikdortgen.dikdortgen()
print("dikdörtgenin alanı:",alan,"çevresi:",cevre)
if kare==True:
    print("Bu dikdörtgen, bir karedir")

alan,cevre,kare=dikdortgen.dikdortgen(5)
print("dikdörtgenin alanı:",alan,"çevresi:",cevre)
if kare==True:
    print("Bu dikdörtgen, bir karedir")

kenar1=int(input("dikdörtgenin bir kenarının uzunluğunu giriniz:"))
kenar2=int(input("dikdörtgenin diğer kenarının uzunluğunu giriniz:"))
alan,cevre,kare=dikdortgen.dikdortgen(kenar1,kenar2)
print("dikdörtgenin alanı:",alan,"çevresi:",cevre)
if kare==True:
    print("Bu dikdörtgen, bir karedir")

taban=int(input("tabanı giriniz:"))
us=int(input("üssü giriniz(0 ya da daha büyük):"))
print(taban,"üzeri", us,":",kuvvet.kuvvet(taban,us))
