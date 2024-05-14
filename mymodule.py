# mymodule.py

def harf_kontrol(harf):
    ascii_value = ord(harf)

    if(ascii_value>=65 and ascii_value<=90)or(ascii_value>=97 and ascii_value<=122):
        return True
    else:
        return False

def kucuk_harfe_cevir(harf):
    ascii_value = ord(harf)
    if ascii_value >= 65 and ascii_value <= 90:
        return chr(ascii_value + 32)
    else:
        return harf

def frekans_hesapla(metin):
    harf_sayisi = {}
    toplam_harf = 0

    for char in metin:
        if char.isalpha():
            char = char.lower()
            harf_sayisi[char] = harf_sayisi.get(char, 0) + 1
            toplam_harf += 1

    frekans = {char: count / toplam_harf * 100 for char, count in harf_sayisi.items()}
    return frekans

def print_info():
    print("Ad: Ahmet Talha")
    print("Soyad: Can")
    print("Öğrenci Numarası: 211220057")
    print("Not: Düşünmek insanı hür, fikirleri özgür kılar.")
