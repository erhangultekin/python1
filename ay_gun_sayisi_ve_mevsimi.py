#Problem:
# Numarası verilen bir ayın (1-12) kaç gün ve hangi mevsimde olduğunu bulan
# bir algoritma ve program yazınız (Şubat ayının 28 gün olduğunu kabul ediniz.).
# Ay numarası 1-12 arasında değilse kullanıcıya hata mesajı verilmelidir.


#Algoritma:
#ay_no=input()
#
#if ay_no<1 or ay_no>12:
#    print("Hatalı giriş")
#else: #Ay no'su hatasız girilmişse... 
#    if ay_no==2:
#        print("28 gün")
#    elif ay_no==4 or ay_no==6 or ay_no==9 or ay_no==11:
#        print("30 gün")
#    else:
#        print("31 gün")
#
#    ay_no_0_11=ay_no%12 #Tüm mevsimlerin ay no'ları, ardışık sayılar haline geliyor
#    if ay_no_0_11<3:
#        print("Kış")
#    elif ay_no_0_11<6:
#        print("İlkbahar")
#    elif ay_no_0_11<9:
#        print("Yaz")
#    else:
#        print("Sonbahar")


#Program:
ay_no=int(input("Ay numarasını giriniz(1-12):"))

if ay_no<1 or ay_no>12:
    print("Ay numarası 1-12 arasında olmalıydı!")
else: #Ay no'su hatasız girilmişse...
    if ay_no==2:
        print("Bu ay 28 gündür")
    elif ay_no==4 or ay_no==6 or ay_no==9 or ay_no==11:
        print("Bu ay 30 gündür")
    else:
        print("Bu ay 31 gündür")
    
    ay_no_0_11=ay_no%12 #Tüm mevsimlerin ay no'ları, ardışık sayılar haline geliyor
    if ay_no_0_11<3:
        print("Bu ay Kış mevsimindedir")
    elif ay_no_0_11<6:
        print("Bu ay İlkbahar mevsimindedir")
    elif ay_no_0_11<9:
        print("Bu ay Yaz mevsimindedir")
    else:
        print("Bu ay Sonbahar mevsimindedir")
