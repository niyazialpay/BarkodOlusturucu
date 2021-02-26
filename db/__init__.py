import os
import sqlite3
from db import regex_data

dir_path = os.path.dirname(os.path.realpath(__file__))

db_file = dir_path + "/../system.db"

connection = sqlite3.connect(db_file)
connection.row_factory = sqlite3.Row

db = connection.cursor()

regex = regex_data.regex_data()


def check_db():
    return os.path.exists(db_file)


def insert_kumas(isim, kod):
    db.execute(
        "insert into kumaslar (kumas_adi, kumas_kodu) values ('" + str(regex.string(isim)) + "', '" + str(
            regex.integer(kod)) + "')")
    connection.commit()


def select_kumas(isim=None):
    if isim is None:
        db.execute("select * from kumaslar order by kumas_adi asc")
        result = db.fetchall()
    else:
        db.execute("select * from kumaslar where kumas_adi='" + str(regex.string(isim)) + "'")
        result = db.fetchone()["kumas_kodu"]
    return result


def insert_renk(isim, kodu):
    db.execute(
        "insert into renkler (renk_adi, renk_kodu) values ('" + str(regex.string(isim)) + "', '" + str(
            regex.integer(kodu)) + "')")
    connection.commit()


def select_renk(isim=None):
    if isim is None:
        db.execute("select * from renkler order by renk_adi asc")
        result = db.fetchall()
    else:
        db.execute("select * from renkler where renk_adi='" + str(regex.string(isim)) + "'")
        result = db.fetchone()["renk_kodu"]
    return result


def insert_mevsim(isim, kodu):
    db.execute(
        "insert into mevsimler (mevsim_adi, mevsim_kodu) values ('" + str(regex.string(isim)) + "', '" + str(
            regex.integer(kodu)) + "')")
    connection.commit()


def select_mevsim(isim=None):
    if isim is None:
        db.execute("select * from mevsimler order by mevsim_adi asc")
        result = db.fetchall()
    else:
        db.execute("select * from mevsimler where mevsim_adi='" + str(regex.string(isim)) + "'")
        result = db.fetchone()["mevsim_kodu"]
    return result


def insert_magaza(isim, kodu):
    db.execute(
        "insert into magazalar (magaza_adi, magaza_kodu) values ('" + str(regex.string(isim)) + "', '" + str(
            regex.integer(kodu)) + "')")
    connection.commit()


def select_magaza(isim=None):
    if isim is None:
        db.execute("select * from magazalar order by magaza_adi asc")
        result = db.fetchall()
    else:
        db.execute("select * from magazalar where magaza_adi='" + str(regex.string(isim)) + "'")
        result = db.fetchone()["magaza_kodu"]
    return result


def insert_magaza_urunleri(isim, kodu):
    db.execute(
        "insert into magaza_urunleri (magaza_urun_adi, magaza_urun_kodu) values ('" + str(
            regex.string(isim)) + "', '" + str(
            regex.integer(kodu)) + "')")
    connection.commit()


def select_magaza_urunleri(isim=None):
    if isim is None:
        db.execute("select * from magaza_urunleri order by magaza_urun_adi asc")
        result = db.fetchall()
    else:
        db.execute("select * from magaza_urunleri where magaza_urun_adi='" + str(regex.string(isim)) + "'")
        result = db.fetchone()["magaza_urun_kodu"]
    return result


def delete_kumas(kod):
    db.execute("delete from kumaslar where kumas_kodu='" + str(regex.integer(kod)) + "'")
    connection.commit()


def delete_magaza(kod):
    db.execute("delete from magazalar where magaza_kodu='" + str(regex.integer(kod)) + "'")
    connection.commit()


def delete_magaza_urunleri(kod):
    db.execute("delete from magaza_urunleri where magaza_urun_kodu='" + str(regex.integer(kod)) + "'")
    connection.commit()


def delete_mevsim(kod):
    db.execute("delete from mevsimler where mevsim_kodu='" + str(regex.integer(kod)) + "'")
    connection.commit()


def delete_renk(kod):
    db.execute("delete from renkler where renk_kodu='" + str(regex.integer(kod)) + "'")
    connection.commit()


def insert_barkod(urun_kodu, barkod):
    db.execute(
        "insert into barkod_listesi (urun_kodu, barkod) values ('" + str(
            regex.integer(urun_kodu)) + "', '" + str(
            regex.integer(barkod)) + "')")
    connection.commit()


def select_barkod(kod=None):
    if kod is None:
        query = "select * from barkod_listesi order by urun_kodu desc"
    else:
        query = "select * from barkod_listesi where urun_kodu='" + str(regex.integer(kod)) + "' or barkod='" + str(
            regex.integer(kod)) + "' limit 1"
    db.execute(query)
    result = db.fetchall()
    return result


def delete_barkod(kod):
    db.execute("delete from barkod_listesi where barkod='" + str(regex.integer(kod)) + "'")
    connection.commit()
