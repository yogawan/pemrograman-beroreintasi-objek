class Menu:
    def __init__(self, nama, deskripsi, harga):
        self.nama = nama
        self.deskripsi = deskripsi
        self.harga = harga
    
    def diPesan(self):
        print("\n{} Baru saja memesan {} seharga {} ribu.".format(
            self.nama,
            self.deskripsi,
            self.harga
            )
        )

class Buku:
    def __init__(self, name, judul, pengarang, tahun):
        self.name = name
        self.judul = judul
        self.pengarang = pengarang
        self.tahun = tahun
    
    def diPinjam(self):
        print("\nNama: {}, baru saja meminjam buku dengan keterangan sebagai berikut.\nJudul: {},Pengarang: {},Tahun: {}".format(
            self.name,
            self.judul,
            self.pengarang,
            self.tahun
        ))

    def diKembalikan(self):
        print("\nNama: {}, baru saja mengembalikan buku dengan keterangan sebagai berikut.\nJudul: {},Pengarang: {},Tahun: {}".format(
            self.name,
            self.judul,
            self.pengarang,
            self.tahun
        ))

class Garis:
    def __init__(self, garisX, garisY):
        self.garisX = garisX
        self.garisY = garisY

    def rotasi(self):
        print("Garis X: {} berotasi dengan Garis Y: {}".format(
            self.garisX,
            self.garisY
        ))

    def translasi(self):
        print("Garis X: {} translasi dengan Garis Y: {}".format(
            self.garisX,
            self.garisY
        ))

class Pelajar:
    def __init__(self, noInduk, name, kelas, gender, tempatLahir, tanggalLahir):
        self.noInduk = noInduk
        self.name = name
        self.kelas = kelas
        self.gender = gender
        self.tempatLahir = tempatLahir
        self.tanggalLahir = tanggalLahir
    
    def lulus(self):
        print("{} dinyatakan lulus.".format(
            self.name
        ))

    def naikKelas(self):
        print("{} dinyatakan naik kelas.".format(
            self.name
        ))

    def bayarSPP(self):
        print("{} harus membayar spp.".format(
            self.name
        ))

# Menu = Menu("Yoga", "Amer", 100)
# Menu.diPesan()

# Buku = Buku("Marsha", "Iluminsti", "Jupri", 2019)
# Buku.diPinjam()
# Buku.diKembalikan()

# Garis = Garis(128, 256)
# Garis.rotasi()
# Garis.translasi()

# Pelajar = Pelajar(5220411056, "Yogawan", "Informatika B", "Laki-laki", "Klaten", "29 Januari 2005")
# Pelajar.lulus()
# Pelajar.naikKelas()
# Pelajar.bayarSPP()