ad_soyad= (input("Adınızı ve soyadınızı giriniz:"))
tt_neti= float (input("Türkçe Testi net sayınızı giriniz:"))
sbt_neti= float (input ("Sosyal Bilimler Testi net sayınızı giriniz:"))
tmt_neti= float (input("Temel Matematik TEsti net sayınızı giriniz:"))
fbt_neti= float (input("Fen Bilimleri Testi net sayınızı giriniz:"))
ayt_neti= float (input("Alan Yeterlilik Testi net sayınızı giriniz:"))
ayt_puani=0
tyt_puani=0
yks_puani=0



if tt_neti >= 0.5 or tmt_neti >= 0.5:
    tyt_puani= (tt_neti*2.4) +(tmt_neti*2.4) + (sbt_neti*2.3) + (fbt_neti*2.3)
    if tyt_puani >= 150 and ayt_neti >= 2.5:
        ayt_puani= ayt_neti*2.5

print ("Sayın:", ad_soyad)
print ("A-TYT puanınız:", format (tyt_puani, ".5f"))
print ("A-AYT puanınız:", format (ayt_puani, ".5f"))

if ayt_puani >= 180 and tyt_puani >= 150:
      yks_puani= (tyt_puani*0.4)+(ayt_puani*0.6)
      print("Üniversitelerin lisans programlarına tercih yapma hakkınız bulunmaktadır ve yerleştirmede kullanılacak YKS puanınız:", format(yks_puani,".5f" ))


if tyt_puani < 150 or ayt_puani < 180:
    print ("Üniversitelerin lisans programlarına tercih yapma hakkınız bulunmamaktadır: ")







