def Login_User():
    print("$ login")
    username = input("Masukan username:")
    password = input("Masukan password:")
    for row in (array_user):
        if row != "*":
            if((row["Username"] == username) and (row["Password"] == password)):
                print("Selamat bersenang-senang,",row["Nama"],"!")
            else:
                print("Ups, password salah atau kamu tidak terdaftar dalam sistem kami. Silakan coba lagi!")
                Login_User()
