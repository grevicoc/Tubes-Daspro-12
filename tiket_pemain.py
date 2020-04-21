def tiket_pemain():
    username = input("Masukkan username: ")
    print("Riwayat:")
    for row in (array_kepemilikan_tiket):
        if row!= "*": 
            if username == row["Username"]:
                for line in (array_wahana):
                    if line !="*":
                        if row["ID_Wahana"] == line["ID_Wahana"]:
                            print(line["ID_Wahana"],"|",line["Nama_Wahana"],"|",row["Jumlah_Tiket"])
