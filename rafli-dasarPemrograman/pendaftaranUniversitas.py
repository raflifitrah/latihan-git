nama = str(input("Masukkan nama anda: "))
tempat_lahir = str(input("Masukkan tempat lahir anda: "))
tanggal_lahir = int(input("Masukkan tanggal lahir anda: "))
tahun_lahir = int(input("Masukkan tahun lahir anda: "))
tahun_sekarang = int(input("Masukkan tahun sekarang: "))
jenis_kelamin = str(input("Masukkan jenis kelamin anda: "))

umur = tahun_sekarang-tahun_lahir

nilai_english = float(input("Masukkan nilai English anda: "))
nilai_matematika = float(input("Masukkan nilai Matematika anda: "))
nilai_indonesia = float(input("Masukkan nilai Indonesia anda: "))

nilai_rata_rata = (nilai_english+nilai_matematika+nilai_indonesia) / 3

print("Nilai rata-rata anda adalah : %.2f" % nilai_rata_rata)

if nilai_rata_rata >= 80 and jenis_kelamin == "laki laki" and umur <=25:
    print("Anda masuk jurusan teknik informatika")
elif nilai_rata_rata >=80 and jenis_kelamin == "Perempuan" and umur <=25:
    print("Anda masuk jurusan sistem informasi")
elif umur <=25:
    print("Anda masuk jurusan DKV")
else:
    print("Anda tidak diterima di jurusan manapun")