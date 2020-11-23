ad_soyad=input('ad soyad giriniz:')

diploma_notu=float(input('diploma notunuzu 100 üzerinden giriniz:'))

sinav_puani=float(input('sınav puanınızı giriniz:'))

kayitli_kayitsiz=float(input('önceki yıl yükseköğretim programına kayıt yaptırdıysanız 1 yaptırmadıysanız 0 giriniz:'))

obp=diploma_notu*5


alan_disi_ek_puan = float((obp*0.12-obp*((kayitli_kayitsiz*1/2)*0.12)))

alan_ici_ek_puan = float((obp*0.12-obp*((kayitli_kayitsiz/2)*0.12))+(obp*0.06-obp*((kayitli_kayitsiz/2)*0.06)))

alan_disi_yerlestirme_puan = sinav_puani + alan_disi_ek_puan

alan_ici_yerlestirme_puani = sinav_puani+alan_ici_ek_puan


print ('sayın', ad_soyad)
print ('OBPniz :', format(obp, '.5f'))
print("Alan disi ek puan : ", format(alan_disi_ek_puan, ".5f"))
print("Alan ici ek puan : ", format(alan_ici_ek_puan, ".5f"))
print("Alan disi yerlestirme puani : ", format(alan_disi_yerlestirme_puan, ".5f"))
print("Alan ici yerlestirme puani : ", format(alan_ici_yerlestirme_puani,".5f"))

