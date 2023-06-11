class Item:
    def __init__(self, nama, kepentingan):
        self.nama = nama
        self.kepentingan = kepentingan
        self.next = None

class Tas:
    def __init__(self):
        self.head = None

    def tambahkan_item(self, nama, kepentingan):
        item_baru = Item(nama, kepentingan)

        if self.head is None:
            self.head = item_baru
        else:
            current_item = self.head
            if item_baru.kepentingan > current_item.kepentingan:
                item_baru.next = current_item
                self.head = item_baru
            else:
                while (current_item.next is not None and
                       item_baru.kepentingan <= current_item.next.kepentingan):
                    current_item = current_item.next
                item_baru.next = current_item.next
                current_item.next = item_baru

    def hapus_item(self, nama):
        current_item = self.head

        if current_item is not None:
            if current_item.nama == nama:
                self.head = current_item.next
                return

        while current_item is not None:
            if current_item.nama == nama:
                break
            prev_item = current_item
            current_item = current_item.next

        if current_item is None:
            return

        prev_item.next = current_item.next

    def cetak_daftar_item(self):
        current_item = self.head

        if current_item is None:
            print("Tas kosong")
        else:
            print("Daftar item dalam tas:")
            while current_item is not None:
                print("Nama: {}, Kepentingan: {}".format(current_item.nama, current_item.kepentingan))
                current_item = current_item.next

# Contoh penggunaan
tas = Tas()

while True:
    print("\nMenu:")
    print("1. Tambahkan item ke dalam tas")
    print("2. Hapus item dari tas")
    print("3. Cetak daftar item dalam tas")
    print("4. Keluar")

    pilihan = input("Pilih menu (1/2/3/4): ")

    if pilihan == "1":
        nama = input("Masukkan nama item: ")
        kepentingan = int(input("Masukkan tingkat kepentingan item: "))
        tas.tambahkan_item(nama, kepentingan)
        print("Item ditambahkan ke dalam tas!")

    elif pilihan == "2":
        nama = input("Masukkan nama item yang akan dihapus: ")
        tas.hapus_item(nama)
        print("Item dihapus dari tas!")

    elif pilihan == "3":
        tas.cetak_daftar_item()

    elif pilihan == "4":
        print("Terima kasih!")
        break

    else:
        print("Pilihan tidak valid. Silakan pilih menu yang tersedia.")
