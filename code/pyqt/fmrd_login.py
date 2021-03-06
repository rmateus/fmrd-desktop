#!/usr/bin/env python
#
#    Desktop-based data entry tool for the Football Match Result Database (FMRD)
#
#    Copyright (C) 2010-2011, Howard Hamilton
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.

from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtSql import *

from FmrdMain import (ui_fmrdlogin, ui_fmrddbfile)
from FmrdLib import Constants

"""
Contains implementation of login dialog for access to FMRD.

Classes: 
DBLoginDlg -- login dialog for database access (Postgres)
DBFileLoadDlg -- dialog for opening SQLite database file
"""

class DBFileLoadDlg(QDialog, ui_fmrddbfile.Ui_DBFileLoadDlg):
    """Implements SQLite file selection dialog for access to database application.
    
    Inherits Ui_DBFileLoadDlg (ui_fmrddbfile)
    """
    
    def __init__(self):
        """ Constructor for DBFileLoadDlg class."""
        super(DBFileLoadDlg, self).__init__()
        self.setupUi(self)
        
        self.option = Constants.USER*self.userButton.isChecked() + Constants.ADMIN*self.adminButton.isChecked()
        
        # Define signals and slots
        self.connect(self.openButton, SIGNAL("clicked()"), self.loadDatabaseFile)
        self.connect(self.cancelButton, SIGNAL("clicked()"), self.reject)
        
    def loadDatabaseFile(self):
        """Loads SQLite database file, starting in current directory of FMRD executable."""
        
        self.option = Constants.USER*self.userButton.isChecked() + Constants.ADMIN*self.adminButton.isChecked()
        dbFileName = QFileDialog.getOpenFileName(self, "Open Database File", ".", "Database file (*.db)")
        if dbFileName:
            db = QSqlDatabase.addDatabase("QSQLITE")
            db.setDatabaseName(dbFileName)
            if not db.open():
                QMessageBox.critical(None,
                    "Database Error",
                    "Unable to open or create database file. Please check your SQLite3 installation.", 
                    QMessageBox.Close)
                self.reject()
            # set foreign key checking to ON
            cmd = QSqlQuery()
            cmd.exec_("PRAGMA foreign_key = ON")
            self.accept()
        else:
            self.reject()
            
    def execute(self):
        """Calls exec_() and returns a tuple.
        
        Returns two-member tuple that contains return value of exec_() and switchboard type.
        
        """
        ok = self.exec_()
        return (ok, self.option)


class DBLoginDlg(QDialog, ui_fmrdlogin.Ui_DBLoginDlg):
    """Implements login dialog for access to database application.
    
    Inherits Ui_DBLoginDlg (ui_fmrdlogin)
    """
        
    def __init__(self):
        """ Constructor for DBLoginDlg class."""
        super(DBLoginDlg, self).__init__()
        self.setupUi(self)

        self.attempts = 0
        self.conn = 0

        self.option = Constants.USER*self.userButton.isChecked() + Constants.ADMIN*self.adminButton.isChecked()
        
        self.dbNameEdit.setFocus()
        # Define signals and slots
        self.connect(self.dbNameEdit, SIGNAL("textChanged()"), lambda: self.enableWidget(self.loginEdit))
        self.connect(self.loginEdit, SIGNAL("textChanged()"), lambda: self.enableWidget(self.passwordEdit))

    def authenticate(self):
        """ Performs database authentication.  
        
        Records value corresponding to switchboard type selection.
        If authentication is successful, hides login dialog and returns.
        If authentication is not successful, alerts user and clears entry fields.
        If three consecutive failed logins have been made, returns Rejected to caller function.
        
        """
        # get authentication data
        dbName = self.dbNameEdit.text()
        login = self.loginEdit.text()
        password = self.passwordEdit.text()

        self.option = Constants.USER*self.userButton.isChecked() + Constants.ADMIN*self.adminButton.isChecked()
        
        # attempt to open connection to database
        if self.attempts == 0:
            db = QSqlDatabase.addDatabase("QPSQL") 
            self.conn = db.connectionName()
        else:
            db = QSqlDatabase.database(self.conn, False)
        db.setDatabaseName(dbName)
        db.setUserName(login)
        db.setPassword(password)
        
        if not db.open() or dbName.isEmpty():
            # Alert user of incorrect userid/password combo
            QMessageBox.warning(None,
                "Login Incorrect",
                "The user id and password you entered are incorrect.", 
                QMessageBox.Close)
            self.attempts += 1
            
            # Clear LineEdit fields
            self.dbNameEdit.setText(QString())
            self.loginEdit.setText(QString())
            self.passwordEdit.setText(QString())
            
            # Set focus on dbNameEdit
            self.dbNameEdit.setFocus()
            
            # Alert user and send rejection to exec_() if it's 3rd consecutive fail
            if self.attempts == Constants.MAXLOGINS:
                QMessageBox.critical(None,
                    "Maximum Login Attempts Exceeded",
                    "You have exceeded the maximum number of login attempts. Press Close to exit.", 
                    QMessageBox.Close)
                self.reject()
        else:
            self.accept()

    def enableWidget(self, widget):
        """Enables widget passed as a parameter if not already enabled."""
        if not widget.isEnabled():
            widget.setEnabled(True)

    def execute(self):
        """Calls exec_() and returns a tuple.
        
        Returns two-member tuple that contains return value of exec_() and switchboard type.
        
        """
        ok = self.exec_()
        return (ok, self.option)
