from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox

import db


class Ui_MainWindow(object):
    def __init__(self):
        super().__init__()
        self.message = QMessageBox()
        self.icon = QtGui.QIcon()
        self.icon.addPixmap(QtGui.QPixmap("img/logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.delete_icon = QtGui.QIcon('img/delete.png')

        self.menu = QtWidgets.QMenu()
        self.delete_column_action = self.menu.addAction("Kaydı Sil")
        self.delete_column_action.setIcon(self.delete_icon)

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
            db.insert_renk(self.txtRenkAdi.text(), self.txtRenkKodu.text())
            self.RenkListesi()
            self.txtRenkAdi.clear()
            self.txtRenkKodu.clear()

    def mevsimEkle(self):
        if len(self.txtMevsimAdi.text()) == 0 \
                or len(self.txtMevsimKodu.text()) == 0:
            self.messageBox("Tüm alanların dolu olması gerekmektedir!")
        else:
            db.insert_mevsim(self.txtMevsimAdi.text(), self.txtMevsimKodu.text())
            self.MevsimListesi()
            self.txtMevsimAdi.clear()
            self.txtMevsimKodu.clear()

    def kumasEkle(self):
        if len(self.txtKumaAdi.text()) == 0 \
                or len(self.txtKumasKodu.text()) == 0:
            self.messageBox("Tüm alanların dolu olması gerekmektedir!")
        else:
            db.insert_kumas(self.txtKumaAdi.text(), self.txtKumasKodu.text())
            self.KumasListesi()
            self.txtKumaAdi.clear()
            self.txtKumasKodu.clear()

    def magazaEkle(self):
        if len(self.txtMagazaAdi.text()) == 0 \
                or len(self.txtMagazaKodu.text()) == 0:
            self.messageBox("Tüm alanların dolu olması gerekmektedir!")
        else:
            db.insert_magaza(self.txtMagazaAdi.text(), self.txtMagazaKodu.text())
            self.MagazaListesi()
            self.txtMagazaAdi.clear()
            self.txtMagazaKodu.clear()

    def magazaUrunEkle(self):
        if len(self.txtMagazaUrunAdi.text()) == 0 \
                or len(self.txtMagazaUrunKodu.text()) == 0:
            self.messageBox("Tüm alanların dolu olması gerekmektedir!")
        else:
            db.insert_magaza_urunleri(self.txtMagazaUrunAdi.text(), self.txtMagazaUrunKodu.text())
            self.MagazaUrunListesi()
            self.txtMagazaUrunAdi.clear()
            self.txtMagazaUrunKodu.clear()

    def bedenEkle(self):
        if len(self.txtBedenAd.text()) == 0 \
                or len(self.txtBedenKodu.text()) == 0:
            self.messageBox("Tüm alanların dolu olması gerekmektedir!")
        else:
            db.insert_beden(self.txtBedenAd.text(), self.txtBedenKodu.text())
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
            self.tableWidgetBedenler.setItem(row_number, 1,QtWidgets.QTableWidgetItem(str(row_data["beden_kodu"])))

            self.comboBoxBeden.addItem(str(row_data["beden_adi"]))

    def BarkodListesi(self, kod=None):
        barkodlar = db.select_barkod(kod)
        self.tableWidgetBarkodListesi.setRowCount(0)
        for row_number, row_data in enumerate(barkodlar):
            self.tableWidgetBarkodListesi.insertRow(row_number)
            self.tableWidgetBarkodListesi.setItem(row_number, 0,
                                                  QtWidgets.QTableWidgetItem(str(row_data["urun_kodu"])))
            self.tableWidgetBarkodListesi.setItem(row_number, 1,
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
            barkod = self.txtTarih.text() + self.KodGetir(self.comboBoxMevsim.currentText(), 'mevsim') + self.txtUrunKodu.text() + self.KodGetir(
                self.comboBoxMagaza.currentText(), 'magaza') + self.KodGetir(self.comboBoxMagazaUrun.currentText(),'magaza_urun') + self.KodGetir(self.comboBoxBeden.currentText(), 'beden') + self.KodGetir(
                self.comboBoxRenk.currentText(), 'renk') + self.KodGetir(self.comboBoxKumas.currentText(), 'kumas')

            db.insert_barkod(self.txtUrunKodu.text(), barkod)
            self.BarkodListesi()

            self.txtBarkod.setText(barkod)

    def BarkodAra(self):
        if len(self.txtBarkodUrunKodu.text()) > 0:
            kod = self.txtBarkodUrunKodu.text()
        else:
            kod = None
        self.BarkodListesi(kod)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(554, 435)
        MainWindow.setMinimumSize(QtCore.QSize(554, 435))
        MainWindow.setMaximumSize(QtCore.QSize(554, 435))
        MainWindow.setBaseSize(QtCore.QSize(554, 435))
        MainWindow.setWindowIcon(self.icon)

        MainWindow.setStyleSheet("QHeaderView::section {\n"
                                 "    height: 32px;\n"
                                 "}\n"
                                 "QTableWidget{\n"
                                 "    color:#000000;\n"
                                 "border-color: rgb(0, 0, 0);\n"
                                 "border-width : 1px;\n"
                                 "border-style:inset;\n"
                                 "}")

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(2, 3, 552, 431))
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.North)
        self.tabWidget.setElideMode(QtCore.Qt.ElideMiddle)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.txtTarih = QtWidgets.QLineEdit(self.tab_3)
        self.txtTarih.setGeometry(QtCore.QRect(292, 7, 141, 20))
        self.txtTarih.setObjectName("txtTarih")
        self.comboBoxMevsim = QtWidgets.QComboBox(self.tab_3)
        self.comboBoxMevsim.setGeometry(QtCore.QRect(292, 45, 141, 22))
        self.comboBoxMevsim.setObjectName("comboBoxMevsim")
        self.txtUrunKodu = QtWidgets.QLineEdit(self.tab_3)
        self.txtUrunKodu.setGeometry(QtCore.QRect(292, 86, 141, 20))
        self.txtUrunKodu.setObjectName("txtUrunKodu")
        self.label = QtWidgets.QLabel(self.tab_3)
        self.label.setGeometry(QtCore.QRect(106, 10, 47, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.tab_3)
        self.label_2.setGeometry(QtCore.QRect(106, 46, 61, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.tab_3)
        self.label_3.setGeometry(QtCore.QRect(106, 88, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.tab_3)
        self.label_4.setGeometry(QtCore.QRect(106, 124, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.tab_3)
        self.label_5.setGeometry(QtCore.QRect(106, 255, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.tab_3)
        self.label_6.setGeometry(QtCore.QRect(106, 293, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.comboBoxRenk = QtWidgets.QComboBox(self.tab_3)
        self.comboBoxRenk.setGeometry(QtCore.QRect(292, 252, 141, 22))
        self.comboBoxRenk.setObjectName("comboBoxRenk")
        self.comboBoxKumas = QtWidgets.QComboBox(self.tab_3)
        self.comboBoxKumas.setGeometry(QtCore.QRect(292, 293, 141, 22))
        self.comboBoxKumas.setObjectName("comboBoxKumas")
        self.line = QtWidgets.QFrame(self.tab_3)
        self.line.setGeometry(QtCore.QRect(102, 27, 331, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.tab_3)
        self.line_2.setGeometry(QtCore.QRect(102, 68, 331, 16))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.line_3 = QtWidgets.QFrame(self.tab_3)
        self.line_3.setGeometry(QtCore.QRect(102, 111, 331, 10))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.line_4 = QtWidgets.QFrame(self.tab_3)
        self.line_4.setGeometry(QtCore.QRect(102, 148, 331, 16))
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.line_5 = QtWidgets.QFrame(self.tab_3)
        self.line_5.setGeometry(QtCore.QRect(102, 232, 331, 16))
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.txtBarkod = QtWidgets.QLineEdit(self.tab_3)
        self.txtBarkod.setGeometry(QtCore.QRect(51, 368, 441, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.txtBarkod.setFont(font)
        self.txtBarkod.setReadOnly(True)
        self.txtBarkod.setObjectName("txtBarkod")
        self.pushButtonOlustur = QtWidgets.QPushButton(self.tab_3)
        self.pushButtonOlustur.setGeometry(QtCore.QRect(236, 329, 71, 31))
        self.pushButtonOlustur.setObjectName("pushButtonOlustur")
        self.line_6 = QtWidgets.QFrame(self.tab_3)
        self.line_6.setGeometry(QtCore.QRect(104, 277, 331, 16))
        self.line_6.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.label_7 = QtWidgets.QLabel(self.tab_3)
        self.label_7.setGeometry(QtCore.QRect(105, 161, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.comboBoxMagaza = QtWidgets.QComboBox(self.tab_3)
        self.comboBoxMagaza.setGeometry(QtCore.QRect(291, 124, 141, 22))
        self.comboBoxMagaza.setObjectName("comboBoxMagaza")
        self.comboBoxMagazaUrun = QtWidgets.QComboBox(self.tab_3)
        self.comboBoxMagazaUrun.setGeometry(QtCore.QRect(291, 163, 141, 22))
        self.comboBoxMagazaUrun.setObjectName("comboBoxMagazaUrun")
        self.label_8 = QtWidgets.QLabel(self.tab_3)
        self.label_8.setGeometry(QtCore.QRect(105, 210, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.line_7 = QtWidgets.QFrame(self.tab_3)
        self.line_7.setGeometry(QtCore.QRect(101, 187, 331, 16))
        self.line_7.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_7.setObjectName("line_7")
        self.comboBoxBeden = QtWidgets.QComboBox(self.tab_3)
        self.comboBoxBeden.setGeometry(QtCore.QRect(291, 207, 141, 22))
        self.comboBoxBeden.setObjectName("comboBoxBeden")
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_8 = QtWidgets.QWidget()
        self.tab_8.setObjectName("tab_8")
        self.tableWidgetBarkodListesi = QtWidgets.QTableWidget(self.tab_8)
        self.tableWidgetBarkodListesi.setGeometry(QtCore.QRect(0, 40, 545, 365))
        self.tableWidgetBarkodListesi.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.tableWidgetBarkodListesi.setCornerButtonEnabled(False)
        self.tableWidgetBarkodListesi.setObjectName("tableWidgetBarkodListesi")
        self.tableWidgetBarkodListesi.setColumnCount(2)
        self.tableWidgetBarkodListesi.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidgetBarkodListesi.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidgetBarkodListesi.setHorizontalHeaderItem(1, item)
        self.tableWidgetBarkodListesi.horizontalHeader().setDefaultSectionSize(225)
        self.tableWidgetBarkodListesi.horizontalHeader().setMinimumSectionSize(225)
        self.pushButtonBarkodAra = QtWidgets.QPushButton(self.tab_8)
        self.pushButtonBarkodAra.setGeometry(QtCore.QRect(470, 4, 75, 31))
        self.pushButtonBarkodAra.setObjectName("pushButtonBarkodAra")
        self.txtBarkodUrunKodu = QtWidgets.QLineEdit(self.tab_8)
        self.txtBarkodUrunKodu.setGeometry(QtCore.QRect(0, 4, 466, 31))
        self.txtBarkodUrunKodu.setObjectName("txtBarkodUrunKodu")
        self.tabWidget.addTab(self.tab_8, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.tabWidget_2 = QtWidgets.QTabWidget(self.tab)
        self.tabWidget_2.setGeometry(QtCore.QRect(12, 11, 522, 382))
        self.tabWidget_2.setObjectName("tabWidget_2")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tableWidgetRenkler = QtWidgets.QTableWidget(self.tab_2)
        self.tableWidgetRenkler.setGeometry(QtCore.QRect(0, 37, 516, 319))
        self.tableWidgetRenkler.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.tableWidgetRenkler.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidgetRenkler.setCornerButtonEnabled(False)
        self.tableWidgetRenkler.setObjectName("tableWidgetRenkler")
        self.tableWidgetRenkler.setColumnCount(2)
        self.tableWidgetRenkler.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidgetRenkler.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidgetRenkler.setHorizontalHeaderItem(1, item)
        self.tableWidgetRenkler.horizontalHeader().setDefaultSectionSize(225)
        self.tableWidgetRenkler.horizontalHeader().setMinimumSectionSize(225)
        self.txtRenkAdi = QtWidgets.QLineEdit(self.tab_2)
        self.txtRenkAdi.setGeometry(QtCore.QRect(1, 1, 221, 31))
        self.txtRenkAdi.setObjectName("txtRenkAdi")
        self.pushButtonRenkEkle = QtWidgets.QPushButton(self.tab_2)
        self.pushButtonRenkEkle.setGeometry(QtCore.QRect(454, 1, 61, 31))
        self.pushButtonRenkEkle.setObjectName("pushButtonRenkEkle")
        self.txtRenkKodu = QtWidgets.QLineEdit(self.tab_2)
        self.txtRenkKodu.setGeometry(QtCore.QRect(229, 1, 221, 31))
        self.txtRenkKodu.setObjectName("txtRenkKodu")
        self.tabWidget_2.addTab(self.tab_2, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.tableWidgetKumaslar = QtWidgets.QTableWidget(self.tab_4)
        self.tableWidgetKumaslar.setGeometry(QtCore.QRect(0, 37, 516, 319))
        self.tableWidgetKumaslar.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.tableWidgetKumaslar.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidgetKumaslar.setObjectName("tableWidgetKumaslar")
        self.tableWidgetKumaslar.setColumnCount(2)
        self.tableWidgetKumaslar.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidgetKumaslar.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidgetKumaslar.setHorizontalHeaderItem(1, item)
        self.tableWidgetKumaslar.horizontalHeader().setDefaultSectionSize(225)
        self.tableWidgetKumaslar.horizontalHeader().setMinimumSectionSize(225)
        self.txtKumaAdi = QtWidgets.QLineEdit(self.tab_4)
        self.txtKumaAdi.setGeometry(QtCore.QRect(1, 1, 221, 31))
        self.txtKumaAdi.setObjectName("txtKumaAdi")
        self.pushButtonKumasEkle = QtWidgets.QPushButton(self.tab_4)
        self.pushButtonKumasEkle.setGeometry(QtCore.QRect(454, 1, 61, 31))
        self.pushButtonKumasEkle.setObjectName("pushButtonKumasEkle")
        self.txtKumasKodu = QtWidgets.QLineEdit(self.tab_4)
        self.txtKumasKodu.setGeometry(QtCore.QRect(229, 1, 221, 31))
        self.txtKumasKodu.setObjectName("txtKumasKodu")
        self.tabWidget_2.addTab(self.tab_4, "")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.txtMevsimAdi = QtWidgets.QLineEdit(self.tab_5)
        self.txtMevsimAdi.setGeometry(QtCore.QRect(1, 1, 221, 31))
        self.txtMevsimAdi.setObjectName("txtMevsimAdi")
        self.txtMevsimKodu = QtWidgets.QLineEdit(self.tab_5)
        self.txtMevsimKodu.setGeometry(QtCore.QRect(229, 1, 221, 31))
        self.txtMevsimKodu.setObjectName("txtMevsimKodu")
        self.pushButtonMevsimEkle = QtWidgets.QPushButton(self.tab_5)
        self.pushButtonMevsimEkle.setGeometry(QtCore.QRect(454, 1, 61, 31))
        self.pushButtonMevsimEkle.setObjectName("pushButtonMevsimEkle")
        self.tableWidgetMevsimler = QtWidgets.QTableWidget(self.tab_5)
        self.tableWidgetMevsimler.setGeometry(QtCore.QRect(0, 37, 516, 319))
        self.tableWidgetMevsimler.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.tableWidgetMevsimler.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidgetMevsimler.setCornerButtonEnabled(False)
        self.tableWidgetMevsimler.setObjectName("tableWidgetMevsimler")
        self.tableWidgetMevsimler.setColumnCount(2)
        self.tableWidgetMevsimler.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidgetMevsimler.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidgetMevsimler.setHorizontalHeaderItem(1, item)
        self.tableWidgetMevsimler.horizontalHeader().setDefaultSectionSize(225)
        self.tableWidgetMevsimler.horizontalHeader().setMinimumSectionSize(225)
        self.tabWidget_2.addTab(self.tab_5, "")
        self.tab_9 = QtWidgets.QWidget()
        self.tab_9.setObjectName("tab_9")
        self.pushButtonBedenEkle = QtWidgets.QPushButton(self.tab_9)
        self.pushButtonBedenEkle.setGeometry(QtCore.QRect(454, 1, 61, 31))
        self.pushButtonBedenEkle.setObjectName("pushButtonBedenEkle")
        self.txtBedenKodu = QtWidgets.QLineEdit(self.tab_9)
        self.txtBedenKodu.setGeometry(QtCore.QRect(229, 1, 221, 31))
        self.txtBedenKodu.setObjectName("txtBedenKodu")
        self.tableWidgetBedenler = QtWidgets.QTableWidget(self.tab_9)
        self.tableWidgetBedenler.setGeometry(QtCore.QRect(0, 37, 516, 319))
        self.tableWidgetBedenler.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.tableWidgetBedenler.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidgetBedenler.setCornerButtonEnabled(False)
        self.tableWidgetBedenler.setObjectName("tableWidgetBedenler")
        self.tableWidgetBedenler.setColumnCount(2)
        self.tableWidgetBedenler.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidgetBedenler.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidgetBedenler.setHorizontalHeaderItem(1, item)
        self.tableWidgetBedenler.horizontalHeader().setDefaultSectionSize(225)
        self.tableWidgetBedenler.horizontalHeader().setMinimumSectionSize(225)
        self.txtBedenAd = QtWidgets.QLineEdit(self.tab_9)
        self.txtBedenAd.setGeometry(QtCore.QRect(1, 1, 221, 31))
        self.txtBedenAd.setObjectName("txtBedenAd")
        self.tabWidget_2.addTab(self.tab_9, "")
        self.tab_6 = QtWidgets.QWidget()
        self.tab_6.setObjectName("tab_6")
        self.tableWidgetMagazalar = QtWidgets.QTableWidget(self.tab_6)
        self.tableWidgetMagazalar.setGeometry(QtCore.QRect(0, 37, 516, 319))
        self.tableWidgetMagazalar.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.tableWidgetMagazalar.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidgetMagazalar.setCornerButtonEnabled(False)
        self.tableWidgetMagazalar.setObjectName("tableWidgetMagazalar")
        self.tableWidgetMagazalar.setColumnCount(2)
        self.tableWidgetMagazalar.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidgetMagazalar.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidgetMagazalar.setHorizontalHeaderItem(1, item)
        self.tableWidgetMagazalar.horizontalHeader().setDefaultSectionSize(225)
        self.tableWidgetMagazalar.horizontalHeader().setMinimumSectionSize(225)
        self.txtMagazaAdi = QtWidgets.QLineEdit(self.tab_6)
        self.txtMagazaAdi.setGeometry(QtCore.QRect(1, 1, 221, 31))
        self.txtMagazaAdi.setObjectName("txtMagazaAdi")
        self.pushButtonMagazaEkle = QtWidgets.QPushButton(self.tab_6)
        self.pushButtonMagazaEkle.setGeometry(QtCore.QRect(454, 1, 61, 31))
        self.pushButtonMagazaEkle.setObjectName("pushButtonMagazaEkle")
        self.txtMagazaKodu = QtWidgets.QLineEdit(self.tab_6)
        self.txtMagazaKodu.setGeometry(QtCore.QRect(229, 1, 221, 31))
        self.txtMagazaKodu.setObjectName("txtMagazaKodu")
        self.tabWidget_2.addTab(self.tab_6, "")
        self.tab_7 = QtWidgets.QWidget()
        self.tab_7.setObjectName("tab_7")
        self.tableWidgetMagazaUrunleri = QtWidgets.QTableWidget(self.tab_7)
        self.tableWidgetMagazaUrunleri.setGeometry(QtCore.QRect(0, 37, 516, 319))
        self.tableWidgetMagazaUrunleri.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.tableWidgetMagazaUrunleri.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidgetMagazaUrunleri.setCornerButtonEnabled(False)
        self.tableWidgetMagazaUrunleri.setObjectName("tableWidgetMagazaUrunleri")
        self.tableWidgetMagazaUrunleri.setColumnCount(2)
        self.tableWidgetMagazaUrunleri.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidgetMagazaUrunleri.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidgetMagazaUrunleri.setHorizontalHeaderItem(1, item)
        self.tableWidgetMagazaUrunleri.horizontalHeader().setDefaultSectionSize(225)
        self.tableWidgetMagazaUrunleri.horizontalHeader().setMinimumSectionSize(225)
        self.txtMagazaUrunAdi = QtWidgets.QLineEdit(self.tab_7)
        self.txtMagazaUrunAdi.setGeometry(QtCore.QRect(1, 1, 221, 31))
        self.txtMagazaUrunAdi.setObjectName("txtMagazaUrunAdi")
        self.pushButtonMagazaUrunEkle = QtWidgets.QPushButton(self.tab_7)
        self.pushButtonMagazaUrunEkle.setGeometry(QtCore.QRect(454, 1, 61, 31))
        self.pushButtonMagazaUrunEkle.setObjectName("pushButtonMagazaUrunEkle")
        self.txtMagazaUrunKodu = QtWidgets.QLineEdit(self.tab_7)
        self.txtMagazaUrunKodu.setGeometry(QtCore.QRect(229, 1, 221, 31))
        self.txtMagazaUrunKodu.setObjectName("txtMagazaUrunKodu")
        self.tabWidget_2.addTab(self.tab_7, "")
        self.tabWidget.addTab(self.tab, "")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        self.tabWidget_2.setCurrentIndex(0)

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

        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Moodart Barkod Oluşturucu"))
        self.label.setText(_translate("MainWindow", "Tarih"))
        self.label_2.setText(_translate("MainWindow", "Mevsim"))
        self.label_3.setText(_translate("MainWindow", "Ürün Kodu"))
        self.label_4.setText(_translate("MainWindow", "Mağaza Kodu"))
        self.label_5.setText(_translate("MainWindow", "Renk"))
        self.label_6.setText(_translate("MainWindow", "Kumaş Türü"))
        self.txtBarkod.setPlaceholderText(_translate("MainWindow", "Oluşturulan Barkod"))
        self.pushButtonOlustur.setText(_translate("MainWindow", "Oluştur"))
        self.label_7.setText(_translate("MainWindow", "Mağaza Ürün Kodu"))
        self.label_8.setText(_translate("MainWindow", "Beden"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Barkod Oluştur"))
        self.tableWidgetBarkodListesi.setSortingEnabled(True)
        item = self.tableWidgetBarkodListesi.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Ürün Kodu"))
        item = self.tableWidgetBarkodListesi.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Barkod"))
        self.pushButtonBarkodAra.setText(_translate("MainWindow", "Ara"))
        self.txtBarkodUrunKodu.setPlaceholderText(_translate("MainWindow", "Barkod ya da Ürün Kodu Girin"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_8), _translate("MainWindow", "Barkod Listesi"))
        self.tableWidgetRenkler.setSortingEnabled(True)
        item = self.tableWidgetRenkler.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Renk Adı"))
        item = self.tableWidgetRenkler.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Renk Kodu"))
        self.txtRenkAdi.setPlaceholderText(_translate("MainWindow", "Renk Adı"))
        self.pushButtonRenkEkle.setText(_translate("MainWindow", "Ekle"))
        self.txtRenkKodu.setPlaceholderText(_translate("MainWindow", "Renk Kodu"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_2), _translate("MainWindow", "Renk"))
        self.tableWidgetKumaslar.setSortingEnabled(True)
        item = self.tableWidgetKumaslar.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Kumaş Adı"))
        item = self.tableWidgetKumaslar.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Kumaş Kodu"))
        self.txtKumaAdi.setPlaceholderText(_translate("MainWindow", "Kumaş Adı"))
        self.pushButtonKumasEkle.setText(_translate("MainWindow", "Ekle"))
        self.txtKumasKodu.setPlaceholderText(_translate("MainWindow", "Kumaş Kodu"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_4), _translate("MainWindow", "Kumaş"))
        self.txtMevsimAdi.setPlaceholderText(_translate("MainWindow", "Mevsim Adı"))
        self.txtMevsimKodu.setPlaceholderText(_translate("MainWindow", "Mevsim Kodu"))
        self.pushButtonMevsimEkle.setText(_translate("MainWindow", "Ekle"))
        self.tableWidgetMevsimler.setSortingEnabled(True)
        item = self.tableWidgetMevsimler.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Mevsim Adı"))
        item = self.tableWidgetMevsimler.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Mevsim Kodu"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_5), _translate("MainWindow", "Mevsim"))
        self.pushButtonBedenEkle.setText(_translate("MainWindow", "Ekle"))
        self.txtBedenKodu.setPlaceholderText(_translate("MainWindow", "Beden Kodu"))
        self.tableWidgetBedenler.setSortingEnabled(True)
        item = self.tableWidgetBedenler.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Beden Adı"))
        item = self.tableWidgetBedenler.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Beden Kodu"))
        self.txtBedenAd.setPlaceholderText(_translate("MainWindow", "Beden Adı"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_9), _translate("MainWindow", "Beden"))
        self.tableWidgetMagazalar.setSortingEnabled(True)
        item = self.tableWidgetMagazalar.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Mağaza Adı"))
        item = self.tableWidgetMagazalar.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Mağaza Kodu"))
        self.txtMagazaAdi.setPlaceholderText(_translate("MainWindow", "Mağaza Adı"))
        self.pushButtonMagazaEkle.setText(_translate("MainWindow", "Ekle"))
        self.txtMagazaKodu.setPlaceholderText(_translate("MainWindow", "Mağaza Kodu"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_6), _translate("MainWindow", "Mağaza"))
        self.tableWidgetMagazaUrunleri.setSortingEnabled(True)
        item = self.tableWidgetMagazaUrunleri.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Mağaza Ürün Adı"))
        item = self.tableWidgetMagazaUrunleri.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Mağaza Ürün Kodu"))
        self.txtMagazaUrunAdi.setPlaceholderText(_translate("MainWindow", "Mağaza Ürün Adı"))
        self.pushButtonMagazaUrunEkle.setText(_translate("MainWindow", "Ekle"))
        self.txtMagazaUrunKodu.setPlaceholderText(_translate("MainWindow", "Mağaza Ürün Kodu"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_7), _translate("MainWindow", "Mağaza Ürünleri"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Diğer Kodlar"))

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
                self.MessageBoxButon(
                    self.tableWidgetBarkodListesi.item(self.tableWidgetBarkodListesi.currentRow(), 0).text())
                button = self.message.exec()
                if button == QMessageBox.Ok:
                    db.delete_barkod(
                        self.tableWidgetBarkodListesi.item(self.tableWidgetBarkodListesi.currentRow(), 1).text())
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
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
