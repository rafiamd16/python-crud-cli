from . import Operasi

DB_NAME = "data.txt"
TEMPLATE = {
    "pk": "XXXXXX",
    "date_add": "yyyy-mm-dd",
    "judul": 255 * " ",
    "penulis": 255 * " ",
    "tahun": "yyyy",
}


def init_console():
    print("Mengecek Database")
    try:
        with open(DB_NAME, "r") as file:
            print("Database Tersedia")
    except FileNotFoundError:
        print("Database tidak tersedia, silakan buat database baru!")
        Operasi.create_first_data()
