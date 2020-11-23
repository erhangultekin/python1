# ax+b=c şeklinde verilen bir lineer denklem
# aşağıdaki formül kullanılarak çözülebilir:
#
# x=(c-b)/a
#
# Buna göre (a,b,c) sayılarını kullanıcıdan alan ve x’in değerini bularak
# ekrana yazdıran bir program yazınız.

a_int=int(input("a sayısını giriniz:"))
b_int=int(input("b sayısını giriniz:"))
c_int=int(input("c sayısını giriniz:"))

x=(c_int-b_int)/a_int

print("x=",x)
