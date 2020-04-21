def riwayat_wahana():
    wahana = input("Masukkan ID Wahana: ")
    print("Riwayat:")
    i = 0
    while array_penggunaan_tiket[i]!= "*":
            if array_penggunaan_tiket[i]['ID_Wahana'] == wahana:
                print(array_penggunaan_tiket[i]['Tanggal_Penggunaan'],"|",array_penggunaan_tiket[i]['Username'],"|",array_penggunaan_tiket[i]['Jumlah_Tiket'])
            i += 1
