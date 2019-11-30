
list = []
nomor = 0
while True:
    nama = input("Masukkan Nama: ")
    nim = input("Masukkan Nim: ")
    tugas = int(input("Masukkan Nilai Tugas: "))
    uts = int(input("Masukkan Nilai UTS: "))
    uas = int(input("Masukkan Nilai UAS: "))
    akhir = (tugas*.3 + uts*.35 + uas*.35)
    nomor+=1
    list.append([nomor,nama, nim, tugas, uts, uas, akhir])
    ulang = input("Tambah Data: (y/t)")
    if ulang == "t":
        break
print("="*67)
print("| NO |    NAMA    |   NIM   |  TUGAS  |  UTS  |  UAS  |   AKHIR   |")
print("="*67)
for i in list:
    print("| {0:1d}  |  {1:8s}  |   {2:4s}  | {3:5d}   | {4:4d}  | {5:4d}  |    {6}   |".format(i[0], i[1], i[2], i[3], i[4], i[5], i[6]))
print("="*67)