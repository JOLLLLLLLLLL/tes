nama = input("MASUKKAN NAMA MAHASISWA : ")
target = int(input("Masukkan Target : "))

percobaan = 0

while percobaan <= 3:
    percobaan += 1
    nilai = int(input(f"Nilai {percobaan} : "))
    
    if nilai >= target:
        print(f"\n{nama} berhasil lulus setelah {percobaan} percobaan!")
        break
else:
    print(f"\n{nama} tidak lulus setelah 3 kali percobaan.")