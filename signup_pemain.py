def Sign_Up():
    nama = input("Masukan nama pemain:")
    birth = input("Masukan tanggal lahir pemain:")
    tinggi = input("Masukan tinggi badan pemain (cm):")
    username = input("Masukan username pemain:")
    password = input("Masukan password pemain:")
    a = 0
    for i in range(30):
        if array_user[i] == "*" :
            array_user[i] = [nama,birth,tinggi,username,password,"guest",0,"no"]
            a = i
        elif (i > a):
            array_used[i] = "*"

    print("Selamat menjadi pemain,",nama,". Selamat bermain.")
