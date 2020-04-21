def riwayat_wahana():
    wahana = input("Masukkan ID Wahana: ")
    print("Riwayat:")
    for row in (array_penggunaan_tiket):
        if row != "*": #Pada array_penggunaan_tiket mark == "*"
            if row['ID_Wahana'] == wahana:
                print(row['Tanggal_Penggunaan'],"|",row['Username'],"|",row['Jumlah_Tiket'])
