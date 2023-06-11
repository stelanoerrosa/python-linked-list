class Peserta:
    def __init__(self, nama, peringkat):
        self.nama = nama
        self.peringkat = peringkat
        self.next = None

class TurnamenCatur:
    def __init__(self):
        self.head = None

    def daftar_peserta(self, nama, peringkat):
        peserta_baru = Peserta(nama, peringkat)

        if self.head is None:
            self.head = peserta_baru
        else:
            current_peserta = self.head
            if peserta_baru.peringkat < current_peserta.peringkat:
                peserta_baru.next = current_peserta
                self.head = peserta_baru
            else:
                while (current_peserta.next is not None and
                       peserta_baru.peringkat >= current_peserta.next.peringkat):
                    current_peserta = current_peserta.next
                peserta_baru.next = current_peserta.next
                current_peserta.next = peserta_baru

    def hapus_peserta(self, nama):
        current_peserta = self.head

        if current_peserta is not None and current_peserta.nama == nama:
            self.head = current_peserta.next
            return

        while current_peserta is not None:
            if current_peserta.nama == nama:
                break
            prev_peserta = current_peserta
            current_peserta = current_peserta.next

        if current_peserta is None:
            return

        prev_peserta.next = current_peserta.next

    def cetak_daftar_peserta(self):
        current_peserta = self.head

        if current_peserta is None:
            print("Belum ada peserta terdaftar.")
        else:
            print("Daftar peserta:")
            while current_peserta is not None:
                print("Nama: {}, Peringkat: {}".format(current_peserta.nama, current_peserta.peringkat))
                current_peserta = current_peserta.next

# Contoh penggunaan
turnamen = TurnamenCatur()

while True:
    print("\nMenu:")
    print("1. Daftarkan peserta")
    print("2. Hapus peserta yang kalah")
    print("3. Cetak daftar peserta")
    print("4. Keluar")

    pilihan = input("Pilih menu (1/2/3/4): ")

    if pilihan == "1":
        nama = input("Masukkan nama peserta: ")
        peringkat = int(input("Masukkan peringkat peserta: "))
        turnamen.daftar_peserta(nama, peringkat)
        print("Peserta terdaftar!")

    elif pilihan == "2":
        nama = input("Masukkan nama peserta yang kalah: ")
        turnamen.hapus_peserta(nama)
        print("Peserta dihapus!")

    elif pilihan == "3":
        turnamen.cetak_daftar_peserta()

    elif pilihan == "4":
        print("Terima kasih!")
        break

    else:
        print("Pilihan tidak valid. Silakan pilih menu yang tersedia.")
