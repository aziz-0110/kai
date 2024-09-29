import cv2
import numpy as np
from ultralytics import YOLO
from PyQt5.QtCore import QThread, pyqtSignal


class Model(QThread):
    signal_slot = pyqtSignal(np.ndarray, np.ndarray)

    def __init__(self, path_vid, playing):
        super().__init__()
        self.path_vid = path_vid
        self.cap = cv2.VideoCapture(path_vid)
        self.model = YOLO("model/model.pt")
        self.playing = playing

    def run(self):
        while self.playing:
            ret, frame = self.cap.read()
            if not ret:
                break

            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            results = self.model(frame)
            predic_frame = results[0].plot()

            self.signal_slot.emit(frame, predic_frame)

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