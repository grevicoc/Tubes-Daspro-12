def riwayat_wahana():
    id = input("Masukkan ID Wahana: ")
    print("Riwayat:")
    i = 0
    while ((array_penggunaan_tiket[i] != "*") and (i < 30)):  #Menelusuri Riwayat Penggunaan Tiket
        if (array_penggunaan_tiket[i][2] == id):
            print(array_penggunaan_tiket[i][1], "|", array_penggunaan_tiket[i][0], "|",array_penggunaan_tiket[i][3])
        i += 1
