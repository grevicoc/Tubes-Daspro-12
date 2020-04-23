def Login_User():
    print("$ login")
    username = input("Masukan username:")
    password = input("Masukan password:")
    for i in range(30):
        if(array_user[i][4] == username and array_user[i][5] == password):
             print("Selamat bersenang-senang,",row["Nama"],"!")
        else:
             print("Ups, password salah atau kamu tidak terdaftar dalam sistem kami. Silakan coba lagi!")
             Login_User()
