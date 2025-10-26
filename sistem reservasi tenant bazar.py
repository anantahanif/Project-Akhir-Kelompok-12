import json
import os
import time
from datetime import datetime
from prettytable import PrettyTable
from pwinput import pwinput
import sys
os.system("cls")

# Bersihkan Layar
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def format_rp(angka):
    return f"Rp{angka:,.0f}".replace(",", ".")

'''=========================================='''
'''               JSON TENANT                '''
'''=========================================='''

def BacaTenant():
    with open('Tenant.json', 'r') as file:
        menu = json.load(file)
    return menu

def SimpanTenant(data):
    with open("Tenant.json", "w") as file:
        json.dump(data, file, indent=4)

'''=========================================='''
'''                JSON AKUN                 '''
'''=========================================='''

def BacaAkun():
    with open('AkunUser.json', 'r') as file:
        menu = json.load(file)
    return menu

def SimpanAkun(Data):
    with open('AkunUser.json', 'w') as file:
        json.dump(Data, file, indent=4)

'''=========================================='''
'''             JSON RESERVASI               '''
'''=========================================='''

def BacaReservasi():
    with open("Reservasi.json", "r") as file:
        return json.load(file)

def SimpanReservasi(data):
    with open("Reservasi.json", "w") as file:
        json.dump(data, file, indent=4)

'''=========================================='''
'''             JSON TRANSAKSI               '''
'''=========================================='''

def BacaTransaksi():
    with open("Transaksi.json", "r") as file:
        return json.load(file)

def SimpanTransaksi(data):
    with open("Transaksi.json", "w") as file:
        json.dump(data, file, indent=4)

'''============================================================================================================'''
'''                                                   MULAI                                                    '''
'''============================================================================================================'''

def mulai():
    while True:
        print("+========================================================+")
        print("|               PA DDP Kelompok 12 - A'25                |")
        print("+========================================================+")
        print("|      SELAMAT DATANG DI TENANT FARIZAHRATHA FEST        |")
        print("+========================================================+")
        print("|                      1. Admin                          |")
        print("|                      2. Penyewa                        |")
        print("|                      3. Keluar                         |")
        print("+========================================================+")

        try:
            pilihan = int(input("Pilih menu login anda (1/2/3): "))
            os.system("cls")

            if pilihan == 1:
                Admin()
            elif pilihan == 2:
                Penyewa()
            elif pilihan == 3:
                print("+=======================================================+")
                print("|             ! Anda Keluar Dari Program !              |")
                print("+=======================================================+")
                print("|              Terima Kasih & Sampai Jumpa              |")
                print("+=======================================================+")
                sys.exit()  # keluar program
            else:
                print("+=======================================================+")
                print("|              ! Pilihan Tidak Tersedia  !              |")
                print("+=======================================================+")
                print("|             Masukkan Pilihan Anda Kembali             |")
                print("+=======================================================+")

        except ValueError:
            print("+=======================================================+")
            print("|             ! Input Harus Berupa Angka !              |")
            print("+=======================================================+")
            print("|       Masukkan angka 1, 2, atau 3 untuk memilih       |")
            print("+=======================================================+")

        except Exception as e:
            print("+=======================================================+")
            print("|         ! Terjadi Kesalahan Tak Terduga !             |")
            print("+=======================================================+")
            print(f"|               Detail error: {str(e)}"                  )                     
            print("+=======================================================+")


'''============================================================================================================'''
'''                                         ANIMASI LOADING                                                    '''
'''============================================================================================================'''

def Animasi1():
    animasi1 = "Loading (Mohon Menunggu)......"
    for _ in range(2):
        print(animasi1, end='\r')
        time.sleep(1)

def Animasi2():
    animasi1 = "Akun Anda Sedang Di Buat......."
    for i in range(1, 30):
        print(animasi1[:i]+ '' * (11 - i) + '\r', end='')
        time.sleep(0.3)
    print()

'''============================================================================================================'''
'''                                                   ADMIN                                                    '''
'''============================================================================================================'''

def Admin():
    global akun_login
    os.system("cls")
    
    akun_admin = {
        "username": "Admin",
        "password": "1234",
        "role": "admin"
    }

    print("+===============================================================+")
    print("|                             LOGIN                             |")
    print("+===============================================================+")
    print("|         Masukkan Username dan Password Anda Dengan Benar      |")
    print("+===============================================================+")

    kesempatan = 3
    while kesempatan > 0:
        try:
            username = input("Username Admin: ")
            password = pwinput("Password Admin: ")

            if username.lower() == akun_admin["username"].lower() and password == akun_admin["password"]:
                os.system("cls")
                print("+===============================================================+")
                print("|                           LOGIN BERHASIL                      |")
                print("+===============================================================+")
                akun_login = akun_admin
                return MenuAdmin()
            else:
                kesempatan -= 1
                print(f"Username/Password salah. Sisa percobaan: {kesempatan}")

        except Exception as e:
            print("+===============================================================+")
            print("|                   TERJADI KESALAHAN INPUT                     |")
            print(f"|             Detail error: {str(e)}")
            print("+===============================================================+")
            kesempatan -= 1

    os.system("cls")
    print("+===============================================================+")
    print("|                  AKUN ANDA TERKUNCI SEMENTARA                 |")
    print("+===============================================================+")
    input("Tekan Enter untuk kembali.....                      ")
    for i in range(5, 0, -1):
        print(f" {i}...")
        time.sleep(1)
    os.system('cls')
    mulai()
    return


'''============================================================================================================'''
'''                                                   PENYEWA                                                  '''
'''============================================================================================================'''

def Penyewa():
    while True:
        clear()
        print("+================================================================+")
        print("|                         MENU PENYEWA                           |")
        print("+================================================================+")
        print("| 1. Registrasi Akun Penyewa Baru                                |")
        print("| 2. Login sebagai Penyewa                                       |")
        print("| 3. Kembali / Keluar                                            |")
        print("+================================================================+")

        pilihan = input("Pilih menu (1-3): ").strip()
        if pilihan == "1":
            RegistrasiPenyewa()
        elif pilihan == "2":
            LoginPenyewa()
        elif pilihan == "3":
            print("+=======================================================+")
            print("|             ! Anda Keluar Dari Program !              |")
            print("+=======================================================+")
            print("|              Terima Kasih & Sampai Jumpa              |")
            print("+=======================================================+")
            sys.exit()  # keluar program
        else:
            print("+=======================================================+")
            print("|              ! Pilihan Tidak Tersedia  !              |")
            print("+=======================================================+")
            print("|             Masukkan Pilihan Anda Kembali             |")
            print("+=======================================================+")

# 1. Registrasi Penyewa
def RegistrasiPenyewa():
    clear()
    data_user = BacaAkun()  
    while True:
        print('\n')
        print("+==================================================================+")
        print("|                           Selamat Datang                         |")
        print("+==================================================================+")
        print("|    Hallo, silahkan buat akun anda untuk menikmati layanan kami   |")
        print("+==================================================================+")

        username = input("Masukkan Username (3-10 karakter): ").strip()
        password = pwinput("Masukkan Password (3-6 karakter): ").strip()
        clear()


        if not username:
            print("⚠️ Username tidak boleh kosong.")
            input("Tekan Enter...")
            clear()
            continue
        if len(username) < 3 or len(username) > 10:
            print("⚠️ Username harus 3-10 karakter.")
            input("Tekan Enter...")
            clear()
            continue
        if not password:
            print("⚠️ Password tidak boleh kosong.")
            input("Tekan Enter...")
            clear()
            continue
        if len(password) < 3 or len(password) > 6:
            print("⚠️ Password harus 3-6 karakter.")
            input("Tekan Enter...")
            clear()
            continue

        existing = data_user.get("Akun", [])
        if any(u.get("username","").lower() == username.lower() for u in existing):
            print("⚠️ Username sudah terpakai, gunakan yang lain.")
            input("Tekan Enter...")
            clear()
            continue

        # Menambahkan user baru ke data JSON dan simpan
        user_baru = {
            "username": username,
            "password": password,
            "e-money": 0
        }

        Animasi2()
        data_user["Akun"].append(user_baru)
        SimpanAkun(data_user)           
        print("+==================================================================+")
        print("|                   AKUN ANDA BERHASIL DIBUAT                      |")
        print("+==================================================================+")
        print(f"Username Anda: {username}")
        print(f"Password Anda: {password}")
        print('\n')
        input("Tekan Enter Untuk Melanjutkan........")
        clear()
        return  # kembali ke menu utama / selesai registrasi

# 2. Login Penyewa
def LoginPenyewa():
    global akun_login
    os.system("cls")
    
    data_user = BacaAkun()

    print("+===============================================================+")
    print("|                             LOGIN                             |")
    print("+===============================================================+")
    print("|         Masukkan Username dan Password Anda Dengan Benar      |")
    print("+===============================================================+")

    kesempatan = 3

    while kesempatan > 0:
        try:
            username = input("Username Penyewa: ")
            password = pwinput("Password Penyewa: ")
            
            usernames_lower = [x["username"].lower() for x in data_user.get("Akun", [])]
            if username.lower() in usernames_lower:
                idx = usernames_lower.index(username.lower())
                user = data_user["Akun"][idx]
                if password == user["password"]:
                    os.system("cls")
                    akun_login = user
                    print("+===============================================================+")
                    print(f"    LOGIN PENYEWA BERHASIL\nSelamat datang {user['username']}                                                ")
                    print("+===============================================================+")
                    print("+===============================================================+")
                    return MenuPenyewa()
                else:
                    kesempatan -= 1
            else:
                kesempatan -= 1
            
            print(f"Username/Password salah. Sisa percobaan: {kesempatan}")

        except Exception as e:
            print("+===============================================================+")
            print("|                   TERJADI KESALAHAN INPUT                     |")
            print(f"|             Detail error: {str(e)}")
            print("+===============================================================+")
            kesempatan -= 1

    os.system("cls")
    print("+===============================================================+")
    print("|                  AKUN ANDA TERKUNCI SEMENTARA                 |")
    print("+===============================================================+")
    input("Tekan Enter untuk kembali.....                      ")
    for i in range(5, 0, -1):
        print(f" {i}...")
        time.sleep(1)
    os.system('cls')
    mulai()
    return

'''============================================================================================================'''
'''                                                   MENU                                                     '''
'''============================================================================================================'''

def MenuAdmin():
    while True:
        os.system('cls')
        print("+================================================================+")
        print("|                           MENU ADMIN                           |")
        print("+================================================================+")
        print("| 1. Lihat Semua Tenant                                          |")
        print("| 2. Tambah Tenant                                               |")
        print("| 3. Ubah Tenant                                                 |")
        print("| 4. Hapus Tenant                                                |")
        print("| 5. Logout                                                      |")
        print("+================================================================+")

        try:
            pilihan = input("Pilih menu (1-5): ")

            if pilihan == "1":
                LihatSemuaTenant()
            elif pilihan == "2":
                TambahTenant()
            elif pilihan == "3":
                UbahTenant()
            elif pilihan == "4":
                HapusTenant()
            elif pilihan == "5":
                print("Keluar ke menu utama dalam ...")
                for i in range(5, 0, -1):
                    print(f" {i}...")
                    time.sleep(1)
                os.system('cls')
                mulai()
                return
            else:
                print("Pilihan tidak valid! Silakan pilih angka 1-5.")

        except Exception:
            print("+===============================================================+")
            print("|                 TERJADI KESALAHAN TAK TERDUGA                 |")
            print("+===============================================================+")
            print("|        Silakan periksa input Anda atau coba lagi nanti        |")
            print("+===============================================================+")
            input("Tekan Enter untuk kembali ke menu...")

# 1. Lihat Semua Slot Tenant
def LihatSemuaTenant():
    try:
        clear()
        data = BacaTenant()

        if not data or "Tenant" not in data:
            print("Data tenant tidak ditemukan.")
            input("Tekan Enter untuk kembali ke menu...")
            return

        table = PrettyTable()
        table.field_names = ["Nomor Tenant", "Nama Tenant", "Harga/Hari", "Slot Tersedia", "Status"]

        for tenant in data.get("Tenant", []):
            nomor = tenant.get("nomor_tenant", "-")
            nama = tenant.get("nama_tenant", "-")
            slot = tenant.get("slot_tersedia", "-")
            status = tenant.get("status", "-")

            try:
                harga = format_rp(int(tenant.get("harga_per_hari", 0)))
            except ValueError:
                harga = "Data tidak valid"

            table.add_row([nomor, nama, harga, slot, status])

        print("+=====================================================================================+")
        print("|                                  DAFTAR SLOT TENANT                                 |")
        print("+=====================================================================================+")
        print(table)

    except KeyboardInterrupt:
        print("\nProses dibatalkan oleh pengguna.")
    finally:
        input("Tekan Enter untuk kembali ke menu...")


# 2. Tambah Slot Tenant
def TambahTenant():
    clear()
    data = BacaTenant()
    print("+========================================================================================+")
    print("|                                   TAMBAH SLOT TENANT                                   |")
    print("+========================================================================================+")
    try:
        tenants = data.get("Tenant", [])
        table = PrettyTable()
        table.field_names = ["Nomor Tenant", "Nama Tenant", "Harga/Hari", "Slot Tersedia", "Status"]
        for t in tenants:
            table.add_row([
                t.get("nomor_tenant", "-"),
                t.get("nama_tenant", "-"),
                format_rp(int(t.get("harga_per_hari", 0))),
                t.get("slot_tersedia", "-"),
                t.get("status", "-")
            ])
        print("+=====================================================================================+")
        print("|                                  DAFTAR SLOT TENANT                                 |")
        print("+=====================================================================================+")
        print(table)
    except Exception:
        pass
    try:
        nomor = str(len(data["Tenant"]) + 1)

        # Input Nama (ulang sampai valid)
        while True:
            nama = input("Nama Tenant: ").strip()
            if nama:
                break
            print("Nama Tenant tidak boleh kosong.")

        # Input Harga (ulang sampai valid angka >= 500000)
        while True:
            harga_in = input("Harga per hari: ").strip()
            try:
                harga_num = int(harga_in)
                if harga_num >= 500000:
                    harga = str(harga_num)
                    break
                print("Harga per hari minimal Rp500.000.")
            except ValueError:
                print("Harga per hari harus berupa angka.")

        # Input Slot (ulang sampai valid integer >= 0)
        while True:
            slot_in = input("Jumlah slot tersedia: ").strip()
            try:
                slot_int = int(slot_in)
                if slot_int >= 0:
                    slot = str(slot_int)
                    break
                print("Jumlah slot tersedia tidak boleh negatif.")
            except ValueError:
                print("Jumlah slot tersedia harus berupa angka bulat.")

        status = "Tersedia" if int(slot) > 0 else "Tidak Tersedia"

        new_tenant = {
            "nomor_tenant": nomor,
            "nama_tenant": nama,
            "harga_per_hari": harga,
            "status": status,
            "slot_tersedia": slot
        }

        data["Tenant"].append(new_tenant)
        SimpanTenant(data)
        print("+=====================================================================================+")
        print("|                           Tenant Berhasil Ditambahkan!                              |")
        print("+=====================================================================================+")

        table = PrettyTable()
        table.field_names = ["Nomor Tenant", "Nama Tenant", "Harga/Hari", "Slot Tersedia", "Status"]

        for tenant in data.get("Tenant", []):
            table.add_row([
                tenant.get("nomor_tenant", "-"),
                tenant.get("nama_tenant", "-"),
                format_rp(int(tenant.get("harga_per_hari", 0))),
                tenant.get("slot_tersedia", "-"),
                tenant.get("status", "-")
            ])
        
        print(table)

    except Exception as e:
        print("Terjadi kesalahan:", e)

    input("Tekan Enter untuk kembali ke menu...")

# 3. Ubah Slot Tenant
def UbahTenant():
    clear()
    data = BacaTenant()

    print("+===========================================================================+")
    print("|                           DAFTAR SLOT TENANT                              |")
    print("+===========================================================================+")
    table_awal = PrettyTable()
    table_awal.field_names = ["No", "Nama Tenant", "Harga/Hari", "Status", "Slot Tersedia"]
    for t in data.get("Tenant", []):
        table_awal.add_row([t["nomor_tenant"], t["nama_tenant"], t["harga_per_hari"], t["status"], t["slot_tersedia"]])
    print(table_awal)

    print("+===========================================================================+")
    print("|                              UBAH SLOT TENANT                             |")
    print("+===========================================================================+")
    try:
        while True:
            nomor = input("Masukkan nomor tenant yang ingin diubah (ketik 'batal' untuk kembali): ").strip().lower()
            if nomor == "batal":
                print("Dibatalkan.")
                break

            tenant = next((x for x in data["Tenant"] if x["nomor_tenant"].lower() == nomor), None)
            if tenant:
                print(f"Nama sekarang: {tenant['nama_tenant']}")
                tenant['nama_tenant'] = input("Nama baru (Enter untuk tetap): ") or tenant['nama_tenant']
                
                print(f"Harga/Hari sekarang: {tenant['harga_per_hari']}")
                tenant['harga_per_hari'] = input("Harga baru (Enter untuk tetap): ") or tenant['harga_per_hari']
                
                print(f"Slot Tersedia sekarang: {tenant['slot_tersedia']}")
                slot_baru = input("Slot baru (Enter untuk tetap): ") or tenant['slot_tersedia']
                tenant['slot_tersedia'] = slot_baru

                if int(slot_baru) > 0:
                    tenant['status'] = "Tersedia"
                else:
                    tenant['status'] = "Tidak Tersedia"

                SimpanTenant(data)
                table = PrettyTable()
                table.field_names = ["No", "Nama Tenant", "Harga/Hari", "Status", "Slot Tersedia"]
                for t in data["Tenant"]:
                    table.add_row([t["nomor_tenant"], t["nama_tenant"], t["harga_per_hari"], t["status"], t["slot_tersedia"]])
                print("\nTenant berhasil diperbarui! Berikut data terbaru:\n")
                print(table)
                break
            else:
                print("Tenant dengan nomor tersebut tidak ditemukan. Coba lagi.")
    except Exception as e:
        print("Terjadi kesalahan:", e)
    input("Tekan Enter untuk kembali ke menu...")

# 4. Hapus Slot Tenant
def HapusTenant():
    clear()
    data = BacaTenant()

    # Tampilkan data tenant awal
    print("+===========================================================================+")
    print("|                          DAFTAR SLOT TENANT                               |")
    print("+===========================================================================+")
    table_awal = PrettyTable()
    table_awal.field_names = ["No", "Nama Tenant", "Harga/Hari", "Status", "Slot Tersedia"]
    for t in data.get("Tenant", []):
        table_awal.add_row([t["nomor_tenant"], t["nama_tenant"], t["harga_per_hari"], t["status"], t["slot_tersedia"]])
    print(table_awal)

    print("+===========================================================================+")
    print("|                             HAPUS SLOT TENANT                             |")
    print("+===========================================================================+")

    try:
        nomor = input("Masukkan nomor tenant yang ingin dihapus: ")
        tenant = next((x for x in data["Tenant"] if x["nomor_tenant"] == nomor), None)
        if tenant:
            data["Tenant"].remove(tenant)
            SimpanTenant(data)
            print("\nTenant berhasil dihapus! Berikut data terbaru:\n")
            
            # Tampilkan data tenant terbaru
            table_baru = PrettyTable()
            table_baru.field_names = ["No", "Nama Tenant", "Harga/Hari", "Status", "Slot Tersedia"]
            for t in data["Tenant"]:
                table_baru.add_row([t["nomor_tenant"], t["nama_tenant"], t["harga_per_hari"], t["status"], t["slot_tersedia"]])
            print(table_baru)
        else:
            print("Tenant dengan nomor tersebut tidak ditemukan.")
    except Exception as e:
        print("Terjadi kesalahan:", e)


# MENU PENYEWA
def MenuPenyewa():
    global akun_login
    while True:
        clear()
        print("+================================================================+")
        print("|                        MENU PENYEWA                            |")
        print("+================================================================+")
        print("| 1. Lihat Semua Tenant                                          |")
        print("| 2. Reservasi Tenant                                            |")
        print("| 3. Top-up Saldo                                                |")
        print("| 4. Cek Riwayat Transaksi                                       |")
        print("| 5. Logout                                                      |")
        print("+================================================================+")

        pilihan = input("Pilih menu (1-5): ").strip()
        if pilihan=="1":
            LihatSemuaTenant()
        elif pilihan=="2":
            ReservasiTenant(akun_login)
        elif pilihan=="3":
            TopUpSaldo(akun_login)
        elif pilihan=="4":
            CekRiwayatTransaksi(akun_login)
        elif pilihan=="5":
            print("+=======================================================+")
            print("|             ! Anda Keluar Dari Program !              |")
            print("+=======================================================+")
            print("|              Terima Kasih & Sampai Jumpa              |")
            print("+=======================================================+")
            return
        else:
            print("Pilihan tidak valid! Silakan pilih angka 1-5.")



# 1. Lihat Semua Slot Tenant
def LihatSemuaTenant():
    clear()
    data = BacaTenant()

    tenants = data.get("Tenant", [])
    if not tenants:
        print("❌ Belum ada data tenant tersedia.")
        input("Tekan Enter untuk kembali ke menu...")
        return

    table = PrettyTable()
    table.field_names = ["Nomor Tenant", "Nama Tenant", "Harga/Hari", "Slot Tersedia", "Status"]

    for tenant in tenants:
        table.add_row([
            tenant.get("nomor_tenant", "-"),
            tenant.get("nama_tenant", "-"),
            format_rp(int(tenant.get("harga_per_hari", 0))),
            tenant.get("slot_tersedia", "-"),
            tenant.get("status", "-")
        ])

    print("+=====================================================================================+")
    print("|                                  DAFTAR SLOT TENANT                                 |")
    print("+=====================================================================================+")
    print(table)
    input("Tekan Enter untuk kembali ke menu...")  

# 2. Reservasi Tenant
def ReservasiTenant(user):
    clear()
    try:
        data_tenant = BacaTenant()
        data_reservasi = BacaReservasi()
    except Exception as e:
        print("❌ Gagal membaca data tenant atau reservasi:", e)
        time.sleep(2)
        return

    # Tampilkan daftar tenant
    from prettytable import PrettyTable
    table_list = PrettyTable()
    table_list.field_names = ["No", "Tenant", "Harga/Hari", "Slot", "Status"]
    for t in data_tenant.get("Tenant", []):
        table_list.add_row([
            t["nomor_tenant"],
            t["nama_tenant"],
            format_rp(int(t["harga_per_hari"])),
            t["slot_tersedia"],
            t["status"]
        ])
    print(table_list)

    # Pilih tenant
    while True:
        nomor = input("Pilih tenant nomor (ketik 'batal' untuk kembali): ").strip()
        if nomor.lower() == 'batal':
            return

        tenant = next((t for t in data_tenant["Tenant"] if t["nomor_tenant"] == nomor), None)
        if not tenant:
            print("❌ Tenant tidak ditemukan. Coba lagi.")
            continue

        # Cek ketersediaan tenant
        try:
            status_ok = str(tenant.get("status", "")).strip().lower() == "tersedia"
            slot_ok = int(str(tenant.get("slot_tersedia", 0)).strip()) > 0
            if not status_ok or not slot_ok:
                print("❌ Tenant tidak tersedia untuk reservasi (slot habis). Pilih tenant lain.")
                continue
        except Exception:
            print("❌ Data ketersediaan tenant tidak valid. Pilih tenant lain.")
            continue
        break

    # Input lama sewa 
    while True:
        try:
            hari_in = input("Berapa hari ingin disewa?: ").strip()
            hari = int(hari_in)
            if hari <= 0:
                print("❌ Input hari tidak valid! Harus berupa angka")
                continue
            break
        except ValueError:
            print("❌ Input hari tidak valid! Harus berupa angka")
            continue
        except Exception as e:
            print("❌ Terjadi kesalahan:", e)
            continue

    # Hitung total biaya
    try:
        harga_per_hari = int(tenant["harga_per_hari"])
        total_biaya = harga_per_hari * hari
    except Exception as e:
        print("❌ Data harga tenant tidak valid:", e)
        time.sleep(2)
        return

    # Cek saldo
    if user.get("e-money", 0) < total_biaya:
        print("❌ Saldo e-money tidak cukup!")
        time.sleep(2)
        return

    # Update saldo & slot tenant
    try:
        user["e-money"] -= total_biaya
        tenant["slot_tersedia"] = str(int(tenant["slot_tersedia"]) - 1)
        if int(tenant["slot_tersedia"]) <= 0:
            tenant["status"] = "Tidak Tersedia"
    except Exception as e:
        print("❌ Gagal mengupdate saldo atau slot:", e)
        time.sleep(2)
        return

    # Simpan perubahan di akun & tenant
    try:
        data_akun = BacaAkun()
        for u in data_akun["Akun"]:
            if u["username"] == user["username"]:
                u["e-money"] = user["e-money"]
                break
        SimpanAkun(data_akun)
        SimpanTenant(data_tenant)
    except Exception as e:
        print("❌ Gagal menyimpan data:", e)
        time.sleep(2)
        return

    # Catat transaksi
    try:
        if "Reservasi" not in data_reservasi:
            data_reservasi["Reservasi"] = []
        data_reservasi["Reservasi"].append({
            "username": user["username"],
            "tenant": tenant["nama_tenant"],
            "lama_sewa": hari,
            "total": total_biaya,
            "tanggal": time.strftime("%d-%m-%Y %H:%M:%S")
        })
        SimpanReservasi(data_reservasi)
    except Exception as e:
        print("❌ Gagal mencatat transaksi:", e)
        time.sleep(2)
        return

    # Tampilkan struk 
    struk_table = PrettyTable()
    struk_table.field_names = ["Username", "Tenant", "Hari", "Total", "Tanggal"]
    last_reservasi = data_reservasi["Reservasi"][-1]
    struk_table.add_row([
        last_reservasi["username"],
        last_reservasi["tenant"],
        last_reservasi["lama_sewa"],
        format_rp(last_reservasi["total"]),
        last_reservasi["tanggal"]
    ])
    print("\n✅ Reservasi berhasil! Berikut struk:\n")
    print(struk_table)
    input("Tekan Enter...")

def TopUpSaldo(user):
    clear()
    try:
        print(f"Saldo saat ini: {format_rp(user['e-money'])}")
    except KeyError:
        print("❌ Data user tidak valid!")
        time.sleep(2)
        return

    # Input jumlah top-up
    try:
        jumlah = int(input("Masukkan jumlah top-up: Rp "))
        if jumlah <= 0:
            raise ValueError("Jumlah harus lebih dari 0.")
    except ValueError as ve:
        print(f"❌ Input tidak valid! {ve}")
        time.sleep(2)
        return
    except Exception as e:
        print("❌ Terjadi kesalahan:", e)
        time.sleep(2)
        return

    # Update saldo user langsung
    try:
        user["e-money"] += jumlah
    except KeyError:
        print("❌ Data user tidak valid!")
        time.sleep(2)
        return
    except Exception as e:
        print("❌ Terjadi kesalahan saat update saldo:", e)
        time.sleep(2)
        return

    # Update di file JSON
    try:
        data_akun = BacaAkun()
        for u in data_akun["Akun"]:
            if u["username"] == user["username"]:
                u["e-money"] = user["e-money"]
                break
        SimpanAkun(data_akun)
    except FileNotFoundError:
        print("❌ File akun tidak ditemukan!")
        time.sleep(2)
        return
    except Exception as e:
        print("❌ Terjadi kesalahan saat menyimpan data:", e)
        time.sleep(2)
        return

    # Tampilkan struk/top-up pakai tabel
    try:
        table = PrettyTable()
        table.field_names = ["Username", "Jumlah Top-Up", "Saldo Baru", "Tanggal"]
        table.add_row([
            user["username"],
            format_rp(jumlah),
            format_rp(user["e-money"]),
            time.strftime("%d-%m-%Y %H:%M:%S")
        ])
        print("\n✅ Top-up berhasil! Berikut struk Anda:\n")
        print(table)
    except Exception as e:
        print("❌ Terjadi kesalahan saat menampilkan struk:", e)
        time.sleep(2)
        return

    input("Tekan Enter untuk kembali ke menu...")

def CekRiwayatTransaksi(user):
    try:
        clear()
        data_reservasi = BacaReservasi()
        if not data_reservasi or "Reservasi" not in data_reservasi:
            print("Data reservasi tidak ditemukan.")
            input("\nTekan Enter untuk kembali ke menu...")
            return

        table = PrettyTable()
        table.field_names = ["Tanggal", "Tenant", "Lama Sewa (hari)", "Total"]

        ada_transaksi = False
        for trx in data_reservasi.get("Reservasi", []):
            try:
                if trx.get("username") == user.get("username"):
                    table.add_row([
                        trx.get("tanggal", "-"),
                        trx.get("tenant", "-"),
                        trx.get("lama_sewa", "-"),
                        format_rp(trx.get("total", 0))
                    ])
                    ada_transaksi = True
            except KeyError as e:
                print(f"Data reservasi tidak lengkap: {e}")
                continue

        if ada_transaksi:
            print("=== 🧾 RIWAYAT TRANSAKSI ANDA ===")
            print(table)
        else:
            print("❌ Belum ada transaksi ditemukan.")

    except FileNotFoundError:
        print("File reservasi tidak ditemukan.")
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")
    finally:
        input("\nTekan Enter untuk kembali ke menu...")

mulai()
