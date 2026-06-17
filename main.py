import os
import CRUD

if __name__ == "__main__":
    sistem_operasi = os.name
    match sistem_operasi:
        case "nt":
            os.system("cls")
        case "posix":
            os.system("clear")

    print("SELAMAT DATANG DI PROGRAM")
    print("DATABASE PERPUSTAKAAN")
    print("=" * 25)

    # check database itu ada atau tidak
    CRUD.init_console()

    while True:
        match sistem_operasi:
            case "nt":
                os.system("cls")
            case "posix":
                os.system("clear")

        print("SELAMAT DATANG DI PROGRAM")
        print("DATABASE PERPUSTAKAAN")
        print("=" * 25)

        print("1. Read Data")
        print("2. Create Data")
        print("3. Update Data")
        print("4. Delete Data\n")

        user_option = input("Masukan opsi: ")

        match user_option:
            case "1":
                CRUD.read_console()
            case "2":
                CRUD.create_console()
            case "3":
                print("Update Data")
            case "4":
                print("Delete Data")
            case _:
                print("Tidak ada opsi tersebut")

        is_done = input("Apakah sudah selesai? (y/n): ")
        if is_done == "y" or is_done == "Y":
            break

    print("Program selesai")
