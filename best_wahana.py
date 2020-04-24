def best_wahana():
    arrbest = ["*" for k in range(30)]
    i = 1 # Indeks Pencacah i akan dimulai dari 1 ketika file memiliki header
    x = 0
    done = False
    while array_pembelian_tiket[i]!="*" and not done :    # Menggabungkan jumlah tiket masing - masing wahana ke dalam array arrbest
        found = False
        j = 0
        tempid = array_pembelian_tiket[i][2]
        jumlah_tiket = int(array_pembelian_tiket[i][3])
        while j < 30 and not found:
            if arrbest[j][0] == tempid :
                found = True
            j+=1
        if not found : # Memproses wahana yang belum pernah diproses sebelumnya
            for k in range(i+1,30):
                if array_pembelian_tiket[k]!="*" and tempid == array_pembelian_tiket[k][2]:
                    jumlah_tiket += int(array_pembelian_tiket[k][3])
            arrbest[x] = tempid,jumlah_tiket
            x += 1
        if i < 29:
            i += 1
        else:
            done = True

    i = 0
    done = False
    while not done and arrbest[i] != "*": #Melakukan sorting terhadap array arrbest berdasarkan jumlah tiket
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
        if i < 29:
            i += 1
        else:
            done = True

    i = 0
    while arrbest[i] != "*" and i < 3: # Mencari 3 nama wahana dengan jumlah tiket terbanyak kemudian mencetaknya
        j = 0
        found = False
        while array_wahana[j] != "*" and not found:
            if arrbest[i][0] == array_wahana[j][0]:
                tempwhn = array_wahana[j][1]
                found = True
            j += 1
        print(i+1, "|", arrbest[i][0], "|", tempwhn, "|", arrbest[i][1])
        i += 1
