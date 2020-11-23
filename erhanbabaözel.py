toplam_aday=0
en_az_bir_test_bos=0
toplam_dogru=0
toplam_yanlis=0
max_dogru_aday_no=0
max_dogru=0
max_dogru_adayin_yanlis=0
yanlis_dogrudan_fazla=0


aday_no=int (input("Aday numaranızı giriniz:"))
while aday_no>0:
    toplam_aday+=1
    for i in range (1,6):
        adayin_toplam_dogru=0
        adayin_toplam_yanlis=0
        print("Test" ,i,)
        dogru_sayisi=int (input("Doğru sayısını giriniz:"))
        yanlis_sayisi=int (input("Yanlış sayısını giriniz:"))
        adayin_toplam_dogru+=dogru_sayisi
        adayin_toplam_yanlis+=yanlis_sayisi
        if dogru_sayisi+yanlis_sayisi>40 or dogru_sayisi+yanlis_sayisi<0 or dogru_sayisi<0 or dogru_sayisi>40 or yanlis_sayisi<0 or yanlis_sayisi>40:
            print("Doğru ve yanlış sayılarınızı kontrol edip tekrar giriniz:")
            dogru_sayisi = int(input("Doğru sayısını giriniz:"))
            yanlis_sayisi = int(input("Yanlış sayısını giriniz:"))
        if dogru_sayisi+yanlis_sayisi=="0":
            en_az_bir_test_bos+=1
        if adayin_toplam_dogru<adayin_toplam_yanlis:
            yanlis_fazla+=1
        if adayin_toplam_dogru>max_dogru:
            max_dogru_aday_no=aday_no
            max_dogru=adayin_toplam_dogru
            max_dogru_adayin_yanlis=adayin_toplam_yanlis
            
            

print("Aday başına toplam doğru sayısı:") (toplam_dogru*100/toplam_aday)
print("Toplam yanlış sayısı toplam doğru sayısından fazla olan adayların sayısı ve yüzdesi",yanlis_fazla,"%", yanlis_fazla*100/toplam_aday)
print("En az 1 testi (tüm sorularını) boş bırakan adayların sayısı ve yüzdesi",en_az_bir_test_bos,"%", en_az_bir_test_bos*100/toplam_aday)
print("Toplam doğru sayısı en çok olan adayın aday numarası, toplam doğru ve yanlış sayısı:",max_dogru_aday_no,max_dogru,max_yanlis)










