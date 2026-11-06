
def input_positif(pesan):
    while True:
        try:
            nilai = float(input(pesan))

            if nilai > 0:
                return nilai

            print("Ukuran harus lebih dari 0.")

        except ValueError:
            print("Input tidak valid. Masukkan angka.")


def tampilkan_menu():
    print("\n" + "=" * 44)
    print("          EUCLID LAB")
    print("   Interactive Geometry Learning")
    print("=" * 44)
    print("1. Persegi")
    print("2. Persegi Panjang")
    print("3. Segitiga")
    print("4. Lingkaran")
    print("5. Keluar")
    print("=" * 44)

    return input("Pilih bangun datar (1-5): ").strip()