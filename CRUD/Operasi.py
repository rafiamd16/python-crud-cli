import time
from .Utils import random_string
from . import Database


def update(no_buku, pk, data_add, penulis, judul, tahun):
    data = Database.TEMPLATE.copy()

    data["pk"] = pk
    data["date_add"] = data_add
    data["penulis"] = penulis + Database.TEMPLATE["penulis"][len(penulis) :]
    data["judul"] = judul + Database.TEMPLATE["judul"][len(penulis) :]
    data["tahun"] = str(tahun)

    data_str = f'{data["pk"]}, {data["date_add"]}, {data["penulis"]}, {data["judul"]}, {data["tahun"]}\n'

    panjang_data = len(data_str)

    try:
        # with open(Database.DB_NAME, "r", encoding="utf-8") as file:
        #     file.seek(panjang_data * (no_buku - 1))
        #     file.write(data_str)
        with open(Database.DB_NAME, "r") as file:
            data_sementara = file.readlines()
            data_sementara[no_buku - 1] = data_str
        with open(Database.DB_NAME, "w") as file:
            file.writelines(data_sementara)
    except:
        print("\nData gagal diupdate")


def create(penulis, judul, tahun):
    data = Database.TEMPLATE.copy()

    data["pk"] = random_string(6)
    data["date_add"] = time.strftime("%Y-%m-%d-%H-%M-%S%z", time.gmtime())
    data["penulis"] = penulis + Database.TEMPLATE["penulis"][len(penulis) :]
    data["judul"] = judul + Database.TEMPLATE["judul"][len(penulis) :]
    data["tahun"] = str(tahun)

    data_str = f'{data["pk"]}, {data["date_add"]}, {data["penulis"]}, {data["judul"]}, {data["tahun"]}\n'

    try:
        with open(Database.DB_NAME, "a", encoding="utf-8") as file:
            file.write(data_str)
    except:
        print("\nData gagal ditambahkan")


def create_first_data():
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

    data = Database.TEMPLATE.copy()

    data["pk"] = random_string(6)
    data["date_add"] = time.strftime("%Y-%m-%d-%H-%M-%S%z", time.gmtime())
    data["penulis"] = penulis + Database.TEMPLATE["penulis"][len(penulis) :]
    data["judul"] = judul + Database.TEMPLATE["judul"][len(penulis) :]
    data["tahun"] = str(tahun)

    data_str = f'{data["pk"]}, {data["date_add"]}, {data["penulis"]}, {data["judul"]}, {data["tahun"]}\n'
    print(data_str)

    try:
        with open(Database.DB_NAME, "w", encoding="utf-8") as file:
            file.write(data_str)
    except:
        print("\nTerjadi Kesalahan")


def read(**kwargs):
    try:
        with open(Database.DB_NAME, "r") as file:
            content = file.readlines()
            jumlah_buku = len(content)

            if "index" in kwargs:
                index_buku = kwargs["index"] - 1
                if index_buku < 0 or index_buku > jumlah_buku:
                    return False
                else:
                    return content[index_buku]
            else:
                return content
    except:
        print("\nMembaca database error")
        return False
