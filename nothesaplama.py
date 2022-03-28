for ogrenci in range(1,6):
    print(ogrenci)
    print("inci ögrenci notunu giriniz")
    yazili1=int(input("birinci yazılı notunu giriniz..:"))
    yazili2=int(input("ikinci yazılı notunu giriniz..:"))
    yort=(yazili1+yazili2)/2
    sozlu1=int(input("birinci sözlü notunu giriniz..:"))
    sozlu2=int(input("ikinci sözlü notunu giriniz..:"))
    sort=(sozlu1+sozlu2)/2
    ortalama=(yort+sort)/2
    if ortalama<45:
        print("kaldı..:")
        print(ortalama)
    elif ortalama<55:
        print("zayıf..:")
        print(ortalama)
    elif ortalama<70:
        print("orta..:")
        print(ortalama)
    elif ortalama<85:
        print("iyi..:")
        print(ortalama)
    else:
        print("pekiyi..:")
        print(ortalama)
input("devam etmek için bir tuşa basınız")
