from PyQt5 import QtCore, QtGui, QtWidgets, QtMultimedia
from PyQt5.QtCore import QObject, QThread, pyqtSignal
import sys, time
from pynput import mouse, keyboard
import winsound, random

mouse1 = mouse.Controller()



class SoundPlay(QObject):
    def run(self):
        playsound('background.mp3.wav')
        return
    
class Worker(QObject):
    cSignal = pyqtSignal(tuple)
    sSignal = pyqtSignal()
    def on_click(self,x, y, button, pressed):
        if pressed:
            self.cSignal.emit((x,y))
    def on_press(self,key):
        try:
          if key == keyboard.Key.ctrl_l:
            pos = mouse1.position
            self.cSignal.emit((pos[0],pos[1]))
          elif key == keyboard.Key.alt_l:
            self.sSignal.emit()
        except:
            print("key error")

    def run(self):
        #with mouse.Listener(on_click=self.on_click) as listener:
        #    listener.join()
        with keyboard.Listener(on_press=self.on_press) as listener:
            listener.join()
class Ui_Form(object):
    crackLi= ["glasscrack1.png","glasscrack2.png", "glasscrack3.png"]
    dragonx=980
    dragony=200
    tinu=0
    svol=50
    def gifFinished(self, fn):
        if fn == 25:
            self.movie2.stop()
            
    def on_valueChanged(self,val, x,y, lb):
        xx = val.x()
        yy = val.y()
        if xx == x and yy == y:
            print("blast")
            self.alabel.close()
            self.label2.move(x-30, y-45)
            self.movie2.start()
            newLba = QtWidgets.QLabel(self.widget)
            newLba.setGeometry(QtCore.QRect(x-70, y-60, 120, 120))
            newLba.setScaledContents(True)
            pixmap = QtGui.QPixmap(self.crackLi[random.randint(0, 0)])
            newLba.setPixmap(pixmap)
            newLba.show()
            #self.widget.deleteLater()
    def makeLbl(self,x,y):
        self.alabel = QtWidgets.QLabel(self.widget)
        self.alabel.setGeometry(QtCore.QRect(1060, 565, 100, 100))
        #movie1 = QtGui.QMovie("fireball.gif")
        #label.setMovie(movie1)
        self.alabel.setScaledContents(True)
        #movie1.start()
        pixmap = QtGui.QPixmap('fireball.png')
        self.alabel.setPixmap(pixmap)
        self.alabel.show()
        #return label
        anim1 = QtCore.QPropertyAnimation(self.alabel, b"geometry")
        anim1.setDuration(700)
        anim1.setStartValue(QtCore.QRect(1060, self.dragony+165,0, 0))
        anim1.setEasingCurve(QtCore.QEasingCurve.InOutCubic)
        anim1.setEndValue(QtCore.QRect(1040, self.dragony+155,40, 40))
        self.anim_group.addAnimation(anim1)
        #self.anim_group.start()
        #anim1.start()
        anim2 = QtCore.QPropertyAnimation(self.alabel, b"geometry")
        anim2.setDuration(1000)
        anim2.setStartValue(QtCore.QRect(1040, self.dragony+155, 40, 40))
        anim2.setEasingCurve(QtCore.QEasingCurve.InOutCubic)
        anim2.setEndValue(QtCore.QRect(x, y, 20, 20))
        anim2.valueChanged.connect(lambda valueChanged: self.on_valueChanged(valueChanged, x, y, self.alabel))
        self.anim_group.addAnimation(anim2)
        #print(self.anim_group)
        #self.anim_group.start()
        #anim.start()
    def on_valueChanged2(self, val, x, y):
        xx = val.x()
        yy = val.y()
        if yy == 200 or yy == 0 or yy == 500:
            self.anim_group = QtCore.QSequentialAnimationGroup()
            self.makeLbl(x,y)
            self.anim_group.start()
            winsound.PlaySound("sound1.wav", winsound.SND_ASYNC | winsound.SND_ALIAS )
            return
    def on_valueChanged3(self, val):
        self.timer2.start(500)
        return
    def doAnimation4(self, pos):
        if self.dragony == 0 and pos[1]<150:
            self.on_valueChanged2(QtCore.QPoint(self.dragonx, self.dragony), pos[0], pos[1])
        elif self.dragony == 500 and pos[1]> 550:
            self.on_valueChanged2(QtCore.QPoint(self.dragonx, self.dragony), pos[0], pos[1])
        elif self.dragony == 200 and 150 < pos[1] < 550:
            self.on_valueChanged2(QtCore.QPoint(self.dragonx, self.dragony), pos[0], pos[1])
        else:
            self.anim4 = QtCore.QPropertyAnimation(self.label, b"pos")
            self.anim4.setDuration(3000)
            self.anim4.setStartValue(QtCore.QPoint(self.dragonx, self.dragony))
            self.anim4.setEasingCurve(QtCore.QEasingCurve.InOutCubic)#
            if pos[1]< 150:
                self.dragony = 0
            elif pos[1]> 550:
                self.dragony = 500
            else:
                self.dragony = 200
            print("#",pos[1], self.dragony)
            self.anim4.setEndValue(QtCore.QPoint(self.dragonx, self.dragony))
            self.anim4.valueChanged.connect(lambda valueChanged: self.on_valueChanged2(valueChanged, pos[0], pos[1]))
            self.anim4.start()
            #self.dragony = pos[1]-150
        
    def hello(self,pos):
        print(pos)
        self.doAnimation4(pos)
        
    def doAnimation(self):
        self.anim = QtCore.QPropertyAnimation(self.label, b"pos")
        self.anim.setDuration(7000)
        self.anim.setStartValue(QtCore.QPoint(2000, 200))
        self.anim.setEasingCurve(QtCore.QEasingCurve.InOutCubic)
        self.anim.setEndValue(QtCore.QPoint(980, 400))
        self.anim.start()
    
    def doAnimation2(self):
        self.anim2 = QtCore.QPropertyAnimation(self.label_3, b"pos")
        self.anim2.setDuration(3000)
        self.anim2.setStartValue(QtCore.QPoint(294, -200))
        self.anim2.setEndValue(QtCore.QPoint(294, 241))
        self.anim2.start()
    
    def doAnimation3(self):
        self.anim3 = QtCore.QPropertyAnimation(self.label_4, b"pos")
        self.anim3.setDuration(3000)
        self.anim3.setStartValue(QtCore.QPoint(294, -50))
        self.anim3.setEndValue(QtCore.QPoint(294, 390))
        self.anim3.start()
    def startAnimations(self):
        self.doAnimation2()
        self.doAnimation3()
        self.doAnimation()
        url = QtCore.QUrl.fromLocalFile("background.mp3")
        content = QtMultimedia.QMediaContent(url)
        self.player = QtMultimedia.QMediaPlayer()
        self.player.setMedia(content)
        self.player.setVolume(self.svol+10)
        self.player.play()
        self.timer.start(1000)
    def doAnimation5(self):
        self.anim5 = QtCore.QPropertyAnimation(self.label_3, b"pos")
        self.anim5.setDuration(3000)
        self.anim5.setStartValue(QtCore.QPoint(294, 241))
        self.anim5.setEndValue(QtCore.QPoint(294, 2000))
        self.anim5.start()
    def doAnimation6(self):
        self.anim6 = QtCore.QPropertyAnimation(self.label_4, b"pos")
        self.anim6.setDuration(3000)
        self.anim6.setStartValue(QtCore.QPoint(294, 390))
        self.anim6.setEndValue(QtCore.QPoint(294, 2150))
        self.anim6.start()
    def doAnimation7(self):
        self.anim7 = QtCore.QPropertyAnimation(self.label, b"pos")
        self.anim7.setDuration(3000)
        self.anim7.setStartValue(QtCore.QPoint(980, 400))
        self.anim7.setEndValue(QtCore.QPoint(980, 200))
        self.anim7.valueChanged.connect(lambda valueChanged: self.on_valueChanged3(valueChanged))
        self.anim7.start()
    def endAni(self):
        if self.tinu == 7:
            self.timer.stop()
            self.doAnimation5()
            self.doAnimation6()
            self.doAnimation7()
            
        self.tinu +=1
    def soundL(self):
        print(self.svol)
        if self.svol ==0:
            return
        self.player.setVolume(self.svol)
        self.svol -=10
    def setupUi(self, Form):
        sizeObject = QtWidgets.QDesktopWidget().screenGeometry(-1)
        print(" Screen size : "  + str(sizeObject.height()) + "x"  + str(sizeObject.width()))
        Form.setObjectName("Form")
        Form.resize(sizeObject.width(), sizeObject.height())
        Form.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        Form.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(0, 0, sizeObject.width(), sizeObject.height()))
        self.widget.setObjectName("widget")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(2000, 200, 300, 300))
        self.movie1 = QtGui.QMovie("dragon.gif")
        self.label.setMovie(self.movie1)
        self.label.setScaledContents(True)
        self.movie1.start()
    
        self.label2 = QtWidgets.QLabel(Form)
        self.label2.setGeometry(QtCore.QRect(533, 110, 60, 60))
        self.label2.setScaledContents(True)
        self.movie2 = QtGui.QMovie("exp.gif")
        self.label2.setMovie(self.movie2)
        self.movie2.frameChanged.connect(self.gifFinished)

        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(2940, 161, sizeObject.width(), 200))
        self.label_3.setScaledContents(True)
        self.label_3.setStyleSheet("color:rgba(255, 255, 255, 200);")
        font = QtGui.QFont()
        font.setPointSize(60)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setText("Python Dragon War")

        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(2940, 310, 800, 50))
        self.label_4.setScaledContents(True)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setStyleSheet("color:rgba(255, 255, 255, 200);")
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setText("Created by SihinaCODE")
        self.thread = QThread()
        self.worker = Worker()
        self.worker.moveToThread(self.thread)

        self.thread.started.connect(self.worker.run)
        self.worker.cSignal.connect(self.hello)
        self.worker.sSignal.connect(self.startAnimations)
        self.thread.start()

        #self.thread1 = QThread()
        #self.sp = SoundPlay()
        #self.sp.moveToThread(self.thread1)

        #self.thread1.started.connect(self.sp.run)
        #self.thread1.start()
        #self.startAnimations()
        self.timer = QtCore.QTimer(Form)
        self.timer.timeout.connect(self.endAni)
        self.timer2 = QtCore.QTimer(Form)
        self.timer2.timeout.connect(self.soundL)
        self.label.raise_()
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        
        

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.showFullScreen()
    sys.exit(app.exec_())

