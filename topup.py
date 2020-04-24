def topup():
    username = input("Masukkan username: ") # Asumsi masukan username valid
    saldo = int(input("Masukkan saldo yang di top-up: "))
    i = 0
    changed = False
    while (not changed): #Username valid maka saldo selalu dapat diubah
            if (array_user[i][3] == username):  # Mencari data username terkait
                newBalance = int(array_user[i][6]) + saldo
                nama = array_user[i][0]
                array_user[i][6] = newBalance
                changed =True
            i+=1
    print("Top up berhasil. Saldo", nama, "bertambah menjadi", newBalance)
