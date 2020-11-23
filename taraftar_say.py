# Belirsiz sayıda kişiden, taraftarı olduğu takımın kısa adını (büyük harflerle) alan ve
# girilen takımların kısa adlarını ve taraftar sayılarını ekranda listeleyen bir program yazınız.

takim_taraftar_say ={}
devam='e'
while devam=='e':
    takim=input("Taraftari oldugunuz takimin kisa adini giriniz:")

    # Alternatif-1
    # if takim in takim_taraftar_say:
    #     takim_taraftar_say[takim]+=1
    # else:
    #     takim_taraftar_say[takim]=1

    # Alternatif-2
    # try:
    #     takim_taraftar_say[takim] += 1
    # except KeyError:
    #     takim_taraftar_say[takim] = 1

    # Alternatif-3
    takim_taraftar_say[takim]=takim_taraftar_say.get(takim,0)+1

    devam=input("Baska taraftar var mi?")

# Alternatif-1
# for takim in takim_taraftar_say:
#     print(takim,takim_taraftar_say[takim])

#Alternatif-2
for takim,taraftar_say in takim_taraftar_say.items():
    print(takim,taraftar_say)
