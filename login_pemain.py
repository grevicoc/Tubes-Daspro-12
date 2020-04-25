def Login_User():
    print("$ login")
    username = input("Masukan username:")
    password = input("Masukan password:")
    ambil_data(array_user,username)
    for i in range(30):
        if (array_user[i][3] == username):  
            if (array_user[i][4] == password):
                print("Selamat bersenang-senang,",array_user[i][0],"!")   
            else:
                print("Ups, password salah atau kamu tidak terdaftar dalam sistem kami. Silakan coba lagi!")
                Login_user()

def ambil_data(arr,x):
    array_login = 0
    for i in range(30):
        if (arr[i][3] == x):
            array_login = arr[i]
    return array_login
        
    
    
