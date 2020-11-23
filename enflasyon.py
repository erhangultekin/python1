#Bir ürünün adını, geçen ayki fiyatını ve bu ayki fiyatını kullanıcıdan
#alan ve ürünün fiyatında meydana gelen aylık değişimin miktarını ve
#yüzdesini bulan bir program yazınız (fiyatlar gerçel sayı olmalıdır,
#çıktılarda ondalık basamak sayısı 2 olmalıdır, girdi sırasında hata
#kontolü yapılmasına gerek yoktur).

urun_adi=input("ürün adını giriniz:")

onceki_fiyat_str=input("ürünün geçen ayki fiyatını giriniz:")
onceki_fiyat=float(onceki_fiyat_str)

simdiki_fiyat_str=input("ürünün bu ayki fiyatını giriniz:")
simdiki_fiyat=float(simdiki_fiyat_str)

fiyat_farki=simdiki_fiyat-onceki_fiyat
fiyat_degisim_orani=fiyat_farki*100/onceki_fiyat

print(urun_adi,"ürününün fiyatındaki aylık değişim;")
print("miktarı:",format(fiyat_farki,".2f"), "TL")
print("oranı: %",format(fiyat_degisim_orani,".2f"))
