# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'f:\My_Projects\Temperature-Uart\src\orders_inquire.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_TabWidget(object):
    def setupUi(self, TabWidget):
        TabWidget.setObjectName("TabWidget")
        TabWidget.resize(801, 564)
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(14)
        TabWidget.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("f:\\My_Projects\\Temperature-Uart\\src\\../ico/find.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        TabWidget.setWindowIcon(icon)
        TabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        TabWidget.setDocumentMode(False)
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(20, 220, 51, 51))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("f:\\My_Projects\\Temperature-Uart\\src\\../ico/sdml.ico"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.textBrowser_1 = QtWidgets.QTextBrowser(self.tab)
        self.textBrowser_1.setGeometry(QtCore.QRect(89, 21, 691, 491))
        font = QtGui.QFont()
        font.setFamily("华文楷体")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.textBrowser_1.setFont(font)
        self.textBrowser_1.setObjectName("textBrowser_1")
        TabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.tab_2)
        self.textBrowser_2.setGeometry(QtCore.QRect(89, 21, 691, 491))
        font = QtGui.QFont()
        font.setFamily("华文楷体")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.textBrowser_2.setFont(font)
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.label_2 = QtWidgets.QLabel(self.tab_2)
        self.label_2.setGeometry(QtCore.QRect(20, 220, 51, 51))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("f:\\My_Projects\\Temperature-Uart\\src\\../ico/cxml.ico"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        TabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.textBrowser_3 = QtWidgets.QTextBrowser(self.tab_3)
        self.textBrowser_3.setGeometry(QtCore.QRect(89, 30, 691, 481))
        font = QtGui.QFont()
        font.setFamily("华文楷体")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.textBrowser_3.setFont(font)
        self.textBrowser_3.setObjectName("textBrowser_3")
        self.label_3 = QtWidgets.QLabel(self.tab_3)
        self.label_3.setGeometry(QtCore.QRect(20, 220, 51, 51))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("f:\\My_Projects\\Temperature-Uart\\src\\../ico/bcml.ico"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        TabWidget.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.textBrowser_4 = QtWidgets.QTextBrowser(self.tab_4)
        self.textBrowser_4.setGeometry(QtCore.QRect(89, 31, 691, 481))
        font = QtGui.QFont()
        font.setFamily("华文楷体")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.textBrowser_4.setFont(font)
        self.textBrowser_4.setObjectName("textBrowser_4")
        self.label_4 = QtWidgets.QLabel(self.tab_4)
        self.label_4.setGeometry(QtCore.QRect(20, 220, 51, 51))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("f:\\My_Projects\\Temperature-Uart\\src\\../ico/xx.ico"))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        TabWidget.addTab(self.tab_4, "")

        self.retranslateUi(TabWidget)
        TabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(TabWidget)

    def retranslateUi(self, TabWidget):
        _translate = QtCore.QCoreApplication.translate
        TabWidget.setWindowTitle(_translate("TabWidget", "指令查询框"))
        TabWidget.setTabText(TabWidget.indexOf(self.tab), _translate("TabWidget", "设定命令"))
        TabWidget.setTabText(TabWidget.indexOf(self.tab_2), _translate("TabWidget", "查询命令"))
        TabWidget.setTabText(TabWidget.indexOf(self.tab_3), _translate("TabWidget", "保存命令"))
        TabWidget.setTabText(TabWidget.indexOf(self.tab_4), _translate("TabWidget", "其它命令"))
