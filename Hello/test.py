from PySide6.QtCore import Qt, QUrl
from PySide6.QtGui import QCursor
from PySide6.QtWebEngineCore import QWebEnginePage
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel

class Header(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setStyleSheet('background-color: #F8F8F8;')
        self.setFixedHeight(32)

        self.title = QLabel('Window Title')
        self.title.setAlignment(Qt.AlignCenter)

        self.close_button = QPushButton('X')
        self.close_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.close_button.setFixedSize(32, 32)
        self.close_button.setStyleSheet('QPushButton { border: none; background-color: transparent; } QPushButton:hover { background-color: #FF6666; }')

        layout = QHBoxLayout(self)
        layout.addWidget(self.title)
        layout.addStretch()
        layout.addWidget(self.close_button)
        layout.setContentsMargins(12, 0, 12, 0)
        self.setLayout(layout)

class BrowserWindow(QWidget):
    def __init__(self, url):
        super().__init__()

        self.url = url
        self.setWindowFlag(Qt.CustomizeWindowHint)
        self.setWindowFlag(Qt.WindowMaximizeButtonHint, False)
        self.setWindowFlag(Qt.WindowMinimizeButtonHint, False)
        self.setWindowFlag(Qt.WindowCloseButtonHint, False)

        self.title_bar = Header(self)
        self.title_bar.close_button.clicked.connect(self.close)

        self.web_view = QWebEngineView(self)
        self.page = QWebEnginePage()
        self.web_view.setPage(self.page)
        self.web_view.load(QUrl(self.url))

        layout = QVBoxLayout(self)
        layout.addWidget(self.title_bar)
        layout.addWidget(self.web_view)
        layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(layout)

        self.setGeometry(0, 0, 800, 600)

        self.show()


if __name__ == '__main__':
    app = QApplication([])
    url = "http://localhost:3000/"
    browser = BrowserWindow(url)
    browser.show()
