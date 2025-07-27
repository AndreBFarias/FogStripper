import os
from PyQt6.QtCore import QThread, pyqtSignal
from rembg import remove, new_session
from PIL import Image

class ProcessThread(QThread):
    progress = pyqtSignal(int)
    finished = pyqtSignal(str)

    def __init__(self, input_path, potencia):
        super().__init__()
        self.input_path = input_path
        self.potencia = potencia

    def run(self):
        try:
            self.progress.emit(10)
            input_img = Image.open(self.input_path)
            self.progress.emit(30)
            session = new_session(provider='CUDAExecutionProvider', model_name='u2net')
            erode_size = 5 + int((self.potencia / 100) * 35)
            bg_threshold = 15 - int((self.potencia / 100) * 20)
            self.progress.emit(50)
            output_img = remove(input_img, session=session, alpha_matting=True, alpha_matting_foreground_threshold=240, alpha_matting_background_threshold=bg_threshold, alpha_matting_erode_size=erode_size, post_process_mask=True)
            self.progress.emit(80)
            output_path = os.path.splitext(self.input_path)[0] + '_despido.png'
            if os.path.exists(output_path):
                os.remove(output_path)
            output_img.save(output_path, format='PNG')
            self.progress.emit(100)
            self.finished.emit(output_path)
        except Exception as e:
            print(f"Erro no processamento: {str(e)}")
            self.finished.emit("")