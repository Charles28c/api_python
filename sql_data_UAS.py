# Buat koneksi ke server MySQL
import mysql.connector
db_connection = mysql.connector.connect(

    host="localhost",

    user="root",

    password="",

    database="test_database"  # Ganti dengan nama database yang telah Anda buat

)

 

# Buat objek cursor

db_cursor = db_connection.cursor()

 

# Definisikan struktur tabel 'users'
drop_table_query = """
DROP TABLE IF EXISTS uas;
"""
create_table_query = """
CREATE TABLE uas (
    id bigint(20) primary key auto_increment,
    kode_provinsi text,
    nama_provinsi text,
    bps_kode_kabupaten_kota text,
    bps_nama_kabupaten_kota text,
    ruangan text,
    jumlah_layanan bigint(20),
    satuan text,
    tahun text
)

"""

 

# Eksekusi perintah SQL untuk membuat tabel
db_cursor.execute(drop_table_query)
db_cursor.execute(create_table_query)

 

# Komit perubahan ke database

db_connection.commit()

 

# Tutup cursor dan koneksi