# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Beta4.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import pf_02

class Ui_RGS(object):
    def setupUi(self, RGS):
        RGS.setObjectName("RGS")
        RGS.resize(886, 767)
        RGS.setMinimumSize(QtCore.QSize(200, 201))
        RGS.setMaximumSize(QtCore.QSize(1000, 1000))
        RGS.setStyleSheet("#frame{\n"
"background: rgba(0,0,0,0.7);\n"
"}\n"
"#BG{\n"
"background: url(:/img/PF.jpg);\n"
"background-repeat:norepeat;\n"
"}\n"
"#credits{\n"
"color:white;\n"
"}")
        self.BG = QtWidgets.QWidget(RGS)
        self.BG.setMinimumSize(QtCore.QSize(820, 547))
        self.BG.setObjectName("BG")
        self.frame = QtWidgets.QFrame(self.BG)
        self.frame.setGeometry(QtCore.QRect(50, 40, 791, 681))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.frame.setFont(font)
        self.frame.setStyleSheet("*{\n"
"bavkground: rgba(0, 0, 0, 0.9)\n"
"}\n"
"QLabel{\n"
"color: white;\n"
"background: transparent;\n"
"}\n"
"#Gunomizer_label{\n"
"color:skyblue;\n"
"}\n"
"#rank_input{\n"
"color:white;\n"
"background:transparent;\n"
"}\n"
"#go{\n"
"color:white;\n"
"background:transparent;\n"
"border-width : 2px;\n"
"border-style: solid;\n"
"border-color: white;\n"
"border-radius: 24px;\n"
"}\n"
"QCheckBox{\n"
"color:white;\n"
"}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.PF_label = QtWidgets.QLabel(self.frame)
        self.PF_label.setGeometry(QtCore.QRect(160, 20, 461, 51))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.PF_label.setFont(font)
        self.PF_label.setAlignment(QtCore.Qt.AlignCenter)
        self.PF_label.setObjectName("PF_label")
        self.Gunomizer_label = QtWidgets.QLabel(self.frame)
        self.Gunomizer_label.setGeometry(QtCore.QRect(170, 90, 441, 41))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.Gunomizer_label.setFont(font)
        self.Gunomizer_label.setAlignment(QtCore.Qt.AlignCenter)
        self.Gunomizer_label.setObjectName("Gunomizer_label")
        self.rank_input = QtWidgets.QLineEdit(self.frame)
        self.rank_input.setGeometry(QtCore.QRect(382, 190, 113, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.rank_input.setFont(font)
        self.rank_input.setAlignment(QtCore.Qt.AlignCenter)
        self.rank_input.setDragEnabled(True)
        self.rank_input.setObjectName("rank_input")
        self.rank_label = QtWidgets.QLabel(self.frame)
        self.rank_label.setGeometry(QtCore.QRect(260, 190, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.rank_label.setFont(font)
        self.rank_label.setAlignment(QtCore.Qt.AlignCenter)
        self.rank_label.setObjectName("rank_label")
        self.gun_output = QtWidgets.QLabel(self.frame)
        self.gun_output.setGeometry(QtCore.QRect(166, 461, 461, 61))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.gun_output.setFont(font)
        self.gun_output.setAlignment(QtCore.Qt.AlignCenter)
        self.gun_output.setObjectName("gun_output")
        self.go = QtWidgets.QPushButton(self.frame)
        self.go.setGeometry(QtCore.QRect(324, 569, 151, 71))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.go.setFont(font)
        self.go.setObjectName("go")
        self.assault_check = QtWidgets.QCheckBox(self.frame)
        self.assault_check.setGeometry(QtCore.QRect(30, 270, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.assault_check.setFont(font)
        self.assault_check.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.assault_check.setObjectName("assault_check")
        self.pdw_check = QtWidgets.QCheckBox(self.frame)
        self.pdw_check.setGeometry(QtCore.QRect(30, 350, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pdw_check.setFont(font)
        self.pdw_check.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.pdw_check.setObjectName("pdw_check")
        self.lmg_check = QtWidgets.QCheckBox(self.frame)
        self.lmg_check.setGeometry(QtCore.QRect(220, 270, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lmg_check.setFont(font)
        self.lmg_check.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.lmg_check.setObjectName("lmg_check")
        self.sniper_check = QtWidgets.QCheckBox(self.frame)
        self.sniper_check.setGeometry(QtCore.QRect(220, 350, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.sniper_check.setFont(font)
        self.sniper_check.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.sniper_check.setObjectName("sniper_check")
        self.carbine_check = QtWidgets.QCheckBox(self.frame)
        self.carbine_check.setGeometry(QtCore.QRect(410, 270, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.carbine_check.setFont(font)
        self.carbine_check.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.carbine_check.setObjectName("carbine_check")
        self.dmr_check = QtWidgets.QCheckBox(self.frame)
        self.dmr_check.setGeometry(QtCore.QRect(410, 350, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.dmr_check.setFont(font)
        self.dmr_check.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.dmr_check.setObjectName("dmr_check")
        self.battle_check = QtWidgets.QCheckBox(self.frame)
        self.battle_check.setGeometry(QtCore.QRect(580, 270, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.battle_check.setFont(font)
        self.battle_check.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.battle_check.setObjectName("battle_check")
        self.shotgun_check = QtWidgets.QCheckBox(self.frame)
        self.shotgun_check.setGeometry(QtCore.QRect(580, 350, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.shotgun_check.setFont(font)
        self.shotgun_check.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.shotgun_check.setObjectName("shotgun_check")
        self.credits = QtWidgets.QLabel(self.BG)
        self.credits.setGeometry(QtCore.QRect(660, 720, 191, 41))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.credits.setFont(font)
        self.credits.setAlignment(QtCore.Qt.AlignCenter)
        self.credits.setObjectName("credits")
        RGS.setCentralWidget(self.BG)

        self.go.clicked.connect(self.push)

        self.retranslateUi(RGS)
        QtCore.QMetaObject.connectSlotsByName(RGS)

    def retranslateUi(self, RGS):
        _translate = QtCore.QCoreApplication.translate
        RGS.setWindowTitle(_translate("RGS", "Phantom forces"))
        self.PF_label.setText(_translate("RGS", "PHANTOM FORCES"))
        self.Gunomizer_label.setText(_translate("RGS", "Gunomizer"))
        self.rank_input.setText(_translate("RGS", "0"))
        self.rank_label.setText(_translate("RGS", "RANK"))
        self.gun_output.setText(_translate("RGS", ""))
        self.go.setText(_translate("RGS", "GO"))
        self.assault_check.setText(_translate("RGS", "ASSAULT"))
        self.pdw_check.setText(_translate("RGS", "PDW"))
        self.lmg_check.setText(_translate("RGS", "LMG"))
        self.sniper_check.setText(_translate("RGS", "SNIPER"))
        self.carbine_check.setText(_translate("RGS", "CARBINE"))
        self.dmr_check.setText(_translate("RGS", "DMR"))
        self.battle_check.setText(_translate("RGS", "BATTLE RIFLE"))
        self.shotgun_check.setText(_translate("RGS", "SHOTGUN"))
        self.credits.setText(_translate("RGS", "BY -NISHAN SINGH"))

    def push(self):
        at = self.assault_check.isChecked()
        pt = self.pdw_check.isChecked()
        lt = self.lmg_check.isChecked()
        srt = self.sniper_check.isChecked()
        ct = self.carbine_check.isChecked()
        dt = self.dmr_check.isChecked()
        brt = self.battle_check.isChecked()
        st = self.shotgun_check.isChecked()
        rank = int(self.rank_input.text())
        try:
                if rank < 0:
                        self.gun_output.setText("ENTER VALID RANK")
                else:
                        self.gun_output.setText(pf_02.generate(rank, at, pt, lt, srt, ct, dt, brt, st))
        except:
                self.gun_output.setText("INVALID")

import img


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    RGS = QtWidgets.QMainWindow()
    ui = Ui_RGS()
    ui.setupUi(RGS)
    RGS.show()
    sys.exit(app.exec_())
