class Buku:
    def __init__(self, judul):
        self.judul = judul
        self.next = None

class Pengunjung:
    def __init__(self, nama):
        self.nama = nama
        self.buku = None

    def pinjam_buku(self, judul):
        buku_baru = Buku(judul)
        if self.buku is None:
            self.buku = buku_baru
        else:
            buku_sekarang = self.buku
            while buku_sekarang.next is not None:
                buku_sekarang = buku_sekarang.next
            buku_sekarang.next = buku_baru

    def cetak_buku_dipinjam(self):
        if self.buku is None:
            print("{} belum meminjam buku apapun.".format(self.nama))
        else:
            print("{} telah meminjam buku berikut:".format(self.nama))
            buku_sekarang = self.buku
            while buku_sekarang is not None:
                print(buku_sekarang.judul)
                buku_sekarang = buku_sekarang.next

# Contoh penggunaan
pengunjung = {}

while True:
    print("\nMenu:")
    print("1. Catat peminjaman buku")
    print("2. Cetak daftar buku yang dipinjam oleh pengunjung")
    print("3. Keluar")

    pilihan = input("Pilih menu (1/2/3): ")

    if pilihan == "1":
        nama = input("Masukkan nama pengunjung: ")
        judul = input("Masukkan judul buku yang dipinjam: ")

        if nama in pengunjung:
            pengunjung_ini = pengunjung[nama]
        else:
            pengunjung_ini = Pengunjung(nama)
            pengunjung[nama] = pengunjung_ini

        pengunjung_ini.pinjam_buku(judul)
        print("Peminjaman buku dicatat!")

    elif pilihan == "2":
        nama = input("Masukkan nama pengunjung: ")
        if nama in pengunjung:
            pengunjung_ini = pengunjung[nama]
            pengunjung_ini.cetak_buku_dipinjam()
        else:
            print("Pengunjung dengan nama tersebut tidak ditemukan.")

    elif pilihan == "3":
        print("Terima kasih!")
        break

    else:
        print("Pilihan tidak valid. Silakan pilih menu yang tersedia.")
