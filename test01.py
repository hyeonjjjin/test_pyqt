import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, qApp, QPushButton, QCheckBox, QRadioButton
from PyQt5.QtWidgets import QWidget, QToolTip, QDesktopWidget, QVBoxLayout, QLabel, QHBoxLayout, QComboBox
from PyQt5.QtWidgets import QLineEdit, QProgressBar, QSlider, QDial, QDoubleSpinBox, QSpinBox
from PyQt5.QtGui import QIcon, QFont, QPixmap
from PyQt5.QtCore import Qt, QBasicTimer


class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        btn1 = QPushButton('&Button1', self)
        btn1.setCheckable(True)
        btn1.toggle()

        btn2 = QPushButton(self)
        btn2.setText('Button&2')

        btn3 = QPushButton('Button3', self)
        btn3.setEnabled(False)

        #label
        label = QLabel('나는 라벨', self)
        label.setAlignment(Qt.AlignCenter)
        font = label.font()
        font.setPointSize(10)
        font.setFamily('Times New Roman')
        font.setBold(True)
        label.setFont(font)

        #QCheckBox
        cb = QCheckBox('Show title', self)
        cb.move(20, 20)
        cb.toggle()
        #cb.stateChanged.connect(self.changeTitle)
        #여기선 제목을 바꿀 수 없는듯

        rbtn1 = QRadioButton('동구란 버튼', self)
        rbtn1.setChecked(True)
        rbtn2 = QRadioButton(self)
        rbtn2.setText('도옹구란 버튼')

        #ComboBox 생성
        #self.lbl = QLabel('Option1', self)
        cob = QComboBox(self)
        cob.addItem('Option1')
        cob.addItem('Option2')
        cob.addItem('Option3')
        cob.addItem('Option4')
        #cob.activated[str].connect(self.onActivated)

        #LineEdit 생성
        qle = QLineEdit(self)
        #qle.textChanged[str].connect(self.onChanged)

        #ProgressBar 진행상황 막대기
        self.pbar = QProgressBar(self)
        #self.pbar.setGeometry(30, 40, 200, 25)

        self.btnS = QPushButton('Start', self)
        self.btnS.clicked.connect(self.doAction)

        self.timer = QBasicTimer()
        self.step = 0

        #QSlider, QDial
        self.slider = QSlider(Qt.Horizontal, self)
        self.slider.setRange(0, 50)
        self.slider.setSingleStep(2)
        self.dial = QDial(self)
        self.dial.setRange(0, 50)
        self.slider.valueChanged.connect(self.dial.setValue)
        self.dial.valueChanged.connect(self.slider.setValue)

        pixmap = QPixmap('Hanabi.PNG')

        lbl_img = QLabel()
        lbl_img.setPixmap(pixmap)
        lbl_size = QLabel('Width: ' + str(pixmap.width()) + ', Height: ' + str(pixmap.height()))
        lbl_size.setAlignment(Qt.AlignCenter)

        self.lbl1 = QLabel('QSpinBox')
        self.spinbox = QSpinBox()
        self.spinbox.setMinimum(-10)
        self.spinbox.setMaximum(30)
        self.spinbox.setSingleStep(2)
        self.lbl2 = QLabel('0')

        self.spinbox.valueChanged.connect(self.value_changed)

        #doubleSpinBox
        self.lbl3 = QLabel('QDoubleSpinBox')
        self.dspinbox = QDoubleSpinBox()
        self.dspinbox.setRange(0, 100)
        self.dspinbox.setSingleStep(0.5)
        self.dspinbox.setPrefix('$ ')
        self.dspinbox.setDecimals(1)
        self.lbl4 = QLabel('$ 0.0')

        self.dspinbox.valueChanged.connect(self.value_changed)

        layout1 = QHBoxLayout()
        layout2 = QHBoxLayout()
        layout3 = QHBoxLayout()
        layout4 = QHBoxLayout()
        layout5 = QHBoxLayout()

        vlayout = QVBoxLayout()
        vlayout2 = QVBoxLayout()

        layout1.addWidget(btn1)
        layout1.addWidget(btn2)
        layout1.addWidget(cob)

        layout2.addWidget(label)
        layout2.addWidget(cb)
        layout2.addWidget(rbtn1)
        layout2.addWidget(rbtn2)

        layout3.addWidget(btn3)
        layout3.addWidget(qle)

        layout4.addWidget(self.slider)
        layout4.addWidget(self.dial)

        vlayout2.addWidget(self.lbl1)
        vlayout2.addWidget(self.spinbox)
        vlayout2.addWidget(self.lbl2)
        vlayout2.addWidget(self.lbl3)
        vlayout2.addWidget(self.dspinbox)
        vlayout2.addWidget(self.lbl4)

        layout5.addWidget(lbl_img)
        layout5.addLayout(vlayout2)

        vlayout.addLayout(layout1)
        vlayout.addLayout(layout3)
        vlayout.addLayout(layout2)
        vlayout.addWidget(self.pbar)
        vlayout.addWidget(self.btnS)
        vlayout.addLayout(layout4)
        vlayout.addLayout(layout5)
        self.setLayout(vlayout)

    def value_changed(self):
        self.lbl2.setText(str(self.spinbox.value()))

    def onActivated(self, text):
        self.lbl.setText(text)
        self.lbl.adjustSize()

    def onChanged(self, text):
        self.lbl.setText(text)
        self.lbl.adjustSize()

    def timerEvent(self, e):
        if self.step >= 100:
            self.timer.stop()
            self.btnS.setText('Finished')
            return

        self.step = self.step + 1
        self.pbar.setValue(self.step)

    def doAction(self):
        if self.timer.isActive():
            self.timer.stop()
            self.btnS.setText('Start')
        else:
            self.timer.start(100, self)
            self.btnS.setText('Stop')


class MyApp(QMainWindow):
  def __init__(self):
      super().__init__()
      self.initUI()

  def initUI(self):
      wg = MyWidget()
      self.setCentralWidget(wg)

      #창을 가운데로
      #self.setWindowTitle('Centering')
      self.resize(1500, 700)
      self.center()#함수뒤에있음
      self.show()

      exitAction = QAction(QIcon('exit.png'), 'Exit', self)#메뉴에서 exit.png 사진, Exit가 뜸
      exitAction.setShortcut('Ctrl+Q')#단축키 설정
      exitAction.setStatusTip('Exit application')#상태 팁
      exitAction.triggered.connect(qApp.quit)#버튼을 누르며 생긴 시그널 QApplication의 quit()함수로 연결, 종료

      addAction = QAction(QIcon('Hanabi.PNG'), '그냥 예뻐서', self)
      addAction.triggered.connect(qApp.quit)

      printAction = QAction(QIcon('print.png'), '사실 그냥 나가기 버튼', self)
      printAction.triggered.connect(qApp.quit)

      editAction = QAction(QIcon('edit.png'), '편집 기능 없다!', self)
      editAction.triggered.connect(qApp.quit)

      saveAction =  QAction(QIcon('save.png'), '저어장~~!~!', self)
      saveAction.triggered.connect(qApp.quit)

      #Tool Bar
      self.toolbar = self.addToolBar('툴바이름인가? 별로 상관 없는듯?')
      self.toolbar.addAction(exitAction)
      self.toolbar2 = self.addToolBar('툴바이름인가?이건 예쁜 툴바임')
      self.toolbar2.addAction(addAction)
      self.toolbarPrint = self.addToolBar('print')
      self.toolbarPrint.addAction(printAction)
      self.toolbarEdit = self.addToolBar('edit')
      self.toolbarEdit.addAction(editAction)
      self.toolbarSave = self.addToolBar('save')
      self.toolbarSave.addAction(saveAction)

      #메뉴바 생성
      menubar = self.menuBar()
      menubar.setNativeMenuBar(False)
      filemenu = menubar.addMenu('&File')#Alt-F로 실행 ㄱㄴ
      filemenu2 = menubar.addMenu('&Add')  # Alt-A로 실행 ㄱㄴ
      filemenu.addAction(exitAction)#File 메뉴에 exitAction 추가
      filemenu2.addAction(addAction)
      filemenu.addAction(addAction)

      #툴 팁
      QToolTip.setFont(QFont('SansSerif', 10))
      #self.setToolTip('This is a <b>QWidget</b> widget')

      #상태바
      self.statusBar().showMessage('상태바아아아')

      #창 아이콘
      #self.setWindowTitle('Icon')
      self.setWindowIcon(QIcon('Hanabi.PNG'))

      #self.setGeometry(300, 300, 700, 400)
      #self.show()



  def center(self):
      qr = self.frameGeometry()
      cp = QDesktopWidget().availableGeometry().center()
      qr.moveCenter(cp)
      self.move(qr.topLeft())

if __name__ == '__main__':
  app = QApplication(sys.argv)
  ex = MyApp()
  sys.exit(app.exec_())