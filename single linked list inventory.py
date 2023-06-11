class Produk:
    def __init__(self, nama, kode, stok):
        self.nama = nama
        self.kode = kode
        self.stok = stok
        self.next = None

class ManajemenInventaris:
    def __init__(self):
        self.head = None

    def tambah_produk(self, nama, kode, stok):
        produk_baru = Produk(nama, kode, stok)

        if self.head is None:
            self.head = produk_baru
        else:
            current_produk = self.head
            if produk_baru.kode < current_produk.kode:
                produk_baru.next = current_produk
                self.head = produk_baru
            else:
                while (current_produk.next is not None and
                       produk_baru.kode >= current_produk.next.kode):
                    current_produk = current_produk.next
                produk_baru.next = current_produk.next
                current_produk.next = produk_baru

    def hapus_produk(self, kode):
        current_produk = self.head

        if current_produk is not None and current_produk.kode == kode:
            self.head = current_produk.next
            return

        while current_produk is not None:
            if current_produk.kode == kode:
                break
            prev_produk = current_produk
            current_produk = current_produk.next

        if current_produk is None:
            return

        prev_produk.next = current_produk.next

    def cetak_daftar_produk(self):
        current_produk = self.head

        if current_produk is None:
            print("Inventaris kosong.")
        else:
            print("Daftar produk dalam inventaris:")
            while current_produk is not None:
                print("Nama: {}, Kode: {}, Stok: {}".format(current_produk.nama, current_produk.kode, current_produk.stok))
                current_produk = current_produk.next

# Contoh penggunaan
inventaris = ManajemenInventaris()

while True:
    print("\nMenu:")
    print("1. Tambahkan produk ke inventaris")
    print("2. Hapus produk dari inventaris")
    print("3. Cetak daftar produk di inventaris")
    print("4. Keluar")

    pilihan = input("Pilih menu (1/2/3/4): ")

    if pilihan == "1":
        nama = input("Masukkan nama produk: ")
        kode = input("Masukkan kode produk: ")
        stok = int(input("Masukkan jumlah stok produk: "))
        inventaris.tambah_produk(nama, kode, stok)
        print("Produk ditambahkan ke inventaris!")

    elif pilihan == "2":
        kode = input("Masukkan kode produk yang akan dihapus: ")
        inventaris.hapus_produk(kode)
        print("Produk dihapus dari inventaris!")

    elif pilihan == "3":
        inventaris.cetak_daftar_produk()

    elif pilihan == "4":
        print("Terima kasih!")
        break

    else:
        print("Pilihan tidak valid. Silakan pilih menu yang tersedia.")
