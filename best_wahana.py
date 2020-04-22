def best_wahana():
    arrbest = ["*" for k in range(30)]
    i = 0
    x = 0

    while array_pembelian_tiket[i]!="*":    # Menggabungkan jumlah tiket masing - masing wahana ke dalam array arrbest
        found = False
        j = 0
        tempid = array_pembelian_tiket[i]["ID_Wahana"]
        jumlah_tiket = int(array_pembelian_tiket[i]["Jumlah_Tiket"])
        while j < 30 and not found:
            if arrbest[j][0] == tempid :
                found = True
            j+=1
        if not found :
            for k in range(i+1,30):
                if array_pembelian_tiket[k]!="*" and tempid == array_pembelian_tiket[k]["ID_Wahana"]:
                    jumlah_tiket += int(array_pembelian_tiket[k]["Jumlah_Tiket"])
            arrbest[x] = tempid,jumlah_tiket
            x += 1
        i += 1

    i = 0
    while i < 30 and arrbest[i] != "*": #Melakukan sorting terhadap array arrbest berdasarkan jumlah tiket
        temp_jumlah = int(arrbest[i][1])
        temp = arrbest[i]
        j = i + 1
        while j < 30 and arrbest[j] != "*":
            if arrbest[j][1] >= temp_jumlah:
                temp_jumlah = int(arrbest[j][1])
                idx = j
                arrbest[i] = arrbest[idx]
                arrbest[idx] = temp
            j += 1
        i += 1

    i = 0
    while arrbest[i] != "*" and i < 3: # Mencari 3 nama wahana denga jumlah tiket terbanyak kemudian mencetaknya
        j = 0
        found = False
        while array_wahana[j] != "*" and not found:
            if arrbest[i][0] == array_wahana[j]["ID_Wahana"]:
                tempwhn = array_wahana[j]["Nama_Wahana"]
                found = True
            j += 1
        print(i+1, "|", arrbest[i][0], "|", tempwhn, "|", arrbest[i][1])
        i += 1
    if i == 0:
        print("Tidak ada data")
