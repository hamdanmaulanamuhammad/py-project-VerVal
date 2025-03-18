import mysql.connector
from database import get_db_connection
from transaksi import tambah_transaksi, lihat_transaksi, hapus_transaksi

# --- CRUD Barang ---
def tambah_barang(nama_barang, kategori, stok):
    """Menambahkan barang baru ke database."""
    conn = get_db_connection()
    cursor = conn.cursor()
    sql = "INSERT INTO barang (nama_barang, kategori, stok) VALUES (%s, %s, %s)"
    cursor.execute(sql, (nama_barang, kategori, stok))
    conn.commit()
    conn.close()
    print("✅ Barang berhasil ditambahkan!")

def lihat_barang():
    """Menampilkan daftar barang dalam database."""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM barang")
    barang = cursor.fetchall()
    conn.close()
    return barang

def edit_barang(id_barang, nama_barang, kategori, stok):
    """Mengedit data barang berdasarkan ID."""
    conn = get_db_connection()
    cursor = conn.cursor()
    sql = "UPDATE barang SET nama_barang = %s, kategori = %s, stok = %s WHERE id_barang = %s"
    cursor.execute(sql, (nama_barang, kategori, stok, id_barang))
    conn.commit()
    conn.close()
    print("✅ Barang berhasil diperbarui!")

def hapus_barang(id_barang):
    """Menghapus barang berdasarkan ID."""
    conn = get_db_connection()
    cursor = conn.cursor()
    sql = "DELETE FROM barang WHERE id_barang = %s"
    cursor.execute(sql, (id_barang,))
    conn.commit()
    conn.close()
    print("✅ Barang berhasil dihapus!")

# --- MENU UTAMA ---
def menu():
    while True:
        print("\n=== Sistem Manajemen Inventaris ===")
        print("1. CRUD Barang")
        print("2. CRUD Transaksi")
        print("0. Keluar")
        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            menu_barang()
        elif pilihan == "2":
            menu_transaksi()
        elif pilihan == "0":
            print("🚀 Keluar dari program...")
            break
        else:
            print("❌ Pilihan tidak valid! Coba lagi.")

# --- MENU CRUD BARANG ---
def menu_barang():
    while True:
        print("\n=== CRUD Barang ===")
        print("1. Tambah Barang")
        print("2. Lihat Barang")
        print("3. Edit Barang")
        print("4. Hapus Barang")
        print("0. Kembali ke menu utama")
        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            nama = input("Masukkan Nama Barang: ")
            kategori = input("Masukkan Kategori: ")
            stok = int(input("Masukkan Stok: "))
            tambah_barang(nama, kategori, stok)
        elif pilihan == "2":
            barang = lihat_barang()
            for b in barang:
                print(b)
        elif pilihan == "3":
            id_barang = int(input("Masukkan ID Barang: "))
            nama = input("Masukkan Nama Baru: ")
            kategori = input("Masukkan Kategori Baru: ")
            stok = int(input("Masukkan Stok Baru: "))
            edit_barang(id_barang, nama, kategori, stok)
        elif pilihan == "4":
            id_barang = int(input("Masukkan ID Barang yang akan dihapus: "))
            hapus_barang(id_barang)
        elif pilihan == "0":
            break
        else:
            print("❌ Pilihan tidak valid!")

# --- MENU CRUD TRANSAKSI ---
def menu_transaksi():
    while True:
        print("\n=== CRUD Transaksi ===")
        print("1. Tambah Transaksi")
        print("2. Lihat Transaksi")
        print("3. Hapus Transaksi")
        print("0. Kembali ke menu utama")
        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            id_barang = int(input("Masukkan ID Barang: "))
            tanggal = input("Masukkan Tanggal (YYYY-MM-DD): ")
            jumlah = int(input("Masukkan Jumlah: "))
            tipe = input("Masukkan Tipe (masuk/keluar): ")
            tambah_transaksi(id_barang, tanggal, jumlah, tipe)
        elif pilihan == "2":
            transaksi = lihat_transaksi()
            for t in transaksi:
                print(t)
        elif pilihan == "3":
            id_transaksi = int(input("Masukkan ID Transaksi yang akan dihapus: "))
            hapus_transaksi(id_transaksi)
        elif pilihan == "0":
            break
        else:
            print("❌ Pilihan tidak valid!")

if __name__ == "__main__":
    menu()
