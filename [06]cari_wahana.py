def cari_wahana():     
    print("Jenis batasan umur:")
    print("1. Anak-anak (<17 tahun)")
    print("2. Dewasa (>=17 tahun)")
    print("3. Semua Umur\n")
    print("Jenis batasan tinggi badan:")
    print("1. Lebih dari 130 cm")
    print("2. Tanpa batasan")
    
    k=0
    while(array_user[k]!='*'):   # Menandai indeks array yang memiliki username yang sama dengan username saat login
            if(array_user[k][3]==user):
                d=k
            k=k+1

    age = input("Batasan umur pemain: )
    while (age != '1') and (age != '2') and (age != '3'):
        print("Batasan umur tidak valid!")
        age = input("Batasan umur pemain: ")
        
    height = input("Batasan tinggi badan: ")
    while (height != '1') and (height != '2'):
        print("Batasan tinggi badan tidak valid")
        height = input("Batasan tinggi badan: )

    mark = False            #menandakan apakah wahana ditemukan atau tidak

    print("Hasil pencarian: ")
    if age == '1':          
        i=0
        while array_wahana[i] != '*':
            if int(array_wahana[i][3)] < 17:
                if height == '1':
                    if int(array_wahana[i][4]) > 130:
                        if(array_user[d][7]=='yes'):
                            print(f"{array_wahana[i][0]} | {array_wahana[i][1]} | {int(array_wahana[i][2])/2}")
                            mark = True
                            i+=1
                        else:
                            print(f"{array_wahana[i][0]} | {array_wahana[i][1]} | {array_wahana[i][2]}")
                            mark = True
                            i+=1
                    else:
                        i+=1
                else:
                    if(array_user[d][7]=='yes'):
                        print(f"{array_wahana[i][0]} | {array_wahana[i][1]} | {int(array_wahana[i][2])/2}")
                        mark = True
                        i+=1
                    else:
                        print(f"{array_wahana[i][0]} | {array_wahana[i][1]} | {array_wahana[i][2]}")
                        mark = True
                        i+=1
            else:
                i+=1
    elif age == '2':
        i=0
        while array_wahana[i] != '*':
            if int(array_wahana[i][3)] >= 17:
                if height == '1':
                    if int(array_wahana[i][4]) > 130:
                        if(array_user[d][7]=='yes'):
                            print(f"{array_wahana[i][0]} | {array_wahana[i][1]} | {int(array_wahana[i][2])/2}")
                            mark = True
                            i+=1
                        else:
                            print(f"{array_wahana[i][0]} | {array_wahana[i][1]} | {array_wahana[i][2]}")
                            mark = True
                            i+=1
                    else:
                        i+=1
                else:
                    if(array_user[d][7]=='yes'):
                        print(f"{array_wahana[i][0]} | {array_wahana[i][1]} | {int(array_wahana[i][2])/2}")
                        mark = True
                        i+=1
                    else:
                        print(f"{array_wahana[i][0]} | {array_wahana[i][1]} | {array_wahana[i][2]}")
                        mark = True
                        i+=1
            else:
                i+=1
    else:
        i=0
        while array_wahana[i] != '*':
            if height == '1':
                    if int(array_wahana[i][4]) > 130:
                        if(array_user[d][7]=='yes'):
                            print(f"{array_wahana[i][0]} | {array_wahana[i][1]} | {int(array_wahana[i][2])/2}")
                            mark = True
                            i+=1
                        else:
                            print(f"{array_wahana[i][0]} | {array_wahana[i][1]} | {array_wahana[i][2]}")
                            mark = True
                            i+=1
                    else:
                        i+=1
            else:
                if(array_user[d][7]=='yes'):
                        print(f"{array_wahana[i][0]} | {array_wahana[i][1]} | {int(array_wahana[i][2])/2}")
                        mark = True
                        i+=1
                    else:
                        print(f"{array_wahana[i][0]} | {array_wahana[i][1]} | {array_wahana[i][2]}")
                        mark = True
                        i+=1
    if mark == False:
        print("Tidak ada wahana yang sesuai dengan pencarian kamu.")
