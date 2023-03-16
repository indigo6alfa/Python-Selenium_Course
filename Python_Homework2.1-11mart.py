import datetime
import time

# e-Okul Yönetim Bilgi Sistemi

#! Giriş
girisYetki = ["944306" , "06"]
saat = datetime.datetime.now()

print("""
[MEB]=========e-Okul=========[-][o][x]
|       Yönetim Bilgi Sistemi        |
|             Sürüm 1.1              |
|       Lütfen Kullanıcı Adı         |
|         ve Şifreyi Girin           |
|====================================|
""")
time.sleep(0.5)
print("Kimlik Doğrulama Ekranı Yükleniyor...")
time.sleep(1.5)

yaz1 = input(("Kullanıcı Adı: "))
yaz2 = input(("Şifre: "))

while True:
    if yaz1 == girisYetki[0] and yaz2 == girisYetki[1] :
        time.sleep(0.5)
        print("Yönetici Olarak Giriş Yapıldı!")
        print("Giriş Zamanı: " , saat)
        break

    else :
        print ("Hatalı Giriş Yaptınız!")
        print( "Çıkış Sayfasına Yönlendiriliyor...")
        exit()

print("********************************")

ogrenciListe = []

print("Hizmetler Yükleniyor...")
time.sleep(2.5)
islemListe = print(""" 
---------HİZMETLER---------
Lütfen yapmak istediğiniz işlem sayısını girin!
1. Öğrenci Ekle
2. Öğrenci Sil
3. Çoklu Ekle
4. Çoklu Sil
5. No Bul
6. Tam Listeyi Görüntüle
7. Çıkış Yap
---------------------------
""")
print(islemListe)

#! Fonksiyonlar

#? Ekleme İşlemi
def ekle():
    print("*************")
    print("Öğrenci Ekleme Sistemi - Kod 1")
    girdi1 = input("Öğrencinin Adını Girin: ")
    girdi2 = input("Öğrencinin Soyadını Girin: ")
    ogrenciListe.append(girdi1 + girdi2)
    print(girdi1 + girdi2 , "isimli öğrenci Başarıyla Eklendi!")
    time.sleep(0.5)

#? Silme İşlemi
def sil():
    print("*************")
    print("Öğrenci Silme Sistemi - Kod 2")
    girdi1 = input("Öğrencinin Adını Girin: ")
    girdi2 = input("Öğrencinin Soyadını Girin: ")
    ogrenciListe.remove(girdi1 + girdi2)
    print(girdi1 + girdi2 , "isimli öğrenci Başarıyla Silindi!")
    time.sleep(0.5)

#? Çoklu Ekleme İşlemi
def cokluEkle():
    while True:
        print("*************")
        print("Çoklu Kayıt Sistemi - Kod 3")
        print("Eklemeyi iptal etmek için Ad ve Soyad kısmına 0 (Sıfır) sayısını girin.")
        girdi1 = input("Öğrencinin Adını Girin: ")
        girdi2 = input("Öğrencinin Soyadını Girin: ")
        if(girdi1 and girdi2 == "0"):
            break
        
        else:
            ogrenciListe.append(girdi1 + girdi2)
            print(str(girdi1 + girdi2) , "isimli öğrenci Başarıyla Eklendi!")
            time.sleep(0.5)

#? Çoklu Sil
def cokluSil():
    while True:
        print("*************")
        print("Çoklu Silme Sistemi - Kod 4")
        print("Silmeyi iptal etmek için Ad ve Soyad kısmına 0 (Sıfır) sayısını girin.")
        girdi1 = input("Öğrencinin Adını Girin: ")
        girdi2 = input("Öğrencinin Soyadını Girin: ")
        if(girdi1 and girdi2 == "0"):
            break

        elif(girdi1 + girdi2 in ogrenciListe):
            ogrenciListe.remove(girdi1 + girdi2)
            print(str(girdi1 + girdi2) , "isimli öğrenci Başarıyla Silindi!")
            time.sleep(0.5)

        else:
            print("Lütfen girdiğiniz bilgileri kontrol edin!")

#? No Bulma
def noBul():
    print("*************")
    print("Okul Numarası Bulma Sistemi - Kod 5")
    girdi1 = input("Öğrencinin Adını Girin: ")
    girdi2 = input("Öğrencinin Soyadını Girin: ")
    if(girdi1 + girdi2 in ogrenciListe):
        num = ogrenciListe.index(girdi1 + girdi2)
        print(str(girdi1 + girdi2) , "isimli öğrencinin numarası: " , str(num))
        time.sleep(0.5)
        
    else:
        print("Hatalı Öğrenci Bilgisi!")

#? Tam Liste
def tamListe():
    print("*************")
    print("Öğrenci Listesi - Kod 6")
    if(len(ogrenciListe) == 0):
        print("Liste Boş!")

    else:
        for tliste in ogrenciListe:
            print(tliste)

#! Döngüler

while True:
    print("*************")
    islem = input("Lütfen yapmak istediğiniz işlemi giriniz: ")

    if(islem == "1"):
        ekle()

    elif(islem == "2"):
        sil()

    elif(islem == "3"):
        cokluEkle()

    elif(islem == "4"):
        cokluSil()

    elif(islem == "5"):
        noBul()

    elif(islem == "6"):
        tamListe()

    elif(islem == "7"):
        print("*************")
        print("Çıkış Başarılı...")
        time.sleep(0.5)
        print("Çıkış Zamanı: " , saat)
        break

    else:
        print("Hatalı bir işlem kodu girdiniz!")

#! Not: Yapmak istenilen işlemi girerken üstte çıkan "None" yazısı nereden kaynaklanıyor tespit edilemedi! 

#indigo6alfa

#SON
#SON
#SON