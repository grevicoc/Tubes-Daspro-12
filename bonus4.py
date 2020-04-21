arrmilikuser = ["wangkypro"]
arrmilikID = ["DIT025"]
arrmiliktiket = ["2"]
arruserhilang = []
arrtglhilang = []
arrIDhilang = []
arrjumlahtikethilang = []

def hilang_tiket():
    a = input("Masukan username:")
    b = input("Tanggal Kehilangan Tiket:")
    c = input("ID Wahana:")
    d = input("Jumlah tiket yang dihilangkan:")
    input_filehilang(arruserhilang,a)
    input_filehilang(arrtglhilang,b)
    input_filehilang(arrIDhilang,c)
    input_filehilang(arrjumlahtikethilang,d)
    print("")
    print("Laporan kehilangan tiket anda telah direkam")

def input_filehilang(arr,x):
    arr.append(x)
    return arr
    
hilang_tiket()
print(arrIDhilang)
