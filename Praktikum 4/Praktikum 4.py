import random

#Daftar ini memberikan gambaran tentang waktu kegiatan.
Kalimat_starter = random.randint(1, 3)
if Kalimat_starter == 1 :
    kalimat_1 = ("Pada hari minggu, ")
if Kalimat_starter == 2 :
    kalimat_1 = ("Pada hari senin, ")
if Kalimat_starter == 3 :
    kalimat_1 = ("Pada hari selasa, ")
    
#Daftar ini menggambarkan tentang karakter utama dari cerita ini.
karakter = random.randint(1, 3)
if karakter == 1 :
    kalimat_2 = ("andy pergi ke sekolah ")
if karakter == 2 :
    kalimat_2 = ("andy pergi ke toko buku ")
if karakter == 3 :
    kalimat_2 = ("andy pergi ke taman bermain ")

#Daftar ini menentukan hari yang tepat di mana beberapa insiden telah terjadi.
waktu = random.randint(1, 3)
if waktu == 1 :
    kalimat_3 = ("Tony berangkat pada pukul 6 pagi ")
if waktu == 2 :
    kalimat_3 = ("Tony berangkat pada pukul 2 siang ")
if waktu == 3 :
    kalimat_3 = ("Tony berangkat pada pukul 4 sore ")

#Daftar ini mendefinisikan plot cerita.
story_plot = random.randint(1, 3)
if story_plot == 1 :
    kalimat_4 = ("Sesampainya di sana, dia baru menyadari bahwa, ")
if story_plot == 2 :
    kalimat_4 = ("Tiba-tiba, dia dikejutkan oleh seseorang, ")
if story_plot == 3 :
    kalimat_4 = ("andy menghampiri seseorang di sana, ")

#Daftar ini mendefinisikan tempat di mana insiden itu terjadi.
tempat = random.randint(1, 3)
if tempat == 1 :
    kalimat_5 = ("Di dekat coffee shop, ")
if tempat == 2 :
    kalimat_5 = ("Di samping bangunan tua, ")
if tempat == 3 :
    kalimat_5 = ("Di stasiun kereta, ")

#Daftar ini mendefinisikan karakter kedua dari cerita.
second_character = random.randint(1, 3)
if second_character == 1 :
    kalimat_6 = ("emma, orang yang dia kenal, membawa tas plastik ")
if second_character == 2 :
    kalimat_6 = ("dago, sepupu anehnya, berpakaian serba hitam ")
if second_character == 3 :
    kalimat_6 = ("dimas, sahabatnya, berpakaian Santa ")

#Daftar ini menceritakan tentang pekerjaan yang dilakukan karakter kedua.
pekerjaan = random.randint(1, 3)
if pekerjaan == 1 :
    kalimat_7 = ("bertingkah laku mencurigakan ")
if pekerjaan == 2 :
    kalimat_7 = ("mengeluarkan sesuatu dari tasnya ")
if pekerjaan == 3 :
    kalimat_7 = ("menyapa semua orang di sekitarnya ")

#Daftar ini menceritakan interaksi karakter utama dan karakter kedua.
interaksi = random.randint(1, 3)
if interaksi == 1 :
    kalimat_8 = ("yang membuatnya mengejar andy yang sudah lari terlebih dahulu. ")
if interaksi == 2 :
    kalimat_8 = ("andy memberanikan diri untuk menyapanya ")
if interaksi == 8 :
    kalimat_8 = ("andy mengacuhkannya, bertingkah tak mengenalinya ")
    
print (kalimat_1, kalimat_2, kalimat_3, kalimat_4, kalimat_5, kalimat_6, kalimat_7, kalimat_8)
