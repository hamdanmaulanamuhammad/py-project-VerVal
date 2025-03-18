from transaksi import tambah_transaksi, lihat_transaksi, hapus_transaksi
from barang import tambah_barang

# Tambah Barang untuk Transaksi
tambah_barang("Mouse", "Aksesoris", 20)

# Tambah Transaksi (Barang Masuk)
tambah_transaksi(2, "2025-03-18", 5, "masuk")

# Tambah Transaksi (Barang Keluar)
tambah_transaksi(3, "2025-03-18", 5, "masuk")

# Lihat Semua Transaksi
print("📋 Data Transaksi:")
for transaksi in lihat_transaksi():
    print(transaksi)

# Hapus Transaksi
hapus_transaksi(1)
