
from src.input_data import input_positif, tampilkan_menu
from src.proses import (
    hitung_persegi,
    hitung_persegi_panjang,
    hitung_segitiga,
    hitung_lingkaran,
)
from src.output import tampilkan_hasil
from src.visualisasi import tampilkan_animasi


def main():
    while True:
        pilihan = tampilkan_menu()

        try:
            if pilihan == "1":
                sisi = input_positif("Masukkan panjang sisi: ")
                ukuran = {"sisi": sisi}
                hasil = hitung_persegi(sisi)

            elif pilihan == "2":
                panjang = input_positif("Masukkan panjang: ")
                lebar = input_positif("Masukkan lebar: ")
                ukuran = {"panjang": panjang, "lebar": lebar}
                hasil = hitung_persegi_panjang(panjang, lebar)

            elif pilihan == "3":
                alas = input_positif("Masukkan alas: ")
                tinggi = input_positif("Masukkan tinggi: ")
                sisi1 = input_positif("Masukkan sisi pertama: ")
                sisi2 = input_positif("Masukkan sisi kedua: ")
                sisi3 = input_positif("Masukkan sisi ketiga: ")

                ukuran = {
                    "alas": alas,
                    "tinggi": tinggi,
                    "sisi1": sisi1,
                    "sisi2": sisi2,
                    "sisi3": sisi3,
                }
                hasil = hitung_segitiga(
                    alas, tinggi, sisi1, sisi2, sisi3
                )

            elif pilihan == "4":
                jari_jari = input_positif("Masukkan jari-jari: ")
                ukuran = {"jari_jari": jari_jari}
                hasil = hitung_lingkaran(jari_jari)

            elif pilihan == "5":
                print("Terima kasih telah menggunakan EUCLID LAB!")
                break

            else:
                print("Pilihan tidak valid. Pilih angka 1-5.")
                continue

            tampilkan_hasil(hasil)

            print("\nMembuka animasi pembelajaran...")
            tampilkan_animasi(hasil, ukuran)

            print("\nAnimasi selesai. Kembali ke menu.")

        except ValueError as error:
            print(f"Perhitungan gagal: {error}")

        except Exception as error:
            print(f"Terjadi kesalahan: {error}")
            import traceback
            traceback.print_exc()


if __name__ == "__main__":
    main()