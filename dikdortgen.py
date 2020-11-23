# Kenar uzunlukları parametreler (varsayılan değerleri 1) ile belirtilen bir dikdörtgenin
# alanını, çevresini ve kare olup olmadığını hesaplayıp geri döndüren bir fonksiyon yazınız.

def dikdortgen(kenar1=1,kenar2=1):
    return kenar1*kenar2,2*(kenar1+kenar2),kenar1==kenar2