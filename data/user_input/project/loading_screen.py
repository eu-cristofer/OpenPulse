from PyQt5.QtWidgets import QDialog, QLabel, QPushButton
from PyQt5.QtGui import QIcon, QMovie
from PyQt5.QtCore import Qt, pyqtSignal, QObject, QSize, QThread
from PyQt5 import uic
from pathlib import Path

from data.user_input.project.printMessageInput import PrintMessageInput
from pulse import __version__, __release_date__

class QWorker(QObject):
    finished = pyqtSignal()
    def __init__(self, target):
        super().__init__()
        self.target = target

    def run(self):
        if self.target is not None:
            try:
                self.target()
            except Exception as log_error:
                print(log_error)
                title = "An error has been reached in LoadingScreen"
                PrintMessageInput([title, str(log_error), "ERROR"])
                
        self.finished.emit()
        self.thread().quit()

class LoadingScreen(QDialog):
    def __init__(self, target=None, *args, **kwargs):
        super().__init__()

        uic.loadUi(Path('data/user_input/ui_files/Project/loading_window.ui'), self)
        
        self.target = target
        self.title = kwargs.get("title", "")
        self.message = kwargs.get("message", "")
        self.project = kwargs.get("project", None)

        self._load_icons()
        self._config_window()
        self._define_and_connect_qt_variables()
        self._set_texts_and_animation()
        self._start_threading()
        self.exec()
        self.movie.stop()


    def _load_icons(self):
        icon_path = str(Path('data/icons/pulse.png'))
        self.gif_path = str(Path('data/icons/loading0.gif'))
        self.pvfat_icon = QIcon(icon_path)


    def _config_window(self):
        self.setWindowTitle(f"Pulse v{__version__} ({__release_date__})")
        self.setWindowFlags(Qt.WindowStaysOnTopHint)
        self.setWindowFlags(Qt.CustomizeWindowHint | Qt.WindowTitleHint | Qt.WindowMinimizeButtonHint)
        self.setWindowIcon(self.pvfat_icon)
        self.movie = QMovie(self.gif_path)
        self.movie.setScaledSize(QSize(140,140))


    def _define_and_connect_qt_variables(self):
        self.label_animation = self.findChild(QLabel, 'label_animation')
        self.label_message = self.findChild(QLabel, 'label_message')
        self.label_title = self.findChild(QLabel, 'label_title')
        self.pushButton_stop_processing = self.findChild(QPushButton, 'pushButton_stop_processing')
        self.pushButton_stop_processing.clicked.connect(self.pushButton_pressed)
        if self.project is None:
            self.pushButton_stop_processing.setDisabled(True)


    def _set_texts_and_animation(self):
        self.label_title.setText(self.title)
        self.label_message.setText(self.message)
        self.label_animation.setMovie(self.movie)
        self.label_animation.adjustSize()
        self.adjustSize()


    def _start_threading(self):
        self.threadWorker = QThread()
        self.worker = QWorker(self.target)
        self.worker.moveToThread(self.threadWorker)
        self.threadWorker.started.connect(self.worker.run)
        self.threadWorker.finished.connect(self.close)
        self.threadWorker.start()
        self.movie.start()


    def pushButton_pressed(self):
        if self.project is not None:
            self.project.preprocessor.stop_processing = True

    
    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Escape:
            self.pushButton_pressed()