from PyQt5.QtWidgets import QApplication, QFileDialog
from PyQt5 import QtCore
import cv2
from model import Model
from view_rev import Ui_Form


class Controller:
    def __init__(self,view):
        self.model = None
        self.ui = view
        self.cap, self.timer = None, None
        self.playing = False

        self.setup()

    def setup(self):
        self.ui.frame_10.hide()
        self.ui.frame_7.hide()

        self.ui.pushButton.setText('Load Video')
        self.ui.pushButton.clicked.connect(lambda : self.load_video())

        # self.ui.pushButton_2.clicked.connect(lambda : self.load_video())
        self.ui.pushButton_3.clicked.connect(self.clear)
        self.ui.pushButton_play.clicked.connect(self.play_or_pause)
        self.ui.pushButton_forward.clicked.connect(lambda : self.model.skipFrame(1))
        self.ui.pushButton_backward.clicked.connect(lambda : self.model.skipFrame(0))


    def load_video(self):
        import os
        file = QFileDialog.getOpenFileName(filter="Video (*.mp4)")[0]
        # file = "dataset/A7.mp4"

        name_file = file.split('/')[-1] 

        if file != '':
            self.cap = file
            # self.playing = True
            self.ui.name_file.setText(name_file)

            self.model = Model(file , True)
            self.model.signal_slot.connect(self.ui.update_img)

            self.model.video_run.connect(self.graphModels)

            self.model.start()
            self.ui.setIconPlay(1)


    def play_or_pause(self):
        if self.cap != None:
            if self.model.playing:
                self.model.playing = False
                self.ui.setIconPlay(0)
            else:
                self.model.playing = True
                self.ui.setIconPlay(1)
                self.model.start()

    def graphModels(self):
        img_graph = {
            # 'g_1': ["model/graph/graph_accurasy.png", self.ui.label_graph_mdl_1],
            # 'g_2': ["model/graph/graph_loss.png", self.ui.label_graph_mdl_2],
            'g_3': ["model/graph/graph_accurasy.png", self.ui.label_graph_mdl_5],
            'g_4': ["model/graph/graph_loss.png", self.ui.label_graph_mdl_6],
            'g_5': ["model/graph/BoxF1_curve.png", self.ui.label_graph_mdl_7],
            'g_6': ["model/graph/BoxR_curve.png", self.ui.label_graph_mdl_8],
        }

        for key, val in img_graph.items():
            img = cv2.imread(val[0])

            self.ui.graphModel(img, val[1])

    def clear(self):
        self.cap, self.playing = None, False
        self.ui.label_result.setText(" ")
        self.ui.label_ori.setText(" ")
        # self.ui.label_indi.setText("Indikator")
        self.ui.name_file.setText(" ")
        self.ui.label_complite.setText(" ")
        self.ui.label_incomp.setText(" ")
        self.ui.label_graph_mdl_6.setText(" ")
        self.ui.label_graph_mdl_7.setText(" ")
        self.ui.label_graph_mdl_8.setText(" ")
        self.ui.label_graph_mdl_5.setText(" ")

        self.model.stop()
        self.ui.complite_line_right.setData([], [])
        self.ui.incomplite_line_right.setData([], [])
        self.ui.complite_line_left.setData([], [])
        self.ui.incomplite_line_left.setData([], [])
        self.ui.tableView.clear()
        self.ui.setupTable()

    def closeEvent(self, event):
        self.model.stop()

def main():
    import  sys
    app = QApplication(sys.argv)

    view = Ui_Form()
    Controller(view)

    view.setWindowTitle("Maintenance KAI System")
    view.show()

    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
