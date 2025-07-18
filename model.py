import cv2
import numpy as np
from ultralytics import YOLO
from PyQt5.QtCore import QThread, pyqtSignal

class Model(QThread):
    signal_slot = pyqtSignal(np.ndarray, np.ndarray, int, int)
    video_finished = pyqtSignal()

    def __init__(self, path_vid, playing):
        super().__init__()
        self.path_vid = path_vid
        self.cap = cv2.VideoCapture(path_vid)
        self.model = YOLO("model/model.pt")
        self.playing = playing

    def run(self):
        k = 0
        while self.playing:
            ret, frame = self.cap.read()
            if not ret:
                self.cap = None
                break

            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            results = self.model(frame)
            predic_frame = results[0].plot()

            cal_com, cal_incom = 0, 0

            for r in results:
                boxes = r.boxes.cpu()
                cls = boxes.cls.tolist()

                com = cls.count(0)
                incom = cls.count(1)
                total = len(cls)

                # cal_com = int((com/total)*100)
                # cal_incom = int((incom/total)*100)

            # predic_frame = cv2.cvtColor(predic_frame, cv2.COLOR_BGR2RGB)
            if k == 0:
                self.video_finished.emit()
                k += 1
                
            self.signal_slot.emit(frame, predic_frame, com, incom)

    def skipFrame(self, condition):
        if(self.cap != None):
            self.playing = False
            current_frame = int(self.cap.get(cv2.CAP_PROP_POS_FRAMES))
            frame_skip = current_frame + 20 if condition == 1 else current_frame - 20
            self.cap.set(cv2.CAP_PROP_POS_FRAMES, frame_skip)
            self.playing = True
            self.start()

    def stop(self):
        self.playing = False
        self.wait()

    def predict(self, cap):
        # from ultralytics import YOLO

        # model = YOLO("model/model.pt")

        ret, frame = cap.read()

        predic_frame = frame.copy()
        if ret:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            results = self.model(frame)

            predic_frame = results[0].plot()
            # frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        return ret, frame, predic_frame