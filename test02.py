import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QPushButton, QHBoxLayout
from PyQt5.QtWidgets import QGridLayout, QLineEdit, QTextEdit, QCheckBox, QComboBox
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtCore import Qt

class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        lbl_red = QLabel('Red')
        lbl_green = QLabel('Green')
        lbl_green.setStyleSheet("color: green;"
                                "background-color: #7FFFD4")
        lbl_red.setStyleSheet("color: red;"
                              "border-style: solid;"
                              "border-width: 2px;"
                              "border-color: #FA8072;"
                              "border-radius: 3px")

        '''
        lbl_blue = QLabel('Blue')
        lbl_blue.setStyleSheet("color: blue;"
                              "background-color: #87CEFA;"
                              "border-style: dashed;"
                              "border-width: 3px;"
                              "border-color: #1E90FF")

        vbox = QVBoxLayout()
        vbox.addWidget(lbl_red)
        vbox.addWidget(lbl_green)
        vbox.addWidget(lbl_blue)

        self.setLayout(vbox)

        btn = QPushButton('Quit 버튼', self)
        btn.setToolTip('팁이다아ㅏ아ㅏ')
        btn.move(500, 500)
        btn.resize(btn.sizeHint())
        btn.clicked.connect(QCoreApplication.instance().quit)

        label1 = QLabel('Label1', self)
        label1.move(20, 20)
        label2 = QLabel('Label2', self)
        label2.move(20, 60)

        btn1 = QPushButton('Button1', self)
        btn1.move(80, 13)
        btn2 = QPushButton('Button2', self)
        btn2.move(80, 53)
        '''
        '''
        박스 레이아웃
        okButton = QPushButton('OK')
        okButton.clicked.connect(QCoreApplication.instance().quit)

        cancelButton = QPushButton('Cancel')

        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(okButton)
        hbox.addWidget(cancelButton)
        hbox.addStretch(1)

        vbox = QVBoxLayout()
        vbox.addStretch(2)
        vbox.addWidget(lbl_red)
        vbox.addStretch(1)
        vbox.addLayout(hbox)
        vbox.addWidget(lbl_green)
        vbox.addStretch(1)

        self.setLayout(vbox)
        '''
        #QCheckBox
        cb = QCheckBox('Show title', self)
        cb.move(20, 20)
        cb.toggle()
        cb.stateChanged.connect(self.changeTitle)

        grid = QGridLayout()
        self.setLayout(grid)

        grid.addWidget(cb, 0, 0)
        grid.addWidget(QLabel('Author:'), 1, 0)
        grid.addWidget(QLabel('Review:'), 2, 0)

        grid.addWidget(QLineEdit(), 0, 1)
        grid.addWidget(QLineEdit(), 1, 1)
        grid.addWidget(QTextEdit(), 2, 1)

        self.lbl = QLabel('Option1', self)
        cb = QComboBox(self)
        cb.addItem('Option1')
        cb.addItem('Option2')
        cb.addItem('Option3')
        cb.addItem('Option4')
        cb.move(50, 50)

        cb.activated[str].connect(self.onActivated)

        self.setWindowIcon(QIcon('Hanabi.PNG'))
        #self.setWindowTitle('나는 제목')
        self.setGeometry(300, 300, 800, 800)
        self.show()



    def changeTitle(self, state):
    #CheckBox
        if state == Qt.Checked:
            self.setWindowTitle('에엥')
        else:
            self.setWindowTitle('왜안나와 ')

    def onActivated(self, text):
        self.lbl.setText(text)
        self.lbl.adjustSize()




if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())