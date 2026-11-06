
import math


def hitung_persegi(sisi):
    if sisi <= 0:
        raise ValueError("Sisi harus lebih dari 0.")

    return {
        "bangun": "Persegi",
        "luas": sisi ** 2,
        "keliling": 4 * sisi
    }


def hitung_persegi_panjang(panjang, lebar):
    if panjang <= 0 or lebar <= 0:
        raise ValueError("Panjang dan lebar harus lebih dari 0.")

    return {
        "bangun": "Persegi Panjang",
        "luas": panjang * lebar,
        "keliling": 2 * (panjang + lebar)
    }


def hitung_segitiga(alas, tinggi, sisi1, sisi2, sisi3):
    if min(alas, tinggi, sisi1, sisi2, sisi3) <= 0:
        raise ValueError("Semua ukuran harus lebih dari 0.")

    if (sisi1 + sisi2 <= sisi3
            or sisi1 + sisi3 <= sisi2
            or sisi2 + sisi3 <= sisi1):
        raise ValueError("Ukuran sisi tidak membentuk segitiga valid.")

    return {
        "bangun": "Segitiga",
        "luas": 0.5 * alas * tinggi,
        "keliling": sisi1 + sisi2 + sisi3
    }


def hitung_lingkaran(jari_jari):
    if jari_jari <= 0:
        raise ValueError("Jari-jari harus lebih dari 0.")

    return {
        "bangun": "Lingkaran",
        "luas": math.pi * jari_jari ** 2,
        "keliling": 2 * math.pi * jari_jari
    }