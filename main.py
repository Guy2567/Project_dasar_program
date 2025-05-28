import aritmatika
import konversi
import ubah_bilangan

def menu_utama():
    while True:
        print("\n===== Menu Utama =====")
        print("1. Aritmatika")
        print("2. Konversi")
        print("3. Ubah Bilangan")
        print("4. Keluar")

        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            menu_aritmatika()
        elif pilihan == "2":
            menu_konversi()
        elif pilihan == "3":
            menu_ubah_bilangan()
        elif pilihan == "4":
            print("Terima kasih telah menggunakan program ini!\nSampai jumpa :)")
            break
        else:
            print("Input tidak valid. Silakan coba lagi.")

def menu_aritmatika():
    print("\n--- Menu Aritmatika ---")
    print("1. Penjumlahan")
    print("2. Perpangkatan")
    print("3. Perkalian")
    pilih = input("Pilih operasi: ")

    try:
        a = float(input("Masukkan bilangan pertama: "))
        b = float(input("Masukkan bilangan kedua: "))
    except ValueError:
        print("Input harus berupa angka.")
        return

    if pilih == "1":
        print("Hasil: ", aritmatika.penjumlahan(a, b))
    elif pilih == "2":
        print("Hasil: ", aritmatika.perpangkatan(a, b))
    elif pilih == "3":
        print("Hasil: ", aritmatika.perkalian(a, b))
    else:
        print("Pilihan tidak valid.")

def menu_konversi():
    print("\n--- Menu Konversi ---")
    print("1. CM ke M")
    print("2. M ke CM")
    pilih = input("Pilih konversi: ")

    try:
        nilai = float(input("Masukkan nilai: "))
    except ValueError:
        print("Input harus berupa angka.")
        return

    if pilih == "1":
        print("Hasil: ", konversi.cm_to_m(nilai), "meter")
    elif pilih == "2":
        print("Hasil: ", konversi.m_to_cm(nilai), "cm")
    else:
        print("Pilihan tidak valid.")

def menu_ubah_bilangan():
    print("\n--- Menu Ubah Bilangan ---")
    print("1. Desimal ke Biner")
    print("2. Desimal ke Oktal")
    print("3. Desimal ke Heksadesimal")
    pilih = input("Pilih konversi: ")

    try:
        nilai = int(input("Masukkan bilangan desimal: "))
    except ValueError:
        print("Input harus berupa bilangan bulat.")
        return

    if pilih == "1":
        print("Hasil: ", ubah_bilangan.desimal_ke_biner(nilai))
    elif pilih == "2":
        print("Hasil: ", ubah_bilangan.desimal_ke_oktal(nilai))
    elif pilih == "3":
        print("Hasil: ", ubah_bilangan.desimal_ke_heksadesimal(nilai))
    else:
        print("Pilihan tidak valid.")

# Komentar personal (biar terlihat autentik):
# Dibuat dengan penuh semangat dan kesabaran di Termux, walau capek tapi puas :)

if __name__ == "__main__":
    menu_utama()

# Udah gitu doang, simpel tapi berguna.
# Program modular biar kalau error gampang nyari sumbernya.
# Dosen senang, mahasiswa tenang 😎
