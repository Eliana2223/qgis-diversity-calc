# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'diversity_results_dialog_ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_dlgResults(object):
    def setupUi(self, dlgResu):
        dlgResu.setObjectName("dlgResu")
        dlgResu.resize(400, 300)
        self.verticalLayoutWidget = QtWidgets.QWidget(dlgResu)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 381, 281))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.lytMain = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.lytMain.setContentsMargins(0, 0, 0, 0)
        self.lytMain.setObjectName("lytMain")
        self.trwresult = QtWidgets.QTreeWidget(self.verticalLayoutWidget)
        self.trwresult.setAlternatingRowColors(True)
        self.trwresult.setObjectName("trwresult")
        self.lytMain.addWidget(self.trwresult)

        self.retranslateUi(dlgResu)
        QtCore.QMetaObject.connectSlotsByName(dlgResu)

    def retranslateUi(self, dlgResu):
        _translate = QtCore.QCoreApplication.translate
        dlgResu.setWindowTitle(_translate("dlgResu", "Diversity Results"))
        self.trwresult.headerItem().setText(0, _translate("dlgResu", "Name"))
        self.trwresult.headerItem().setText(1, _translate("dlgResu", "Count"))
        self.trwresult.headerItem().setText(2, _translate("dlgResu", "Richness"))
        self.trwresult.headerItem().setText(3, _translate("dlgResu", "Evenness"))
        self.trwresult.headerItem().setText(4, _translate("dlgResu", "Shannons"))
        self.trwresult.headerItem().setText(5, _translate("dlgResu", "Simpsons"))
