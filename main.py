import sys
from PyQt5 import QtWidgets, uic, QtCore, QtGui
from PyQt5.QtGui import QCursor, QIcon
from PyQt5.QtWidgets import QMessageBox, QMenu
import db
import details


class Ui(QtWidgets.QMainWindow):

    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi("Templates/main.ui", self)

        self.message = QMessageBox()
        self.icon = QtGui.QIcon()
        self.icon.addPixmap(QtGui.QPixmap("Templates/img/logo.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)

        self.delete_icon = QtGui.QIcon('Templates/img/delete.png')

        self.menu = QtWidgets.QMenu()
        self.delete_column_action = self.menu.addAction("Kaydı Sil")
        self.delete_column_action.setIcon(self.delete_icon)

        self.updateList()

        self.pushButtonRenkEkle.clicked.connect(self.renkEkle)
        self.txtRenkKodu.returnPressed.connect(self.renkEkle)
        self.txtRenkAdi.returnPressed.connect(self.renkEkle)

        self.pushButtonKumasEkle.clicked.connect(self.kumasEkle)
        self.txtKumaAdi.returnPressed.connect(self.kumasEkle)
        self.txtKumasKodu.returnPressed.connect(self.kumasEkle)

        self.pushButtonMevsimEkle.clicked.connect(self.mevsimEkle)
        self.txtMevsimAdi.returnPressed.connect(self.mevsimEkle)
        self.txtMevsimKodu.returnPressed.connect(self.mevsimEkle)

        self.pushButtonMagazaEkle.clicked.connect(self.magazaEkle)
        self.txtMagazaAdi.returnPressed.connect(self.magazaEkle)
        self.txtMagazaKodu.returnPressed.connect(self.magazaEkle)

        self.pushButtonMagazaUrunEkle.clicked.connect(self.magazaUrunEkle)
        self.txtMagazaUrunAdi.returnPressed.connect(self.magazaUrunEkle)
        self.txtMagazaUrunKodu.returnPressed.connect(self.magazaUrunEkle)

        self.pushButtonBedenEkle.clicked.connect(self.bedenEkle)
        self.txtBedenAd.returnPressed.connect(self.bedenEkle)
        self.txtBedenKodu.returnPressed.connect(self.bedenEkle)

        self.tableWidgetRenkler.customContextMenuRequested.connect(self.customContextMenuRenkler)

        self.tableWidgetKumaslar.customContextMenuRequested.connect(self.customContextMenuKumaslar)

        self.tableWidgetMevsimler.customContextMenuRequested.connect(self.customContextMenuMevsimler)

        self.tableWidgetMagazalar.customContextMenuRequested.connect(self.customContextMenuMagaza)

        self.tableWidgetMagazaUrunleri.customContextMenuRequested.connect(self.customContextMenuMagazaUrunleri)

        self.tableWidgetBedenler.customContextMenuRequested.connect(self.customContextMenuBedenListesi)

        self.tableWidgetBarkodListesi.customContextMenuRequested.connect(self.customContextMenuBarkodListesi)

        self.pushButtonOlustur.clicked.connect(self.BarkodOlustur)
        self.pushButtonBarkodAra.clicked.connect(self.BarkodAra)

        self.tableWidgetBarkodListesi.doubleClicked.connect(self.BarkodDetaylari)

        self.txtBarkodUrunKodu.returnPressed.connect(self.BarkodAra)

        self.show()

    def messageBox(self, mesaj):
        self.message.setIcon(QMessageBox.Warning)
        self.message.setText(mesaj)
        self.message.setWindowTitle("Uyarı")
        self.message.setStandardButtons(QMessageBox.Ok)
        self.message.setWindowIcon(self.icon)
        self.message.exec()

    def renkEkle(self):
        if len(self.txtRenkAdi.text()) == 0 \
                or len(self.txtRenkKodu.text()) == 0:
            self.messageBox("Tüm alanların dolu olması gerekmektedir!")
        else:
            try:
                db.insert_renk(self.txtRenkAdi.text(), self.txtRenkKodu.text())
            except:
                self.messageBox("Aynı kayıt iki kere girilememektedir!")
            self.RenkListesi()
            self.txtRenkAdi.clear()
            self.txtRenkKodu.clear()

    def mevsimEkle(self):
        if len(self.txtMevsimAdi.text()) == 0 \
                or len(self.txtMevsimKodu.text()) == 0:
            self.messageBox("Tüm alanların dolu olması gerekmektedir!")
        else:
            try:
                db.insert_mevsim(self.txtMevsimAdi.text(), self.txtMevsimKodu.text())
            except:
                self.messageBox('Aynı kayıt iki kere girilememektedir!')
            self.MevsimListesi()
            self.txtMevsimAdi.clear()
            self.txtMevsimKodu.clear()

    def kumasEkle(self):
        if len(self.txtKumaAdi.text()) == 0 \
                or len(self.txtKumasKodu.text()) == 0:
            self.messageBox("Tüm alanların dolu olması gerekmektedir!")
        else:
            try:
                db.insert_kumas(self.txtKumaAdi.text(), self.txtKumasKodu.text())
            except:
                self.messageBox('Aynı kayıt iki kere girilememektedir!')
            self.KumasListesi()
            self.txtKumaAdi.clear()
            self.txtKumasKodu.clear()

    def magazaEkle(self):
        if len(self.txtMagazaAdi.text()) == 0 \
                or len(self.txtMagazaKodu.text()) == 0:
            self.messageBox("Tüm alanların dolu olması gerekmektedir!")
        else:
            try:
                db.insert_magaza(self.txtMagazaAdi.text(), self.txtMagazaKodu.text())
            except:
                self.messageBox('Aynı kayıt iki kere girilememektedir!')
            self.MagazaListesi()
            self.txtMagazaAdi.clear()
            self.txtMagazaKodu.clear()

    def magazaUrunEkle(self):
        if len(self.txtMagazaUrunAdi.text()) == 0 \
                or len(self.txtMagazaUrunKodu.text()) == 0:
            self.messageBox("Tüm alanların dolu olması gerekmektedir!")
        else:
            try:
                db.insert_magaza_urunleri(self.txtMagazaUrunAdi.text(), self.txtMagazaUrunKodu.text())
            except:
                self.messageBox('Aynı kayıt iki kere girilememektedir!')
            self.MagazaUrunListesi()
            self.txtMagazaUrunAdi.clear()
            self.txtMagazaUrunKodu.clear()

    def bedenEkle(self):
        if len(self.txtBedenAd.text()) == 0 \
                or len(self.txtBedenKodu.text()) == 0:
            self.messageBox("Tüm alanların dolu olması gerekmektedir!")
        else:
            try:
                db.insert_beden(self.txtBedenAd.text(), self.txtBedenKodu.text())
            except:
                self.messageBox('Aynı kayıt iki kere girilememektedir!')
            self.BedenListesi()
            self.txtBedenAd.clear()
            self.txtBedenKodu.clear()

    def updateList(self):
        self.RenkListesi()
        self.KumasListesi()
        self.MevsimListesi()
        self.MagazaListesi()
        self.MagazaUrunListesi()
        self.BedenListesi()
        self.BarkodListesi()

    def RenkListesi(self):
        renkler = db.select_renk()
        self.comboBoxRenk.clear()
        self.comboBoxRenk.addItem("")
        self.tableWidgetRenkler.setRowCount(0)
        for row_number, row_data in enumerate(renkler):
            self.tableWidgetRenkler.insertRow(row_number)
            self.tableWidgetRenkler.setItem(row_number, 0, QtWidgets.QTableWidgetItem(str(row_data["renk_adi"])))
            self.tableWidgetRenkler.setItem(row_number, 1, QtWidgets.QTableWidgetItem(str(row_data["renk_kodu"])))

            self.comboBoxRenk.addItem(str(row_data["renk_adi"]))

    def KumasListesi(self):
        kumaslar = db.select_kumas()
        self.comboBoxKumas.clear()
        self.comboBoxKumas.addItem("")
        self.tableWidgetKumaslar.setRowCount(0)
        for row_number, row_data in enumerate(kumaslar):
            self.tableWidgetKumaslar.insertRow(row_number)
            self.tableWidgetKumaslar.setItem(row_number, 0, QtWidgets.QTableWidgetItem(str(row_data["kumas_adi"])))
            self.tableWidgetKumaslar.setItem(row_number, 1, QtWidgets.QTableWidgetItem(str(row_data["kumas_kodu"])))

            self.comboBoxKumas.addItem(str(row_data["kumas_adi"]))

    def MevsimListesi(self):
        mevsimler = db.select_mevsim()
        self.comboBoxMevsim.clear()
        self.comboBoxMevsim.addItem("")
        self.tableWidgetMevsimler.setRowCount(0)
        for row_number, row_data in enumerate(mevsimler):
            self.tableWidgetMevsimler.insertRow(row_number)
            self.tableWidgetMevsimler.setItem(row_number, 0, QtWidgets.QTableWidgetItem(str(row_data["mevsim_adi"])))
            self.tableWidgetMevsimler.setItem(row_number, 1, QtWidgets.QTableWidgetItem(str(row_data["mevsim_kodu"])))

            self.comboBoxMevsim.addItem(str(row_data["mevsim_adi"]))

    def MagazaListesi(self):
        magazalar = db.select_magaza()
        self.comboBoxMagaza.clear()
        self.comboBoxMagaza.addItem("")
        self.tableWidgetMagazalar.setRowCount(0)
        for row_number, row_data in enumerate(magazalar):
            self.tableWidgetMagazalar.insertRow(row_number)
            self.tableWidgetMagazalar.setItem(row_number, 0, QtWidgets.QTableWidgetItem(str(row_data["magaza_adi"])))
            self.tableWidgetMagazalar.setItem(row_number, 1, QtWidgets.QTableWidgetItem(str(row_data["magaza_kodu"])))

            self.comboBoxMagaza.addItem(str(row_data["magaza_adi"]))

    def MagazaUrunListesi(self):
        magaza_urunleri = db.select_magaza_urunleri()
        self.comboBoxMagazaUrun.clear()
        self.comboBoxMagazaUrun.addItem("")
        self.tableWidgetMagazaUrunleri.setRowCount(0)
        for row_number, row_data in enumerate(magaza_urunleri):
            self.tableWidgetMagazaUrunleri.insertRow(row_number)
            self.tableWidgetMagazaUrunleri.setItem(row_number, 0,
                                                   QtWidgets.QTableWidgetItem(str(row_data["magaza_urun_adi"])))
            self.tableWidgetMagazaUrunleri.setItem(row_number, 1,
                                                   QtWidgets.QTableWidgetItem(str(row_data["magaza_urun_kodu"])))

            self.comboBoxMagazaUrun.addItem(str(row_data["magaza_urun_adi"]))

    def BedenListesi(self):
        bedenler = db.select_beden()
        self.comboBoxBeden.clear()
        self.comboBoxBeden.addItem("")
        self.tableWidgetBedenler.setRowCount(0)
        for row_number, row_data in enumerate(bedenler):
            self.tableWidgetBedenler.insertRow(row_number)
            self.tableWidgetBedenler.setItem(row_number, 0, QtWidgets.QTableWidgetItem(str(row_data["beden_adi"])))
            self.tableWidgetBedenler.setItem(row_number, 1, QtWidgets.QTableWidgetItem(str(row_data["beden_kodu"])))

            self.comboBoxBeden.addItem(str(row_data["beden_adi"]))

    def BarkodListesi(self, kod=None):
        barkodlar = db.select_barkod(kod)
        self.tableWidgetBarkodListesi.setRowCount(0)
        for row_number, row_data in enumerate(barkodlar):
            self.tableWidgetBarkodListesi.insertRow(row_number)
            self.tableWidgetBarkodListesi.setItem(row_number, 0,
                                                  QtWidgets.QTableWidgetItem(row_data["urun_adi"]))
            self.tableWidgetBarkodListesi.setItem(row_number, 1,
                                                  QtWidgets.QTableWidgetItem(str(row_data["urun_kodu"])))
            self.tableWidgetBarkodListesi.setItem(row_number, 2,
                                                  QtWidgets.QTableWidgetItem(str(row_data["barkod"])))

    def KodGetir(self, isim=None, kod_turu=None):
        if len(isim) > 0:
            if kod_turu == "kumas":
                return db.select_kumas(isim)
            elif kod_turu == "renk":
                return db.select_renk(isim)
            elif kod_turu == "magaza":
                return db.select_magaza(isim)
            elif kod_turu == "magaza_urun":
                return db.select_magaza_urunleri(isim)
            elif kod_turu == "mevsim":
                return db.select_mevsim(isim)
            elif kod_turu == "beden":
                return db.select_beden(isim)
            else:
                return ""
        else:
            return ""

    def BarkodOlustur(self):
        if len(self.txtUrunKodu.text()) == 0:
            self.messageBox('Ürün kodu girmeniz gerekmektedir!')
        else:
            barkod = self.txtTarih.text() + self.KodGetir(self.comboBoxMevsim.currentText(),
                                                          'mevsim') + self.txtUrunKodu.text() + self.KodGetir(
                self.comboBoxMagaza.currentText(), 'magaza') + self.KodGetir(self.comboBoxMagazaUrun.currentText(),
                                                                             'magaza_urun') + self.KodGetir(
                self.comboBoxBeden.currentText(), 'beden') + self.KodGetir(
                self.comboBoxRenk.currentText(), 'renk') + self.KodGetir(self.comboBoxKumas.currentText(), 'kumas')

            db.insert_barkod(
                urun_adi=self.txtUrunAdi.text(),
                urun_kodu=self.txtUrunKodu.text(),
                barkod=barkod,
                tarih=self.txtTarih.text(),
                mevsim=self.comboBoxMevsim.currentText(),
                magaza=self.comboBoxMagaza.currentText(),
                magaza_urun=self.comboBoxMagazaUrun.currentText(),
                renk=self.comboBoxRenk.currentText(),
                beden=self.comboBoxBeden.currentText(),
                kumas=self.comboBoxKumas.currentText()
            )
            self.BarkodListesi()

            self.txtBarkod.setText(barkod)

    def BarkodAra(self):
        if len(self.txtBarkodUrunKodu.text()) > 0:
            kod = self.txtBarkodUrunKodu.text()
        else:
            kod = None
        self.BarkodListesi(kod)

    def BarkodDetaylari(self):
        w = details.detailsDialog()
        barkod = \
        db.select_barkod(self.tableWidgetBarkodListesi.item(self.tableWidgetBarkodListesi.currentRow(), 2).text())[0]
        w.setWindowTitle(str(barkod["urun_adi"]) + " - " + barkod["barkod"])
        w.lineEditTarih.setText(barkod["tarih"])
        w.lineEditUrunKodu.setText(barkod["urun_kodu"])
        w.lineEditBeden.setText(barkod["beden"])
        w.lineEditMevsim.setText(barkod["mevsim"])
        w.lineEditRenk.setText(barkod["renk"])
        w.lineEditKumasTuru.setText(barkod["kumas"])
        w.lineEditMagazaKodu.setText(barkod["magaza"])
        w.lineEditMagazaUrunKodu.setText(barkod["magaza_urun"])
        w.lineEditUrunAdi.setText(barkod["urun_adi"])
        w.exec_()

    def MessageBoxButon(self, item):
        self.message.setIcon(QMessageBox.Warning)
        self.message.setText("'" + item + "' öğesini silmek istediğinize emin misiniz?")
        self.message.setWindowTitle("Uyarı")
        self.message.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        self.message.setWindowIcon(self.icon)

    def customContextMenuRenkler(self, pos):
        try:
            action = self.menu.exec_(self.tableWidgetRenkler.viewport().mapToGlobal(pos))
            if action == self.delete_column_action:
                self.MessageBoxButon(self.tableWidgetRenkler.item(self.tableWidgetRenkler.currentRow(), 0).text())
                button = self.message.exec()
                if button == QMessageBox.Ok:
                    db.delete_renk(self.tableWidgetRenkler.item(self.tableWidgetRenkler.currentRow(), 1).text())
                    self.RenkListesi()
        except:
            self.messageBox('Geçerli bir satır seçmelisiniz!')

    def customContextMenuKumaslar(self, pos):
        try:
            action = self.menu.exec_(self.tableWidgetKumaslar.viewport().mapToGlobal(pos))
            if action == self.delete_column_action:
                self.MessageBoxButon(self.tableWidgetKumaslar.item(self.tableWidgetKumaslar.currentRow(), 0).text())
                button = self.message.exec()
                if button == QMessageBox.Ok:
                    db.delete_kumas(self.tableWidgetKumaslar.item(self.tableWidgetKumaslar.currentRow(), 1).text())
                    self.KumasListesi()
        except:
            self.messageBox('Geçerli bir satır seçmelisiniz!')

    def customContextMenuMevsimler(self, pos):
        try:
            action = self.menu.exec_(self.tableWidgetMevsimler.viewport().mapToGlobal(pos))
            if action == self.delete_column_action:
                self.MessageBoxButon(self.tableWidgetMevsimler.item(self.tableWidgetMevsimler.currentRow(), 0).text())
                button = self.message.exec()
                if button == QMessageBox.Ok:
                    db.delete_mevsim(self.tableWidgetMevsimler.item(self.tableWidgetMevsimler.currentRow(), 1).text())
                    self.MevsimListesi()
        except:
            self.messageBox('Geçerli bir satır seçmelisiniz!')

    def customContextMenuMagaza(self, pos):
        try:
            action = self.menu.exec_(self.tableWidgetMagazalar.viewport().mapToGlobal(pos))
            if action == self.delete_column_action:
                self.MessageBoxButon(self.tableWidgetMagazalar.item(self.tableWidgetMagazalar.currentRow(), 0).text())
                button = self.message.exec()
                if button == QMessageBox.Ok:
                    db.delete_magaza(self.tableWidgetMagazalar.item(self.tableWidgetMagazalar.currentRow(), 1).text())
                    self.MagazaListesi()
        except:
            self.messageBox('Geçerli bir satır seçmelisiniz!')

    def customContextMenuMagazaUrunleri(self, pos):
        try:
            action = self.menu.exec_(self.tableWidgetMagazaUrunleri.viewport().mapToGlobal(pos))
            if action == self.delete_column_action:
                self.MessageBoxButon(
                    self.tableWidgetMagazaUrunleri.item(self.tableWidgetMagazaUrunleri.currentRow(), 0).text())
                button = self.message.exec()
                if button == QMessageBox.Ok:
                    db.delete_magaza_urunleri(
                        self.tableWidgetMagazaUrunleri.item(self.tableWidgetMagazaUrunleri.currentRow(), 1).text())
                    self.MagazaUrunListesi()
        except:
            self.messageBox('Geçerli bir satır seçmelisiniz!')

    def customContextMenuBarkodListesi(self, pos):
        try:
            action = self.menu.exec_(self.tableWidgetBarkodListesi.viewport().mapToGlobal(pos))
            if action == self.delete_column_action:
                self.MessageBoxButon(self.tableWidgetBarkodListesi.item(self.tableWidgetBarkodListesi.currentRow(),
                                                                        0).text() + ' - ' + self.tableWidgetBarkodListesi.item(
                    self.tableWidgetBarkodListesi.currentRow(), 1).text())
                button = self.message.exec()
                if button == QMessageBox.Ok:
                    db.delete_barkod(
                        self.tableWidgetBarkodListesi.item(self.tableWidgetBarkodListesi.currentRow(), 2).text())
                    self.BarkodListesi()
        except:
            self.messageBox('Geçerli bir satır seçmelisiniz!')

    def customContextMenuBedenListesi(self, pos):
        try:
            action = self.menu.exec_(self.tableWidgetBedenler.viewport().mapToGlobal(pos))
            if action == self.delete_column_action:
                self.MessageBoxButon(self.tableWidgetBedenler.item(self.tableWidgetBedenler.currentRow(), 0).text())
                button = self.message.exec()
                if button == QMessageBox.Ok:
                    print(self.tableWidgetBedenler.item(self.tableWidgetBedenler.currentRow(), 1).text())
                    db.delete_beden(
                        self.tableWidgetBedenler.item(self.tableWidgetBedenler.currentRow(), 1).text())
                    self.BedenListesi()
        except:
            self.messageBox('Geçerli bir satır seçmelisiniz!')


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = Ui()
    app.exec_()
