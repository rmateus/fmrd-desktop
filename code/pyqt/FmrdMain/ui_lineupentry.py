# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui/lineup_select.ui'
#
# Created: Mon Aug  8 00:07:27 2011
#      by: PyQt4 UI code generator 4.7.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_LineupEntryDlg(object):
    def setupUi(self, LineupEntryDlg):
        LineupEntryDlg.setObjectName("LineupEntryDlg")
        LineupEntryDlg.resize(500, 375)
        LineupEntryDlg.setMinimumSize(QtCore.QSize(500, 375))
        LineupEntryDlg.setMaximumSize(QtCore.QSize(500, 375))
        self.layoutWidget = QtGui.QWidget(LineupEntryDlg)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 280, 361, 41))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.firstEntry = QtGui.QPushButton(self.layoutWidget)
        self.firstEntry.setMinimumSize(QtCore.QSize(81, 31))
        self.firstEntry.setMaximumSize(QtCore.QSize(81, 31))
        self.firstEntry.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/images/first.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.firstEntry.setIcon(icon)
        self.firstEntry.setObjectName("firstEntry")
        self.horizontalLayout_2.addWidget(self.firstEntry)
        self.prevEntry = QtGui.QPushButton(self.layoutWidget)
        self.prevEntry.setMinimumSize(QtCore.QSize(81, 31))
        self.prevEntry.setMaximumSize(QtCore.QSize(81, 31))
        self.prevEntry.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/images/prev.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.prevEntry.setIcon(icon1)
        self.prevEntry.setObjectName("prevEntry")
        self.horizontalLayout_2.addWidget(self.prevEntry)
        self.nextEntry = QtGui.QPushButton(self.layoutWidget)
        self.nextEntry.setMinimumSize(QtCore.QSize(81, 31))
        self.nextEntry.setMaximumSize(QtCore.QSize(81, 31))
        self.nextEntry.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/images/next.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.nextEntry.setIcon(icon2)
        self.nextEntry.setObjectName("nextEntry")
        self.horizontalLayout_2.addWidget(self.nextEntry)
        self.lastEntry = QtGui.QPushButton(self.layoutWidget)
        self.lastEntry.setMinimumSize(QtCore.QSize(81, 31))
        self.lastEntry.setMaximumSize(QtCore.QSize(81, 31))
        self.lastEntry.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/images/last.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.lastEntry.setIcon(icon3)
        self.lastEntry.setObjectName("lastEntry")
        self.horizontalLayout_2.addWidget(self.lastEntry)
        self.line = QtGui.QFrame(LineupEntryDlg)
        self.line.setGeometry(QtCore.QRect(360, 10, 20, 311))
        self.line.setFrameShape(QtGui.QFrame.VLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName("line")
        self.layoutWidget1 = QtGui.QWidget(LineupEntryDlg)
        self.layoutWidget1.setGeometry(QtCore.QRect(10, 10, 351, 221))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.gridLayout = QtGui.QGridLayout(self.layoutWidget1)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtGui.QLabel(self.layoutWidget1)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.matchID_display = QtGui.QLineEdit(self.layoutWidget1)
        self.matchID_display.setMinimumSize(QtCore.QSize(120, 27))
        self.matchID_display.setMaximumSize(QtCore.QSize(120, 27))
        self.matchID_display.setStyleSheet("background-color: rgb(194, 190, 186);")
        self.matchID_display.setMaxLength(7)
        self.matchID_display.setReadOnly(True)
        self.matchID_display.setObjectName("matchID_display")
        self.gridLayout.addWidget(self.matchID_display, 0, 1, 1, 1)
        self.label_2 = QtGui.QLabel(self.layoutWidget1)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.team_display = QtGui.QLineEdit(self.layoutWidget1)
        self.team_display.setMinimumSize(QtCore.QSize(231, 31))
        self.team_display.setMaximumSize(QtCore.QSize(231, 31))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(194, 190, 186))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(194, 190, 186))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(194, 190, 186))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(194, 190, 186))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(194, 190, 186))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(194, 190, 186))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.team_display.setPalette(palette)
        self.team_display.setReadOnly(True)
        self.team_display.setObjectName("team_display")
        self.gridLayout.addWidget(self.team_display, 1, 1, 1, 1)
        self.label_3 = QtGui.QLabel(self.layoutWidget1)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.lineupID_display = QtGui.QLineEdit(self.layoutWidget1)
        self.lineupID_display.setMinimumSize(QtCore.QSize(120, 27))
        self.lineupID_display.setMaximumSize(QtCore.QSize(120, 27))
        self.lineupID_display.setStyleSheet("background-color: rgb(194, 190, 186);")
        self.lineupID_display.setMaxLength(7)
        self.lineupID_display.setReadOnly(True)
        self.lineupID_display.setObjectName("lineupID_display")
        self.gridLayout.addWidget(self.lineupID_display, 2, 1, 1, 1)
        self.label_4 = QtGui.QLabel(self.layoutWidget1)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)
        self.playerSelect = QtGui.QComboBox(self.layoutWidget1)
        self.playerSelect.setMinimumSize(QtCore.QSize(231, 31))
        self.playerSelect.setMaximumSize(QtCore.QSize(231, 31))
        self.playerSelect.setObjectName("playerSelect")
        self.gridLayout.addWidget(self.playerSelect, 3, 1, 1, 1)
        self.label_5 = QtGui.QLabel(self.layoutWidget1)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 4, 0, 1, 1)
        self.positionSelect = QtGui.QComboBox(self.layoutWidget1)
        self.positionSelect.setMinimumSize(QtCore.QSize(231, 31))
        self.positionSelect.setMaximumSize(QtCore.QSize(231, 31))
        self.positionSelect.setObjectName("positionSelect")
        self.gridLayout.addWidget(self.positionSelect, 4, 1, 1, 1)
        self.layoutWidget2 = QtGui.QWidget(LineupEntryDlg)
        self.layoutWidget2.setGeometry(QtCore.QRect(40, 230, 291, 51))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.horizontalLayout = QtGui.QHBoxLayout(self.layoutWidget2)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.startingButton = QtGui.QCheckBox(self.layoutWidget2)
        self.startingButton.setObjectName("startingButton")
        self.horizontalLayout.addWidget(self.startingButton)
        spacerItem = QtGui.QSpacerItem(58, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.captButton = QtGui.QCheckBox(self.layoutWidget2)
        self.captButton.setObjectName("captButton")
        self.horizontalLayout.addWidget(self.captButton)
        self.layoutWidget3 = QtGui.QWidget(LineupEntryDlg)
        self.layoutWidget3.setGeometry(QtCore.QRect(10, 321, 487, 41))
        self.layoutWidget3.setObjectName("layoutWidget3")
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.layoutWidget3)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_6 = QtGui.QLabel(self.layoutWidget3)
        self.label_6.setMinimumSize(QtCore.QSize(71, 17))
        self.label_6.setMaximumSize(QtCore.QSize(71, 17))
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_3.addWidget(self.label_6)
        self.NumStarter_display = QtGui.QLineEdit(self.layoutWidget3)
        self.NumStarter_display.setMinimumSize(QtCore.QSize(30, 30))
        self.NumStarter_display.setMaximumSize(QtCore.QSize(30, 30))
        self.NumStarter_display.setMaxLength(2)
        self.NumStarter_display.setReadOnly(True)
        self.NumStarter_display.setObjectName("NumStarter_display")
        self.horizontalLayout_3.addWidget(self.NumStarter_display)
        self.label_7 = QtGui.QLabel(self.layoutWidget3)
        self.label_7.setMinimumSize(QtCore.QSize(91, 17))
        self.label_7.setMaximumSize(QtCore.QSize(91, 17))
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_3.addWidget(self.label_7)
        self.NumSubs_display = QtGui.QLineEdit(self.layoutWidget3)
        self.NumSubs_display.setMinimumSize(QtCore.QSize(30, 30))
        self.NumSubs_display.setMaximumSize(QtCore.QSize(30, 30))
        self.NumSubs_display.setMaxLength(2)
        self.NumSubs_display.setReadOnly(True)
        self.NumSubs_display.setObjectName("NumSubs_display")
        self.horizontalLayout_3.addWidget(self.NumSubs_display)
        self.captStatus = QtGui.QLabel(self.layoutWidget3)
        self.captStatus.setMinimumSize(QtCore.QSize(71, 17))
        self.captStatus.setMaximumSize(QtCore.QSize(71, 17))
        self.captStatus.setObjectName("captStatus")
        self.horizontalLayout_3.addWidget(self.captStatus)
        self.NumCapt_display = QtGui.QLineEdit(self.layoutWidget3)
        self.NumCapt_display.setMinimumSize(QtCore.QSize(30, 30))
        self.NumCapt_display.setMaximumSize(QtCore.QSize(30, 30))
        self.NumCapt_display.setMaxLength(2)
        self.NumCapt_display.setReadOnly(True)
        self.NumCapt_display.setObjectName("NumCapt_display")
        self.horizontalLayout_3.addWidget(self.NumCapt_display)
        self.captStatus_2 = QtGui.QLabel(self.layoutWidget3)
        self.captStatus_2.setMinimumSize(QtCore.QSize(90, 17))
        self.captStatus_2.setMaximumSize(QtCore.QSize(90, 17))
        self.captStatus_2.setObjectName("captStatus_2")
        self.horizontalLayout_3.addWidget(self.captStatus_2)
        self.NumGK_display = QtGui.QLineEdit(self.layoutWidget3)
        self.NumGK_display.setMinimumSize(QtCore.QSize(30, 30))
        self.NumGK_display.setMaximumSize(QtCore.QSize(30, 30))
        self.NumGK_display.setMaxLength(2)
        self.NumGK_display.setReadOnly(True)
        self.NumGK_display.setObjectName("NumGK_display")
        self.horizontalLayout_3.addWidget(self.NumGK_display)
        self.widget = QtGui.QWidget(LineupEntryDlg)
        self.widget.setGeometry(QtCore.QRect(380, 30, 101, 191))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtGui.QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.addEntry = QtGui.QPushButton(self.widget)
        self.addEntry.setMinimumSize(QtCore.QSize(80, 33))
        self.addEntry.setMaximumSize(QtCore.QSize(80, 33))
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/images/add.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.addEntry.setIcon(icon4)
        self.addEntry.setObjectName("addEntry")
        self.verticalLayout.addWidget(self.addEntry)
        spacerItem1 = QtGui.QSpacerItem(20, 13, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.saveEntry = QtGui.QPushButton(self.widget)
        self.saveEntry.setMinimumSize(QtCore.QSize(80, 33))
        self.saveEntry.setMaximumSize(QtCore.QSize(80, 33))
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/images/save.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.saveEntry.setIcon(icon5)
        self.saveEntry.setObjectName("saveEntry")
        self.verticalLayout.addWidget(self.saveEntry)
        spacerItem2 = QtGui.QSpacerItem(20, 13, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem2)
        self.deleteEntry = QtGui.QPushButton(self.widget)
        self.deleteEntry.setMinimumSize(QtCore.QSize(80, 33))
        self.deleteEntry.setMaximumSize(QtCore.QSize(80, 33))
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/images/delete.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.deleteEntry.setIcon(icon6)
        self.deleteEntry.setObjectName("deleteEntry")
        self.verticalLayout.addWidget(self.deleteEntry)
        spacerItem3 = QtGui.QSpacerItem(20, 13, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem3)
        self.closeButton = QtGui.QPushButton(self.widget)
        self.closeButton.setMinimumSize(QtCore.QSize(80, 33))
        self.closeButton.setMaximumSize(QtCore.QSize(80, 33))
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/images/quit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.closeButton.setIcon(icon7)
        self.closeButton.setObjectName("closeButton")
        self.verticalLayout.addWidget(self.closeButton)
        self.label.setBuddy(self.matchID_display)

        self.retranslateUi(LineupEntryDlg)
        QtCore.QMetaObject.connectSlotsByName(LineupEntryDlg)

    def retranslateUi(self, LineupEntryDlg):
        LineupEntryDlg.setWindowTitle(QtGui.QApplication.translate("LineupEntryDlg", "Player Lineup Entry", None, QtGui.QApplication.UnicodeUTF8))
        self.firstEntry.setToolTip(QtGui.QApplication.translate("LineupEntryDlg", "First Entry", None, QtGui.QApplication.UnicodeUTF8))
        self.prevEntry.setToolTip(QtGui.QApplication.translate("LineupEntryDlg", "Previous Entry", None, QtGui.QApplication.UnicodeUTF8))
        self.nextEntry.setToolTip(QtGui.QApplication.translate("LineupEntryDlg", "Next Entry", None, QtGui.QApplication.UnicodeUTF8))
        self.lastEntry.setToolTip(QtGui.QApplication.translate("LineupEntryDlg", "Last Entry", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("LineupEntryDlg", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Sans Serif\'; font-weight:600;\">Match &amp;ID</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("LineupEntryDlg", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Team</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("LineupEntryDlg", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Lineup ID</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("LineupEntryDlg", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Player</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("LineupEntryDlg", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Position</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.startingButton.setText(QtGui.QApplication.translate("LineupEntryDlg", "Starting Player", None, QtGui.QApplication.UnicodeUTF8))
        self.captButton.setText(QtGui.QApplication.translate("LineupEntryDlg", "Captain", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("LineupEntryDlg", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Starters</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.NumStarter_display.setToolTip(QtGui.QApplication.translate("LineupEntryDlg", "Number of starters", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("LineupEntryDlg", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Substitutes</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.NumSubs_display.setToolTip(QtGui.QApplication.translate("LineupEntryDlg", "Number of starters", None, QtGui.QApplication.UnicodeUTF8))
        self.captStatus.setText(QtGui.QApplication.translate("LineupEntryDlg", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Captain</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.NumCapt_display.setToolTip(QtGui.QApplication.translate("LineupEntryDlg", "Number of starters", None, QtGui.QApplication.UnicodeUTF8))
        self.captStatus_2.setText(QtGui.QApplication.translate("LineupEntryDlg", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Goalkeeper</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.NumGK_display.setToolTip(QtGui.QApplication.translate("LineupEntryDlg", "Number of starters", None, QtGui.QApplication.UnicodeUTF8))
        self.addEntry.setToolTip(QtGui.QApplication.translate("LineupEntryDlg", "Add Entry", None, QtGui.QApplication.UnicodeUTF8))
        self.addEntry.setText(QtGui.QApplication.translate("LineupEntryDlg", "&Add", None, QtGui.QApplication.UnicodeUTF8))
        self.saveEntry.setToolTip(QtGui.QApplication.translate("LineupEntryDlg", "Delete Entry", None, QtGui.QApplication.UnicodeUTF8))
        self.saveEntry.setText(QtGui.QApplication.translate("LineupEntryDlg", "&Save", None, QtGui.QApplication.UnicodeUTF8))
        self.deleteEntry.setToolTip(QtGui.QApplication.translate("LineupEntryDlg", "Delete Entry", None, QtGui.QApplication.UnicodeUTF8))
        self.deleteEntry.setText(QtGui.QApplication.translate("LineupEntryDlg", "&Delete", None, QtGui.QApplication.UnicodeUTF8))
        self.closeButton.setToolTip(QtGui.QApplication.translate("LineupEntryDlg", "Close Window", None, QtGui.QApplication.UnicodeUTF8))
        self.closeButton.setText(QtGui.QApplication.translate("LineupEntryDlg", "&Close", None, QtGui.QApplication.UnicodeUTF8))

import fmrd_resources_rc
