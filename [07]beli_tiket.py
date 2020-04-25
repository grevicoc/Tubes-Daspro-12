import csv

def validasi_umur(object_lahir, tanggal, batas_umur):     #object_umur adalah umur sang pengguna dan batas_umur adalah batasan umur wahana dan tanggal adalah hari ini
    tahun_tanggal = int(tanggal[6:10])
    bulan_tanggal = int(tanggal[3:5])
    hari_tanggal = int(tanggal[0:2]) 
    
    tahun_user = int(object_lahir[6:10])
    bulan_user = int(object_lahir[3:5])
    hari_user = int(object_lahir[0:2])

    if (hari_tanggal - hari_user) < 0:  #dengan penyederhanaan 1 bulan 30 hari dan tidak ada tahun kabisat
        hari_tanggal += 30              #toh perbedaan 1-2 hari tidak terlalu signifikan
        bulan_tanggal -= 1
        if (bulan_tanggal - bulan_user) < 0:
            bulan_tanggal += 12
            tahun_tanggal -= 1
            sum = (hari_tanggal-hari_user) + (30*(bulan_tanggal-bulan_user)) + (365*(tahun_tanggal-tahun_user))
        else:
            sum = (hari_tanggal-hari_user) + (30*(bulan_tanggal-bulan_user)) + (365*(tahun_tanggal-tahun_user))
    else:
        if (bulan_tanggal - bulan_user) < 0:
            bulan_tanggal += 12
            tahun_tanggal -= 1
            sum = (hari_tanggal-hari_user) + (30*(bulan_tanggal-bulan_user)) + (365*(tahun_tanggal-tahun_user))
        else:
            sum = (hari_tanggal-hari_user) + (30*(bulan_tanggal-bulan_user)) + (365*(tahun_tanggal-tahun_user))

    umur = sum/365
    if batas_umur > umur:
        return False
    elif batas_umur <= umur:
        return True



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
