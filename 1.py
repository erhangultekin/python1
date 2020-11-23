lise_ogrencileri=0
mezun_ogrenciler=0
toplam_aday=0
lise_ogrencileri_net=0
mezun_ogrenciler_net=0
sifir_ceken_lise_ogrencileri=0
en_az_bir_dogru_ve_sifir_yanlis_yapan=0
while True:
    mezuniyet_durumu=input("Adayın mezuniyet durumunu (lise son sınıf için ö,mezun için m) giriniz:")
    dogru_cevap=int(input("Adayın doğru cevap sayısını giriniz:"))
    yanlis_cevap=int(input("Adayın yanlış cevap sayısını giriniz:"))
    net_cevap=dogru_cevap-(yanlis_cevap/4)
    if net_cevap<0 :
        net_cevap=0
    if mezuniyet_durumu=="ö":
        lise_ogrencileri+=1
        lise_ogrencileri_net+=net_cevap
    else:
        mezun_ogrenciler+=1
        mezun_ogrenciler_net+=net_cevap
    print("Bu adayın net cevap sayısı=", format(net_cevap,".2f"))
    if net_cevap==0 and mezuniyet_durumu=="ö":
        sifir_ceken_lise_ogrencileri+=1
    if dogru_cevap>=1 and yanlis_cevap==0:
        en_az_bir_dogru_ve_sifir_yanlis_yapan+=1
    baska_aday=input("Başka aday var mı? (e/h):")
    if baska_aday=="h":
        break
toplam_aday=lise_ogrencileri+mezun_ogrenciler
lise_ogrencileri_yuzdesi=lise_ogrencileri*100/toplam_aday
mezun_ogrenciler_yuzdesi=mezun_ogrenciler*100/toplam_aday
toplam_net=lise_ogrencileri_net+mezun_ogrenciler_net
lise_ogrencileri_ort_net=lise_ogrencileri_net/lise_ogrencileri
mezun_ogrenciler_ort_net=mezun_ogrenciler_net/mezun_ogrenciler
tum_adaylar_ort_net=toplam_net/toplam_aday
sifir_ceken_lise_ogrencileri_yuzdesi=sifir_ceken_lise_ogrencileri*100/lise_ogrencileri
print("Lise son sınıf öğrencilerinin sayısı=",lise_ogrencileri,"ve yüzdesi=%",format(lise_ogrencileri_yuzdesi,".2f"))
print("Mezun öğrencilerin sayısı=",mezun_ogrenciler,"ve yüzdesi=%",format(mezun_ogrenciler_yuzdesi,".2f"))
print("Lise son sınıf öğrencilerinin ortalama net sayısı=",format(lise_ogrencileri_ort_net,".2f"))
print("Mezun öğrencilerin ortalama net sayısı=",format(mezun_ogrenciler_ort_net,".2f"))
print("Tüm adayların ortalama net sayısı=",format(tum_adaylar_ort_net,".2f"))
print("En az 1 doğrusu olup hiç yanlışı olmayan öğrenci sayısı=",en_az_bir_dogru_ve_sifir_yanlis_yapan)
print("Sıfır net yapan lise öğrencilerinin tüm lise öğrencileri içindeki yüzdesi=%",format(sifir_ceken_lise_ogrencileri_yuzdesi,".2f"))
