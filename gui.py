# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(1126, 719)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(mainWindow.sizePolicy().hasHeightForWidth())
        mainWindow.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        mainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(parent=mainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget_4 = QtWidgets.QWidget(parent=self.centralwidget)
        self.horizontalLayoutWidget_4.setGeometry(QtCore.QRect(0, 0, 1131, 61))
        self.horizontalLayoutWidget_4.setObjectName("horizontalLayoutWidget_4")
        self.header_Layout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_4)
        self.header_Layout.setContentsMargins(0, 0, 0, 0)
        self.header_Layout.setObjectName("header_Layout")
        self.bank_name_Label = QtWidgets.QLabel(parent=self.horizontalLayoutWidget_4)
        self.bank_name_Label.setMinimumSize(QtCore.QSize(75, 0))
        self.bank_name_Label.setMaximumSize(QtCore.QSize(500, 16777215))
        font = QtGui.QFont()
        font.setFamily("Goudy Old Style")
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.bank_name_Label.setFont(font)
        self.bank_name_Label.setAutoFillBackground(True)
        self.bank_name_Label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.bank_name_Label.setObjectName("bank_name_Label")
        self.header_Layout.addWidget(self.bank_name_Label)
        self.horizontalLayoutWidget = QtWidgets.QWidget(parent=self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(300, 60, 401, 41))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.fname_Layout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.fname_Layout.setContentsMargins(0, 0, 0, 0)
        self.fname_Layout.setObjectName("fname_Layout")
        self.searchURL_Label = QtWidgets.QLabel(parent=self.horizontalLayoutWidget)
        self.searchURL_Label.setMaximumSize(QtCore.QSize(110, 16777215))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.searchURL_Label.setFont(font)
        self.searchURL_Label.setObjectName("searchURL_Label")
        self.fname_Layout.addWidget(self.searchURL_Label, 0, QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.searchUrl_Entry = QtWidgets.QLineEdit(parent=self.horizontalLayoutWidget)
        self.searchUrl_Entry.setMinimumSize(QtCore.QSize(280, 0))
        self.searchUrl_Entry.setMaximumSize(QtCore.QSize(280, 16777215))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.searchUrl_Entry.setFont(font)
        self.searchUrl_Entry.setMaxLength(40)
        self.searchUrl_Entry.setObjectName("searchUrl_Entry")
        self.fname_Layout.addWidget(self.searchUrl_Entry)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(parent=self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(10, 60, 291, 41))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.searchName_Layout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.searchName_Layout.setContentsMargins(0, 0, 0, 0)
        self.searchName_Layout.setObjectName("searchName_Layout")
        self.searchName_Label = QtWidgets.QLabel(parent=self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.searchName_Label.setFont(font)
        self.searchName_Label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.searchName_Label.setObjectName("searchName_Label")
        self.searchName_Layout.addWidget(self.searchName_Label)
        self.searchName_Entry = QtWidgets.QLineEdit(parent=self.horizontalLayoutWidget_2)
        self.searchName_Entry.setMinimumSize(QtCore.QSize(200, 0))
        self.searchName_Entry.setMaximumSize(QtCore.QSize(200, 16777215))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.searchName_Entry.setFont(font)
        self.searchName_Entry.setObjectName("searchName_Entry")
        self.searchName_Layout.addWidget(self.searchName_Entry)
        self.items_TableWidget = QtWidgets.QTableWidget(parent=self.centralwidget)
        self.items_TableWidget.setGeometry(QtCore.QRect(10, 160, 1109, 471))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.items_TableWidget.sizePolicy().hasHeightForWidth())
        self.items_TableWidget.setSizePolicy(sizePolicy)
        self.items_TableWidget.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.items_TableWidget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.SizeAdjustPolicy.AdjustToContents)
        self.items_TableWidget.setEditTriggers(QtWidgets.QAbstractItemView.EditTrigger.NoEditTriggers)
        self.items_TableWidget.setShowGrid(False)
        self.items_TableWidget.setWordWrap(False)
        self.items_TableWidget.setCornerButtonEnabled(False)
        self.items_TableWidget.setObjectName("items_TableWidget")
        self.items_TableWidget.setColumnCount(5)
        self.items_TableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.items_TableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.items_TableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.items_TableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.items_TableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.items_TableWidget.setHorizontalHeaderItem(4, item)
        self.horizontalLayoutWidget_5 = QtWidgets.QWidget(parent=self.centralwidget)
        self.horizontalLayoutWidget_5.setGeometry(QtCore.QRect(700, 60, 141, 41))
        self.horizontalLayoutWidget_5.setObjectName("horizontalLayoutWidget_5")
        self.saveSearch_Layout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_5)
        self.saveSearch_Layout.setContentsMargins(0, 0, 0, 0)
        self.saveSearch_Layout.setObjectName("saveSearch_Layout")
        self.search_pushButton = QtWidgets.QPushButton(parent=self.horizontalLayoutWidget_5)
        self.search_pushButton.setMinimumSize(QtCore.QSize(110, 0))
        self.search_pushButton.setMaximumSize(QtCore.QSize(110, 16777215))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.search_pushButton.setFont(font)
        self.search_pushButton.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.search_pushButton.setObjectName("search_pushButton")
        self.saveSearch_Layout.addWidget(self.search_pushButton)
        self.horizontalLayoutWidget_9 = QtWidgets.QWidget(parent=self.centralwidget)
        self.horizontalLayoutWidget_9.setGeometry(QtCore.QRect(720, 630, 401, 51))
        self.horizontalLayoutWidget_9.setObjectName("horizontalLayoutWidget_9")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_9)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.exit_pushButton = QtWidgets.QPushButton(parent=self.horizontalLayoutWidget_9)
        self.exit_pushButton.setMinimumSize(QtCore.QSize(80, 0))
        self.exit_pushButton.setMaximumSize(QtCore.QSize(80, 16777215))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.exit_pushButton.setFont(font)
        self.exit_pushButton.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.exit_pushButton.setAutoDefault(False)
        self.exit_pushButton.setObjectName("exit_pushButton")
        self.horizontalLayout_2.addWidget(self.exit_pushButton)
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(parent=self.centralwidget)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(240, 100, 501, 41))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.outputText_Label = QtWidgets.QLabel(parent=self.horizontalLayoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.outputText_Label.setFont(font)
        self.outputText_Label.setText("")
        self.outputText_Label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.outputText_Label.setObjectName("outputText_Label")
        self.horizontalLayout.addWidget(self.outputText_Label)
        mainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=mainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1126, 18))
        self.menubar.setObjectName("menubar")
        mainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=mainWindow)
        self.statusbar.setObjectName("statusbar")
        mainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "GC Used Guitar Price Tracker"))
        self.bank_name_Label.setText(_translate("mainWindow", "GC Used Guitar Price Tracker"))
        self.searchURL_Label.setText(_translate("mainWindow", "HTML Filename:"))
        self.searchName_Label.setText(_translate("mainWindow", "Search Name"))
        self.items_TableWidget.setSortingEnabled(False)
        item = self.items_TableWidget.horizontalHeaderItem(1)
        item.setText(_translate("mainWindow", "Current price"))
        item = self.items_TableWidget.horizontalHeaderItem(2)
        item.setText(_translate("mainWindow", "Name"))
        item = self.items_TableWidget.horizontalHeaderItem(3)
        item.setText(_translate("mainWindow", "Date"))
        item = self.items_TableWidget.horizontalHeaderItem(4)
        item.setText(_translate("mainWindow", "List Price"))
        self.search_pushButton.setText(_translate("mainWindow", "Search"))
        self.exit_pushButton.setText(_translate("mainWindow", "EXIT"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = QtWidgets.QMainWindow()
    ui = Ui_mainWindow()
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec())
