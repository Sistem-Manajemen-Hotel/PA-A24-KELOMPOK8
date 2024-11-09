from prettytable import PrettyTable
from datetime import datetime
import json
import random
import pwinput
import sys
import os
import time
os.system("cls")

json_path = "D:\VSC Codingan\PA\Database\database.json"

with open(json_path, "r") as jsondatabase:
    data = json.loads(jsondatabase.read())

def UpdateTable():
    with open(json_path, "w") as jsondatabase:
        json.dump(data, jsondatabase, indent=4)

def data_tamu():
    table = PrettyTable()
    table.field_names = ["No", "Nama Panjang", "Username", "PIN", "No HP", "Saldo E-Money"]

    username = data["Username"]
    name_panjang = data["Nama_Panjang"]
    pin = data["PIN"]
    no_hp = data["No_HP"]
    saldo_emoney = data["Saldo_E Money"]

    for i in range(len(username)):
        table.add_row([i + 1, name_panjang[i][0], username[i], pin[i], no_hp[i], saldo_emoney[i]])
    print(table)

def urutan_hotel(data):
    kamar = []
    
    if "kamar" not in data:
        print("Data kamar tidak ditemukan!")
        return kamar 
    
    for lantai in data["kamar"]:
        for nomor_kamar, details in data["kamar"][lantai].items():
            kamar.append({
                "nomor kamar": nomor_kamar,
                "tipe": details["tipe"],
                "fasilitas": details["fasilitas"],
                "harga/malam": details["harga/malam"]
            })

    urutan_kamar = sorted(kamar, key=lambda x: int(x["nomor kamar"]))
    
    return urutan_kamar

def tampilkan_daftar_kamar(urutan_kamar):
    if not urutan_kamar:
        print("Tidak ada kamar yang tersedia.")
        return
    
    table = PrettyTable()
    table.field_names = ["Nomor Kamar", "Tipe Kamar", "Fasilitas", "Harga/Malam"]

    for room in urutan_kamar:
        table.add_row([
            room['nomor kamar'],
            room['tipe'],
            room['fasilitas'],
            f"Rp {room['harga/malam']:,}"
        ])
    
    print("=" * 10 + "Daftar Kamar Hotel Jatra Balikpapan" + "=" * 10)
    print(table)

def Akun():
    print("    ╔════════════════════════════════════════╗")
    print("     Selamat Datang Di Hotel Jatra Balikpapan")
    print("                     ( ꩜ ᯅ ꩜ )            ")
    print("    ╚════════════════════════════════════════╝")
    print("╭▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬╮")
    print("             Silakan Pilih Login Menu ")
    print("          1. Login (Jika Sudah Punya akun)")
    print("          2. Daftar Akun (Jika Belum Punya akun)")
    print("╰▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬╯")

    while True:
        try:
            mode = input("Silakan Pilih masukan sesuai menu Login/Daftar Akun : ").strip()
            if mode == "1" or mode.lower() == "login":
                login()
            elif mode == "2" or mode.lower() == "Daftar Akun":
                daftar()
            else:
                print("Menu tidak tersedia!")
            continue
        except KeyboardInterrupt:
            print("\n" + "=" * 10 + "Program akan keluar" + "=" * 10)
            sys.exit()

def login():
    os.system("cls")
    print("Masukan Username dan PIN")

    login_admin  = data.get("Admin",)
    login_username = data.get("Username", )
    login_pin = data.get("PIN",)
    percobaan_login = 3
    
    try:
        for i in range(percobaan_login):
            input_username = input("Username : ")
            if input_username == data.get("AdminHotel", {}).get("Username"):
                input_pin = pwinput.pwinput(prompt="PIN : ")
                if input_pin == data.get("AdminHotel", {}).get("PIN"):
                    admin()
                else:
                    print("PIN Admin salah!")
            elif input_username in data.get("Username", []):
                index = login_username.index(input_username)
                data_pin = login_pin[index]
                input_pin = int(pwinput.pwinput(prompt="PIN : "))
                if input_pin == data_pin:
                    tamu(input_username)
                    return  
                else:  
                        print("PIN salah!")
            else:
                print("Username anda tidak valid ( ꩜ ᯅ ꩜;)⁭ ⁭")

        print("Anda telah menggunakan semua kesempatan login, Silakan Ulang kembali Program ᕙ(⇀‸↼‶)ᕗ.")
        loading(10)
        Akun()
        return

    except ValueError:
        print("DATA ANDA TIDAK VALID YA (˶˃ ᵕ ˂˶)!")
    except KeyboardInterrupt:
        print("Program dihentikan")
        exit()

def admin():
    os.system("cls")
    while True:
            print("╭▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬╮")
            print(" === Menu Admin Hotel Jatra Balikpapan ===")
            print("╰▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬╯")
            print("1. Daftar Kamar")
            print("2. Tambah Kamar") 
            print("3. Update kamar") 
            print("4. Hapus kamar")
            print("5. Daftar Reservasi")
            print("6. Daftar Akun")
            print("7. Keluar")
            
            opsi = input("Pilih opsi (1-7): ").strip()
            
            if opsi == '1':
                daftar_kamar()
            elif opsi == '2':
                tambah_kamar() 
            elif opsi == '3':
                update_kamar()
            elif opsi == '4':
                hapus_kamar()
            elif opsi == '5':
                daftar_reservasi_hotel()
            elif opsi == '6':
                daftar_Akun()
            elif opsi == '7':
                mode_login = input ("Apakah anda ingin Keluar atau Kembali ke mode login? (Keluar/Mulai) : ").capitalize()
                if mode_login == "Keluar":
                    print("╭▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬╮")
                    print(   "Terimakasih telah berkunjung di Hotel Jatra Balikpapan")
                    print("╰▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬╯")
                    sys.exit()
                elif mode_login == "Mulai":
                    Akun()
                    break  
            else:
                print("Pilihan tidak valid!")

def daftar_Akun():
    os.system("cls")
    data_tamu()
    while True:
        print("=" * 10 + "Daftar Akun" + "=" * 10)
        print("1. Melihat daftar akun ")
        print("2. Cari Akun")
        print("3. kembali")
        opsi = input("Pilih opsi (1-3): ").strip()

        if opsi == '1':
            urutan_nama = urutan_akun(data)
            tampilkan_daftar_nama(urutan_nama)
        elif opsi == '2':
            search_username = input("Masukkan Username yang ingin Anda cari: ").strip().lower()
            user_data = search_data_username(data, search_username)

            if user_data:
                tampilkan_data_username(user_data)
            else:
                print("Username tidak ditemukan.")
        elif opsi == '3':
            admin()
            break
        else:
            print("Pilihan tidak valid ༼ つ ◕_◕ ༽つ!")

def daftar_kamar():
    os.system("cls")

    while True:
        print("=" * 10 + "Daftar Kamar" + "=" * 10)
        print("1. Melihat daftar kamar ")
        print("2. Cari kamar")
        print("3. kembali")

        opsi = input("Pilih opsi (1-3): ").strip()
        
        if opsi == '1':
            urutan_data = urutan_hotel(data)
            tampilkan_daftar_kamar(urutan_data)
        elif opsi == '2':
            search_kamar = input("Masukkan nomor kamar yang ingin Anda cari: ").strip()
            data_kamar = search_data_hotel(data, search_kamar)
            if data_kamar:
                tampilkan_data_kamar(data_kamar)
            else:
                print("Username tidak valid")
        elif opsi == '3':
            admin()
            break
        else:
            print("Pilihan tidak valid ༼ つ ◕_◕ ༽つ!")

def tambah_kamar():
    os.system("cls")

    urutan_data = urutan_hotel(data)
    tampilkan_daftar_kamar(urutan_data)

    lantai = input("Masukkan lantai kamar (3, 4, atau 5): ").strip()
    
    if lantai not in data["kamar"]:
        print("Lantai tidak valid! Harap masukkan 3, 4, atau 5.")
        return
    
    nomor_kamar = input("Masukkan nomor kamar: ")

    if not nomor_kamar_valid(int(lantai), nomor_kamar):
        print(f"Nomor kamar untuk lantai {lantai} harus dalam rentang {lantai}00 - {lantai}99.")
        return
    
    if nomor_kamar in data["kamar"][lantai]:
        print(f"Kamar {nomor_kamar} sudah ada di lantai {lantai}.")
        return

    if lantai not in data["kamar"]:
        data["kamar"][lantai] = {}  

    tipe_kamar = input("Masukkan tipe kamar: ")
    fasilitas = input("Masukkan fasilitas: ")
    harga = input("Masukkan harga per malam: ")

    if not harga.isdigit() or int(harga) <= 0:
        print("Input harga tidak sesuai! Harap masukkan angka bulat!")
        return

    data["kamar"][lantai][nomor_kamar] = {
        'tipe': tipe_kamar,
        'fasilitas': fasilitas,
        'harga/malam': int(harga)
    }
    
    print(f"Kamar {nomor_kamar} berhasil ditambahkan di lantai {lantai}.")
    UpdateTable()

def nomor_kamar_valid(lantai, nomor_kamar):
    try:
        nomor_kamar_int = int(nomor_kamar)
        return (lantai * 100) <= nomor_kamar_int <= (lantai * 100 + 99)
    except ValueError:
        return False

def update_kamar():
    os.system("cls")
    urutan_data = urutan_hotel(data)
    tampilkan_daftar_kamar(urutan_data)

    try:
        lantai = input("Pilih lantai kamar (3, 4, 5): ").strip()
        index = input("Masukkan nomor kamar: ").strip()

        if lantai in data["kamar"]:
            if str(index) in data["kamar"][lantai]:
                nomor_baru = input("Masukkan nomor kamar baru: ")
                tipe_baru = input("Masukkan tipe kamar baru: ")
                fasilitas_baru = input("Masukkan fasilitas baru: ")
                harga = input("Masukkan harga per malam: ")

                data["kamar"][lantai][nomor_baru] = {
                    'tipe': tipe_baru,
                    'fasilitas': fasilitas_baru,
                    'harga/malam': int(harga)
                }
                print(f"Kamar {index} berhasil diupdate menjadi {nomor_baru}!")
                UpdateTable()
            else:
                print("Nomor kamar tidak ditemukan.")
        else:
            print("Lantai tidak ditemukan.")
            
    except ValueError:
        print("Input harus berupa angka!")

def hapus_kamar():
    os.system("cls")
    urutan_data = urutan_hotel(data)
    tampilkan_daftar_kamar(urutan_data)
    nomor_kamar = input("Masukkan nomor kamar yang ingin dihapus: ").strip()
    
    for lantai in data["kamar"]:
        if nomor_kamar in data["kamar"][lantai]:
            del data["kamar"][lantai][nomor_kamar]
            print(f"Kamar {nomor_kamar} berhasil dihapus!")
            return
    
    print("Nomor kamar tidak ditemukan.")
    UpdateTable()

def daftar_reservasi_hotel():
    if not data.get("reservasi"):  
        print("Tidak ada reservasi yang terdaftar.")
        return
    
    table = PrettyTable()
    table.field_names = ["Nomor Kamar", "Username", "Tanggal Reservasi", "Waktu Reservasi", "Status"]
    
    for nomor_kamar, info in data["reservasi"].items():
        status = info.get('status', "Tersedia")  
        table.add_row([nomor_kamar, info['Username'], info['tanggal'], info['waktu'], status])
    
    print("\n=== Daftar Reservasi Hotel Jatra Balikpapan ===")
    print(table)


def hapus_akun():
    os.system("cls")
    urutan_nama = urutan_akun(data)  
    tampilkan_daftar_nama(urutan_nama)
    nama_panjang = input("Masukkan nama panjang yang ingin dihapus: ")
    
    for i in range(len(data["Nama_Panjang"])):
        if data["Nama_Panjang"][i] == nama_panjang:
            del data["Nama_Panjang"][i]
            del data["Username"][i]
            del data["PIN"][i]
            del data["No_HP"][i]
            del data["Saldo_E Money"][i]

            print(f"Akun {nama_panjang} berhasil dihapus!")
            return
    
    print("Nama panjang tidak ditemukan.")

def tamu(username):
        os.system("cls")
        if username in data.get("Username"):
            index = data.get("Username").index(username)
            nama = data.get("Nama_Panjang")[index][0]
        print(" ╔═══════════════════════════════════════════════════════════════════════════════════╗")
        print(f"           Selamat Datang di Hotel Jatra Balikpapan, {nama} ")
        print(" ╚═══════════════════════════════════════════════════════════════════════════════════╝")
        print(f" ▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬ Menu Fitur Tamu ▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")
        print( "   1. Daftar Kamar ")
        print( "   2. Buat Reservasi")
        print( "   3. Daftar Reservasi ")
        print( "   4. Cek Saldo E money")
        print( "   5. Top Up Saldo ")
        print( "   6. Update Akun")
        print( "   7. Cek Informasi Akun ")
        print( "   8. Log Out ")
        print(" ╚══════════════════════════════════════════════════════════════════════════════════╝")

        while True:
            opsi = input("Pilih opsi (1-8): ").strip()
            
            if opsi == '1':
                os.system("cls")
                urutan_data = urutan_hotel(data)
                tampilkan_daftar_kamar(urutan_data)
                os.system("pause")
                tamu(username)
            elif opsi == '2':
                buat_reservasi(username)
            elif opsi == '3':
                daftar_reservasi(username)
            elif opsi == '4':
                cek_saldo(username)
            elif opsi == '5':
                topup_saldo(username)
            elif opsi == '6':
                update_akun(username)
            elif opsi == '7':
                cek_informasi_akun(username)
            elif opsi == '8':
                mode_login = input ("Apakah anda ingin Keluar atau Kembali ke mode login? (Keluar/mulai) : ").capitalize()
                if mode_login == "Keluar":
                    print("Terimakasih telah berkunjung di Hotel Jatra Balikpapan")
                    sys.exit()
                elif mode_login == "Mulai":
                    login()
                    break  
                break
            else:
                print("Pilihan tidak valid!")

def buat_reservasi(username):
    os.system("cls")
    urutan_data = urutan_hotel(data)
    tampilkan_daftar_kamar(urutan_data)

    try:
        nomor_kamar = input("Masukkan nomor kamar yang ingin Anda dipesan: ").strip()
        
        if username in data["Username"]:
            index = data["Username"].index(username)
            saldo_Emoney = data["Saldo_E Money"][index]
            format_saldo = f"{saldo_Emoney:,}"
        
            if nomor_kamar in data.get("reservasi", {}):
                print(f"Kamar {nomor_kamar} sudah dipesan! Silakan pilih kamar lain.")
                os.system("pause")
                tamu(username)
            
            harga_kamar = next((detail["harga/malam"] for lantai in data["kamar"].values() for nomor_kamar_detail, detail in lantai.items() 
            if nomor_kamar_detail == nomor_kamar), None)

            if harga_kamar is None:
                print(f"Kamar {nomor_kamar} tidak ditemukan!")
                os.system("pause")
                tamu(username)

            if saldo_Emoney >= harga_kamar:
                tanggal_reservasi = input("Masukkan tanggal reservasi (YYYY-MM-DD): ")
                waktu_reservasi = input("Masukkan waktu reservasi (HH:MM): ")
                

                try:
                    datetime.strptime(tanggal_reservasi, "%Y-%m-%d")
                    datetime.strptime(waktu_reservasi, "%H:%M")
                except ValueError:
                    print("Format tanggal atau waktu tidak valid!")
                    os.system("pause")
                    tamu(username)
                
                if 'reservasi' not in data:
                    data['reservasi'] = {}

                data["reservasi"][nomor_kamar] = {
                    'Username': username,
                    'tanggal': tanggal_reservasi,
                    'waktu': waktu_reservasi,
                    'status': 'Terpesan'
                }
                data["Saldo_E Money"][index] -= harga_kamar
                
                invoice_content = buat_invoice_reservasi(username, nomor_kamar, tanggal_reservasi, waktu_reservasi, harga_kamar)
                invoice_path = "D:\\VSC Codingan\\PA\\New folder\\invoice_reservasi_hotel.txt"
                with open(invoice_path, "a") as invoice_file:
                    invoice_file.write(invoice_content + "\n")

                print(invoice_content)
                print(f"Reservasi untuk {username} di kamar {nomor_kamar} pada {tanggal_reservasi} pukul {waktu_reservasi} berhasil! Sisa E-Money Anda: Rp.{data['Saldo_E Money'][index]:,.2f}")

                UpdateTable()  
                os.system("pause")
                tamu(username)
            else:
                print("Saldo Anda tidak cukup! Mohon top up terlebih dahulu.")
                os.system("pause")
                tamu(username)
    except Exception as e:
        print(f"Terjadi kesalahan: {str(e)}")

def daftar_reservasi(username):
    os.system("cls")
    
    table = PrettyTable()
    table.field_names = ["Nomor Kamar", "Username", "Tanggal Reservasi", "Waktu Reservasi", "Status"]
    
    for nomor_kamar, info in data["reservasi"].items():
            if info['Username'] == username:  
                status = info.get('status', "Tersedia")  
                table.add_row([nomor_kamar, info['Username'], info['tanggal'], info['waktu'], status])
        
    print("\n=== Daftar Reservasi Hotel Jatra Balikpapan ===")
    print(table)
    os.system("pause")
    tamu(username)

def daftar():
    os.system("cls")
    while True:
        try:
            print(" ◀▬▬▬▬▬▬▬▬▬▬▬▬▬▬ Sign Up Akun ▬▬▬▬▬▬▬▬▬▬▬▬▬▬▶")
            nama = str(input("Masukkan nama panjang anda : "))
            username = input("Masukkan username anda : ")
            if username in data["Username"]:
                print("Username telah terdaftar. silakan cari username yang lain!")
                continue
            nomor_hp = input("Masukan nomor Hp anda : ").strip()
            if nomor_hp.isdigit():
                if len(nomor_hp) == 12:
                    data["No_HP"].append(nomor_hp)
                    Kode_pin = random_kode_pin()
                    data["Nama_Panjang"].append([nama])
                    data["Username"].append(username)
                    data["PIN"].append(Kode_pin)
                    
                    data["Saldo_E Money"].append(0)  
                    os.system('cls')
                    print("▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")
                    print(f"   Selamat Datang {nama}, Dengan username {username} dan Nomor HP {nomor_hp}")
                    print("╔═══════════════════════════════════════════════════════════════════════════════════╗")
                    print(f"  Saldo E-Money Anda: Rp.{data['Saldo_E Money'][-1]:,}, HARAP MELAKUKAN PENGISIAN!")
                    print("╚═══════════════════════════════════════════════════════════════════════════════════╝")
                    print("╔═══════════════════════════════════════════════════════════════════════════════════╗")
                    print(f"               PIN Anda adalah: {Kode_pin}, Jangan sampai lupa ya")
                    print("╚═══════════════════════════════════════════════════════════════════════════════════╝")

                    UpdateTable()
                    while True:
                        mode_login = input("Apakah anda ingin Keluar atau Kembali ke mode login? (Keluar/Mulai) : ").capitalize()
                        if mode_login == "Keluar":
                            print("Terimakasih telah berkunjung di Hotel Jatra Balikpapan")
                            sys.exit()
                        elif mode_login == "Mulai":
                                Akun()
                                break  
                        else:
                            print("Pilihan tidak valid!")
                else:
                    print("Nomor HP harus terdiri dari 12 digit. Silakan coba lagi.")
            else:
                print("Nomor HP harus berupa angka. Silakan coba lagi.")
        except ValueError:
            print("Inputan Harus Berupa Angka!")
            os.system("pause")

def cek_saldo(username):
    os.system("cls")  
    
    if username in data["Username"]:
        index = data["Username"].index(username)  
        saldo_emoney = data["Saldo_E Money"][index]  
        
        format_saldo = f"{saldo_emoney:,.2f}"
        
        print("====== Cek Saldo ======")
        print(f"Saldo E-Money Anda: Rp. {format_saldo}") 
    else:
        print("Username tidak ditemukan!")
    
    os.system("pause") 
    tamu(username) 

def topup_saldo(username):
    os.system("cls")
    print("◇─◇──◇─────◇──◇─◇ Isi Saldo ◇─◇──◇─────◇──◇─◇")
    try:
        topup_amount = float(input("Masukkan jumlah saldo yang ingin Anda isi: "))
        
        if topup_amount < 20000:
            print("Jumlah saldo harus lebih dari 20000.")
            os.system("pause")
            tamu(username)
            return  
        elif topup_amount > 6000000:
            print("Jumlah saldo melebihi batas.")
            os.system("pause")
            tamu(username)
            return  

        confirm = input(f"Konfirmasi pengisian Rp.{topup_amount:,.2f} saldo? (y/n): ")
        
        if confirm.lower() == "y":
            index_penerima = data["Username"].index(username)
            data["Saldo_E Money"][index_penerima] += topup_amount
            
            UpdateTable()

            print(f"Isi saldo berhasil. Saldo Anda sekarang: Rp.{data['Saldo_E Money'][index_penerima]:,.2f}")

            current_time = datetime.now()
            formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")
            
            invoice_content = invoice_isisaldo(formatted_time, topup_amount, username)

            invoice_path = "D:\\VSC Codingan\\PA\\txt\\invoice_topup_saldo.txt"
            with open(invoice_path, "a") as invoice_file:
                invoice_file.write(invoice_content + "\n")

            print(invoice_content)
            os.system("pause")
            cek_saldo(username)  
        else:
            print("Pengisian saldo dibatalkan (˶˃ ᵕ ˂˶).")
            os.system("pause")
            
    except ValueError:
        print("Masukan harus berupa angka(˶˃ ᵕ ˂˶).")
        os.system("pause")

def update_akun(username):
    if username in data["Username"]:
        index = data["Username"].index(username)
    else:
        print("Username tidak ditemukan.")
        return

    print("Pilih informasi yang ingin diubah:")
    print("1. Username")
    print("2. PIN")
    print("3. No HP")
        
    opsi = input("Masukkan pilihan (1-3): ").strip()

    if opsi == '1':
        username_baru = input("Masukkan nama username baru anda: ").strip()
        if username_baru in data["Username"]:
            print("Username telah di pakai bro! silakan masukan username lain ༼ つ ◕_◕ ༽つ!")
        else:
            data["Username"][index] = username_baru
            print(f"Username telah berhasil di update menjadi {username_baru}")
            UpdateTable()
            Akun()
    elif opsi == '2':
        pin_baru = input("Masukkan pin baru anda: ").strip()
        if pin_baru.isdigit() and len(pin_baru) == 5:
            if pin_baru in data["PIN"]:
                print("PIN telah di pakai bro! silakan masukan PIN lain ༼ つ ◕_◕ ༽つ!")
            else:
                data["PIN"][index] = pin_baru
                print(f"PIN anda telah berhasil di update menjadi {pin_baru}")
        else:
            print("PIN harus terdiri dari 5 digit angka.")
            UpdateTable()
            Akun()
    elif opsi == '3':
            nohp_baru = input("Masukkan Nomor hp baru anda: ").strip()
            if nohp_baru.isdigit() and len(nohp_baru) == 12:
                if nohp_baru in data["No_HP"]:
                    print("Nomor hp telah di pakai bro! silakan masukan Nomor hp lain ༼ つ ◕_◕ ༽つ!")
                else:
                    data["No_HP"][index] = nohp_baru
                    print(f"Nomor HP anda telah berhasil di update menjadi {nohp_baru}")
            else:
                print("Nomor HP harus terdiri dari 12 digit angka.")
                UpdateTable()
                Akun()
    else:
        print("Pilihan tidak valid!")
        return

def cek_informasi_akun(username):
    os.system("cls")
    table = PrettyTable()
    table.field_names = ["Nama Panjang", "Username", "PIN", "No HP",]
    
    if username not in data["Username"]:
        print("Data tidak tersedia.")
        return
    
    index = data["Username"].index(username)
    
    nama_panjang = data["Nama_Panjang"][index][0]
    table.add_row([
        nama_panjang,
        data["Username"][index],
        data["PIN"][index],
        data["No_HP"][index],
    ])
    print("\n=== Informasi Akun ===")
    UpdateTable()
    print(table)
    os.system("pause")
    tamu(username)

def urutan_akun(data):
    nama_panjang = [item[0] if isinstance(item, list) else item for item in data["Nama_Panjang"]]

    urutan_nama = sorted(zip(nama_panjang, data["Username"], data["PIN"], data["No_HP"], data["Saldo_E Money"]), key=lambda x: x[0])
    return {
        "Nama Panjang": [item[0] for item in urutan_nama],
        "Username": [item[1] for item in urutan_nama],
        "PIN": [item[2] for item in urutan_nama],
        "No HP": [item[3] for item in urutan_nama],
        "Saldo E Money": [item[4] for item in urutan_nama]
    }

def tampilkan_daftar_nama(urutan_nama):
    table = PrettyTable()
    table.field_names = ["Nama Panjang", "Username", "PIN", "No HP", "Saldo E Money"]

    for i in range(len(urutan_nama["Nama Panjang"])):
        table.add_row([
            urutan_nama['Nama Panjang'][i],
            urutan_nama['Username'][i],
            urutan_nama['PIN'][i],
            urutan_nama['No HP'][i],
            f"Rp {urutan_nama['Saldo E Money'][i]:,.0f}"
        ])
    
    print("\n=== Daftar Akun ===")
    print(table)

def search_data_username(data, search_username):
    user_data = {
        "Nama Panjang": [],
        "Username": [],
        "PIN": [],
        "No HP": [],
        "Saldo E Money": []
    }

    for i in range(len(data["Username"])):
        if data["Username"][i] == search_username:
            user_data["Nama Panjang"].append(data["Nama_Panjang"][i])
            user_data["Username"].append(data["Username"][i])
            user_data["PIN"].append(data["PIN"][i])
            user_data["No HP"].append(data["No_HP"][i])
            user_data["Saldo E Money"].append(data["Saldo_E Money"][i])

    return user_data

def tampilkan_data_username(user_data):
    table = PrettyTable()
    table.field_names = ["Nama Panjang", "Username", "PIN", "No HP", "Saldo E Money"]

    for i in range(len(user_data["Username"])):
        table.add_row([
            user_data["Nama Panjang"][i],
            user_data["Username"][i],
            user_data["PIN"][i],
            user_data["No HP"][i],
            f"Rp {user_data['Saldo E Money'][i]:,.2f}"
        ])

    print(table)

def search_data_hotel(data, search_kamar):
    data_kamar = {
        "nomor kamar": [],
        "tipe": [],
        "fasilitas": [],
        "harga/malam": []
    }

    for lantai in data["kamar"]:
        for nomor, details in data["kamar"][lantai].items():
            if nomor == search_kamar:
                data_kamar["nomor kamar"].append(nomor)
                data_kamar["tipe"].append(details["tipe"])
                data_kamar["fasilitas"].append(details["fasilitas"])
                data_kamar["harga/malam"].append(details["harga/malam"])

    return data_kamar

def tampilkan_data_kamar(data_kamar):
    from prettytable import PrettyTable
    
    table = PrettyTable()
    table.field_names = ["nomor kamar", "tipe", "fasilitas", "harga/malam"]

    for nomor_kamar, tipe, fasilitas, harga in zip(
        data_kamar["nomor kamar"],
        data_kamar["tipe"],
        data_kamar["fasilitas"],
        data_kamar["harga/malam"]
    ):
        table.add_row([nomor_kamar, tipe, fasilitas, harga])

    print(table)
    
def invoice_isisaldo(formatted_time, topup_amount, username_penerima):
    invoice_content = f"===== Detail Invoice =====\n"
    invoice_content += f"Waktu Transfer: {formatted_time}\n"
    invoice_content += f"Jumlah: Rp.{topup_amount:,}\n"
    invoice_content += f"Dikirim ke: {username_penerima}\n"
    invoice_content += f"===========================\n"
    invoice_content += f"Terimakasih Telah berkunjung di Hotel Jatra Balikpapan!\n"
    return invoice_content

def buat_invoice_reservasi(username, nomor_kamar, tanggal_reservasi, waktu_reservasi, harga_kamar):
        invoice_content = f"===== Detail Invoice Reservasi =====\n"
        invoice_content += f"Username: {username}\n"
        invoice_content += f"Nomor Kamar: {nomor_kamar}\n"
        invoice_content += f"Tanggal Reservasi: {tanggal_reservasi}\n"
        invoice_content += f"Waktu Reservasi: {waktu_reservasi}\n"
        invoice_content += f"Harga Kamar: Rp.{harga_kamar:,}\n"
        invoice_content += f"===================================\n"
        invoice_content += f"Terimakasih telah berkunjung di Hotel Jatra Balikpapan!\n"
        return invoice_content

def random_kode_pin():
    return random.randint(10000, 99999)

def loading(duration):
    for i in range(duration):
        sys.stdout.write(f"\r ── ⪼ {'»' * (i + 1)}{' ' * (duration - i - 1)} ── ⟢  {duration - i} detik tersisa untuk membuka blokir.")
        sys.stdout.flush()
        time.sleep(1)
    sys.stdout.write("\n")

if __name__ == "__main__":
    Akun()