import cv2
import numpy as np
from ultralytics import YOLO
from PyQt5.QtCore import QThread, pyqtSignal
from collections import Counter

class Model(QThread):
    signal_slot = pyqtSignal(np.ndarray, np.ndarray, tuple, tuple)
    video_run = pyqtSignal()

    def __init__(self, path_vid, playing):
        super().__init__()
        self.path_vid = path_vid
        self.cap = cv2.VideoCapture(path_vid)
        # self.model = YOLO("model/best1.pt")
        self.model = YOLO("/home/main/Documents/riset/training-model/datasets/kai/split/train3/weights/best.pt")
        self.cls_clr = {
            0: ['Complite Right', (8, 165, 0)],
            1: ['Complite Left', (8, 165, 0)],
            2: ['Incomplite Right', (200, 0, 0)],
            3: ['Incomplite Left', (187, 193, 0)],
        }
        self.playing = playing

    def run(self):
        frame_counter = 0
        initial_frame_emitted = False

        while self.playing:
            if self.cap is None:
                print("VideoCapture belum disiapkan.")
                break

            ret, frame = self.cap.read()
            if not ret:
                print("Frame tidak terbaca. Mungkin video habis.")
                break

            '''INI WAJIB DIBUKA AGAR JARAKNYA KM/M NYA BISA BERFUNGSI, 
            JIKA TIDAK 1 BATALAN BISA DIDETEKSI BEBERAPAKALI,
            SEDANGKAN YG DIBUTUHKAN ITU 1 BANTALAN 1 KALI PREDIKSI.
            NILAI 16 ITU BANYAK FRAME YG DI SKIP AGAR BISA LANGSUNG MENDETEKSI 
            5 BANTALAN SELANJUTNYA'''
            frame_counter += 1
            if frame_counter % 5 != 0:
                continue  # Lewatkan frame, hemat prediksi
            '''END'''

            # --- Konversi dan prediksi ---
            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            try:
                results = self.model.predict(frame_rgb, conf=0.5, iou=0.01)
            except Exception as e:
                print(f"Model gagal prediksi: {e}")
                continue

            r = results[0]
            # predic_frame = r.plot()
            predic_frame = frame_rgb.copy() 

            # --- Hitung jumlah kelas ---
            boxes = r.boxes
            if boxes is None or boxes.cls is None:
                print("Tidak ada deteksi.")
                cls_list = []
            else:
                boxes = boxes.cpu()
                cls_list = list(map(int, boxes.cls.tolist()))

            xyxy_list = boxes.xyxy.tolist()

            # Tempatkan objek ke list sesuai sisi
            left_objs = []   # kelas 1 & 3
            right_objs = []  # kelas 0 & 2

            for box, cls_id in zip(xyxy_list, cls_list):
                if cls_id in [1, 3]:  # sisi kiri
                    left_objs.append((box, cls_id))
                elif cls_id in [0, 2]:  # sisi kanan
                    right_objs.append((box, cls_id))

            # Batasi masing-masing sisi hanya 5 objek
            left_objs = left_objs[:5]
            right_objs = right_objs[:5]

            # Gabungkan untuk digambar
            limited_objs = left_objs + right_objs

            # Hitung jumlah untuk emit
            all_cls_ids = [cls_id for _, cls_id in limited_objs]

            counts = Counter(all_cls_ids)

            cal_right = (counts.get(0, 0), counts.get(2, 0))
            cal_left = (counts.get(1, 0), counts.get(3, 0))


            # Gambar bounding box + teks dengan background
            for box, cls_id in limited_objs:
                x1, y1, x2, y2 = map(int, box)
                label = self.cls_clr[cls_id][0]
                color = self.cls_clr[cls_id][1]

                font = cv2.FONT_HERSHEY_SIMPLEX
                font_scale = 2 
                thickness = 2
                (tw, th), bl = cv2.getTextSize(label, font, font_scale, thickness)
                text_x, text_y = x1, y1 - 10
                text_y = max(text_y, th + 5)

                cv2.rectangle(predic_frame, (text_x, text_y - th - bl), (text_x + tw, text_y + bl), color, cv2.FILLED)
                cv2.putText(predic_frame, label, (text_x, text_y), font, font_scale, (255, 255, 255), thickness)

                cv2.rectangle(predic_frame, (x1, y1), (x2, y2), color, 8)


            # --- Emit sinyal ke GUI ---
            if not initial_frame_emitted:
                self.video_run.emit()
                initial_frame_emitted = True

            # Pastikan sinyal ini terkoneksi ke slot tampilan
            self.signal_slot.emit(frame, predic_frame, cal_right, cal_left)



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