
arruser=["wangkypro","iqbalganteng","koncomu"]
arrpass=["coklatenakno1","akuanakmama","mantap"]
arrname=["Willy Wangky","Iqbal Alam","Konco"]
    

def Login_cek(x,y):
    i=0
    while(i< len(arruser)):
        if((arruser[i] == x) and (arrpass[i] == y)):
            print("")
            print("Selamat bersenang-senang,",arrname[i],"!")
            break
        elif((arruser[i] != x) and (arrpass[i] != y)):
            if((cek_array(arruser,x) == False) and (cek_array(arrpass,y) == False)):
                print("")
                print("Ups, password salah atau kamu tidak terdaftar dalam sistem kami. Silakan coba lagi!")
                break
            else:
                i = i+1
        else:
            print("")
            print("Ups, password salah atau kamu tidak terdaftar dalam sistem kami. Silakan coba lagi!")
            print("")
            Login_User()

def cek_array(arr,x):
    p = x in arr
    return p
        
            
def Login_User():
    a = input("Masukan username:")
    b = input("Masukan password:")
    Login_cek(a,b)
    
Login_User()

