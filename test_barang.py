from barang import tambah_barang, lihat_barang, update_barang, hapus_barang

# Tambah Barang Baru
tambah_barang("Laptop", "Elektronik", 10)

# Lihat Data Barang
print("📋 Data Barang:")
for barang in lihat_barang():
    print(barang)

# Update Barang
update_barang(1, "Laptop Gaming", "Elektronik", 8)

# Hapus Barang
hapus_barang(1)
