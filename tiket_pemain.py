def tiket_pemain():
    username = input("Masukkan username: ")#Asumsi Username valid
    print("Riwayat:")
    i = 0
    done = False
    while ((array_kepemilikan_tiket[i] != "*") and not done):
        if (username == array_kepemilikan_tiket[i][0]): # Menemukan data username yang dimasukkan
            j = 0
            found = False
            while (not found): # Username valid maka wahana pasti ditemukan
                if (array_kepemilikan_tiket[i][1] == array_wahana[j][0]): # Menemukan data wahana yang digunakan oleh username terkait
                        print(array_wahana[j][0], "|", array_wahana[j][1], "|", array_kepemilikan_tiket[i][2])
                        found = True
                j += 1
        if i < 29:
            i += 1
        else:
            done = True
