masukkan_1 = str(input("Masukkan daftar siswa :"))
print ("Daftar siswa:",masukkan_1.title().split())

masukkan_2 = str(input("Masukkan siswa yang ingin ditambahkan:"))
combine = masukkan_1.title() + " " + masukkan_2.upper()
print("Hasil penambahan pada daftar siswa :",combine.split())