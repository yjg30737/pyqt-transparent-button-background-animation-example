from PyQt5.QtCore import QAbstractAnimation, QPropertyAnimation, Qt
from PyQt5.QtGui import QPalette, QBrush
from PyQt5.QtWidgets import QPushButton, QGraphicsOpacityEffect, QMainWindow, QApplication, QGridLayout, QWidget, \
    QVBoxLayout, QTextEdit


class HoverButton(QPushButton):
    def __init__(self):
        super().__init__()
        self.__initUi()

    def __initUi(self):
        self.setText('ABC')
        self.__animation = QPropertyAnimation(self, b"opacity")
        self.__animation.valueChanged.connect(self.__setOpacity)
        self.__animation.setStartValue(0.0)
        self.__animation.setEndValue(0.5)
        self.__animation.setDuration(200)
        self.__styleInit(0.0)

    def __styleInit(self, opacity: float):
        style = f'QPushButton {{ background-color: rgb(127, 127, 127, {opacity});' \
                f'border: 0;' \
                f'padding: 5;' \
                f'border-radius: 10; }}'
        self.setStyleSheet(style)

    def enterEvent(self, e):
        self.__animation.setDirection(QAbstractAnimation.Forward)
        self.__animation.start()
        return super().enterEvent(e)

    def leaveEvent(self, e):
        self.__animation.setDirection(QAbstractAnimation.Backward)
        self.__animation.start()
        return super().leaveEvent(e)

    def __setOpacity(self, opacity):
        self.__styleInit(opacity)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.__initUi()

    def __initUi(self):
        btn = HoverButton()
        lay = QGridLayout()
        lay.addWidget(btn)
        mainWidget = QWidget()
        mainWidget.setLayout(lay)
        self.setCentralWidget(mainWidget)

if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.show()
    sys.exit(app.exec_())