def beli_tiket():
    id = input("Masukkan ID wahana: ")
    tanggal = input("Masukkan tanggal hari ini: ")
    tiket = int(input("Masukkan jumlah tiket yang dibeli: "))

    while array_wahana != '*':
        if array_wahana[i][0] == id:            #asumsi wahana ditemukan dengan indeks i
            if validasi_umur(user[i][1], tanggal, array_wahana[i][3]):
                if user[2] >= array_wahana[i][4]:
                    if (user[6]-(tiket*int(array_wahana[i][2]))) > 0:
                        user[6] = user[6]-(tiket*int(array_wahana[i][2]))   #requirement terpenuhi, saldo berkurang
                        j = 0
                        while True:
                            if array_pembelian_tiket[j] == '*':
                                array_pembelian_tiket[j] = [user[3], tanggal, id, str(tiket)] #memasukkan riwayat pembelian tiket
                                break
                            else:
                                j+=1
                        j = 0
                        while True:
                            if array_kepemilikan_tiket[j] == '*':
                                array_kepemilikan_tiket[j] = [user[3], id, str(tiket)] #memasukkan riwayat kepemilikan tiket
                                break
                            else:
                                j+=1
                        print(f"Selamat bermain di {array_wahana[i][1]}.")
                        break
                    else:
                        print("Saldo Anda tidak cukup.")
                        print("Silakan mengisi saldo Anda.")
                        break    
                else:
                    print("Anda tidak memenuhi persyaratan untuk memainkan wahana ini.")
                    print("Silakan menggunakan wahana lain yang tersedia.")
            else:
                print("Anda tidak memenuhi persyaratan untuk memainkan wahana ini.")
                    print("Silakan menggunakan wahana lain yang tersedia.")
        else:
            i+=1
