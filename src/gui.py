# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main-window-gui.ui'
#
# Created: Fri May 27 16:23:50 2011
#      by: PyQt4 UI code generator 4.8.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s


class Ui_Hakija(object):
    def setupUi(self, Hakija):
        Hakija.setObjectName(_fromUtf8("Hakija"))
        Hakija.resize(650, 450)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed,
                                       QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Hakija.sizePolicy().hasHeightForWidth())
        Hakija.setSizePolicy(sizePolicy)
        Hakija.setMaximumSize(QtCore.QSize(650, 1000))
        Hakija.setAutoFillBackground(True)
        Hakija.setAnimated(True)
        self.centralwidget = QtGui.QWidget(Hakija)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed,
                                       QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.scrollArea = QtGui.QScrollArea(self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(20, 150, 611, 241))
        self.scrollArea.setHorizontalScrollBarPolicy(
            QtCore.Qt.ScrollBarAlwaysOff)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName(_fromUtf8("scrollArea"))
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 607, 237))
        self.scrollAreaWidgetContents.setObjectName(
            _fromUtf8("scrollAreaWidgetContents"))
        self.verticalLayout = QtGui.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.progressUpdate = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.progressUpdate.setStyleSheet(_fromUtf8(""))
        self.progressUpdate.setText(_fromUtf8(""))
        self.progressUpdate.setObjectName(_fromUtf8("progressUpdate"))
        self.verticalLayout.addWidget(self.progressUpdate)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.layoutWidget = QtGui.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(19, 15, 611, 28))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.startDateLabel = QtGui.QLabel(self.layoutWidget)
        self.startDateLabel.setObjectName(_fromUtf8("startDateLabel"))
        self.horizontalLayout.addWidget(self.startDateLabel)
        self.startDate = QtGui.QDateTimeEdit(self.layoutWidget)
        self.startDate.setCalendarPopup(True)
        self.startDate.setObjectName(_fromUtf8("startDate"))
        self.horizontalLayout.addWidget(self.startDate)
        self.endDateLabel = QtGui.QLabel(self.layoutWidget)
        self.endDateLabel.setObjectName(_fromUtf8("endDateLabel"))
        self.horizontalLayout.addWidget(self.endDateLabel)
        self.endDate = QtGui.QDateTimeEdit(self.layoutWidget)
        self.endDate.setAccelerated(False)
        self.endDate.setCalendarPopup(True)
        self.endDate.setObjectName(_fromUtf8("endDate"))
        self.horizontalLayout.addWidget(self.endDate)
        self.downloadButton = QtGui.QPushButton(self.layoutWidget)
        self.downloadButton.setEnabled(True)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed,
                                       QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.downloadButton.sizePolicy().hasHeightForWidth())
        self.downloadButton.setSizePolicy(sizePolicy)
        self.downloadButton.setAutoDefault(True)
        self.downloadButton.setDefault(True)
        self.downloadButton.setObjectName(_fromUtf8("downloadButton"))
        self.horizontalLayout.addWidget(self.downloadButton)
        self.cancelButton = QtGui.QPushButton(self.layoutWidget)
        self.cancelButton.setObjectName(_fromUtf8("cancelButton"))
        self.horizontalLayout.addWidget(self.cancelButton)
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 50, 151, 16))
        self.label.setObjectName(_fromUtf8("label"))
        self.layoutWidget1 = QtGui.QWidget(self.centralwidget)
        self.layoutWidget1.setGeometry(QtCore.QRect(20, 80, 611, 23))
        self.layoutWidget1.setObjectName(_fromUtf8("layoutWidget1"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_2.setMargin(0)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.bhavcopyCB = QtGui.QCheckBox(self.layoutWidget1)
        self.bhavcopyCB.setChecked(True)
        self.bhavcopyCB.setObjectName(_fromUtf8("bhavcopyCB"))
        self.horizontalLayout_2.addWidget(self.bhavcopyCB)
        self.nseniftyCB = QtGui.QCheckBox(self.layoutWidget1)
        self.nseniftyCB.setChecked(True)
        self.nseniftyCB.setObjectName(_fromUtf8("nseniftyCB"))
        self.horizontalLayout_2.addWidget(self.nseniftyCB)
        self.niftyjuniorCB = QtGui.QCheckBox(self.layoutWidget1)
        self.niftyjuniorCB.setChecked(True)
        self.niftyjuniorCB.setObjectName(_fromUtf8("niftyjuniorCB"))
        self.horizontalLayout_2.addWidget(self.niftyjuniorCB)
        self.nse100CB = QtGui.QCheckBox(self.layoutWidget1)
        self.nse100CB.setChecked(True)
        self.nse100CB.setObjectName(_fromUtf8("nse100CB"))
        self.horizontalLayout_2.addWidget(self.nse100CB)
        self.bankniftyCB = QtGui.QCheckBox(self.layoutWidget1)
        self.bankniftyCB.setChecked(True)
        self.bankniftyCB.setObjectName(_fromUtf8("bankniftyCB"))
        self.horizontalLayout_2.addWidget(self.bankniftyCB)
        self.layoutWidget2 = QtGui.QWidget(self.centralwidget)
        self.layoutWidget2.setGeometry(QtCore.QRect(20, 110, 611, 23))
        self.layoutWidget2.setObjectName(_fromUtf8("layoutWidget2"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.layoutWidget2)
        self.horizontalLayout_3.setMargin(0)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.nsemidcapCB = QtGui.QCheckBox(self.layoutWidget2)
        self.nsemidcapCB.setChecked(True)
        self.nsemidcapCB.setObjectName(_fromUtf8("nsemidcapCB"))
        self.horizontalLayout_3.addWidget(self.nsemidcapCB)
        self.nseitCB = QtGui.QCheckBox(self.layoutWidget2)
        self.nseitCB.setChecked(True)
        self.nseitCB.setObjectName(_fromUtf8("nseitCB"))
        self.horizontalLayout_3.addWidget(self.nseitCB)
        self.nse500CB = QtGui.QCheckBox(self.layoutWidget2)
        self.nse500CB.setChecked(True)
        self.nse500CB.setObjectName(_fromUtf8("nse500CB"))
        self.horizontalLayout_3.addWidget(self.nse500CB)
        self.midcap50CB = QtGui.QCheckBox(self.layoutWidget2)
        self.midcap50CB.setChecked(True)
        self.midcap50CB.setObjectName(_fromUtf8("midcap50CB"))
        self.horizontalLayout_3.addWidget(self.midcap50CB)
        self.vixCB = QtGui.QCheckBox(self.layoutWidget2)
        self.vixCB.setChecked(True)
        self.vixCB.setObjectName(_fromUtf8("vixCB"))
        self.horizontalLayout_3.addWidget(self.vixCB)
        Hakija.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(Hakija)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        Hakija.setStatusBar(self.statusbar)
        self.menubar = QtGui.QMenuBar(Hakija)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 650, 23))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuHelp = QtGui.QMenu(self.menubar)
        self.menuHelp.setObjectName(_fromUtf8("menuHelp"))
        Hakija.setMenuBar(self.menubar)
        self.actionExit = QtGui.QAction(Hakija)
        self.actionExit.setObjectName(_fromUtf8("actionExit"))
        self.actionAbout = QtGui.QAction(Hakija)
        self.actionAbout.setObjectName(_fromUtf8("actionAbout"))
        self.actionAbout_2 = QtGui.QAction(Hakija)
        self.actionAbout_2.setObjectName(_fromUtf8("actionAbout_2"))
        self.actionaboutHakija = QtGui.QAction(Hakija)
        self.actionaboutHakija.setObjectName(_fromUtf8("actionaboutHakija"))
        self.menuFile.addAction(self.actionExit)
        self.menuHelp.addAction(self.actionaboutHakija)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(Hakija)
        QtCore.QMetaObject.connectSlotsByName(Hakija)

    def retranslateUi(self, Hakija):
        Hakija.setWindowTitle(
            QtGui.QApplication.translate("Hakija", "Hakija", None,
                                         QtGui.QApplication.UnicodeUTF8))
        self.startDateLabel.setText(
            QtGui.QApplication.translate("Hakija", "  Start Date:", None,
                                         QtGui.QApplication.UnicodeUTF8))
        self.startDate.setDisplayFormat(
            QtGui.QApplication.translate("Hakija", "dd/MM/yy", None,
                                         QtGui.QApplication.UnicodeUTF8))
        self.endDateLabel.setText(
            QtGui.QApplication.translate("Hakija", "    End Date:", None,
                                         QtGui.QApplication.UnicodeUTF8))
        self.endDate.setDisplayFormat(
            QtGui.QApplication.translate("Hakija", "dd/MM/yy", None,
                                         QtGui.QApplication.UnicodeUTF8))
        self.downloadButton.setText(
            QtGui.QApplication.translate("Hakija", "Download", None,
                                         QtGui.QApplication.UnicodeUTF8))
        self.cancelButton.setText(
            QtGui.QApplication.translate("Hakija", "Cancel", None,
                                         QtGui.QApplication.UnicodeUTF8))
        self.label.setText(
            QtGui.QApplication.translate("Hakija", "Download Options:", None,
                                         QtGui.QApplication.UnicodeUTF8))
        self.bhavcopyCB.setText(
            QtGui.QApplication.translate("Hakija", "NSE Bhavcopy", None,
                                         QtGui.QApplication.UnicodeUTF8))
        self.nseniftyCB.setText(
            QtGui.QApplication.translate("Hakija", "NSENIFTY", None,
                                         QtGui.QApplication.UnicodeUTF8))
        self.niftyjuniorCB.setText(
            QtGui.QApplication.translate("Hakija", "NIFTY Junior", None,
                                         QtGui.QApplication.UnicodeUTF8))
        self.nse100CB.setText(
            QtGui.QApplication.translate("Hakija", "NSE100", None,
                                         QtGui.QApplication.UnicodeUTF8))
        self.bankniftyCB.setText(
            QtGui.QApplication.translate("Hakija", "BANKNIFTY", None,
                                         QtGui.QApplication.UnicodeUTF8))
        self.nsemidcapCB.setText(
            QtGui.QApplication.translate("Hakija", "NSEMIDCAP", None,
                                         QtGui.QApplication.UnicodeUTF8))
        self.nseitCB.setText(
            QtGui.QApplication.translate("Hakija", "NSEIT", None,
                                         QtGui.QApplication.UnicodeUTF8))
        self.nse500CB.setText(
            QtGui.QApplication.translate("Hakija", "NSE500", None,
                                         QtGui.QApplication.UnicodeUTF8))
        self.midcap50CB.setText(
            QtGui.QApplication.translate("Hakija", "MIDCAP50", None,
                                         QtGui.QApplication.UnicodeUTF8))
        self.vixCB.setText(
            QtGui.QApplication.translate("Hakija", "VIX", None,
                                         QtGui.QApplication.UnicodeUTF8))
        self.menuFile.setTitle(
            QtGui.QApplication.translate("Hakija", "File", None,
                                         QtGui.QApplication.UnicodeUTF8))
        self.menuHelp.setTitle(
            QtGui.QApplication.translate("Hakija", "Help", None,
                                         QtGui.QApplication.UnicodeUTF8))
        self.actionExit.setText(
            QtGui.QApplication.translate("Hakija", "Exit", None,
                                         QtGui.QApplication.UnicodeUTF8))
        self.actionAbout.setText(
            QtGui.QApplication.translate("Hakija", "About", None,
                                         QtGui.QApplication.UnicodeUTF8))
        self.actionAbout_2.setText(
            QtGui.QApplication.translate("Hakija", "About", None,
                                         QtGui.QApplication.UnicodeUTF8))
        self.actionaboutHakija.setText(
            QtGui.QApplication.translate("Hakija", "About Hakija", None,
                                         QtGui.QApplication.UnicodeUTF8))


if __name__ == "__main__":
    import sys

    app = QtGui.QApplication(sys.argv)
    Hakija = QtGui.QMainWindow()
    ui = Ui_Hakija()
    ui.setupUi(Hakija)
    Hakija.show()
    sys.exit(app.exec_())
