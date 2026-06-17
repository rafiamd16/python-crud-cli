from . import Operasi


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
            if len(str(tahun)) > 4 or tahun < 1:
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
