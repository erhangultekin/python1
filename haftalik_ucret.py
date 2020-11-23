# Birim saat ücreti 23,45 TL olan bir işçinin, bir haftada kaç saat
# çalıştığını (tamsayı) alan ve o hafta işçiye ödenecek haftalık ücreti
# hesaplayarak ekrana yazdıran bir program yazınız.
# Haftalık normal çalışma süresi 40 saattir ve bu süreyi aşan saatler
# için birim saat ücretinin 1,5 katı ödeme yapılmaktadır.

calisma_suresi=int(input("Haftalık çalışma süresini (tamsayı) giriniz:"))

ek_ucret=0
if calisma_suresi>40:
    ek_ucret=(calisma_suresi-40)*23.45/2

ucret=calisma_suresi*23.45+ek_ucret

print("Ödenecek ücret:",format(ucret,".2f"),"TL")
