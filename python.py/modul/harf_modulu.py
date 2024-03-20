# harf_modulu.py

# karakterin harf olup olmadığını kontrol etme
def karakter_harf_mi(karakter):
    return karakter.isalpha()

# büyük harfi küçük harfe çevirme
def buyuk_harf_kucuk_yap(harf):
    return harf.lower()

#haflerin kullanım sıklığını bulma
def harf_kullanim_sikligi(metin):
   
    harf_frekanslari = {}
    toplam_harf_sayisi = 0

    for harf in metin:
        if harf.islower():
            if harf in harf_frekanslari:
                harf_frekanslari[harf] += 1
            else:
                harf_frekanslari[harf] = 1
    toplam_harf_sayisi = sum(harf_frekanslari.values())

    
   
    harf_sikliklari = {}
    for harf, frekans in harf_frekanslari.items():
        yuzde = (frekans / toplam_harf_sayisi) * 100
        harf_sikliklari[harf] = yuzde

    return harf_sikliklari
        


def ogrenci_bilgisi():
    ad="Sena"
    soyad="Kurşun"
    ogrenci_no="211213031"
    notu="Sevgi her şeyi güzelleştirir!"
    return f"Ad: {ad}\nSoyad: {soyad}\nÖğrenci No: {ogrenci_no}\nNot: {notu}"