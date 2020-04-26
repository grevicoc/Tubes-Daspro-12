def kehilangan_tiket():
    username = input("Masukan username:")
    tanggal = input("Tanggal kehilangan tiket:")
    ID = input("ID wahana:")
    jumlah = int(input("Jumlah tiket yang dihilangkan:"))
    array_hilang = ["*" for i in range(30)]
    a = 99
    for i in range(30):
        if array_hilang[i] == "*":
            if (i > a):
                array_hilang[i] = "*"
            else:
                array_hilang[i] = [username,tanggal,ID,jumlah]
                a = i    
    kurang_tiket(array_kepemilikan_tiket,jumlah)       
    print("")
    print("Laporan kehilangan tiket anda telah direkam")



def kurang_tiket(arr,jumlah):
    for j in range(30):
        if arr[j][0] == username :
            if arr[j][1] == ID:
                arr[j][2] = arr[j][2] - jumlah
    return arr
   
        
