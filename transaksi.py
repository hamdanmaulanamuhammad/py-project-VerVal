""" Modul transaksi untuk mengelola data transaksi dalam sistem inventaris. """

from database import get_db_connection

# CREATE (Menambahkan Transaksi)
def tambah_transaksi(id_barang, tanggal, jumlah, tipe):
    """Menambahkan transaksi barang ke database dan memperbarui stok barang.

    Args:
        id_barang (int): ID barang terkait.
        tanggal (str): Tanggal transaksi dalam format 'YYYY-MM-DD'.
        jumlah (int): Jumlah barang dalam transaksi.
        tipe (str): Jenis transaksi ('masuk' atau 'keluar').
    """
    conn = get_db_connection()
    cursor = conn.cursor()

    try:
        # Insert ke tabel transaksi
        sql_insert = "INSERT INTO transaksi (id_barang, tanggal, jumlah, tipe) VALUES (%s, %s, %s, %s)"
        cursor.execute(sql_insert, (id_barang, tanggal, jumlah, tipe))

        # Update stok barang
        sql_update = None
        if tipe == "masuk":
            sql_update = "UPDATE barang SET stok = stok + %s WHERE id_barang = %s"
        elif tipe == "keluar":
            sql_update = "UPDATE barang SET stok = stok - %s WHERE id_barang = %s"

        if sql_update:
            cursor.execute(sql_update, (jumlah, id_barang))

        conn.commit()
        print(f"✅ Transaksi {tipe} berhasil ditambahkan!")

    except Exception as e:
        conn.rollback()
        print(f"❌ Terjadi kesalahan: {e}")

    finally:
        conn.close()

# READ (Melihat Semua Transaksi)
def lihat_transaksi():
    """Mengambil semua data transaksi dari database.

    Returns:
        list: Daftar transaksi dalam bentuk tuple.
    """
    conn = get_db_connection()
    cursor = conn.cursor()

    try:
        cursor.execute("SELECT * FROM transaksi")
        result = cursor.fetchall()
        return result

    finally:
        conn.close()

# DELETE (Menghapus Transaksi)
def hapus_transaksi(id_transaksi):
    """Menghapus transaksi berdasarkan ID dan mengembalikan stok barang ke kondisi sebelumnya.

    Args:
        id_transaksi (int): ID transaksi yang akan dihapus.
    """
    conn = get_db_connection()
    cursor = conn.cursor()

    try:
        # Ambil data transaksi yang akan dihapus
        cursor.execute("SELECT id_barang, jumlah, tipe FROM transaksi WHERE id_transaksi = %s", (id_transaksi,))
        transaksi = cursor.fetchone()

        if transaksi:
            id_barang, jumlah, tipe = transaksi

            # Kembalikan stok ke kondisi sebelum transaksi
            sql_update = None
            if tipe == "masuk":
                sql_update = "UPDATE barang SET stok = stok - %s WHERE id_barang = %s"
            elif tipe == "keluar":
                sql_update = "UPDATE barang SET stok = stok + %s WHERE id_barang = %s"

            if sql_update:
                cursor.execute(sql_update, (jumlah, id_barang))

            # Hapus transaksi
            sql_delete = "DELETE FROM transaksi WHERE id_transaksi = %s"
            cursor.execute(sql_delete, (id_transaksi,))
            conn.commit()
            print("✅ Transaksi berhasil dihapus!")

    except Exception as e:
        conn.rollback()
        print(f"❌ Terjadi kesalahan: {e}")

    finally:
        conn.close()
