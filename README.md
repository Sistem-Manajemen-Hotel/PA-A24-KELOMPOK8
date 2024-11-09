# PROJECT AKHIR-KELOMPOK 8-DASPRO
Sistem Informasi-A 2024
   
**Sistem Manajemen Hotel**

# Anggota Kelompok 
1. Hendri Zaidan (2409116013)
2. Najmi Hafizh Mauludan Zain (2409116028)
3. Maifariza Aulia Dyas (2409116032)

# Flowchart

![PA (2)](https://github.com/user-attachments/assets/3631bc1c-0490-4cb3-8415-7bc711b547d4)

# Menu Login atau Sign Up
![Screenshot (164)](https://github.com/user-attachments/assets/30df4070-5d49-42b0-9a7f-c556b166da81)

Pada awal program, akan ditampilkan menu utama dengan melakukan Login atau Sign Up terlebih dahulu.
1. Login (jika sudah punya akun)
  
   Ketika user telah memiliki akun atau telah memasukkan Username dan PIN yang disimpan dalam database maka user ketik 1, dan dengan otomatis akan diarahkan me menu fitur tamu.
   
   * Tampilan jika user salah menginputkan Username.
     
![Screenshot (197)](https://github.com/user-attachments/assets/d6cdcb06-96ce-4115-ac00-74786f450357)

   User yang salah memasukkan Username dan PIN, diminta untuk menginputkan data kembali.
   
2. Sign Up (jika belum punya akun)
   
   Jika user belum memiliki akun maka user menginputkan 2 untuk masuk ke menu sign up.

# Jika Masuk dengan Username dan PIN "Admin" (Menu Fitur Admin)

![Screenshot (165)](https://github.com/user-attachments/assets/50bf684e-7a5e-4cf4-b99f-396047fac8a8)

Ketika user menginputkan Username "adminhotel" dan PIN "202921", maka user telah terdaftar sebagai admin. Setelah berhasil melakukan login, admin akan ditampilkan dengan menu fitur admin yang di menu fitur admin ini bisa melakukan proses CRUD (Create, Read, Update, Delete) data kamar, melihat daftar reservasi, melihat daftar akun, serta logout.

# Jika Masuk dengan Username Tamu (Menu Fitur Tamu)

![Screenshot (232)](https://github.com/user-attachments/assets/c641477e-c674-4310-95a4-0c935a53438e)

Tamu menginputkan Username dan PIN yang sudah terdaftar dalam database. Seperti gambar diatas, user menginputkan Username "Mepa" dan PIN "15937" maka user telah berhasil melakukan login sebagai tamu. Selanjutnya tamu akan diarahkan ke menu fitur tamu, yang di menu fitur tamu ini bisa melakukan melihat daftar kamar, buat reservasi, daftar reservasi, cek saldo E Money, Top Up saldo, Update Akun, Cek informasi akun, serta log out dari menu fitur tamu. 

# Sign Up Akun (Daftar Akun Baru)
![Screenshot (167)](https://github.com/user-attachments/assets/0bd44bf7-8d0b-4dfe-bd3e-11049e45413b)

Bagi user yang belum memiliki akun untuk melakukan login, maka user bisa sign up dengan menginputkan nama panjang, username dan no. Hp.

* Tampilan output jika user menginputkan username yang telah terdaftar, dan diarahkan untuk sig up kembali. 
![Screenshot (166)](https://github.com/user-attachments/assets/e31934d1-7032-4780-922e-6cec26ff5c68)

Setelah proses sign up berhasil dilakukan, dengan otomatis akan menampilkan output seperti gambar dibawah dengan saldo E Money dan PIN yang telah disimpan dalam database.

![Screenshot (168)](https://github.com/user-attachments/assets/7c3e23e0-91e0-45df-b4cb-f33859780d0d)


# Jika memilih opsi 1 maka akan diarahkan ke Daftar Kamar
![Screenshot (170)](https://github.com/user-attachments/assets/17749cb0-1e85-4508-bfb1-8180a3b91a5c)

Setelah masuk ke menu fitur tamu, tamu dapat ketik opsi 1. Pada opsi 1, tamu bisa melihat daftar kamar yang ada di hotel dengan keterangan Nomor kamar, Tipe, Fasilitas, serta Harga/Malam nya.

![Screenshot (231)](https://github.com/user-attachments/assets/92af0dd7-0454-43fa-bb54-bab69748ea1b)


# Jika memilih opsi 2 maka akan diarahkan ke Buat Reservasi
Opsi ini dibuat untuk para pengunjung Hotel Jatra Balikpapan untuk melakukan reservasi kamar. 
Usert melihat daftar kamar terlebih dahulu untuk menginputkan nomor kamar, tanggal reservasi dan waktu reservasi kamar. Tampilannya seperti pada gambar dibawah ini.

![Screenshot (224)](https://github.com/user-attachments/assets/a6a1f764-ef17-4046-bd0e-18391846b94d)

* Jika memasukkan nomor kamar yang tidak tersedia di daftar kamar
  
![Screenshot (220)](https://github.com/user-attachments/assets/0ff0cd23-8619-4d64-b13c-6751ca9ff67d)

* Setelah transaksi reservasi kamar berhasil maka user ditampilkan invoice

  ![343675a2-0573-4543-8f6a-7abba77ae322](https://github.com/user-attachments/assets/1e3cd638-ee93-426c-a571-df84f2adaa4d)

Invoice berguna sebagai bukti pembayaran bahwa reservasi kamar telah berhasil dilakukan.

# Jika memilih opsi 3 maka akan diarahkan ke Daftar Reservasi
Opsi ini dibuat untuk tamu yang sudah melakukan reservasi kamar dan ingin mengecek apakah sudah ter-reservasi atau belum. 

* Jika user telah berhasil melakukan reservasi dan ingin mengecek reservasi kamarnya maka tampilan seperti pada gambar di bawah ini

![Screenshot (230)](https://github.com/user-attachments/assets/650b2dde-98f4-447d-8ced-b6f53a883e70)

  Telah ditampilkan pada tabel diatas bahwa Putri sudah melakukan reservasi kamar di Hotel Jatra Balikpapan.

# Jika memilih opsi 4 maka akan diarahkan ke Cek Saldo E Money
![Screenshot (174)](https://github.com/user-attachments/assets/3aa5b9eb-c767-4068-a3ce-29588803809d)

Pada opsi 4, tamu bisa mengecek terlebih dahulu nominal saldo di E Money yang telah disimpan dalam database.

# Jika memilih opsi 5 maka akan diarahkan ke Top Up Saldo
![Screenshot (175)](https://github.com/user-attachments/assets/73230227-4ec7-45a6-a063-314e2320ee09)

Saat ingin menambah saldo ke E Money, tamu diminta untuk memasukkan nominal untuk ditambahkan. Dan nominal harus lebih dari 0.

* Jika memasukkan nominal kurang dari 0
Akan menampilkan output bahwa jumlah top up harus lebih dari 0 dan setelah itu diminta memilih opsi 1-5 kembali.
![Screenshot (187)](https://github.com/user-attachments/assets/2155bc43-2136-4208-aa20-28adf39497ca)

* Ketik 4 jika ingin mengecek saldo E Money tamu setelah nominal tadi ditambahkan
  
![Screenshot (176)](https://github.com/user-attachments/assets/68001e60-f4f5-420b-ae0d-bed428be6798)

* Setelah transaksi Top Up saldo berhasil maka user ditampilkan invoice

![invoice saldo](https://github.com/user-attachments/assets/16ce4f0b-127f-4ad5-8da4-cfa5bdab8bea)

Invoice berguna sebagai bukti pembayaran bahwa transaksi pengisian saldo telah berhasil dilakukan.

# Jika memilih opsi 6 maka akan diarahkan ke Update Akun

![Screenshot (214)](https://github.com/user-attachments/assets/30547465-f37f-4400-af45-e416e30f0043)

Tamu juga bisa meng-Update akun yang mereka punya dengan mengubah Username, PIN, ataupun No. Hp yang baru. Pada gambar diatas, user ingin mengubah PIN lama dengan memasukkan PIN nya yang baru.

* Ketik 7 untuk mengecek informasi akun baru setelah di update.
  
![Screenshot (215)](https://github.com/user-attachments/assets/5883373e-128a-4791-9b9a-8dd7a46133c3)


# Jika memilih opsi 7 maka akan diarahkan ke Cek Informasi Akun

![Screenshot (205)](https://github.com/user-attachments/assets/229e9718-be97-4892-8661-2c0b89123f36)

Pada opsi ini tamu akan melihat informasi tentang akun mereka yang telah disimpan dalam database seperti Nama Panjang, Username, PIN, serta No.Hp.

# Jika memilih opsi 8 maka akan diarahkan ke Log Out
![Screenshot (189)](https://github.com/user-attachments/assets/1030ab3a-f98f-48eb-985e-3c4ca0c88185)

Pada opsi 8 ini tamu bisa melakukan Log Out dari program atau mulai kembali.

* Tampilan jika keluar dari program
  Jika memilih keluar dari program, maka menampilkan output seperti dibawah ini.
  
![Screenshot (187)](https://github.com/user-attachments/assets/1f526bcd-a11e-44c1-9ab7-3a8ba75be858)

* Tampilan jika mulai kembali
  Jika mulai kembali, maka kembali diminta untuk memasukkan Username dan PIN.

![Screenshot (186)](https://github.com/user-attachments/assets/93df42e8-9423-4c23-8510-db3652cd6194)

# Tampilan Mode Create (Tambah Kamar) Pada Admin
 Jika admin ingin menambah kamar hotel, input angka 2.

 Setelah itu admin diminta memasukkan nomor lantai, nomor kamar, tipe kamar, fasilitas kamar, dan harga per malam sesuai keinginan admin. 

Proses tambah kamar berhasil dilakukan dan masuk ke daftar kamar Hotel Jatra Balikpapan.

# Tampilan Mode Read pada Admin (Insert Fitur Sorting dan Searching)

![Screenshot (207)](https://github.com/user-attachments/assets/ea744330-5594-43ab-ab72-0a464abf8459)

Pada opsi ini admin bisa melakukan proses menyusun data atau elemen-elemen dalam suatu urutan tertentu. Berdasarkan gambar diatas seperti nomor, nama panjang, username, PIN, No. Hp, dan saldo E Money. , abjad, atau karakteristik lainnya. Sorting dan searching ini sangat berguna dalam berbagai aplikasi, mulai dari penyimpanan data, pemrosesan informasi, hingga optimasi pencarian.

* Tampilan Mode Sorting

Menampilkan data yang telah disorting.

![Screenshot (211)](https://github.com/user-attachments/assets/4f4cf06b-8977-46c3-ad7f-b84a3eb681ee)

*Tampilan Mode Searching

Admin bisa melakukan searching akun dari tamu dengan memasukkan username yang ingin dicari. Setelah itu program akan menampilkan informasi akun yang dicari.

![Screenshot (210)](https://github.com/user-attachments/assets/685d68b2-d0c5-4e78-b2ad-6ebcfcdcd063)

# Tampilan Mode Update Kamar pada Admin
![Screenshot (194)](https://github.com/user-attachments/assets/3d1c700f-72bc-404b-bc36-4cd57fe1a332)

Admin bisa melakukan update kamar dengan memilih lantai kamar, masukkan nomor kamar yang ingin diubah, masukkan nomor baru, masukkan tipe kamar baru, dan harga per malam. Nomor kamar yang ingin diubah harus tersedia dalam daftar kamar.

* Jika nomor kamar yang dimasukkan tidak ditemukan.
  
![Screenshot (191)](https://github.com/user-attachments/assets/b9dad1f3-cf05-40a7-942a-0082d89c0e37)


# Tampilan Mode Remove (Hapus Kamar) pada Admin
![Screenshot (182)](https://github.com/user-attachments/assets/333d1860-eef6-4025-a6c7-e79c599ce749)

Pada opsi ini, admin bisa menghapus kamar dari daftar kamar dengan memasukkan nomor kamar yang ingin dihapus.
 
* Untuk melihat daftar kamar setelah nomor kamar tersebut dihapus yaitu dengan ketik 1.
  
![Screenshot (183)](https://github.com/user-attachments/assets/eee18b77-1b04-44a0-b138-905a90a0bee4)

Nomor kamar sudah tidak ada dalam daftar kamar.


# Tampilan Mode Read (Daftar Reservasi)

Opsi ini dibuat untuk tamu yang sudah melakukan reservasi mengecek kembali apakah sudah reservasi atau belum. 

# Tampilan Mode Read (Daftar Akun)

![Screenshot (218)](https://github.com/user-attachments/assets/b2105f31-15c4-4b09-96ba-7a918453a523)

Pada opsi 6 ini, admin dapat melihat daftar-daftar akun dari para tamu pengunjung hotel. 

# Tampilan Mode Log Out
![Screenshot (184)](https://github.com/user-attachments/assets/bad2ad02-edc6-4b3a-a566-ad82323c5d46)

Jika admin cukup menggunakan fiturnya, tamu bisa memilih opsi 7 yaitu Keluar atau Mulai ke Mode Login. Disaat memilih admin akan diberikan dua opsi yaitu
Keluar yang bisa diartikan langsung keluar exit dari program dan mulai ke Mode Login yang otomatis ketika admin input "Mulai", tamu akan diarahkan ke Mode Login lagi.

* Tampilan jika keluar dari program
  
  Jika memilih keluar dari program, maka menampilkan output seperti dibawah ini.
  
![Screenshot (190)](https://github.com/user-attachments/assets/a38e7adb-57ac-4358-82ae-cf3eb97bdaba)


* Tampilan jika mulai kembali
  
  Jika mulai kembali, maka admin kembali ke menu login untuk memasukkan Username dan PIN kembali. 

![Screenshot (186)](https://github.com/user-attachments/assets/a1c69469-ad00-4bd7-b0b3-26b57178237c)
