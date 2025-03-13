from PySide6.QtWidgets import QWidget, QApplication
from switch_button import SwitchButton

class Preview(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Preview SwitchButton")
        self.setFixedSize(360, 120)
        self.btn_left = SwitchButton()
        self.btn_left.setParent(self)
        self.btn_left.move(20, 40)

        self.btn_right = SwitchButton()
        self.btn_right.setParent(self)
        self.btn_right.move(200, 40)


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    win = Preview()
    win.show()

    sys.exit(app.exec())
