# # import json
# # import time
# #
# # from PyQt5.QtCore import QUrl, Qt
# # from PyQt5.QtGui import QPalette, QColor
# # from PyQt5.QtWidgets import QApplication, QMainWindow, QDesktopWidget, QProgressBar
# # import sys
# #
# #
# # from PyQt5 import QtCore
# # from main_ui import Ui_EmptyDialog
# # import requests
# # from PyQt5.QtWebEngineWidgets import QWebEngineView
# #
# #
# # class MainWindow(QMainWindow, Ui_EmptyDialog):
# #     def __init__(self):
# #         super().__init__()
# #         self.setupUi(self)
# #         # palette = self.palette()
# #         # palette.setColor(QPalette.Window, QColor(Qt.black))
# #         # self.setPalette(palette)
# #
# #         # Определяем размер доступной области экрана
# #         screen_size = QDesktopWidget().availableGeometry()
# #         # Устанавливаем размер окна в соответствии с размером экрана
# #         self.setGeometry(screen_size)
# #
# #
# #
# #         # response = requests.get('http://127.0.0.1:8000/api/get_sites/')
# #         response = requests.get('http://localhost:3000/')
# #
# #         self.webView = QWebEngineView()
# #         self.setCentralWidget(self.webView)
# #
# #         url = 'http://localhost:3000/'
# #         self.webView.load(QtCore.QUrl(url))
# #
# #
# #
# #
# # if __name__ == '__main__':
# #     app = QApplication(sys.argv)
# #     window = MainWindow()
# #     window.show()
# #     sys.exit(app.exec_())
# #
# #
# # # from PyQt5.QtCore import QUrl
# # # from PyQt5.QtWidgets import QApplication
# # # from PyQt5.QtWebEngineWidgets import QWebEnginePage, QWebEngineView
# # #
# # # class MyWebEnginePage(QWebEnginePage):
# # #     def __init__(self):
# # #         super().__init__()
# # #
# # #     def javaScriptConsoleMessage(self, level, message, lineNumber, sourceID):
# # #         print("Console message:", level, message, lineNumber, sourceID)
# # #
# # # app = QApplication([])
# # # page = MyWebEnginePage()
# # # view = QWebEngineView()
# # # view.setPage(page)
# # #
# # # url = QUrl("http://localhost:3000/")
# # # page.load(url)
# # #
# # # view.show()
# # # app.exec_()
#
import sys
from PySide6.QtCore import Qt, QUrl
from PySide6.QtGui import QWindow, QGuiApplication
from PySide6.QtWebEngineCore import QWebEnginePage
from PySide6.QtWidgets import QApplication, QWidget, QHBoxLayout
from PySide6.QtWebEngineWidgets import QWebEngineView


from PyQt5.QtCore import Qt, QUrl
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QDesktopWidget
from PyQt5.QtWebEngineWidgets import QWebEngineView, QWebEnginePage


# class TitleBar(QWidget):
#     def __init__(self, parent, width):
#         super().__init__(parent)
#         self._parent = parent
#
#         self.setStyleSheet('background-color: #444444; color: #ffffff; font-size: 18px; font-weight: bold; width:100vw;')
#         self.setFixedHeight(50)
#
#         self.title = QLabel("Hello World", self)
#         self.title.setAlignment(Qt.AlignCenter)
#         self.title.move(5, 5)
#         print(width)
#         self.close_button = QPushButton("x", self)
#         self.close_button.setGeometry(width - 700, 0, 30, 0)
#         self.close_button.clicked.connect(self._parent.close)
#
#     def mousePressEvent(self, event):
#         self.offset = event.pos()
#
#     def mouseMoveEvent(self, event):
#         x = event.globalX()
#         y = event.globalY()
#         x_w = self.offset.x()
#         y_w = self.offset.y()
#         self._parent.move(x - x_w, y - y_w)
#

class BrowserWindow(QWidget):
    def __init__(self, url):
        super().__init__()
        self.url = url

        desktop = QDesktopWidget()
        screenRect = desktop.screenGeometry()
        width = screenRect.width()
        height = screenRect.height()

        print(self.width())
        self.setGeometry(0, 0, width, height)

        self.setWindowTitle("Hello world")
        self.web_view = QWebEngineView(self)
        self.page = QWebEnginePage()
        self.web_view.setPage(self.page)
        self.web_view.load(QUrl(self.url))

        layout = QVBoxLayout(self)

        layout.addWidget(self.web_view)
        layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(layout)

        self.show()


if __name__ == '__main__':
    app = QApplication([])
    url = "http://localhost:3000/"
    browser = BrowserWindow(url)
    browser.show()
    app.exec_()


# import sys
#
# from PySide6.QtCore import Qt
# from PySide6.QtWidgets import QApplication, QFrame, QHBoxLayout, QLabel, QMainWindow, QVBoxLayout, QWidget
#
# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle("My Application")
#         self.setFixedHeight(500)  # фиксируем высоту окна
#
#
#
#
#
#
#
# if __name__ == "__main__":
#     app = QApplication([])
#     window = MainWindow()
#     window.show()
#     sys.exit(app.exec())
