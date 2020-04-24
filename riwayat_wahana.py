def riwayat_wahana():
    id = input("Masukkan ID Wahana: ")
    print("Riwayat:")
    i = 0
    done = False
    while ((array_penggunaan_tiket[i] != "*") and (not done)):  #Menelusuri Riwayat Penggunaan Tiket
        if (array_penggunaan_tiket[i][2] == id):
            print(array_penggunaan_tiket[i][1], "|", array_penggunaan_tiket[i][0], "|",array_penggunaan_tiket[i][3])
        if i < 29 :
            i += 1
        else:
            done = True
