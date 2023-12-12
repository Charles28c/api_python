import requests #library yang kita gunakan untuk mengakses API/json
import pandas as pd
import json
 
# Alamat URL API
api_url = "https://opendata.bandung.go.id/api/bigdata/rumah_sakit_umum_daerah_kota_bandung/jmlh_plynn_krhnn_psn_rwt_np_brdsrkn_kmr_prwtn_d_rsd_kt_bndng_2"
  
try:
    # Mengirim permintaan GET ke API
    response = requests.get(api_url)
 
    # Memeriksa status kode respons
    if response.status_code == 200:
        # Parse data JSON yang diterima
        data_ = response.json()

        # Baca data JSON dari file
        with open('data.json', 'r') as json_file:
            data = json_file.read()  
            
        # Ubah JSON menjadi DataFrame pandas
        df = pd.read_json(data)

        # Simpan DataFrame ke dalam file Excel
        excel_file = 'data_uas.xlsx'
        df.to_excel(excel_file, index=False)

        print(f"Data telah disimpan dalam file Excel: {excel_file}")
 
        # Menampilkan hasil
        for uas in data_['data']:
            print(f"id: {uas['id']}")
            print(f"kode_provinsi: {uas['kode_provinsi']}")
            print(f"nama_provinsi: {uas['nama_provinsi']}")
            print(f"bps_kode_kabupaten_kota: {uas['bps_kode_kabupaten_kota']}")
            print(f"bps_nama_kabupaten_kota: {uas['bps_nama_kabupaten_kota']}")
            print(f"ruangan: {uas['ruangan']}")
            print(f"jumlah_layanan: {uas['jumlah_layanan']}")
            print(f"satuan: {uas['satuan']}")
            print(f"tahun: {uas['tahun']}")
            print("-" * 30)
    else:
        print(f"Gagal mengambil data. Kode status: {response.status_code}")
 
except requests.exceptions.RequestException as e:
    print(f"Terjadi kesalahan saat menghubungi API: {str(e)}")