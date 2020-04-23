def tiket_pemain():
    username = input("Masukkan username: ")
    print("Riwayat:")
    i = 0
    while ((array_kepemilikan_tiket[i] != "*") and (i < 30)):
        if (username == array_kepemilikan_tiket[i][0]): # Menemukan data username yang dimasukkan
            j = 0
            found = False
            while ((array_wahana[j]!="*")  and not found):
                if (array_kepemilikan_tiket[i][1] == array_wahana[j][0]): # Menemukan data wahana yang digunakan oleh username terkait
                        print(array_wahana[j][0], "|", array_wahana[j][1], "|", array_kepemilikan_tiket[i][2])
                        found = True
                j +=1
        i+=1
