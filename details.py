from PyQt5 import QtWidgets, uic, QtCore
from PyQt5.QtWidgets import QDialog


class detailsDialog(QDialog):

    def __init__(self, *args, **kwargs):
        super(detailsDialog, self).__init__(*args, **kwargs)
        uic.loadUi("Templates/details.ui", self)