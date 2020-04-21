
def tiket_pemain():
    username = input("Masukkan username: ")
    print("Riwayat:")
    i = 0
    while array_kepemilikan_tiket[i] != "*":
        if username == array_kepemilikan_tiket[i]["Username"]:
            for line in (array_wahana):
                if line != "*" and array_kepemilikan_tiket[i]["ID_Wahana"] == line["ID_Wahana"]:
                        print(line["ID_Wahana"], "|", line["Nama_Wahana"], "|", array_kepemilikan_tiket[i]["Jumlah_Tiket"])
        i+=1
