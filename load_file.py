import csv

def load_file(object_file):
    csv_file = open(object_file, 'r')
    reader = csv.DictReader(csv_file, delimiter = ',')  #object_file dibaca dan dimasukkan ke variable reader
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

print("File perusahaan Willy Wangky’s Chocolate Factory telah di-load.")



    
