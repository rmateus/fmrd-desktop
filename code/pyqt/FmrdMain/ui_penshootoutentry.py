# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui/penshootout_entry.ui'
#
# Created: Sat Nov 19 20:17:16 2011
#      by: PyQt4 UI code generator 4.7.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_PenShootoutEntryDlg(object):
    def setupUi(self, PenShootoutEntryDlg):
        PenShootoutEntryDlg.setObjectName("PenShootoutEntryDlg")
        PenShootoutEntryDlg.resize(640, 460)
        PenShootoutEntryDlg.setMinimumSize(QtCore.QSize(640, 460))
        PenShootoutEntryDlg.setMaximumSize(QtCore.QSize(640, 460))
        self.layoutWidget_3 = QtGui.QWidget(PenShootoutEntryDlg)
        self.layoutWidget_3.setGeometry(QtCore.QRect(80, 400, 381, 41))
        self.layoutWidget_3.setObjectName("layoutWidget_3")
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.layoutWidget_3)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.firstEntry = QtGui.QPushButton(self.layoutWidget_3)
        self.firstEntry.setMinimumSize(QtCore.QSize(90, 30))
        self.firstEntry.setMaximumSize(QtCore.QSize(90, 30))
        self.firstEntry.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/images/first.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.firstEntry.setIcon(icon)
        self.firstEntry.setObjectName("firstEntry")
        self.horizontalLayout_2.addWidget(self.firstEntry)
        self.prevEntry = QtGui.QPushButton(self.layoutWidget_3)
        self.prevEntry.setMinimumSize(QtCore.QSize(90, 30))
        self.prevEntry.setMaximumSize(QtCore.QSize(90, 30))
        self.prevEntry.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/images/prev.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.prevEntry.setIcon(icon1)
        self.prevEntry.setObjectName("prevEntry")
        self.horizontalLayout_2.addWidget(self.prevEntry)
        self.nextEntry = QtGui.QPushButton(self.layoutWidget_3)
        self.nextEntry.setMinimumSize(QtCore.QSize(90, 30))
        self.nextEntry.setMaximumSize(QtCore.QSize(90, 30))
        self.nextEntry.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/images/next.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.nextEntry.setIcon(icon2)
        self.nextEntry.setObjectName("nextEntry")
        self.horizontalLayout_2.addWidget(self.nextEntry)
        self.lastEntry = QtGui.QPushButton(self.layoutWidget_3)
        self.lastEntry.setMinimumSize(QtCore.QSize(90, 30))
        self.lastEntry.setMaximumSize(QtCore.QSize(90, 30))
        self.lastEntry.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/images/last.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.lastEntry.setIcon(icon3)
        self.lastEntry.setObjectName("lastEntry")
        self.horizontalLayout_2.addWidget(self.lastEntry)
        self.line = QtGui.QFrame(PenShootoutEntryDlg)
        self.line.setGeometry(QtCore.QRect(10, 170, 521, 16))
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtGui.QFrame(PenShootoutEntryDlg)
        self.line_2.setGeometry(QtCore.QRect(520, 10, 20, 391))
        self.line_2.setFrameShape(QtGui.QFrame.VLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.layoutWidget = QtGui.QWidget(PenShootoutEntryDlg)
        self.layoutWidget.setGeometry(QtCore.QRect(540, 140, 91, 251))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtGui.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.addEntry = QtGui.QPushButton(self.layoutWidget)
        self.addEntry.setMinimumSize(QtCore.QSize(80, 33))
        self.addEntry.setMaximumSize(QtCore.QSize(80, 33))
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/images/add.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.addEntry.setIcon(icon4)
        self.addEntry.setObjectName("addEntry")
        self.verticalLayout.addWidget(self.addEntry)
        self.deleteEntry = QtGui.QPushButton(self.layoutWidget)
        self.deleteEntry.setMinimumSize(QtCore.QSize(80, 33))
        self.deleteEntry.setMaximumSize(QtCore.QSize(80, 33))
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/images/delete.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.deleteEntry.setIcon(icon5)
        self.deleteEntry.setObjectName("deleteEntry")
        self.verticalLayout.addWidget(self.deleteEntry)
        self.saveEntry = QtGui.QPushButton(self.layoutWidget)
        self.saveEntry.setMinimumSize(QtCore.QSize(80, 33))
        self.saveEntry.setMaximumSize(QtCore.QSize(80, 33))
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/images/save.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.saveEntry.setIcon(icon6)
        self.saveEntry.setObjectName("saveEntry")
        self.verticalLayout.addWidget(self.saveEntry)
        spacerItem = QtGui.QSpacerItem(20, 168, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.closeButton = QtGui.QPushButton(self.layoutWidget)
        self.closeButton.setMinimumSize(QtCore.QSize(80, 33))
        self.closeButton.setMaximumSize(QtCore.QSize(80, 33))
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/images/quit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.closeButton.setIcon(icon7)
        self.closeButton.setObjectName("closeButton")
        self.verticalLayout.addWidget(self.closeButton)
        self.widget = QtGui.QWidget(PenShootoutEntryDlg)
        self.widget.setGeometry(QtCore.QRect(20, 0, 488, 181))
        self.widget.setObjectName("widget")
        self.gridLayout = QtGui.QGridLayout(self.widget)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtGui.QLabel(self.widget)
        self.label.setMinimumSize(QtCore.QSize(150, 30))
        self.label.setMaximumSize(QtCore.QSize(150, 30))
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.compSelect = QtGui.QComboBox(self.widget)
        self.compSelect.setMinimumSize(QtCore.QSize(330, 30))
        self.compSelect.setMaximumSize(QtCore.QSize(330, 30))
        self.compSelect.setObjectName("compSelect")
        self.gridLayout.addWidget(self.compSelect, 0, 1, 1, 1)
        self.label_2 = QtGui.QLabel(self.widget)
        self.label_2.setMinimumSize(QtCore.QSize(150, 30))
        self.label_2.setMaximumSize(QtCore.QSize(150, 30))
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.koroundSelect = QtGui.QComboBox(self.widget)
        self.koroundSelect.setMinimumSize(QtCore.QSize(180, 30))
        self.koroundSelect.setMaximumSize(QtCore.QSize(180, 30))
        self.koroundSelect.setObjectName("koroundSelect")
        self.gridLayout.addWidget(self.koroundSelect, 1, 1, 1, 1)
        self.label_3 = QtGui.QLabel(self.widget)
        self.label_3.setMinimumSize(QtCore.QSize(150, 30))
        self.label_3.setMaximumSize(QtCore.QSize(150, 30))
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.label_7 = QtGui.QLabel(self.widget)
        self.label_7.setMinimumSize(QtCore.QSize(150, 30))
        self.label_7.setMaximumSize(QtCore.QSize(150, 30))
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 3, 0, 1, 1)
        self.penFirstSelect = QtGui.QComboBox(self.widget)
        self.penFirstSelect.setMinimumSize(QtCore.QSize(270, 30))
        self.penFirstSelect.setMaximumSize(QtCore.QSize(270, 30))
        self.penFirstSelect.setObjectName("penFirstSelect")
        self.gridLayout.addWidget(self.penFirstSelect, 3, 1, 1, 1)
        self.matchSelect = QtGui.QComboBox(self.widget)
        self.matchSelect.setMinimumSize(QtCore.QSize(330, 30))
        self.matchSelect.setMaximumSize(QtCore.QSize(330, 30))
        self.matchSelect.setObjectName("matchSelect")
        self.gridLayout.addWidget(self.matchSelect, 2, 1, 1, 1)
        self.widget1 = QtGui.QWidget(PenShootoutEntryDlg)
        self.widget1.setGeometry(QtCore.QRect(20, 190, 431, 201))
        self.widget1.setObjectName("widget1")
        self.gridLayout_2 = QtGui.QGridLayout(self.widget1)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_4 = QtGui.QLabel(self.widget1)
        self.label_4.setMinimumSize(QtCore.QSize(120, 30))
        self.label_4.setMaximumSize(QtCore.QSize(120, 30))
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 0, 0, 1, 1)
        self.shootoutID_display = QtGui.QLineEdit(self.widget1)
        self.shootoutID_display.setMinimumSize(QtCore.QSize(120, 30))
        self.shootoutID_display.setMaximumSize(QtCore.QSize(120, 30))
        self.shootoutID_display.setStyleSheet("background-color: rgb(194, 190, 186);")
        self.shootoutID_display.setMaxLength(7)
        self.shootoutID_display.setReadOnly(True)
        self.shootoutID_display.setObjectName("shootoutID_display")
        self.gridLayout_2.addWidget(self.shootoutID_display, 0, 1, 1, 1)
        self.label_8 = QtGui.QLabel(self.widget1)
        self.label_8.setMinimumSize(QtCore.QSize(150, 30))
        self.label_8.setMaximumSize(QtCore.QSize(150, 30))
        self.label_8.setObjectName("label_8")
        self.gridLayout_2.addWidget(self.label_8, 1, 0, 1, 1)
        self.roundSelect = QtGui.QComboBox(self.widget1)
        self.roundSelect.setMinimumSize(QtCore.QSize(180, 30))
        self.roundSelect.setMaximumSize(QtCore.QSize(180, 30))
        self.roundSelect.setObjectName("roundSelect")
        self.gridLayout_2.addWidget(self.roundSelect, 1, 1, 1, 1)
        self.label_5 = QtGui.QLabel(self.widget1)
        self.label_5.setMinimumSize(QtCore.QSize(120, 30))
        self.label_5.setMaximumSize(QtCore.QSize(120, 30))
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 2, 0, 1, 1)
        self.teamSelect = QtGui.QComboBox(self.widget1)
        self.teamSelect.setMinimumSize(QtCore.QSize(270, 30))
        self.teamSelect.setMaximumSize(QtCore.QSize(270, 30))
        self.teamSelect.setObjectName("teamSelect")
        self.gridLayout_2.addWidget(self.teamSelect, 2, 1, 1, 1)
        self.label_10 = QtGui.QLabel(self.widget1)
        self.label_10.setMinimumSize(QtCore.QSize(120, 30))
        self.label_10.setMaximumSize(QtCore.QSize(120, 30))
        self.label_10.setObjectName("label_10")
        self.gridLayout_2.addWidget(self.label_10, 3, 0, 1, 1)
        self.playerSelect = QtGui.QComboBox(self.widget1)
        self.playerSelect.setMinimumSize(QtCore.QSize(270, 30))
        self.playerSelect.setMaximumSize(QtCore.QSize(270, 30))
        self.playerSelect.setObjectName("playerSelect")
        self.gridLayout_2.addWidget(self.playerSelect, 3, 1, 1, 1)
        self.label_6 = QtGui.QLabel(self.widget1)
        self.label_6.setMinimumSize(QtCore.QSize(130, 30))
        self.label_6.setMaximumSize(QtCore.QSize(130, 30))
        self.label_6.setObjectName("label_6")
        self.gridLayout_2.addWidget(self.label_6, 4, 0, 1, 1)
        self.penoutcomeSelect = QtGui.QComboBox(self.widget1)
        self.penoutcomeSelect.setMinimumSize(QtCore.QSize(210, 30))
        self.penoutcomeSelect.setMaximumSize(QtCore.QSize(210, 30))
        self.penoutcomeSelect.setObjectName("penoutcomeSelect")
        self.gridLayout_2.addWidget(self.penoutcomeSelect, 4, 1, 1, 1)

        self.retranslateUi(PenShootoutEntryDlg)
        QtCore.QMetaObject.connectSlotsByName(PenShootoutEntryDlg)

    def retranslateUi(self, PenShootoutEntryDlg):
        PenShootoutEntryDlg.setWindowTitle(QtGui.QApplication.translate("PenShootoutEntryDlg", "Penalty Shootout Entry", None, QtGui.QApplication.UnicodeUTF8))
        self.firstEntry.setToolTip(QtGui.QApplication.translate("PenShootoutEntryDlg", "First Entry", None, QtGui.QApplication.UnicodeUTF8))
        self.prevEntry.setToolTip(QtGui.QApplication.translate("PenShootoutEntryDlg", "Previous Entry", None, QtGui.QApplication.UnicodeUTF8))
        self.nextEntry.setToolTip(QtGui.QApplication.translate("PenShootoutEntryDlg", "Next Entry", None, QtGui.QApplication.UnicodeUTF8))
        self.lastEntry.setToolTip(QtGui.QApplication.translate("PenShootoutEntryDlg", "Last Entry", None, QtGui.QApplication.UnicodeUTF8))
        self.addEntry.setToolTip(QtGui.QApplication.translate("PenShootoutEntryDlg", "Add Entry", None, QtGui.QApplication.UnicodeUTF8))
        self.addEntry.setText(QtGui.QApplication.translate("PenShootoutEntryDlg", "&Add", None, QtGui.QApplication.UnicodeUTF8))
        self.deleteEntry.setToolTip(QtGui.QApplication.translate("PenShootoutEntryDlg", "Delete Entry", None, QtGui.QApplication.UnicodeUTF8))
        self.deleteEntry.setText(QtGui.QApplication.translate("PenShootoutEntryDlg", "&Delete", None, QtGui.QApplication.UnicodeUTF8))
        self.saveEntry.setToolTip(QtGui.QApplication.translate("PenShootoutEntryDlg", "Delete Entry", None, QtGui.QApplication.UnicodeUTF8))
        self.saveEntry.setText(QtGui.QApplication.translate("PenShootoutEntryDlg", "&Save", None, QtGui.QApplication.UnicodeUTF8))
        self.closeButton.setToolTip(QtGui.QApplication.translate("PenShootoutEntryDlg", "Close Window", None, QtGui.QApplication.UnicodeUTF8))
        self.closeButton.setText(QtGui.QApplication.translate("PenShootoutEntryDlg", "&Close", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("PenShootoutEntryDlg", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Competition</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.compSelect.setToolTip(QtGui.QApplication.translate("PenShootoutEntryDlg", "Name of competition", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("PenShootoutEntryDlg", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Knockout Round</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.koroundSelect.setToolTip(QtGui.QApplication.translate("PenShootoutEntryDlg", "Knockout round", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("PenShootoutEntryDlg", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Match</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("PenShootoutEntryDlg", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Team Kicked First</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.penFirstSelect.setToolTip(QtGui.QApplication.translate("PenShootoutEntryDlg", "Team shooting first in penalty shootout", None, QtGui.QApplication.UnicodeUTF8))
        self.matchSelect.setToolTip(QtGui.QApplication.translate("PenShootoutEntryDlg", "Match in knockout stage", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("PenShootoutEntryDlg", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Penalty ID</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setText(QtGui.QApplication.translate("PenShootoutEntryDlg", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Round</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.roundSelect.setToolTip(QtGui.QApplication.translate("PenShootoutEntryDlg", "Shootout round", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("PenShootoutEntryDlg", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Team</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.teamSelect.setToolTip(QtGui.QApplication.translate("PenShootoutEntryDlg", "Team of penalty kick taker", None, QtGui.QApplication.UnicodeUTF8))
        self.label_10.setText(QtGui.QApplication.translate("PenShootoutEntryDlg", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Player</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.playerSelect.setToolTip(QtGui.QApplication.translate("PenShootoutEntryDlg", "Penalty kick taker", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("PenShootoutEntryDlg", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Penalty Outcome</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.penoutcomeSelect.setToolTip(QtGui.QApplication.translate("PenShootoutEntryDlg", "Penalty kick outcome", None, QtGui.QApplication.UnicodeUTF8))

import fmrd_resources_rc
