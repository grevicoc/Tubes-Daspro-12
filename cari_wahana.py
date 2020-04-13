import pandas
import csv

def cari_wahana(mark_umur, tinggi):
    with open('File Wahana.csv', mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        mark = False    #penanda apakah terdapat username atau tidak
        print("Hasil pencarian: ")
        if mark_umur == 1:
            for row in csv_reader:
                if 0 < int(row["Batasan_Umur"]) < 17 :
                    if tinggi < int(row["Batasan_Tinggi"]) :
                        print(f'{row["ID_Wahana"]} | {row["Nama_Wahana"]} | {row["Harga_Tiket"]}')
                        mark = True
        elif mark_umur == 2:
            for row in csv_reader:
                if int(row["Batasan_Umur"]) >= 17 :
                    if tinggi < int(row["Batasan_Tinggi"]) :
                        print(f'{row["ID_Wahana"]} | {row["Nama_Wahana"]} | {row["Harga_Tiket"]}')
                        mark = True
        else:
            for row in csv_reader:
                if tinggi < int(row["Batasan_Tinggi"]) :
                        print(f'{row["ID_Wahana"]} | {row["Nama_Wahana"]} | {row["Harga_Tiket"]}')
                        mark = True
        if mark == False:
                print("Tidak ada wahana yang sesuai dengan pencarian kamu.")
#program
print("Jenis batasan umur:")
print("1. Anak-anak (<17 tahun)")
print("2. Dewasa (>=17 tahun)")
print("3. Semua Umur\n")

age = int(input("Batasan umur pemain: (pilih angka yang sesuai dengan kriteria anda)"))
while age < 1 and age > 3:
    print("Batasan umur tidak valid!")
    age = int(input("Batasan umur pemain: (pilih angka yang sesuai dengan kriteria anda)"))
    
height = int(input("Batasan tinggi pemain: (dengan max = 250 dan min = 0 dalam centimeter)"))
while height < 0 and height > 250:
    print("Batasan tinggi badan tidak valid")
    height = int(input("Batasan tinggi pemain: (pilih angka yang sesuai dengan kriteria anda"))

cari_wahana(age, height)