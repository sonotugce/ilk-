
# windows üzerinden kodu istediğimiz gibi okuması için kullanılan komut. (utf-8 üzerinden oku!) (tüm karakterleri destekler)


"""
fonksyion not hesapla
param 1 = isim (str)
param 2 = vize (int)
param 3 = final(int)
return = int

fonsiyona gönderilen 2 notun vize % 40 final %60 hesaplanıp geri döndürecek
"""
def not_hesapla(isim, vize, final):
    vize_hesapla = (vize * 40)/100
    final_hesapla = (final * 60)/100 
    sonuç = int(vize_hesapla + final_hesapla)
    #print(sonuç)

    if sonuç < 46:
        print(isim, " Adlı öğrencimizin not ortalaması :FF")
    elif sonuç > 46 and sonuç < 52:
        print(isim, " Adlı öğrencimizin not ortalaması :DD")
    elif sonuç > 53 and sonuç < 59:
        print(isim, " Adlı öğrencimizin not ortalaması :DC")
    elif sonuç > 60 and sonuç < 66:
        print(isim, " Adlı öğrencimizin not ortalaması :CC")
    elif sonuç > 67 and sonuç < 73:
        print(isim, " Adlı öğrencimizin not ortalaması :CB")
    elif sonuç > 74 and sonuç < 80:
        print(isim, " Adlı öğrencimizin not ortalaması :BB")
    elif sonuç > 81 and sonuç < 87:
        print(isim, " Adlı öğrencimizin not ortalaması :BB")
    elif sonuç > 88 and sonuç < 100:
        print(isim, " Adlı öğrencimizin not ortalaması :AA")


not_hesapla("Tuğçe",55,80)
