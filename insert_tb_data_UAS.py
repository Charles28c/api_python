import requests
import mysql.connector
 
# Konfigurasi database
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': '',
    'database': 'test_database'
}
 
# Alamat URL API
api_url = "https://opendata.bandung.go.id/api/bigdata/rumah_sakit_umum_daerah_kota_bandung/jmlh_plynn_krhnn_psn_rwt_np_brdsrkn_kmr_prwtn_d_rsd_kt_bndng_2"
 
try:
    # Mengirim permintaan GET ke API
    response = requests.get(api_url)
 
    # Memeriksa status kode respons
    if response.status_code == 200:
        # Parse data JSON yang diterima
        uas_data = response.json()
 
        # Membuka koneksi ke database
        conn = mysql.connector.connect(**db_config)

        cursor = conn.cursor()
 
        # Menambahkan data pengguna ke dalam tabel
        for uas in uas_data['data']:
            cursor.execute('''
                INSERT INTO uas (id, kode_provinsi, nama_provinsi, bps_kode_kabupaten_kota, bps_nama_kabupaten_kota, ruangan, jumlah_layanan, satuan, tahun)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
            ''', (uas['id'], uas['kode_provinsi'], uas['nama_provinsi'], uas['bps_kode_kabupaten_kota'], uas['bps_nama_kabupaten_kota'], uas['ruangan'], uas['jumlah_layanan'], uas['satuan'], uas['tahun']))
 
        # Menyimpan perubahan dan menutup koneksi
        conn.commit()
        conn.close()
 
        print("Data pengguna telah disimpan ke database MySQL.")
    else:
        print(f"Gagal mengambil data. Kode status: {response.status_code}")
 
except requests.exceptions.RequestException as e:
    print(f"Terjadi kesalahan saat menghubungi API: {str(e)}")
 