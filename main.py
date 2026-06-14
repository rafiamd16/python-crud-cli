import os
import CRUD

if __name__ == "__main__":
    sistem_operasi = os.name

    print("SELAMAT DATANG DI PROGRAM")
    print("DATABASE PERPUSTAKAAN")
    print("=" * 25)

    # check database itu ada atau tidak
    CRUD.init_console()

    while True:
        match sistem_operasi:
            case "posix":
                os.system("clear")
            case "nt":
                os.system("cls")

        print("SELAMAT DATANG DI PROGRAM")
        print("DATABASE PERPUSTAKAAN")
        print("=" * 25)

        print("1. Read Data")
        print("2. Create Data")
        print("3. Read Data")
        print("4. Delete Data\n")

        user_option = input("Masukan opsi: ")

        match user_option:
            case "1":
                CRUD.read_console()
            case "2":
                print("Create Data")
            case "3":
                print("Read Data")
            case "4":
                print("Delete Data")
            case _:
                print("Tidak ada opsi")

        is_done = input("Apakah selesai? (y/n): ")
        if is_done == "y" or is_done == "Y":
            break

    print("Program berakhir, terima kasih")
