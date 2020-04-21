def topup():
    username = input("Masukkan username: ")
    saldo = int(input("Masukkan saldo yang di top-up: "))
    for row in (array_user):
        if row != "*":
            if row['Username'] == username:
                newBalance = int(row['Saldo']) + saldo
                nama = row["Nama"]
                row['Saldo'] = newBalance
    print("Top up berhasil. Saldo", nama ,"bertambah menjadi", newBalance)
