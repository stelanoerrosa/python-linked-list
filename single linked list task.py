class Task:
    def __init__(self, description, priority):
        self.description = description
        self.priority = priority
        self.next = None

class TaskList:
    def __init__(self):
        self.head = None

    def add_task(self, description, priority):
        new_task = Task(description, priority)

        if self.head is None:
            self.head = new_task
        else:
            current_task = self.head
            if new_task.priority < current_task.priority:
                new_task.next = current_task
                self.head = new_task
            else:
                while (current_task.next is not None and
                       new_task.priority >= current_task.next.priority):
                    current_task = current_task.next
                new_task.next = current_task.next
                current_task.next = new_task

    def remove_task(self, description):
        current_task = self.head

        if current_task is not None:
            if current_task.description == description:
                self.head = current_task.next
                return

        while current_task is not None:
            if current_task.description == description:
                break
            prev_task = current_task
            current_task = current_task.next

        if current_task is None:
            return

        prev_task.next = current_task.next

    def print_tasks(self):
        current_task = self.head

        if current_task is None:
            print("Daftar tugas kosong")
        else:
            print("Daftar tugas:")
            while current_task is not None:
                print("Deskripsi: {}, Prioritas: {}".format(current_task.description, current_task.priority))
                current_task = current_task.next

# Contoh penggunaan
task_list = TaskList()

while True:
    print("\nMenu:")
    print("1. Tambahkan tugas")
    print("2. Hapus tugas")
    print("3. Cetak daftar tugas")
    print("4. Keluar")

    choice = input("Pilih menu (1/2/3/4): ")

    if choice == "1":
        description = input("Masukkan deskripsi tugas: ")
        priority = int(input("Masukkan prioritas tugas: "))
        task_list.add_task(description, priority)
        print("Tugas ditambahkan!")

    elif choice == "2":
        description = input("Masukkan deskripsi tugas yang akan dihapus: ")
        task_list.remove_task(description)
        print("Tugas dihapus!")

    elif choice == "3":
        task_list.print_tasks()

    elif choice == "4":
        print("Terima kasih!")
        break

    else:
        print("Pilihan tidak valid. Silakan pilih menu yang tersedia.")
