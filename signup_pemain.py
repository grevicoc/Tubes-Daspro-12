def Sign_Up():
    nama = input("Masukan nama pemain:")
    birth = input("Masukan tanggal lahir pemain:")
    tinggi = input("Masukan tinggi badan pemain (cm):")
    username = input("Masukan username pemain:")
    password = input("Masukan password pemain:")
    for i in range(30):
        if array_user[i] == "*" :
            array_user[i] = (nama,birth,tinggi,username,password)
            
    print("Selamat menjadi pemain,",nama,". Selamat bermain.")