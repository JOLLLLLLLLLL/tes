while True:
    while True:
        jumlah = int(input("Masukkan Jumlah Mahasiswa (5-10) :"))
        if jumlah >= 5 and jumlah <=10:
            break
        print("INPUTAN HARUS 5-10")

    total_nilai = 0

    for i in range(jumlah):
        nilai = int(input("Masukkan Nilai Mahasiswa :"))
        total_nilai = total_nilai + nilai

    rata_rata = total_nilai/jumlah
    print(f"Rata Ratanya : {rata_rata}")

    if rata_rata >= 90:
        print("PREDIKAT     :SANGAT BAGUS")
    elif rata_rata >= 80:
        print("PREDIKAT     : BAGUS")
    elif rata_rata >= 70:
        print("PREDIKAT     :CUKUP")
    else:
        print("PREDIKAT     :WADUH")

    pilih = input("\nMau hitung data mahasiswa lain? (y/n): ")
    if pilih.lower() != "y":
        print("\n===== Selesai ya, lek. Mantap! =====\n")
        break 
    print("\n===== PROGRAM DIULANG DARI AWAL =====\n")