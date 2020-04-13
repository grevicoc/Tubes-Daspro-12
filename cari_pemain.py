import pandas
import csv

def cari_pemain(username):
    with open('File User.csv', mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        mark = False    #penanda apakah terdapat username atau tidak
        for row in csv_reader:
            if username == row["Username"]:
                print("Nama Pemain: ", row["Username"])
                print("Tinggi Pemain: ", row["Tinggi_Badan"])
                print("Tanggal Lahir Pemain: ", row["Tanggal_Lahir"])
                mark = True
                break
        if mark == False:
            print("Pemain dengan username tersebut tidak ditemukan.")

#program
cari_pemain(input("Masukkan username: "))
            
          
    