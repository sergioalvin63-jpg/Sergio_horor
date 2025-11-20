import os, time

print("--undefeated mind--")
print("pada suatu hari pemuda terbangun di")
print("dalam suatu rumah terbengkalai...")
print("-------------")
print("terdapat 2 alat makan dia memilih")
print("-------------")
print("1. sumpit")
print("2. gardok")
step_1 = int(input("= "))

if step_1 == 1:
    os.system("cls")
    time.sleep(2)
    print("pemuda melihat ke belakang..")
    time.sleep(4)
    os.system("cls")
    print("sosok hitam mulai mendatangi pemuda tersebut")
    time.sleep(1)
    os.system("cls")
    print("sosok sudah di depan pemudanya!")
    print("1. serang")
    print("2. kabur")
    step_2 = int(input("= "))

    if step_2 == 1:
        print("di tepis serangan pemudanya!")
        print("splashhh!")
        time.sleep(3)
        os.system("cls")
        print("lalu pemuda itu langsung mengambil barang yang ada di sekitar!")
        print("barang di sekitarnya yaitu ada")
        print("1. kayu")
        print("2. air")
        print("3. palu")
        step_3 = int(input("= "))

        if step_3 == 1:
            print("Menang!")
        elif step_3 == 2:
            print("Kalah!")
        elif step_3 == 3:
            print("Menang besar!")
        else:
            print("Pilihan tidak ada, pemuda mati.")

    elif step_2 == 2:
        print("Pemuda itu sangat kencang berlarinya!")
        print("Sehingga tidak bisa ditangkap!")

elif step_1 == 2:
    print("Tersedia nasi vegan di tempatnya!")
    time.sleep(3)
    os.system("cls")
    print("Pemuda mendekati nasi")
    time.sleep(2)
    os.system("cls")
    print("Terlihat ada bangunan dan penduduk di sana.")
