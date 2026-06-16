import os
import CRUD

if __name__ == "__main__":
    sistem_operasi = os.name

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

        print("\n" + "=" * 25 + "\n")

        match user_option:
            case "1":
                print("Read Data")
            case "2":
                print("Create Data")
            case "3":
                print("Update Data")
            case "4":
                print("Delete Data")
            case _:
                print("Tidak ada opsi tersebut")

        print("\n" + "=" * 25 + "\n")
        is_done = input("Apakah sudah selesai? (y/n): ")
        if is_done == "y" or is_done == "Y":
            break

    print("Program selesai")
