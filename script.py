# Definisi kelas Mahasiswa
class Mahasiswa:
    # Konstruktor kelas untuk inisialisasi objek
    def _init_(self, nama, nim, jurusan):
        self.nama = nama
        self.nim = nim
        self.jurusan = jurusan

    # Metode untuk menampilkan aktivitas belajar
    def belajar(self):
        print(f"{self.nama} sedang belajar.")

# Implementasi penggunaan kelas Mahasiswa
mahasiswa1 = Mahasiswa("Fajar Dwi", "123456789", "Informatika")
mahasiswa2 = Mahasiswa("Fajar Dwi", "654313444", "Sistem Informasi")

# Menggunakan metode objek
mahasiswa1.belajar()  # Output: Arya sedang belajar.
mahasiswa2.belajar()  # Output: Arya2 sedang belajar.
