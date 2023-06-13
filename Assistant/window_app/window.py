from PyQt5.QtCore import QUrl
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtWebEngineWidgets import QWebEngineView


class WebPageApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Assistant")
        self.resize(400, self.screen().geometry().height())  # Устанавливаем ширину и высоту окна
        self.move(self.screen().geometry().width() - self.width(), 0)  # Перемещаем окно в правый верхний угол

        # Устанавливаем логотип окна
        icon = QIcon("path/to/logo.png")  # Замените "path/to/logo.png" на путь к вашему изображению
        self.setWindowIcon(icon)

        self.web_view = QWebEngineView(self)
        self.setCentralWidget(self.web_view)

        self.load_web_page()

    def load_web_page(self):
        # Здесь вы можете добавить логику загрузки веб-страницы с помощью QWebEngineView
        url = QUrl("https://pypi.org/project/tkhtmlview/")  # Замените URL на свой
        self.web_view.load(url)


if __name__ == "__main__":
    app = QApplication([])
    window = WebPageApp()
    window.show()
    app.exec_()
