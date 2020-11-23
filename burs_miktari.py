# Özel bir üniversite tüm öğrencilerine aylık 100 TL burs vermektedir.
# Ayrıca üniversite, not ortalaması 4 üzerinden en az 2 olan tüm öğrencilere
# not ortalamasının 25 katı kadar ve ailesinin aylık geliri asgari ücretin (1300 TL)
# altında olan kız öğrencilere 100 TL ek burs vermektedir. Buna göre bir öğrencinin
# adını soyadını, 4 üzerinden not ortalamasını, cinsiyetini (e/k) ve kız ise
# ailesinin aylık gelirini kullanıcıdan alan (hata kontrolüne gerek yoktur) ve
# öğrencinin alacağı aylık burs miktarını hesaplayarak ekrana yazdıran bir program yazınız.

ad_soyad=input("Adınızı ve soyadınızı giriniz:")
not_ort=float(input("4 üzerinden not ortalamanızı girinizi:"))
cinsiyet=input("Cinsiyetinizi giriniz (e/k):")
if cinsiyet=="k":
    aylik_gelir=float(input("Ailenizin aylık gelirini giriniz:"))

if not_ort<2:
    burs=100
else:
    burs=100+not_ort*25

if cinsiyet=="k" and aylik_gelir<1300:
    burs=burs+100

print("Sayın",ad_soyad,"alacağınız aylık burs miktarı:",format(burs,".2f"),"TL")
