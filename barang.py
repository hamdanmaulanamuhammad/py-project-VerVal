from database import get_db_connection

# CREATE (Menambahkan Barang)
def tambah_barang(nama, kategori, stok):
    conn = get_db_connection()
    cursor = conn.cursor()
    sql = "INSERT INTO barang (nama_barang, kategori, stok) VALUES (%s, %s, %s)"
    cursor.execute(sql, (nama, kategori, stok))
    conn.commit()
    conn.close()
    print("✅ Barang berhasil ditambahkan!")

# READ (Melihat Semua Barang)
def lihat_barang():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM barang")
    result = cursor.fetchall()
    conn.close()
    return result

# UPDATE (Mengubah Data Barang)
def update_barang(id_barang, nama, kategori, stok):
    conn = get_db_connection()
    cursor = conn.cursor()
    sql = "UPDATE barang SET nama_barang=%s, kategori=%s, stok=%s WHERE id_barang=%s"
    cursor.execute(sql, (nama, kategori, stok, id_barang))
    conn.commit()
    conn.close()
    print("✅ Barang berhasil diperbarui!")

# DELETE (Menghapus Barang)
def hapus_barang(id_barang):
    conn = get_db_connection()
    cursor = conn.cursor()
    sql = "DELETE FROM barang WHERE id_barang=%s"
    cursor.execute(sql, (id_barang,))
    conn.commit()
    conn.close()
    print("✅ Barang berhasil dihapus!")
