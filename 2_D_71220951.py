print("~~~~ Table Matematika Nich ~~~~")
print("Pilihan Model Matematika")
print("1. Perkalian")
print("2. Pembagian")

masukinmodelya = (input("Masukkan model matematika yang diinginkan 1/2:"))
mautampilinangkabrp = int(input("Menampilkan table matematika dari angka: "))

if(masukinmodelya == "1"):
    for bea in range(1, 11):
        print(mautampilinangkabrp, "x", bea, "=", mautampilinangkabrp*bea)
elif(masukinmodelya == "2"):
    for bea in range(50,66):
        print(bea, ":", mautampilinangkabrp, "=", bea/mautampilinangkabrp)
else:
    print("Pilihan tidak tersedia, jangan ngasal!")

