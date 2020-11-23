#Dönem sonu notu hesabına laboratuvar notunun %20, arasınav notunun %30
#ve final sınavı notunun %50 oranda katıldığı bir dersi alan bir
#öğrencinin öğrenci_no ve ad_soyad bilgileri ile laboratuvar, arasınav ve
#final sınavı notlarını kullanıcıdan alarak öğrencinin o derse ilişkin
#dönem sonu notunu bulan ve öğrencinin tüm bilgilerini ekrana yazdıran
#bir program yazınız (tüm notlar, 100’lük sistemde tamsayı şeklinde
#olmalıdır, girdi sırasında hata kontolü yapılmasına gerek yoktur).


#Algoritma:
#ogr_no=input()
#ad_soyad=input()
#lab_notu=input()
#arasinav_notu=input()
#final_notu=input()

#donem_sonu_notu=lab_notu*0.2+arasinav_notu*0.3+final_notu*0.5

#print(ogr_no,ad_soyad)
#print(lab_notu,arasinav_notu,final_notu)
#print(donem_sonu_notu)


#Program:
ogr_no=input('öğrenci numaranızı giriniz:')
ad_soyad=input('adınızı ve soyadınızı giriniz:')

lab_notu_str=input('lab notunuzu giriniz:')
lab_notu=int(lab_notu_str)

arasinav_notu_str=input('arasinav notunuzu giriniz:')
arasinav_notu=int(arasinav_notu_str)

final_notu_str=input('final sinavi notunuzu giriniz:')
final_notu=int(final_notu_str)

donem_sonu_notu=round(lab_notu*0.2+arasinav_notu*0.3+final_notu*0.5)
#donem_sonu_notu=round(lab_notu*0.2+arasinav_notu*0.3+final_notu*0.5,0)

print("Sayin ", ogr_no, "numaralı ", ad_soyad,";")
print("Lab notunuz:",lab_notu)
print("Arasinav notunuz:",arasinav_notu)
print("Final sinavi notunuz:", final_notu)
print("Donem sonu notunuz:", donem_sonu_notu)
#print("Donem sonu notunuz:", format(donem_sonu_notu,".0f"))
