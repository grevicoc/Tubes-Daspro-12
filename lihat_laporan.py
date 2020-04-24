import csv

def load_file(object_file):
    csv_file = open(object_file, 'r')
    reader = csv.reader(csv_file, delimiter = ',')      #object_file dibaca dan dimasukkan ke variable reader
    array_object = ['*' for i in range (30)]            #array kosong didefinisikan bernilai 30
    i=0                                                 #inisiasi variable untuk meng-akses array_object
    for row in reader:
        array_object[i] = row
        i += 1
    return array_object

user = input("Masukkan nama File User: ")
wahana = input("Masukkan nama File Wahana: ")
pembelian_tiket = input("Masukkan nama File Pembelian Tiket: ")
penggunaan_tiket = input("Masukkan nama File Penggunaan Tiket: ")
kepemilikan_tiket = input("Masukkan nama File Kepemilikan Tiket: ")
refund_tiket = input("Masukkan nama File Refund Tiket: ")
kritik_saran = input("Masukkan nama File Kritik dan Saran: ")

array_user = load_file(user)
array_wahana = load_file(wahana)
array_pembelian_tiket = load_file(pembelian_tiket)
array_penggunaan_tiket = load_file(penggunaan_tiket)
array_kepemilikan_tiket = load_file(kepemilikan_tiket)
array_refund_tiket = load_file(refund_tiket)
array_kritik_saran = load_file(kritik_saran)

# refund
def Refund() :
    
    identitas=str(input("Masukkan ID Wahana: "))
    tanggal=str(input("Masukkan Tanggal Refund: "))
    jumlah_tiket=int(input("Jumlah tiket yang di-refund: "))
    cek=0
    lebih_kecil=-1
    sama_besar=-1

    b=0
    
    while(array_kepemilikan_tiket[b]!='*')      # Memeriksa Kepemilikan Tiket dan Mengganti Jumlah Tiket yang dimiliki pada file kepemilikan tiket apabila Kepemilikan Tiket >= Jumlah Tiket yang ingin direfund
        if(array_kepemilikan_tiket[b][0]=='username' and array_kepemilikan_tiket[b][1]==identitas and int(array_kepemilikan_tiket[b][2])>jumlah_tiket):
            cek=cek+1
            lebih_kecil=b
            array_kepemilikan_tiket[b][2]=array_kepemilikan_tiket[b][2]-jumlah_tiket
        elif(array_kepemilikan_tiket[b][0]=='username' and array_kepemilikan_tiket[b][1]==identitas and int(array_kepemilikan_tiket[b][2])==jumlah_tiket):
            cek=cek+1
            sama_besar=b
            array_kepemilikan_tiket[b][2]=array_kepemilikan_tiket[b][2]-jumlah_tiket
        b=b+1

    j=0
    while(array_wahana[j]!='*')     # Mengambil data harga tiket untuk digunakan dalam perhitungan uang yang akan direfund
        if(array_wahana[j][0]==identitas):
            if(array_user[k][7]=='yes'):
                kembalian=float(jumlah_tiket*0.35*array_wahana[j][2])
            else:
                kembalian=float(jumlah_tiket*0.7*array_wahana[j][2])
        j=j+1

    k=0
    while(array_user[k]!='*')   # Mengembalikan uang kepada Saldo penguna
        if(lebih_kecil>-1 or sama_besar>-1):
            if(array_user[k][3]='username' and cek>0):
                array_user[k][6]=float(array_user[k][6]+kembalian)
        k=k+1

    a=0
    while(array_refund_tiket[a][0]!='*'):
        a=a+1
        
    if(cek>0):      # Menambahkan data pada file refund
        array_refund_tiket[a] = ['username',tanggal,identitas,jumlah_tiket]
        print("Uang refund sudah kami berikan pada akun Anda.")
    else:
        print("Anda tidak memiliki tiket terkait.")

# kritik_saran
def Kritik_dan_Saran() :
    identitas=str(input("Masukkan ID Wahana: "))
    tanggal=str(input("Masukkan tanggal pelaporan: "))
    kritik=str(input("Kritik/saran Anda: "))
    
    c=0
    while(array_kritik_saran[c][0]!='*'):
        c=c+1
        
    array_kritik_saran[c] = ['username',tanggal,identitas,kritik]

        
# lihat_laporan

def Lihat_Kritik_dan_Saran():
    e=0
    while(array_kritik_saran[e][0]!='*'):
        e=e+1
        
    for k in range (1,e):
        temp=array_kritik_saran[k][2][0]
        tempgeser=array_kritik_saran[k]
        l=k-1
        while(temp<array_kritik_saran[l][2][0] and l>0):
            array_kritik_saran[l+1]=array_kritik_saran[l]
            l=l-1
        if(temp>=array_kritik_saran[l][2][0]):
            array_kritik_saran[l+1]=tempgeser
        elif(l==0):
            array_kritik_saran[l+1]=array_kritik_saran[l]
            array_kritik_saran[l]=tempgeser
    
    for k in range (1,e):
        temp=array_kritik_saran[k][2][1]
        tempgeser=array_kritik_saran[k]
        l=k-1
        if(temp==array_kritik_saran[k][2][0]):
            while(temp<array_kritik_saran[l][2][1] and l>0):
                array_kritik_saran[l+1]=array_kritik_saran[l]
                l=l-1
            if(temp>=array_kritik_saran[l][2][1]):
                array_kritik_saran[l+1]=tempgeser
            elif(l==0):
                array_kritik_saran[l+1]=array_kritik_saran[l]
                array_kritik_saran[l]=tempgeser
                
    for k in range (1,e):
        temp=array_kritik_saran[k][2][2]
        tempgeser=array_kritik_saran[k]
        l=k-1
        if(temp==array_kritik_saran[k][2][1]):
            while(temp<array_kritik_saran[l][2][2] and l>0):
                array_kritik_saran[l+1]=array_kritik_saran[l]
                l=l-1
            if(temp>=array_kritik_saran[l][2][2]):
                array_kritik_saran[l+1]=tempgeser
            elif(l==0):
                array_kritik_saran[l+1]=array_kritik_saran[l]
                array_kritik_saran[l]=tempgeser

    for k in range (1,e):
        temp=array_kritik_saran[k][2][3]
        tempgeser=array_kritik_saran[k]
        l=k-1
        if(temp==array_kritik_saran[k][2][2]):
            while(temp<array_kritik_saran[l][2][3] and l>0):
                array_kritik_saran[l+1]=array_kritik_saran[l]
                l=l-1
            if(temp>=array_kritik_saran[l][2][3]):
                array_kritik_saran[l+1]=tempgeser
            elif(l==0):
                array_kritik_saran[l+1]=array_kritik_saran[l]
                array_kritik_saran[l]=tempgeser

    for k in range (1,e):
        temp=array_kritik_saran[k][2][4]
        tempgeser=array_kritik_saran[k]
        l=k-1
        if(temp==array_kritik_saran[k][2][3]):
            while(temp<array_kritik_saran[l][2][4] and l>0):
                array_kritik_saran[l+1]=array_kritik_saran[l]
                l=l-1
            if(temp>=array_kritik_saran[l][2][4]):
                array_kritik_saran[l+1]=tempgeser
            elif(l==0):
                array_kritik_saran[l+1]=array_kritik_saran[l]
                array_kritik_saran[l]=tempgeser

    for k in range (1,e):
        temp=array_kritik_saran[k][2][5]
        tempgeser=array_kritik_saran[k]
        l=k-1
        if(temp==array_kritik_saran[k][2][4]):
            while(temp<array_kritik_saran[l][2][5] and l>0):
                array_kritik_saran[l+1]=array_kritik_saran[l]
                l=l-1
            if(temp>=array_kritik_saran[l][2][2]):
                array_kritik_saran[l+1]=tempgeser
            elif(l==0):
                array_kritik_saran[l+1]=array_kritik_saran[l]
                array_kritik_saran[l]=tempgeser
    
    print("Kritik dan saran:")
    for l in range (e):
        if(array_kritik_saran[l][2]!="ID_Wahana" and array_kritik_saran[l][1]!="Tanggal_Kritik" and array_kritik_saran[l][0]!="Username" and array_kritik_saran[l][3]!="Isi_Kritik"):
            print(("{} | {} | {} | {}".format(array_kritik_saran[l][2],array_kritik_saran[l][1],array_kritik_saran[l][0],array_kritik_saran[l][3])))

# tambah_wahana

def tambah_wahana():

    print("Masukkan Informasi Wahana yang ditambahkan:")
    identitas=str(input("Masukkan ID Wahana: "))
    nama=str(input("Masukkan Nama Wahana: "))
    harga=input("Masukkan Harga Tiket: ")
    umur=str(input("Batasan umur: "))
    tinggi=str(input("Batasan tinggi badan: "))
        
    d=0
    while(array_wahana[d][0]!='*'):
        d=d+1
        
    array_wahana[d] = [identitas,nama,harga,umur,tinggi]

    print("Info wahana telah ditambahkan!")

# upgrade_gold

def upgrade_gold():
    user=str(input("Masukkan username yang ingin di-upgrade:"))
    
    k=0
    while(array_user[k]!='*'):   
        if(array_user[k][3]==user):
            array_user[k][6]=array_user[k][6]-50000 # Memotong saldo username yang bersangkutan untuk upgrade akun
            array_user[k][7]='yes' # Menandai akun sebagai akun gold
        k=k+1
        
    print("Akun Anda telah diupgrade.")
