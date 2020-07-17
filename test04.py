import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QTextEdit
, QLineEdit, QTextBrowser, QPushButton, QVBoxLayout, QHBoxLayout)


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.le = QLineEdit()
        self.le.returnPressed.connect(self.append_text)

        self.tb = QTextBrowser()
        self.tb.setAcceptRichText(True)
        self.tb.setOpenExternalLinks(True)

        self.clear_btn = QPushButton('Clear')
        self.clear_btn.pressed.connect(self.clear_text)


        self.lbl1 = QLabel('Enter your sentence:')
        self.te = QTextEdit()
        self.te.setAcceptRichText(False)
        self.lbl2 = QLabel('The number of words is 0')

        self.te.textChanged.connect(self.text_changed)

        layout = QHBoxLayout()
        vbox1 = QVBoxLayout()
        vbox1.addWidget(self.lbl1)
        vbox1.addWidget(self.te)
        vbox1.addWidget(self.lbl2)
        vbox1.addStretch()

        vbox = QVBoxLayout()
        vbox.addWidget(self.le, 0)
        vbox.addWidget(self.tb, 1)
        vbox.addWidget(self.clear_btn, 2)
        layout.addLayout(vbox)
        layout.addLayout(vbox1)

        self.setLayout(layout)

        self.setWindowTitle('으에에ㅔ')
        self.setGeometry(300, 300, 700, 800)
        self.show()


    def append_text(self):
        text = self.le.text()
        self.tb.append(text)
        self.le.clear()

    def clear_text(self):
        self.tb.clear()

    def text_changed(self):
        text = self.te.toPlainText()
        self.lbl2.setText('The number of words is ' + str(len(text.split())))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())