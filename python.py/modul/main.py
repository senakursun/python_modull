# main.py
from harf_modulu import harf_kullanim_sikligi,ogrenci_bilgisi


def main():
    metin = input("Lütfen bir metin girin: ")

    # Harflerin kullanım sıklığını bulma
    harf_sikliklari = harf_kullanim_sikligi(metin)

    # Sonuçları ekrana yazdırma
    print("Metindeki harflerin kullanım sıklığı:")
    for harf, siklik in harf_sikliklari.items():
        print(f"{harf}: %{siklik:.2f}")

    print("\nÖğrenci Bilgileri:")
    print(ogrenci_bilgisi())



if __name__ == "__main__":
    main()


    
