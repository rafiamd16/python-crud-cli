from . import Operasi


def delete_console():
    read_console()

    while True:
        print("Silakan pilih nomor buku yang akan didelete!")
        no_buku = int(input("Nomor Buku: "))
        data_buku = Operasi.read(index=no_buku)

        if data_buku:
            data_break = str(data_buku).split(",")
            pk = data_break[0]
            data_add = data_break[1]
            penulis = data_break[2]
            judul = data_break[3]
            tahun = data_break[4][:-1]

            # data yang ingin diupdate
            print("\n" + "=" * 100)
            print("data yang ingin anda delete!")
            print(f"1. Judul\t: {judul:.40}")
            print(f"2. Penulis\t: {penulis:.40}")
            print(f"3. Tahun\t: {tahun:4}")
            is_done = input("\nApakah anda yakin untuk menghapus data ini? (y/n): ")
            if is_done == "y" or is_done == "Y":
                Operasi.delete(no_buku)
                break
        else:
            print("\nNomor buku tidak valid, silakan masukan ulang!")

    print("\nData berhasil dihapus!")


def update_console():
    read_console()

    while True:
        print("Silakan pilih nomor buku yang akan diupdate!")
        no_buku = int(input("Nomor Buku: "))
        data_buku = Operasi.read(index=no_buku)

        data_break = str(data_buku).split(",")
        pk = data_break[0]
        data_add = data_break[1]
        penulis = data_break[2]
        judul = data_break[3]
        tahun = data_break[4][:-1]

        if data_buku:
            break
        else:
            print("\nNomor buku tidak valid, silakan masukan ulang!")

    while True:
        # data yang ingin diupdate
        print("\n" + "=" * 100)
        print("Silakan pilih data yang ingin diupdate!")
        print(f"1. Judul\t: {judul:.40}")
        print(f"2. Penulis\t: {penulis:.40}")
        print(f"3. Tahun\t: {tahun:4}")

        # memilih mode untuk diupdate
        user_option = input("Pilih data (1/2/3): ")
        print("\n" + "=" * 100)

        match user_option:
            case "1":
                while True:
                    judul = input("Judul\t: ").strip()
                    if len(judul) < 3:
                        print("\nJudul minimal 3 karakter, silakan masukan ulang!")
                        continue
                    break
            case "2":
                while True:
                    penulis = input("Penulis\t: ").strip()
                    if len(penulis) < 3:
                        print("\nPenulis minimal 3 karakter, silakan masukan ulang!")
                        continue
                    elif any(char.isdigit() for char in penulis):
                        print(
                            "\nPenulis tidak boleh mengandung angka, silakan masukan ulang!"
                        )
                        continue
                    break
            case "3":
                while True:
                    try:
                        tahun = int(input("Tahun\t: "))
                        if len(str(tahun)) != 4 or tahun < 1:
                            print("\nTahun tidak valid, silakan masukan ulang!")
                            continue
                        break
                    except ValueError:
                        print(
                            "\nInput tidak valid, tahun harus berupa angka, silakan masukan ulang!"
                        )
            case _:
                print("\nInput tidak valid, silakan masukan ulang!")

        print("Data baru anda")
        print(f"1. Judul\t: {judul:.40}")
        print(f"2. Penulis\t: {penulis:.40}")
        print(f"3. Tahun\t: {tahun:4}")
        is_done = input("\nApakah data sudah sesuai? (y/n): ")
        if is_done == "y" or is_done == "Y":
            break
    Operasi.update(no_buku, pk, data_add, penulis, judul, tahun)


def create_console():

    print("\n\n" + "=" * 100)
    print("Silakan tambah data buku\n")

    while True:
        penulis = input("Penulis\t: ").strip()
        if len(penulis) < 3:
            print("\nPenulis minimal 3 karakter, silakan masukan ulang!")
            continue
        elif any(char.isdigit() for char in penulis):
            print("\nPenulis tidak boleh mengandung angka, silakan masukan ulang!")
            continue
        break

    while True:
        judul = input("Judul\t: ").strip()
        if len(judul) < 3:
            print("\nJudul minimal 3 karakter, silakan masukan ulang!")
            continue
        break

    while True:
        try:
            tahun = int(input("Tahun\t: "))
            if len(str(tahun)) != 4 or tahun < 1:
                print("\nTahun tidak valid, silakan masukan ulang!")
                continue
            break
        except ValueError:
            print(
                "\nInput tidak valid, tahun harus berupa angka, silakan masukan ulang!"
            )

    Operasi.create(penulis, judul, tahun)
    print("\nBerikut adalah data baru anda:")
    read_console()


def read_console():
    data_file = Operasi.read()
    index = "No."
    judul = "Judul"
    penulis = "Penulis"
    tahun = "Tahun"

    # Header
    print("\n" + "=" * 100)
    print(f"{index:4} | {judul:40} | {penulis:40} | {tahun:5}")
    print("-" * 100)

    # Data
    for index, data in enumerate(data_file):  # type: ignore
        data_break = data.split(",")
        pk = data_break[0]
        date_add = data_break[1]
        penulis = data_break[2]
        judul = data_break[3]
        tahun = data_break[4]
        print(f"{index+1:4} | {judul:.40} | {penulis:.40} | {tahun:4}", end="")

    # Footer
    print("=" * 100 + "\n")
