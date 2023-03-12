# Python & Selenium Kursu
# 8 Mart 2023 
# Ödev-1

# Soru-1
# Python Veri Tipleri 

# 1- Metinsel Veri Tipleri (String)

# Dikkat: Metinsel tüm veriler "iki tırnak içinde" yazılmalıdır.

#Örnek
metin = "Bu bir metinsel veridir."
print(type(metin))
print(metin)

# 2- Sayısal Veri Tipleri (int, float, complex)

# int: Tam sayı değerlerini saklar
# float: Ondalıklı sayıları saklar
# complex: Sayı ve harf karmasını saklar

# Dikkat: Sayısal veri tipleri tırnak içinde yazılmaz.

#Örnek
sayi1 = 365 #integer tipinde
print("....................")
print(type(sayi1))
print(sayi1)
print("....................")
sayi2 = 23.59 #float tipinde
print(type(sayi2))
print(sayi2)
print("....................")
sayi3 = 5 + 6j #complex tipinde
print(type(sayi3))
print(sayi3)

# 3- Boolean Veri Tipi (bool)

# bool: Sadece True(1) ve False(0) verisini tutar

#Örnek
print("....................")
print(type(sayi2 == sayi3))
print(sayi2 == sayi3)
print(sayi2 , "Eşit Değil" , sayi3)

# 4- Sıralama Tipi Veriler (list, tuple, range)

# list: Birden çok ögeyi tek değişkende toplar
# tuple: Birden çok ögeyi tek değişkende toplar
# range: Belirli bir dizi arasında tekrarlı döngü sağlar

# Dikkat: list ile tuple arasındaki iki temel fark:
# > list :
# 1- Köşeli [parantez] ile kullanılır 
# 2- İçeriği sıralıdır, "değiştirilebilir" ve yinelenen değerler kullanılabilir

# > tuple :
# 1- Normal (parantez) ile kullanılır
# 2- İçeriği sıralıdır, "değiştirilemez" ve yinelenen değerler kullanılabilir

#Örnek
list1 = ["Python" , "C#" , "Java"]
print("....................")
print(type(list1))
print(list1)
print("....................")
tuple1= ("Yazılım" , "Donanım" , "Bilgisayar")
print(type(tuple1))
print(tuple1)
print("....................")
sayisay = range(7)
print(type(sayisay))
for n in sayisay:
  print(n)

# Dikkat: range(7) yapıldığında 0 ile 6 arasında sayar, zira doğal sayılar kümesi "Sıfır" (0) ile başladığı için onu da saymış olur.

# 5- Haritalama Tipi Veri (dict)

# dict: Sözlük tipidir ve verileri anahtar:değer çifti olarak depolar
# Dikkat: Sözlük sıralı, değişken ve yinelemesiz bir veri tipidir

#Örnek
print("....................")
sozluk = {
  "Ak" : "Beyaz" , 
  "Ar" : "Namus" ,
  "Talebe" : "Öğrenci"
}
print(type(sozluk))
print(sozluk)

# 6- Ayar-Küme Tipi Veriler (set, frozenset)

# set: Bir küme nesnesi oluşturur
# frozenset: Bir küme nesnesini (set) dondurur 
# Dikkat: (set) sırasızdır ve değiştirilebilir, (frozenset) ise (set) tipi ile oluşturulmuş nesne kümesini dondurur ve değiştirilemez yapar

#Örnek
print("....................")
nesne1 = set (('Çilek' , 'Mango' , 'Muz')) 
print(type(nesne1))
print(nesne1)
print("....................")
sebzeler = ['Ispanak' , 'Lahana' , 'Soğan']
nesne2 = frozenset(sebzeler)
print(type(nesne2))
print(sebzeler)

# 7- İkili-Binary Tip Veriler (bytes, bytearray, memoryview)

# bytes: Bir bayt nesnesi döndürür
# bytearray: Bir bayt nesnesi döndürür
# memoryview: Bir nesneden bellek görünümü nesnesi döndürür

# Dikkat: (bytes) ile (bytearray) arasındaki temel fark:
# - bytes = Değiştirilemeyen bir nesne döndürür
# - bytearray = Değiştirilebilir bir nesne döndürür

#Örnek
print("....................")
aa = bytes(6) #Altı bayt'lık nesne döndürür
print(type(aa))
print(aa)
print("....................")
bb = bytearray(6)
print(type(bb))
print(bb)
print("....................")
cc = memoryview(b"Merhaba")
print(type(cc))
print(cc)

#İlk karakterin Unicode değeri için
print(cc[0])
#Altıncı karakterin Unicode değeri için
print(cc[5])


# Soru-2
# Kodlama.io sitesinde:
# string tipindeki veriler: Kurslarım, Kariyer, Sık Sorulan Sorular gibi metinsel ifadeler
# integer tipindeki veriler: Kurs ilerleme yüzdeleri
# list tipindeki veriler: Eğitmen, Kategori

# Soru-3
# Kodlama.io sitesinde bulunan şart blokları:
# 1- Site Giriş sayfası olabilir (Doğru kullanıcı adı ve parola mı)
# 2- Kurs Tamamlama Durumu olabilir (Tamamladı mı tamamlamadı mı)
# 3- Kayıt Ol sekmesi olabilir (Daha önce kayıt olup olmama durumunu)

#Örnek
print("....................")

# Giriş Doğrulaması
print("Kullanıcı Adı:" , " ")
yaz1 = input()
print("Parolanızı Girin" , " ")
yaz2 = input()
if yaz1 == "admin" and yaz2 == "123456" :
  print("Başarıyla Giriş Yaptınız")
else :
  print("Başarısız Giriş! Tekrar Deneyiniz")

print("....................")

#indigo6alfa

#SON
#SON
#SON