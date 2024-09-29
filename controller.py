from PyQt5.QtWidgets import QApplication, QFileDialog
from PyQt5 import QtCore
import cv2

from model import Model
from view import Ui_Form



class Controller:
    def __init__(self,view):
        self.model = None
        self.ui = view
        # self.ui = Ui_Form()
        self.cap, self.timer = None, None
        self.playing = False
        self.setup()

    def setup(self):
        self.ui.pushButton_2.clicked.connect(lambda : self.load_video())
        self.ui.pushButton_3.clicked.connect(self.clear)
        self.ui.pushButton_play.clicked.connect(self.play_or_pause)
        self.ui.pushButton_forward.clicked.connect(lambda : self.skipFrame(0))
        self.ui.pushButton_backward.clicked.connect(lambda : self.skipFrame(1))

    # def load_video(self):
    #     # file = QFileDialog.getOpenFileName(filter="Video (*.mp4)")[0]
    #     file = "dataset/cut.mp4"
    #
    #     if file != '':
    #         self.cap = cv2.VideoCapture(file)
    #         self.playing = True
    #
    #         self.timer = QtCore.QTimer()
    #         self.timer.timeout.connect(self.update_frame)
    #         # self.timer.start()
    #         self.timer.start(30)

    def load_video(self):
        # file = QFileDialog.getOpenFileName(filter="Video (*.mp4)")[0]
        file = "dataset/cut.mp4"

        if file != '':
            self.cap = file
            self.playing = True
            self.model = Model(file, self.playing)
            self.model.signal_slot.connect(self.ui.update_img)

            self.model.start()

    def closeEvent(self, event):
        self.model.stop()

    def update_frame(self):
        if self.playing:
            ret, frame_ori, frame_predict = self.model.predict(self.cap)

            if ret:
                self.ui.set_image(self.ui.label_ori, frame_ori)
                self.ui.set_image(self.ui.label_dp, frame_predict)
                self.ui.setIconPlay(1)
            else:
                self.ui.setIconPlay(0)

    def play_or_pause(self):
        if self.cap != None:
            if self.playing:
                self.playing = False
                self.ui.setIconPlay(0)
            else:
                self.playing = True
                self.ui.setIconPlay(1)
                self.update_frame()

    def skipFrame(self, condition):
        if self.cap != None:
            curren_frame = int(self.cap.get(cv2.CAP_PROP_POS_FRAMES))
            frame_skip = curren_frame + 20 if condition == 0 else curren_frame - 20
            self.cap.set(cv2.CAP_PROP_POS_FRAMES, frame_skip)

    def clear(self):
        self.cap, self.playing = None, False
        self.ui.label_dp.setText(" ")
        self.ui.label_ori.setText(" ")
        self.ui.label_indi_dp.setText("Indikator")
        self.ui.name_file.setText(" ")
        self.ui.label_resolusi.setText(" ")
        self.ui.label_time_pro.setText(" ")
        self.ui.label_status.setText(" ")

def main():
    import  sys
    app = QApplication(sys.argv)

    view = Ui_Form()
    Controller(view)

    view.setWindowTitle("kai")
    view.show()

    sys.exit(app.exec_())

if __name__ == "__main__":
    main()