from . import Database
from .Utils import random_string
import time


def create_first_data():
    penulis = input("Penulis: ")
    judul = input("Judul: ")
    tahun = input("Tahun: ")

    data = Database.TEMPLATE.copy()

    data["pk"] = random_string(6)
    data["date_add"] = time.strftime("%Y-%m-%d-%H-%M-%S%z", time.gmtime())
    data["penulis"] = penulis + Database.TEMPLATE["penulis"][len(penulis) :]
    data["judul"] = penulis + Database.TEMPLATE["judul"][len(judul) :]
    data["tahun"] = tahun

    data_str = f'{data["pk"]}, {data["date_add"]}, {data["judul"]}, {data["penulis"]}, {data["tahun"]}'
    try:
        with open(Database.DB_NAME, "w", encoding="utf-8") as file:
            file.write(data_str)
    except:
        print("Gagal membuat database")


def read():
    try:
        with open(Database.DB_NAME, "r") as file:
            content = file.readlines()
            return content
    except:
        print("Membaca data gagal")
        return False
