# Parametre olarak verilen bir taban sayısının, yine parametre olarak verilen bir kuvvetini
# hesaplayıp geri döndüren özyinelemeli (recursive) bir fonksiyon yazınız.

def kuvvet(taban,us):
    if us==0: # temel durum
        return 1
    else: # özyineleme adimi
        return taban*kuvvet(taban,us-1)

