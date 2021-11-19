print ("==== Kalkulator Akar dan Pangkat ==== ")
print ("Pilihan menu :")
print ("1. Pangkat 2 (Kuadrat)") 
print ("2. Pangkat 3 (kubik)")
print ("3. Akar Kuadrat")

pilihan_menu = int(input("Masukkan menu yang anda pilih :"))

if pilihan_menu == 1 :
    masukkan = int(input("Masukkan bilangan yang ingin di pangkatkan :"))
    operasi = masukkan ** 2
    print("Hasil dari pemangkatan bilangan",masukkan,"dengan 2 (Kuadrat) adalah",operasi)
elif pilihan_menu == 2:
    masukkan = int(input("Masukkan bilangan yang ingin di pangkatkan :"))
    operasi = masukkan ** 3
    print("Hasil dari pemangkatan bilangan",masukkan,"dengan  3 (Kubik) adalah",operasi)
elif pilihan_menu == 3:
    masukkan = int(input("Masukkan bilangan yang ingin di pangkatkan :"))
    operasi = masukkan ** (1/2)
    print("Hasil akar kuadrat dari bilangan",masukkan,"adalah",operasi)
else : 
    print("Pilihan menu yang dimasukkan tidak sesuai!")



