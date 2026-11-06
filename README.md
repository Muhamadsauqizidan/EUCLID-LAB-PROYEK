# EUCLID LAB — Interactive Geometry Learning

**EUCLID LAB** adalah aplikasi pembelajaran geometri berbasis Python yang dirancang untuk membantu pengguna memahami bangun datar melalui perhitungan matematis, visualisasi, animasi, dan narasi suara.

## 1. Latar Belakang

Pembelajaran geometri tidak hanya membutuhkan pemahaman rumus, tetapi juga kemampuan untuk membayangkan bentuk dan memahami proses perhitungannya. EUCLID LAB dikembangkan sebagai media pembelajaran interaktif yang menggabungkan perhitungan geometri dengan visualisasi agar materi lebih mudah dipahami.

## 2. Tujuan Proyek

1. Membantu pengguna memahami konsep dasar bangun datar.
2. Menghitung luas dan keliling berdasarkan ukuran yang dimasukkan.
3. Menampilkan visualisasi bangun datar melalui browser.
4. Menyajikan penjelasan bertahap dengan animasi dan narasi suara.
5. Mengembangkan penerapan algoritma dan pemrograman Python dalam media pembelajaran matematika.

## 3. Fitur Aplikasi

- **Perhitungan geometri:** menghitung luas dan keliling bangun datar sesuai rumus.
- **Empat bangun datar:** persegi, persegi panjang, segitiga, dan lingkaran.
- **Visualisasi interaktif:** menampilkan diagram bangun yang dipilih.
- **Animasi pembelajaran:** menyajikan tahapan penjelasan secara visual.
- **Narasi suara:** membacakan penjelasan menggunakan fitur suara browser yang tersedia.
- **Penjelasan rumus:** menampilkan rumus dan hasil perhitungan.
- **Kontrol pemutaran:** menyediakan kontrol untuk menjalankan, menjeda, mengulang, atau menghentikan penjelasan jika tersedia pada antarmuka.

## 4. Teknologi yang Digunakan

- Python sebagai bahasa pemrograman utama.
- HTML untuk menyusun antarmuka.
- CSS untuk mengatur tampilan aplikasi.
- JavaScript untuk animasi, interaksi, dan narasi suara.
- SVG untuk menggambar bangun datar.
- HTTP Server Python untuk menyajikan antarmuka melalui browser.
- Web Speech API untuk narasi suara apabila didukung browser.

## 5. Struktur Folder

```text
EUCLID LAB-project/
├── data/
│   └── contoh_data.txt
├── docs/
├── src/
│   ├── __init__.py
│   ├── input_data.py
│   ├── output.py
│   ├── proses.py
│   └── visualisasi.py
├── tests/
│   └── test_case.md
├── .gitignore
├── main.py
└── README.md
```

## 6. Persyaratan

- Python terpasang di komputer.
- Browser modern seperti Microsoft Edge atau Google Chrome.
- Koneksi internet tidak diperlukan untuk menjalankan aplikasi jika seluruh komponen tersedia secara lokal.

## 7. Cara Menjalankan

Buka terminal di folder proyek, kemudian jalankan:

```powershell
py main.py
```

Setelah program berjalan:

1. Pilih bangun datar melalui menu terminal.
2. Masukkan ukuran yang diminta.
3. Lihat hasil perhitungan.
4. Buka halaman visualisasi yang muncul di browser.
5. Gunakan kontrol yang tersedia untuk menjalankan penjelasan, animasi, dan narasi suara.

## 8. Rumus Geometri

### Persegi

- Luas = sisi × sisi
- Keliling = 4 × sisi

### Persegi Panjang

- Luas = panjang × lebar
- Keliling = 2 × (panjang + lebar)

### Segitiga

- Luas = ½ × alas × tinggi

### Lingkaran

- Luas = π × jari-jari²
- Keliling = 2 × π × jari-jari

## 9. Pengujian

Pengujian dilakukan menggunakan skenario yang tercantum pada `tests/test_case.md`. Pengujian mencakup ketepatan perhitungan, validasi input, tampilan visualisasi, animasi, dan narasi suara.

Status pengujian harus diperbarui berdasarkan hasil yang benar-benar diperoleh ketika aplikasi dijalankan.

## 10. Pengembang

Proyek ini dikembangkan sebagai penerapan materi algoritma dan pemrograman Python dalam pembuatan media pembelajaran matematika berbasis visualisasi interaktif.

## 11. Penutup

EUCLID LAB diharapkan dapat menjadi media pendukung pembelajaran geometri yang menggabungkan konsep matematika, pemrograman, dan teknologi interaktif dalam satu aplikasi.