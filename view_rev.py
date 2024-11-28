# -*- coding: utf-8 -*-
# Form implementation generated from reading ui file 'ui_main.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets

import numpy as np
from pyqtgraph import PlotWidget
import pyqtgraph as pg


pg.setConfigOption('foreground', 'k')

class Ui_Form(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.complite = []
        self.incomplite = []
        self.tableView =pg.TableWidget()
        self.setupUi(self)

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1280, 720)
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout_9.setContentsMargins(9, 9, 9, 9)
        self.verticalLayout_9.setSpacing(9)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.frame_11 = QtWidgets.QFrame(Form)
        self.frame_11.setMaximumSize(QtCore.QSize(16777215, 1000))
        self.frame_11.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_11.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_11.setObjectName("frame_11")
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout(self.frame_11)
        self.horizontalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_15.setSpacing(6)
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.frame = QtWidgets.QFrame(self.frame_11)
        self.frame.setMinimumSize(QtCore.QSize(0, 0))
        self.frame.setMaximumSize(QtCore.QSize(850, 16777215))
        self.frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setSpacing(6)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.frame_3 = QtWidgets.QFrame(self.frame)
        self.frame_3.setMaximumSize(QtCore.QSize(16777215, 300))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.frame_3.setFont(font)
        self.frame_3.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout_2.setContentsMargins(9, 9, 9, 9)
        self.verticalLayout_2.setSpacing(9)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.frame_3)
        self.label.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setFrameShape(QtWidgets.QFrame.Box)
        self.label.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.frame_10 = QtWidgets.QFrame(self.frame_3)
        self.frame_10.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.frame_10.setFont(font)
        self.frame_10.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_10.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_10.setObjectName("frame_10")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_10)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.radioButton_record = QtWidgets.QRadioButton(self.frame_10)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(False)
        font.setWeight(50)
        self.radioButton_record.setFont(font)
        self.radioButton_record.setObjectName("radioButton_record")
        self.horizontalLayout_2.addWidget(self.radioButton_record)
        self.radioButton_norecord = QtWidgets.QRadioButton(self.frame_10)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(False)
        font.setWeight(50)
        self.radioButton_norecord.setFont(font)
        self.radioButton_norecord.setChecked(True)
        self.radioButton_norecord.setObjectName("radioButton_norecord")
        self.horizontalLayout_2.addWidget(self.radioButton_norecord)
        self.verticalLayout_2.addWidget(self.frame_10)
        self.frame_9 = QtWidgets.QFrame(self.frame_3)
        self.frame_9.setMaximumSize(QtCore.QSize(16777215, 140))
        self.frame_9.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_9.setObjectName("frame_9")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.frame_9)
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_8.setSpacing(3)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.frame_7 = QtWidgets.QFrame(self.frame_9)
        self.frame_7.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.frame_7.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.frame_7)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame_7)
        self.pushButton_2.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout_6.addWidget(self.pushButton_2)
        self.verticalLayout_8.addWidget(self.frame_7)
        self.frame_8 = QtWidgets.QFrame(self.frame_9)
        self.frame_8.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.frame_8.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_8)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(3)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton = QtWidgets.QPushButton(self.frame_8)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.pushButton_3 = QtWidgets.QPushButton(self.frame_8)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout.addWidget(self.pushButton_3)
        self.verticalLayout_8.addWidget(self.frame_8)
        self.verticalLayout_2.addWidget(self.frame_9)
        self.verticalLayout_7.addWidget(self.frame_3)
        self.frame_19 = QtWidgets.QFrame(self.frame)
        self.frame_19.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.frame_19.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_19.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame_19.setObjectName("frame_19")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout(self.frame_19)
        self.verticalLayout_13.setContentsMargins(9, 9, 9, 9)
        self.verticalLayout_13.setSpacing(9)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.label_11 = QtWidgets.QLabel(self.frame_19)
        self.label_11.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setFrameShape(QtWidgets.QFrame.Box)
        self.label_11.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName("label_11")
        self.verticalLayout_13.addWidget(self.label_11)
        # self.label_table = QtWidgets.QLabel(self.frame_19)
        # self.label_table.setText("")
        # self.label_table.setObjectName("label_table")

        self.setupTable()

        self.verticalLayout_13.addWidget(self.tableView)

        self.verticalLayout_7.addWidget(self.frame_19)
        self.horizontalLayout_15.addWidget(self.frame)
        self.frame_5 = QtWidgets.QFrame(self.frame_11)
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame_5)
        self.verticalLayout_5.setContentsMargins(9, 9, 9, 9)
        self.verticalLayout_5.setSpacing(6)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_7 = QtWidgets.QLabel(self.frame_5)
        self.label_7.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setFrameShape(QtWidgets.QFrame.Box)
        self.label_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_5.addWidget(self.label_7)
        self.frame_22 = QtWidgets.QFrame(self.frame_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_22.sizePolicy().hasHeightForWidth())
        self.frame_22.setSizePolicy(sizePolicy)
        self.frame_22.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_22.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_22.setObjectName("frame_22")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout(self.frame_22)
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.label_result = QtWidgets.QLabel(self.frame_22)
        self.label_result.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label_result.setText("")
        self.label_result.setObjectName("label_result")
        self.horizontalLayout_11.addWidget(self.label_result)
        self.label_ori = QtWidgets.QLabel(self.frame_22)
        self.label_ori.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label_ori.setText("")
        self.label_ori.setObjectName("label_ori")
        self.horizontalLayout_11.addWidget(self.label_ori)
        self.verticalLayout_5.addWidget(self.frame_22)
        self.frame_23 = QtWidgets.QFrame(self.frame_5)
        self.frame_23.setMaximumSize(QtCore.QSize(16777215, 85))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.frame_23.setFont(font)
        self.frame_23.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_23.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_23.setObjectName("frame_23")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout(self.frame_23)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.frame_13 = QtWidgets.QFrame(self.frame_23)
        self.frame_13.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_13.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_13.setObjectName("frame_13")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_13)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_informasi_2 = QtWidgets.QLabel(self.frame_13)
        self.label_informasi_2.setMaximumSize(QtCore.QSize(300, 16777215))
        self.label_informasi_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_informasi_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_informasi_2.setObjectName("label_informasi_2")
        self.horizontalLayout_4.addWidget(self.label_informasi_2)
        self.label_10 = QtWidgets.QLabel(self.frame_13)
        self.label_10.setMaximumSize(QtCore.QSize(20, 16777215))
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_4.addWidget(self.label_10)
        self.name_file = QtWidgets.QLabel(self.frame_13)
        self.name_file.setText("")
        self.name_file.setObjectName("name_file")
        self.horizontalLayout_4.addWidget(self.name_file)
        self.horizontalLayout_12.addWidget(self.frame_13)
        self.frame_14 = QtWidgets.QFrame(self.frame_23)
        self.frame_14.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_14.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_14.setObjectName("frame_14")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.frame_14)
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_informasi_6 = QtWidgets.QLabel(self.frame_14)
        self.label_informasi_6.setMaximumSize(QtCore.QSize(300, 16777215))
        self.label_informasi_6.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_informasi_6.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_informasi_6.setObjectName("label_informasi_6")
        self.horizontalLayout_7.addWidget(self.label_informasi_6)
        self.label_17 = QtWidgets.QLabel(self.frame_14)
        self.label_17.setMaximumSize(QtCore.QSize(20, 16777215))
        self.label_17.setObjectName("label_17")
        self.horizontalLayout_7.addWidget(self.label_17)
        self.label_resolusi = QtWidgets.QLabel(self.frame_14)
        self.label_resolusi.setText("")
        self.label_resolusi.setObjectName("label_resolusi")
        self.horizontalLayout_7.addWidget(self.label_resolusi)
        self.horizontalLayout_12.addWidget(self.frame_14)
        self.frame_16 = QtWidgets.QFrame(self.frame_23)
        self.frame_16.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_16.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_16.setObjectName("frame_16")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.frame_16)
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_informasi_7 = QtWidgets.QLabel(self.frame_16)
        self.label_informasi_7.setMaximumSize(QtCore.QSize(300, 16777215))
        self.label_informasi_7.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_informasi_7.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_informasi_7.setObjectName("label_informasi_7")
        self.horizontalLayout_8.addWidget(self.label_informasi_7)
        self.label_19 = QtWidgets.QLabel(self.frame_16)
        self.label_19.setMaximumSize(QtCore.QSize(20, 16777215))
        self.label_19.setObjectName("label_19")
        self.horizontalLayout_8.addWidget(self.label_19)
        self.label_time_pro = QtWidgets.QLabel(self.frame_16)
        self.label_time_pro.setText("")
        self.label_time_pro.setObjectName("label_time_pro")
        self.horizontalLayout_8.addWidget(self.label_time_pro)
        self.horizontalLayout_12.addWidget(self.frame_16)
        self.frame_17 = QtWidgets.QFrame(self.frame_23)
        self.frame_17.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_17.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_17.setObjectName("frame_17")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.frame_17)
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_informasi_8 = QtWidgets.QLabel(self.frame_17)
        self.label_informasi_8.setMaximumSize(QtCore.QSize(300, 16777215))
        self.label_informasi_8.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_informasi_8.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_informasi_8.setObjectName("label_informasi_8")
        self.horizontalLayout_9.addWidget(self.label_informasi_8)
        self.label_21 = QtWidgets.QLabel(self.frame_17)
        self.label_21.setMaximumSize(QtCore.QSize(20, 16777215))
        self.label_21.setObjectName("label_21")
        self.horizontalLayout_9.addWidget(self.label_21)
        self.label_status = QtWidgets.QLabel(self.frame_17)
        self.label_status.setText("")
        self.label_status.setObjectName("label_status")
        self.horizontalLayout_9.addWidget(self.label_status)
        self.horizontalLayout_12.addWidget(self.frame_17)
        self.frame_24 = QtWidgets.QFrame(self.frame_23)
        self.frame_24.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_24.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_24.setObjectName("frame_24")
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout(self.frame_24)
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_13.setSpacing(0)
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.label_informasi_9 = QtWidgets.QLabel(self.frame_24)
        self.label_informasi_9.setMaximumSize(QtCore.QSize(300, 16777215))
        self.label_informasi_9.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_informasi_9.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_informasi_9.setObjectName("label_informasi_9")
        self.horizontalLayout_13.addWidget(self.label_informasi_9)
        self.label_22 = QtWidgets.QLabel(self.frame_24)
        self.label_22.setMaximumSize(QtCore.QSize(20, 16777215))
        self.label_22.setObjectName("label_22")
        self.horizontalLayout_13.addWidget(self.label_22)
        self.label_complite = QtWidgets.QLabel(self.frame_24)
        self.label_complite.setText("")
        self.label_complite.setObjectName("label_complite")
        self.horizontalLayout_13.addWidget(self.label_complite)
        self.horizontalLayout_12.addWidget(self.frame_24)
        self.frame_25 = QtWidgets.QFrame(self.frame_23)
        self.frame_25.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_25.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_25.setObjectName("frame_25")
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout(self.frame_25)
        self.horizontalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_14.setSpacing(0)
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.label_informasi_10 = QtWidgets.QLabel(self.frame_25)
        self.label_informasi_10.setMaximumSize(QtCore.QSize(300, 16777215))
        self.label_informasi_10.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_informasi_10.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_informasi_10.setObjectName("label_informasi_10")
        self.horizontalLayout_14.addWidget(self.label_informasi_10)
        self.label_23 = QtWidgets.QLabel(self.frame_25)
        self.label_23.setMaximumSize(QtCore.QSize(20, 16777215))
        self.label_23.setObjectName("label_23")
        self.horizontalLayout_14.addWidget(self.label_23)
        self.label_incomp = QtWidgets.QLabel(self.frame_25)
        self.label_incomp.setText("")
        self.label_incomp.setObjectName("label_incomp")
        self.horizontalLayout_14.addWidget(self.label_incomp)
        self.horizontalLayout_12.addWidget(self.frame_25)
        self.verticalLayout_5.addWidget(self.frame_23)
        self.frame_12 = QtWidgets.QFrame(self.frame_5)
        self.frame_12.setMaximumSize(QtCore.QSize(16777215, 60))
        self.frame_12.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_12.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_12.setObjectName("frame_12")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.frame_12)
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_10.setSpacing(3)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.pushButton_backward = QtWidgets.QPushButton(self.frame_12)
        self.pushButton_backward.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_backward.setFont(font)
        self.pushButton_backward.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icon/step-backward.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_backward.setIcon(icon)
        self.pushButton_backward.setObjectName("pushButton_backward")
        self.horizontalLayout_10.addWidget(self.pushButton_backward)
        self.pushButton_play = QtWidgets.QPushButton(self.frame_12)
        self.pushButton_play.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_play.setFont(font)
        self.pushButton_play.setStyleSheet("")
        self.pushButton_play.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("icon/play.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        icon1.addPixmap(QtGui.QPixmap("icon/pause.png"), QtGui.QIcon.Disabled, QtGui.QIcon.On)
        self.pushButton_play.setIcon(icon1)
        self.pushButton_play.setObjectName("pushButton_play")
        self.horizontalLayout_10.addWidget(self.pushButton_play)
        self.pushButton_forward = QtWidgets.QPushButton(self.frame_12)
        self.pushButton_forward.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_forward.setFont(font)
        self.pushButton_forward.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("icon/step-forward.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_forward.setIcon(icon2)
        self.pushButton_forward.setObjectName("pushButton_forward")
        self.horizontalLayout_10.addWidget(self.pushButton_forward)
        self.verticalLayout_5.addWidget(self.frame_12)
        self.horizontalLayout_15.addWidget(self.frame_5)
        self.verticalLayout_9.addWidget(self.frame_11)
        self.frame_2 = QtWidgets.QFrame(Form)
        self.frame_2.setMinimumSize(QtCore.QSize(900, 0))
        self.frame_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(9)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_6 = QtWidgets.QFrame(self.frame_2)
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_6)
        self.verticalLayout_4.setContentsMargins(9, 9, 9, 9)
        self.verticalLayout_4.setSpacing(6)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_9 = QtWidgets.QLabel(self.frame_6)
        self.label_9.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setFrameShape(QtWidgets.QFrame.Box)
        self.label_9.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.verticalLayout_4.addWidget(self.label_9)
        self.frame_4 = QtWidgets.QFrame(self.frame_6)
        self.frame_4.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_4)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.frame_21 = QtWidgets.QFrame(self.frame_4)

        self.frame_21.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_21.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_21.setObjectName("frame_21")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.frame_21)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_graph_mdl_1 = QtWidgets.QLabel(self.frame_21)
        self.label_graph_mdl_1.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label_graph_mdl_1.setText("")
        self.label_graph_mdl_1.setObjectName("label_graph_mdl_1")
        self.horizontalLayout_6.addWidget(self.label_graph_mdl_1)
        self.label_graph_mdl_2 = QtWidgets.QLabel(self.frame_21)
        self.label_graph_mdl_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label_graph_mdl_2.setText("")
        self.label_graph_mdl_2.setObjectName("label_graph_mdl_2")
        self.horizontalLayout_6.addWidget(self.label_graph_mdl_2)
        # self.label_graph_mdl_3 = QtWidgets.QLabel(self.frame_21)
        # self.label_graph_mdl_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        # self.label_graph_mdl_3.setText("")
        # self.label_graph_mdl_3.setObjectName("label_graph_mdl_3")
        # self.horizontalLayout_6.addWidget(self.label_graph_mdl_3)

        self.graph_comp = PlotWidget(Form)

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.graph_comp.sizePolicy().hasHeightForWidth())
        self.graph_comp.setSizePolicy(sizePolicy)

        self.graph_comp.setBackground("w")      # w = white
        # self.graph_comp.drawForeground("k")
        self.graph_comp.showGrid(x=True, y=True)
        self.graph_comp.setLabels(left='Percentage', bottom='Complite')
        self.graph_comp.setObjectName('graph_comp')
        self.horizontalLayout_6.addWidget(self.graph_comp)

        self.complite_line = self.graph_comp.plot([], pen=pg.mkPen(0, 255, 0))

        # self.label_graph_mdl_4 = QtWidgets.QLabel(self.frame_21)
        # self.label_graph_mdl_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        # self.label_graph_mdl_4.setText("")
        # self.label_graph_mdl_4.setObjectName("label_graph_mdl_4")
        # self.horizontalLayout_6.addWidget(self.label_graph_mdl_4)

        self.graph_incomp = PlotWidget(Form)
        self.graph_incomp.setSizePolicy(sizePolicy)

        self.graph_incomp.setBackground("w")      # w = white
        self.graph_incomp.showGrid(x=True, y=True)
        self.graph_incomp.setLabels(left='Percentage', bottom='Incomplite')
        self.graph_incomp.setObjectName('graph_comp')
        self.horizontalLayout_6.addWidget(self.graph_incomp)

        self.incomplite_line = self.graph_incomp.plot([], pen=pg.mkPen(255, 0, 0))

        self.verticalLayout_3.addWidget(self.frame_21)
        self.frame_20 = QtWidgets.QFrame(self.frame_4)
        self.frame_20.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_20.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_20.setObjectName("frame_20")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frame_20)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_graph_mdl_5 = QtWidgets.QLabel(self.frame_20)
        self.label_graph_mdl_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label_graph_mdl_5.setText("")
        self.label_graph_mdl_5.setObjectName("label_graph_mdl_5")
        self.horizontalLayout_5.addWidget(self.label_graph_mdl_5)
        self.label_graph_mdl_6 = QtWidgets.QLabel(self.frame_20)
        self.label_graph_mdl_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label_graph_mdl_6.setText("")
        self.label_graph_mdl_6.setObjectName("label_graph_mdl_6")
        self.horizontalLayout_5.addWidget(self.label_graph_mdl_6)
        self.label_graph_mdl_7 = QtWidgets.QLabel(self.frame_20)
        self.label_graph_mdl_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label_graph_mdl_7.setText("")
        self.label_graph_mdl_7.setObjectName("label_graph_mdl_7")
        self.horizontalLayout_5.addWidget(self.label_graph_mdl_7)
        self.label_graph_mdl_8 = QtWidgets.QLabel(self.frame_20)
        self.label_graph_mdl_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label_graph_mdl_8.setText("")
        self.label_graph_mdl_8.setObjectName("label_graph_mdl_8")
        self.horizontalLayout_5.addWidget(self.label_graph_mdl_8)
        self.verticalLayout_3.addWidget(self.frame_20)
        self.verticalLayout_4.addWidget(self.frame_4)
        self.verticalLayout.addWidget(self.frame_6)
        self.verticalLayout_9.addWidget(self.frame_2)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Menu"))
        self.radioButton_record.setText(_translate("Form", "Record"))
        self.radioButton_norecord.setText(_translate("Form", "No Record"))
        self.pushButton_2.setText(_translate("Form", "Load Video"))
        self.pushButton.setText(_translate("Form", "Save"))
        self.pushButton_3.setText(_translate("Form", "Clear"))
        self.label_11.setText(_translate("Form", "Table Informations"))
        self.label_7.setText(_translate("Form", "Result"))
        self.label_informasi_2.setText(_translate("Form", "Name File "))
        self.label_10.setText(_translate("Form", ":"))
        self.label_informasi_6.setText(_translate("Form", "Resolusi"))
        self.label_17.setText(_translate("Form", ":"))
        self.label_informasi_7.setText(_translate("Form", "Time Processing"))
        self.label_19.setText(_translate("Form", ":"))
        self.label_informasi_8.setText(_translate("Form", "Status"))
        self.label_21.setText(_translate("Form", ":"))
        self.label_informasi_9.setText(_translate("Form", "Complite"))
        self.label_22.setText(_translate("Form", ":"))
        self.label_informasi_10.setText(_translate("Form", "Incomplite"))
        self.label_23.setText(_translate("Form", ":"))
        self.label_9.setText(_translate("Form", "Graph"))



    def set_image(self, label, frame):
        h, w, c = frame.shape
        bytes_per_line = 3 * w
        qimg = QtGui.QImage(frame.data, w, h, bytes_per_line, QtGui.QImage.Format.Format_RGB888)
        img = QtGui.QPixmap.fromImage(qimg)
        label.setPixmap((img.scaled(label.size())))

    def convert_img(self, frame):
        h, w, c = frame.shape
        bytes_per_line = 3 * w
        qimg = QtGui.QImage(frame.data, w, h, bytes_per_line, QtGui.QImage.Format.Format_RGB888)
        return QtGui.QPixmap.fromImage(qimg)

    def update_img(self, frame_ori, frame_pred, cal_com, cal_incom):
        img_ori = self.convert_img(frame_ori)
        img_pred = self.convert_img(frame_pred)

        img_ori = img_ori.scaled(self.label_ori.size())
        img_pred = img_pred.scaled(self.label_result.size())

        self.label_complite.setText(f"{cal_com}")
        self.label_incomp.setText(f"{cal_incom}")
        self.complite.append(cal_com)
        self.incomplite.append(cal_incom)

        self.setDataGraph()

        self.setDataTable()

        self.label_result.setPixmap(img_ori)
        self.label_ori.setPixmap(img_pred)

    def setDataGraph(self):
        x_comp = np.arange(0, len(self.complite))
        x_incom = np.arange(0, len(self.incomplite))

        self.complite_line.setData(x_comp, self.complite)
        self.incomplite_line.setData(x_incom, self.incomplite)

    def setIconPlay(self, condition):
        src = 'icon/play.png' if condition == 1 else 'icon/pause.png'
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(src), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.pushButton_play.setIcon(icon)

    def graphModel(self, graph, label):
        img = self.convert_img(graph)

        label.setPixmap((img.scaled(label.size())))

    def setupTable(self):
        header = ["Complite", "Incomplite", "Total", "Km/m", "Information"]

        data = [ {header[i]: ' ' for i in range(5)} for _ in range(9)]  # hasilnya sama dgn komentar diatas

        self.tableView.setData(data)
        # self.tableView.saveAll()

        self.tableView.verticalHeader().setVisible(False)

        self.tableView.setColumnWidth(0, 153)
        self.tableView.setColumnWidth(1, 153)
        self.tableView.setColumnWidth(2, 153)
        self.tableView.setColumnWidth(3, 153)
        self.tableView.setColumnWidth(5, 153)

        for row in range(self.tableView.rowCount()):
            for col in range(self.tableView.columnCount()):
                item = self.tableView.item(row, col)
                if item:

                    item.setTextAlignment(QtCore.Qt.AlignCenter)

    def looping(self):
        """
        a[i:i+lim] => ambil nilai a dari index i sampai i+lim
        range(0, 4, 2) => buatkan range dari 0 sampai 4 tapi lomcat 2 nilai
        """
        a = [1, 2, 3, 4, 5, 6, 7, 8]
        b = ['a', 'b', 'c', 'd', 'e', 'f']
        lim = 2
        ranges = len(a) if len(a) > len(b) else len(b)
        t = [(a[i:i+lim], b[i:i+lim]) for i in range(0, ranges, lim)]
        print(t)

    def setDataTable(self):
        max_frame = 20
        hd = ["Complite", "Incomplite", "Total", "Km/m", "Information"]
        ranges = len(self.complite) if len(self.complite) > len(self.incomplite) else len(self.incomplite)
        data = []

        # penjelasan ada di fungsi looping
        for i in range(0, ranges, max_frame):
            num_com = sum(self.complite[i:i + max_frame])
            num_incom = sum(self.incomplite[i:i + max_frame])
            information = "Success" if num_incom == 0 else "Repair"
            data.append({hd[0]: num_com, hd[1]: num_incom, hd[2]: num_com+num_incom, hd[3]: f"{i} Meter", hd[4]: information})

        # print(data)

        self.tableView.setData(data)
        # self.tableView.saveAll()

        self.tableView.verticalHeader().setVisible(False)

        self.tableView.setColumnWidth(0, 153)
        self.tableView.setColumnWidth(1, 153)
        self.tableView.setColumnWidth(2, 153)
        self.tableView.setColumnWidth(3, 153)
        self.tableView.setColumnWidth(5, 153)

        for row in range(self.tableView.rowCount()):
            for col in range(self.tableView.columnCount()):
                item = self.tableView.item(row, col)
                if item:

                    item.setTextAlignment(QtCore.Qt.AlignCenter)

    def a(self):
        t_com = len(self.complite)
        t_incom = len(self.incomplite)
        total_data = t_com + t_incom
        max_frame = 20

        data = []

        hd = ["Complite", "Incomplite", "Total", "Km/m", "Information"]

        for i in range(0, total_data):
            num_com, num_incom = 0, 0
            num_com += t_com
            num_incom += t_incom
            if i % max_frame == 0 and i != 0:
                if i == max_frame:
                    information = "Success" if self.incomplite == 0 else "Repair"
                    [data.append({hd[0]: num_com, hd[1]: num_incom, hd[2]: total_data, hd[3]: f"{i} Meter", hd[4]: information})]
                    # [data.append({hd[0]: self.complite, hd[1]: self.incomplite, hd[2]: total_data, hd[3]: i, hd[4]: information}) for i in range(1, len(self.t_red))]
                    # totalData.append([complite, incomplite, complite + incomplite, f"{x} Meter", information])
                if i > max_frame:
                    num_com, num_incom = 0, 0
                    num_com += t_com
                    num_incom += t_incom
                    [data.append({hd[0]: num_com, hd[1]: num_incom, hd[2]: total_data, hd[3]: f"{i} Meter", hd[4]: information})]

        self.tableView.setData(data)
        # self.tableView.saveAll()

        self.tableView.verticalHeader().setVisible(False)

        self.tableView.setColumnWidth(0, 153)
        self.tableView.setColumnWidth(1, 153)
        self.tableView.setColumnWidth(2, 153)
        self.tableView.setColumnWidth(3, 153)
        self.tableView.setColumnWidth(5, 153)

        for row in range(self.tableView.rowCount()):
            for col in range(self.tableView.columnCount()):
                item = self.tableView.item(row, col)
                if item:

                    item.setTextAlignment(QtCore.Qt.AlignCenter)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = Ui_Form()
    ui.show()
    sys.exit(app.exec_())
