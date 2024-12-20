# PROJECT AKHIR-KELOMPOK 8-DASPRO
Sistem Informasi - A - 2024
 
**SISTEM MANAJEMEN HOTEL**
<<>> Hotel Jatra Balikpapan <<>>
 
# Anggota Kelompok  
1. Hendri Zaidan (2409116013)
2. Najmi Hafizh Mauludan Zain (2409116028)
3. Maifariza Aulia Dyas (2409116032)

# Flowchart

![PA (2)](https://github.com/user-attachments/assets/3631bc1c-0490-4cb3-8415-7bc711b547d4)

# Menu Login atau daftar akun
![Screenshot (164)](https://github.com/user-attachments/assets/30df4070-5d49-42b0-9a7f-c556b166da81)

Pada awal program, akan ditampilkan menu utama dengan melakukan Login atau daftar akun terlebih dahulu.

   * Jika menginputkan angka selain 1 atau 2

     ![Screenshot (295)](https://github.com/user-attachments/assets/26fe9b2a-24af-4af5-854f-b63e9378a6f8)
  
     Maka outputnya pilihan tidak valid dan otomatis akan looping kembali ke fitur menu tamu.
     

**1. Login (jika sudah memiliki akun)**

   jika user milih no 1 maka menampilkan username dan pin,
   jika user telah memiliki akun yang sudah terdaftar dalam data Hotel maka user diminta menginputkan Username dan PIN,

   * Tampilan jika user benar menginputkan Username atau PIN.

   ![image](https://github.com/user-attachments/assets/9e1edc09-2ef9-48e8-8d34-9cb6c649d71e)

   jika username dan pin benar akan masuk ke menu tamu, maka akan menampilkan seperti ini

   ![image](https://github.com/user-attachments/assets/dc8a47a2-646d-4802-bd50-f9bd9edb02e2)
   
   * Tampilan jika user salah menginputkan Username atau PIN.
    
   ![Screenshot (272)](https://github.com/user-attachments/assets/b4afe12c-fcb9-4ade-96b1-c0aea6792d49)

   ^^User salah menginputkan Username^^

   ![Screenshot (274)](https://github.com/user-attachments/assets/8e1037ef-6965-4d29-b602-e569bc4bac1f)

   ^^User salah menginputkan PIN^^ 

   User yang salah memasukkan Username atau PIN, outputnya username dan pin tidak valid dan diminta untuk menginputkan data kembali.

   * Jika user 3 kali mencoba login maka,

     ![image](https://github.com/user-attachments/assets/5e5cba8d-f3f9-4c69-ae5f-20a427957363)

   Outputnya akan di blokir selama 10 detik karena user menginput username salah ke tiga kali percobaan dan kembali ke menu login dan daftar akun.

   
**2. Sign Up (jika belum memiliki akun)**

   Bagi user yang baru mengunjungi Hotel Jatra Balikpapan dan belum memiliki akun maka user menginputkan 2 untuk masuk ke menu sign up, dengan menginputkan nama panjang, username, dan No. Hp.
   
   ![Screenshot (270)](https://github.com/user-attachments/assets/8cf48db2-f082-46b0-bacd-7fc55834248b)

   * Tampilan jika user menginputkan username yang sudah terdaftar  
     
   ![Screenshot (268)](https://github.com/user-attachments/assets/4646f9c0-d257-4f21-b76a-ed011f88c0fa)

   Jika user memasukkan username yang sudah terdaftar dalam hotel, user diminta menginputkan kembali.
   
   * Tampilan jika user menginputkan No. Hp lebih dari 12 digit

     ![Screenshot (269)](https://github.com/user-attachments/assets/88a8f7eb-53d9-43ff-882a-122cbbc49554)

     No. Hp yang dimasukkan user tidak boleh lebih dari 12 digit.
     
   * Tampilan jika user menginputkan No. Hp berupa huruf maka,

     ![image](https://github.com/user-attachments/assets/687de89f-a1e8-4adb-b258-fc5eb6bc69eb)

     maka outputnya Nomor HP harus berupa angka. Silakan coba lagi dan otomatis looping ke menu daftar akun 
 
   * Tampilan user telah terdaftar
  
     ![Screenshot (271)](https://github.com/user-attachments/assets/cabbf530-f015-4845-b239-b172dcc7e810)

     Jika user berhasil untuk Sign Up, otomatis akan ditampilkan akun user dengan saldo E-Money dan PIN yang telah diberikan.

   * Keluar atau mulai ke Mode Login

     Jika user sudah cukup menggunakan daftar akun, user bisa memilih Keluar atau Mulai ke Mode Login. Disaat memilih user akan diberikan dua opsi yaitu
     Keluar yang bisa diartikan langsung keluar exit dari program dan mulai ke Mode Login yang otomatis ketika admin input "Mulai", user akan diarahkan ke Menu awal lagi.

     Jika user memilih keluar maka,
   
     ![image](https://github.com/user-attachments/assets/2a30a240-eb9a-4a05-bd7c-974897cdc654)

     Jika user memilih mulai maka kembali ke menu awal,
 
     ![image](https://github.com/user-attachments/assets/da74b106-10fb-4895-b621-0bd8c5661785)
  
# Jika Masuk dengan Username dan PIN "Admin" (Menu Fitur Admin)

  ![Screenshot (165)](https://github.com/user-attachments/assets/50bf684e-7a5e-4cf4-b99f-396047fac8a8)

 Ketika user menginputkan Username "adminhotel" dan PIN "202921", maka user telah terdaftar sebagai admin. Setelah berhasil melakukan login, admin akan ditampilkan dengan menu fitur admin yang di menu fitur    admin ini bisa melakukan proses CRUD (Create, Read, Update, Delete) data kamar, melihat daftar reservasi, melihat daftar akun, serta logout.

# Jika Masuk dengan Username Tamu (Menu Fitur Tamu)

 ![Screenshot (244)](https://github.com/user-attachments/assets/02908dde-00fd-40cb-8f49-ed11e1c0cbfc)
 
 Tamu menginputkan Username dan PIN yang sudah terdaftar dalam database. Seperti gambar diatas, user menginputkan Username "Mepa" dan PIN "15937" maka user telah berhasil melakukan login sebagai tamu. Selanjutnya tamu akan diarahkan ke menu fitur tamu, yang di menu fitur tamu ini bisa melakukan melihat daftar kamar, buat reservasi, daftar reservasi, cek saldo E Money, Top Up saldo, Update Akun, Cek informasi akun, serta log out dari menu fitur tamu. 


# Jika memilih opsi 1 maka akan diarahkan ke Daftar Kamar

 Setelah masuk ke menu fitur tamu, tamu dapat ketik opsi 1. Pada opsi 1, tamu bisa melihat daftar kamar yang ada di hotel dengan keterangan Nomor kamar, Tipe, Fasilitas, serta Harga/Malam nya.

 ![Screenshot (231)](https://github.com/user-attachments/assets/92af0dd7-0454-43fa-bb54-bab69748ea1b)


# Jika memilih opsi 2 maka akan diarahkan ke Buat Reservasi

  Opsi ini dibuat untuk para pengunjung Hotel Jatra Balikpapan untuk melakukan reservasi kamar. 
Usert melihat daftar kamar terlebih dahulu untuk menginputkan nomor kamar, tanggal reservasi dan waktu reservasi kamar. Tampilannya seperti pada gambar dibawah ini.

 ![Screenshot (224)](https://github.com/user-attachments/assets/a6a1f764-ef17-4046-bd0e-18391846b94d)

* Jika memasukkan nomor kamar yang tidak tersedia di daftar kamar
  
  ![image](https://github.com/user-attachments/assets/4ac18d89-e6c2-4713-8afa-700ff5265250)

  dan otomatis ke menu tamu

* Jika memasukkan nomor kamar telah dipesan, maka

  ![image](https://github.com/user-attachments/assets/e18e6b2c-7cfb-4217-8a89-5bf9e99597ca)

  outputnya nomor kamar telah dipesan dan otomatis ke menu tamu

* Jika memasukkan tanggal dan waktu yang salah, maka

  ![image](https://github.com/user-attachments/assets/4ad64446-27a2-4060-9790-8f5b5663b8a3)

  outputnya Format tanggal atau waktu tidak valid! dan otomatis ke menu tamu
  
* Jika user memilih nomor kamar kalau saldonya gak cukup, maka
  
  ![image](https://github.com/user-attachments/assets/34d06aa1-8845-402b-bf50-f8bd40d46f2b)

  outputnya Saldo Anda tidak cukup! Mohon top up terlebih dahulu. dan otomatis ke menu tamu

* Setelah transaksi reservasi kamar berhasil maka user ditampilkan invoice

  ![343675a2-0573-4543-8f6a-7abba77ae322](https://github.com/user-attachments/assets/1e3cd638-ee93-426c-a571-df84f2adaa4d)

Invoice berguna sebagai bukti pembayaran bahwa reservasi kamar telah berhasil dilakukan dan saldo e money berkurang secara otomatis.

# Jika memilih opsi 3 maka akan diarahkan ke Daftar Reservasi

Opsi ini dibuat untuk tamu yang sudah melakukan reservasi kamar dan ingin mengecek apakah sudah ter-reservasi atau belum. 

* Jika user telah berhasil melakukan reservasi dan ingin mengecek reservasi kamarnya maka tampilan seperti pada gambar di bawah ini

  ![Screenshot (230)](https://github.com/user-attachments/assets/650b2dde-98f4-447d-8ced-b6f53a883e70)

  Telah ditampilkan pada tabel diatas bahwa Putri sudah melakukan reservasi kamar di Hotel Jatra Balikpapan.

* Jika user belum melakukan reservasi kamar
  
  ![Screenshot (275)](https://github.com/user-attachments/assets/77cdf441-55e8-4be4-bed2-5602c05388b0)

  Jika user belum melakukan reservasi kamar, naka tampilan pada tabel akan kosong.


# Jika memilih opsi 4 maka akan diarahkan ke Cek Saldo E Money

  ![Screenshot (280)](https://github.com/user-attachments/assets/f5ca3e53-3f9c-4801-9842-3f863d2fd89f)

 Pada opsi 4, tamu bisa mengecek terlebih dahulu nominal saldo di E Money mereka yang tersimpan dalam database.


# Jika memilih opsi 5 maka akan diarahkan ke Top Up Saldo

  ![Screenshot (277)](https://github.com/user-attachments/assets/ab844785-be3f-4ff6-9da2-083aec5fe5a9)

  Ketika saldo E Money kurang, user bisa melakukan Top Up saldo ke E Money, tamu diminta untuk memasukkan nominal untuk ditambahkan dan nominal harus minimal 20000 dan maksimal 6000000.

  jika user menginput kurang dari 20000 maka,

  ![image](https://github.com/user-attachments/assets/e115f0ed-2180-4ca5-977f-07ed5cfa72bd)

  outputnya user harus top up saldo lebih dari 20000
  
  ![image](https://github.com/user-attachments/assets/5cdc2cee-141f-4d35-9b40-b432defbbbe5)

  jika user menginput lebih dari 6000000 maka,

  outpunya user harus top up maksimal 6000000 dan tidak boleh melebihi batas,

* Setelah transaksi Top Up saldo berhasil maka user ditampilkan invoice

  ![invoice saldo](https://github.com/user-attachments/assets/16ce4f0b-127f-4ad5-8da4-cfa5bdab8bea)

Invoice berguna sebagai bukti pembayaran bahwa transaksi pengisian saldo telah berhasil dilakukan dan saldo e money nya bertambah secara otomatis.


# Jika memilih opsi 6 maka akan diarahkan ke Update Akun

  Tamu juga bisa meng-Update akun yang mereka punya dengan mengubah Username, PIN, ataupun No. Hp yang baru. 

  ![Screenshot (242)](https://github.com/user-attachments/assets/64fdf766-1ad9-499e-87c4-82ad4220ed48)

  Pada gambar diatas, tamu dengan username "Siti" ingin mengubah usernamenya menjadi "Kela" dan otomatis ke menu login. dan login harus menginput username barunya.

  ![Screenshot (243)](https://github.com/user-attachments/assets/dc79337d-d1b0-4b2e-aaca-6ce74130e507)

  kemudian stelah login, ketika dia mengecek informasi akunnya, usernamenya telah diganti menjadi "Kela".


# Jika memilih opsi 7 maka akan diarahkan ke Cek Informasi Akun

 ![image](https://github.com/user-attachments/assets/d55c37a6-b7e6-4db2-926f-aefa7ffa1c49)

 Tamu dengan nama "Mepa" ingin mengecek informasi akun miliknya dengan memilih opsi 7. Pada opsi ini "Mepa" akan melihat informasi tentang akunnya yang telah disimpan dalam data hotel seperti Nama Panjang, Username, PIN, serta No.Hp.


# Jika memilih opsi 8 maka akan diarahkan ke Log Out

  Jika tamu sudah cukup menggunakan menu tamu, user bisa memilih Keluar atau Mulai ke Mode Login. Disaat memilih tamu akan diberikan dua opsi yaitu
  Keluar yang bisa diartikan langsung keluar exit dari program dan mulai ke Mode admin yang otomatis ketika tamu input "Mulai", user akan diarahkan ke Menu awal lagi.
  
  ![Screenshot (281)](https://github.com/user-attachments/assets/0b6d9ba4-c2a3-40e8-9ffc-f32125e6cbcd)

  Pada opsi 8 ini tamu bisa melakukan Log Out dari program atau mulai kembali ke menu login.

* Tampilan jika keluar dari program
  Jika memilih keluar dari program, maka menampilkan output seperti pada gambar dibawah ini.
  
  ![Screenshot (187)](https://github.com/user-attachments/assets/1f526bcd-a11e-44c1-9ab7-3a8ba75be858)

* Tampilan jika mulai kembali
  Jika mulai kembali, maka kembali diminta untuk memasukkan Username dan PIN.

  ![Screenshot (186)](https://github.com/user-attachments/assets/93df42e8-9423-4c23-8510-db3652cd6194)


# Jika tamu input selain opsi 1-8

  ![Screenshot (296)](https://github.com/user-attachments/assets/9e2f59db-5625-4692-8db7-41b6a7f43dd8)

  Maka outputnya pilihan tidak valid! dan dengan otomatis akan looping kembali ke fitur menu tamu.

# Tampilan Mode Create (Tambah Kamar) Pada Admin

 Jika admin ingin menambah kamar hotel, input angka 2.
 
![Screenshot (253)](https://github.com/user-attachments/assets/c64918d2-81ef-4fa2-908b-2964b178ea62)

 Setelah itu admin diminta memasukkan nomor lantai, nomor kamar, tipe kamar, fasilitas kamar, dan harga per malam sesuai keinginan admin. 
 
![Screenshot (254)](https://github.com/user-attachments/assets/9dc87e23-29ff-4b5b-b7b5-505ab85ac469)

 Proses tambah kamar berhasil dilakukan dan masuk ke daftar kamar Hotel Jatra Balikpapan.

 Jika admin menginput lantai selain lantai dari database hotel, maka

 ![image](https://github.com/user-attachments/assets/0119d5df-2db1-4d93-875f-efcf4de425a1)

 Outputnya Lantai tidak valid! Harap masukkan 3, 4, atau 5. dan otomatis looping ke menu admin.

 Jika admin menginput nomor kamar yang tidak ada di lantai di databse hotel, maka

 ![image](https://github.com/user-attachments/assets/66639d3c-f7b1-4d49-8125-d184a277ffb4)

 Outputnya Nomor kamar untuk lantai 4 harus dalam rentang 400 - 499 dan otomatis looping ke menu admin.

 Jika admin menginput harga/malam selain angka maka,
 
 ![image](https://github.com/user-attachments/assets/1812fed7-09a0-4672-bd13-3f9a9518535b)

 Outputnya Input harga tidak sesuai! Harap masukkan angka bulat! dan otomatis looping ke menu admin.

 Jika admin menginput nomor kamar yang sudah ada di daftar kamar maka,

 ![image](https://github.com/user-attachments/assets/9c75033b-5725-413b-8c45-227d7d32f668)

 Outputnya Kamar 401 sudah ada di lantai 4 dan otomatis looping ke menu admin.

# Tampilan Mode Read pada Admin (Insert Fitur Sorting dan Searching)

Pada opsi ini admin bisa melakukan proses menyusun data atau elemen-elemen dalam suatu urutan tertentu, seperti nomor, nama panjang, username, PIN, No. Hp, dan saldo E Money, abjad, atau karakteristik lainnya. Selain itu, admin juga dapat melakukan searching atau proses mencari informasi atau nilai tertentu dalam suatu kumpulan data atau struktur. Sorting dan searching ini sangat berguna dalam berbagai aplikasi, mulai dari penyimpanan data, pemrosesan informasi, hingga optimasi pencarian.

**1. Sorting dan Searching Daftar Akun**

   **Sorting Akun**

   Admin dapat melakukan sorting daftar akun tamu dengan menyusun data dengan urutan alfabet nama panjang tamu.

   * Sebelum
    
   ![Screenshot (259)](https://github.com/user-attachments/assets/7e8589d5-f3f1-45b0-bd79-eef422e49135)

   Daftar akun tamu sebelum di sorting.

   * Sesudah
    
   ![Screenshot (261)](https://github.com/user-attachments/assets/c07df62c-9fc2-42b5-89a0-5547e9145f93)

   Admin telah melakukan sorting daftar akun tamu dengan menyusun data dengan urutan alfabet nama panjang tamu.

   **Searching Akun**

  Admin dapat melakukan searching akun tamu dengan menginputkan username dari tamu yang ingin dicari.
  
   ![Screenshot (263)](https://github.com/user-attachments/assets/5708801a-1a2e-4168-af1b-b1a07c4c0eaf)

   Seperti pada gambar diatas, user dapat mencari akun dengan menginputkan username "Adel". Otomatis program menampilkan akun "Adel".

   Jika admin melakukan searching akun yang tidak ada maka,

   ![image](https://github.com/user-attachments/assets/7cb3235a-de2c-45af-b5f5-208f4373994a)

   Seperti pada gambar di atas, tabel kosong karena username "risky" ini tidak terdaftar di database hotel

**2. Sorting dan Searching Daftar Kamar**

   **Sorting Daftar Kamar**

   ![Screenshot (294)](https://github.com/user-attachments/assets/aad11e95-eec6-4ab8-80c4-f1141d478db7)

   Admin dapat melakukan sorting daftar kamar dengan menyusun data dengan mengurutan kamar sesuai dengan nomor kamar.

   
   **Searching Kamar**

   ![Screenshot (285)](https://github.com/user-attachments/assets/542b41cf-3214-4e0d-9829-126f31376a32)

   Admin dapat melakukan searching kamar dengan menginputkan nomor kamar yang ingin dicari.

   Jika admin melakukan searching akun yang tidak ada maka,
   
   ![image](https://github.com/user-attachments/assets/6a3fa78a-ba58-4929-9598-c1712a779486)

   Seperti pada gambar di atas, tabel kosong karena nomor kamar "711" ini tidak terdaftar di database hotel
   
# Tampilan Mode Update Kamar pada Admin

![Screenshot (290)](https://github.com/user-attachments/assets/d7ecb9fa-527e-43d2-9d76-25722b070db0)

Admin bisa melakukan update kamar dengan memilih lantai kamar, masukkan nomor kamar yang ingin diubah, masukkan nomor baru, masukkan tipe kamar baru, dan harga per malam. Nomor kamar yang ingin diubah harus tersedia dalam daftar kamar. Seperti pada gambar diatas, admin ingin mengupdate kamar di kamar 311.

* Sebelum di Update

 ![Screenshot (231)](https://github.com/user-attachments/assets/92af0dd7-0454-43fa-bb54-bab69748ea1b)

* Sesudah di Update
  
  ![Screenshot (291)](https://github.com/user-attachments/assets/39f915df-fa45-49d2-9b7c-a1990ffa1a3b)

* Jika nomor kamar yang dimasukkan tidak ditemukan.
  
 ![Screenshot (293)](https://github.com/user-attachments/assets/e425cfd1-8d08-474e-b457-bfe4fa1423ca)


# Tampilan Mode Remove (Hapus Kamar) pada Admin

![Screenshot (256)](https://github.com/user-attachments/assets/8f9c3eff-ae55-4bcd-b1a4-85f70a7c8096)

  Pada opsi ini, admin bisa menghapus kamar dari daftar kamar dengan memasukkan nomor kamar yang ingin dihapus.
 
 
* Untuk melihat daftar kamar setelah nomor kamar tersebut dihapus yaitu dengan ketik 1.
  
 ![Screenshot (257)](https://github.com/user-attachments/assets/1cc81466-caf4-4125-97f5-1d13fda98011)

  Nomor kamar sudah tidak ada dalam daftar kamar.


# Tampilan Mode Read (Daftar Reservasi)

![Screenshot (258)](https://github.com/user-attachments/assets/41381dc1-1963-4a13-87c1-1924000f18a1)

 Opsi ini dibuat untuk admin yang ingin melihat daftar akun tamu yang sudah melakukan reservasi di Hotel Jatra Balikpapan.


# Tampilan Mode Read (Daftar Akun)

 ![Screenshot (259)](https://github.com/user-attachments/assets/7e8589d5-f3f1-45b0-bd79-eef422e49135)

 Pada opsi 6 ini, admin dapat melihat daftar-daftar akun dari para tamu pengunjung hotel. 


# Tampilan Mode Log Out

 ![Screenshot (184)](https://github.com/user-attachments/assets/bad2ad02-edc6-4b3a-a566-ad82323c5d46)

 Jika admin cukup menggunakan fiturnya, tamu bisa memilih opsi 7 yaitu Keluar atau Mulai ke Mode Login. Disaat memilih admin akan diberikan dua opsi yaitu
 Keluar yang bisa diartikan langsung keluar exit dari program dan mulai ke Mode Login yang otomatis ketika admin input "Mulai", tamu akan diarahkan ke Mode Login lagi.

* Tampilan jika keluar dari program
  
  Jika memilih keluar dari program, maka menampilkan output seperti dibawah ini.
  
 ![Screenshot (260)](https://github.com/user-attachments/assets/bacfee43-2c23-457f-a8ee-f2af4f5c57ad)


* Tampilan jika mulai kembali
  
  Jika mulai kembali, maka admin kembali ke menu login untuk memasukkan Username dan PIN kembali. 

 ![Screenshot (186)](https://github.com/user-attachments/assets/a1c69469-ad00-4bd7-b0b3-26b57178237c)


# Jika admin input selain opsi 1-7

![Screenshot (297)](https://github.com/user-attachments/assets/b539ce9b-2549-4e54-86cb-e6edcf95262e)

Maka outputnya pilihan tidak valid dan otomatis akan looping kembali ke fitur menu admin.
