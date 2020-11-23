# ax+b=c şeklinde verilen bir lineer denklem
# aşağıdaki formül kullanılarak çözülebilir:
#
# x=(c-b)/a
#
# Buna göre (a,b,c) sayılarını kullanıcıdan alan ve x’in değerini bularak
# ekrana yazdıran bir program yazınız.

a_float=float(input("a sayısını giriniz:"))
b_float=float(input("b sayısını giriniz:"))
c_float=float(input("c sayısını giriniz:"))

if a_float==0:
    print("Sonuç yok!")
else:
    x=(c_float-b_float)/a_float
    print("x=",x)
