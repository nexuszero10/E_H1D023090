import numpy as np 

def add_book(book_list: list, title: str, year: int) -> list:
    book = {"title": title, "year": year}
    book_list.append(book)
    print(f"Buku '{title} ({year})' berhasil ditambahkan")
    return book_list

def view_all_books(book_list: list):
    print(f"Menampilkan semua buku: ")
    for i in range(len(book_list)):
        print(f"{i+1}. {book_list[i]['title']} ({book_list[i]['year']})")

def view_books(book_list: list, count: int): 
    if len(book_list) == 0:
        print("Daftar buku masih kosong!")
    else:
        count = min(count, len(book_list)) 
        print(f"Menampilkan {count} buku pertama: ")
        for i in range(count):
            print(f"{i+1}. {book_list[i]['title']} ({book_list[i]['year']})")

def update_book(book_list: list, index: int, new_title=None, new_year=None) -> list:
    if 0 <= index < len(book_list):
        if new_title is not None and new_title != "":
            book_list[index]['title'] = new_title
        if new_year is not None and new_year != "":
            book_list[index]['year'] = new_year
        print(f"Buku ke-{index+1} berhasil diperbaharui")
    else:
        print('Index tidak valid')
    return book_list

def delete_book(book_list: list, index: int) -> list:
    if len(book_list) == 0:
        print("Tidak ada buku yang bisa dihapus")
    elif 0 <= index < len(book_list):
        removed_book = book_list.pop(index)
        print(f"Buku '{removed_book['title']} ({removed_book['year']})' berhasil dihapus!")
    else:
        print("Index tidak valid!")
    return book_list

import numpy as np 

def view_books_by_year(book_list) -> list:
    if len(book_list) == 0:
        print("Daftar buku kosong!")
    else:
        book_array = np.array(book_list)
        sorted_indices = np.argsort([book['year'] for book in book_list])
        sorted_books = book_array[sorted_indices]
        print("\nBuku-buku setelah diurutkan berdasarkan tahun terbit:")
        for i, book in enumerate(sorted_books):
            print(f"{i+1}. {book['title']} ({book['year']})")
    
    return book_list


def main():
    book_list = [] 
    while True:
        print("\n=== Daftar Buku ===")
        print("1. Tambah Buku")
        print("2. Lihat Buku")
        print("3. Update Buku")
        print("4. Hapus Buku")
        print("5. Lihat Buku Berdasarkan Jumlah")
        print("6. Lihat Buku Berdasarkan Tahun")
        print("7. Keluar")
        choice = input("Pilih menu: ")

        if choice == "1":
            title = str(input("Masukkan judul buku: "))
            year = int(input("Masukkan tahun terbit: "))
            book_list = add_book(book_list, title, year)
        elif choice == "2":
            view_all_books(book_list)
        elif choice == "3":
            index = int(input("Pilih nomor buku yang ingin diperbaharui: ")) - 1 
            new_title = input("Masukkan judul baru (kosongkan jika tidak ingin mengubah): ")
            new_year = input("Masukkan tahun terbit baru (kosongkan jika tidak ingin mengubah): ")
            new_title = new_title if new_title else None
            new_year = new_year if new_year else None
            book_list = update_book(book_list, index, new_title, new_year)
        elif choice == "4":
            index = int(input("Pilih nomor buku yang ingin dihapus: ")) - 1
            book_list = delete_book(book_list, index)
        elif choice == "5":
            count = int(input("Berapa buku yang ingin ditampilkan: "))
            view_books(book_list, count)
        elif choice == "6":
            book_list = view_books_by_year(book_list)
        elif choice == "7":
            print("Keluar dari program")
            break
        else: 
            print("Pilihan tidak valid")

main()
