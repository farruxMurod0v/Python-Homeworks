# import sys
# from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
#
# def on_button_click():
#     print("Bosildi")
#
#
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#
#     window = QWidget()
#     button = QPushButton("Meni bos", window)
#     button.clicked.connect(on_button_click)
#
#     window.setWindowTitle("PyQt5 Button Example")
#     window.show()
#
#     sys.exit(app.exec_())














#
# import sys
# from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton
#
# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle("Bir")
#         self.setGeometry(200, 350, 400, 300)
#
#         self.label = QLabel(self)
#         self.label.setText("loyiha")
#         self.label.move(150, 50)
#
#         self.button1 = QPushButton(self)
#         self.button1.setText("Meni bos")
#         self.button1.move(150, 100)
#
#         self.button2 = QPushButton(self)
#         self.button2.setText("marta bosildi")
#         self.button2.move(50, 150)
#
#     def mousePressEvent(self, event):
#         print("Tugma bosildi")
#
#     def mouseReleaseEvent(self, event):
#         print("Tugma qo'lib tashlandi")
#
# app = QApplication(sys.argv)
# window = MainWindow()
# window.show()
# sys.exit(app.exec_())



#
# import sys
# import random
# from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton
#
# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle("Only up")
#         self.setGeometry(100, 100, 400, 300)
#
#         self.label = QLabel(self)
#         self.label.setText("Birinchi loyiha")
#         self.label.move(150, 50)
#
#         self.button1 = QPushButton(self)
#         self.button1.setText("Meni bos")
#         self.button1.move(150, 100)
#
#         self.button2 = QPushButton(self)
#         self.button2.setText("Meni nechanchi marta bosganligimni ko’rsat")
#         self.button2.move(50, 150)
#
#         self.names = ["My App", "Hisoblash dasturi", "Macbook App"]
#
#     def mousePressEvent(self, event):
#         if event.button() == 1:
#             new_name = random.choice(self.names)
#             self.setWindowTitle(new_name)
#
# app = QApplication(sys.argv)
# window = MainWindow()
# window.show()
# sys.exit(app.exec_())
#
#
# import sys
# from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QLineEdit
# def on_button_click():
#     text = line_edit.text()
#     label.setText(text)
#
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#
#     window = QWidget()
#
#     layout = QVBoxLayout()
#
#     line_edit = QLineEdit()
#     layout.addWidget(line_edit)
#
#     button = QPushButton("Meni bos", window)
#     button.clicked.connect(on_button_click)
#     layout.addWidget(button)
#
#     label = QLabel()
#     layout.addWidget(label)
#
#     window.setLayout(layout)
#
#     window.setGeometry(100, 100, 200, 200)
#     window.setWindowTitle("PyQt5 Input Example")
#     window.show()
#
#     sys.exit(app.exec_())

#
# import sys
# from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout
#
#
# def on_button_click():
#     button.setText("Bosildi")
#     if button.clickedCount() == 2:
#         button.setText("Niqtama!")
#         print("Niqtama!")
#
#
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#
#     window = QWidget()
#
#     layout = QVBoxLayout()
#
#     button = QPushButton("Meni bos", window)
#     button.clicked.connect(on_button_click)
#     layout.addWidget(button)
#
#     window.setLayout(layout)
#
#     window.setGeometry(100, 100, 200, 200)
#     window.setWindowTitle("PyQt5 Button Example")
#     window.show()
#
#     sys.exit(app.exec_())
# import sys
# from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QLineEdit
#
# class BiyaOyunu(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.initUI()
#
#     def initUI(self):
#         self.setGeometry(100, 100, 300, 200)
#         self.setWindowTitle('Bi%a Oyunu')
#
#         self.label = QLabel(self)
#         self.label.setText("Sichqonchani bosing!")
#         self.label.move(80, 80)
#
#         self.button = QPushButton(self)
#         self.button.setText("10")
#         self.button.move(120, 120)
#         self.button.clicked.connect(self.buttonClicked)
#
#         self.textbox = QLineEdit(self)
#         self.textbox.move(120, 160)
#         self.textbox.textChanged.connect(self.onTextChanged)
#
#         self.show()
#
#     def keyPressEvent(self, event):
#         if event.key() == 16777220: # Enter tuşunun kodu
#             if self.label.text() == "Sichqonchani bosing!":
#                 self.label.setText("Bosildi")
#             elif self.label.text() == "Bosildi":
#                 self.label.setText("Niqtama!")
#
#     def buttonClicked(self):
#         if int(self.button.text()) > 0:
#             self.button.setText(str(int(self.button.text()) - 1))
#             if int(self.button.text()) == 0:
#                 self.button.setEnabled(False)
#
#     def onTextChanged(self, text):
#         self.label.setText("Yozuv uzunligi: " + str(len(text)))
#
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     oyun = BiyaOyunu()
#     sys.exit(app.exec_())







#
# import sys
# from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
#
# class MeniOyunu(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.sana()
#     def sana(self):
#         self.setGeometry(100, 100, 300, 200)
#         self.setWindowTitle('sana bosilganlar sonini')
#
#         self.button = QPushButton(self)
#         self.button.setText("Meni bos")
#         self.button.move(100, 100)
#         self.button.clicked.connect(self.onButtonClicked)
#
#         self.show()
#         self.count = 0
#     def onButtonClicked(self):
#         self.count += 1
#         self.button.setText(f"Meni bos ({self.count})")
#
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     oyun = MeniOyunu()
#     sys.exit(app.exec_())
#
#
# import sys
# from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
#
# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle("Sichqoncha")
#         self.setGeometry(150, 250, 400, 300)
#         self.label = QLabel(self)
#         self.label.setText("Bosildi")
#         self.label.move(150, 50)
#
#         self.count = 0
#     def mousePressEvent(self, event):
#         if event.button() == 1:
#             self.count += 1
#             if self.count == 1:
#                 self.label.setText("Bosildi")
#             elif self.count == 2:
#                 self.label.setText("Niqtama")
#                 self.count = 0
# app = QApplication(sys.argv)
# window = MainWindow()
# window.show()
# sys.exit(app.exec_())





















import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout
from PyQt5.QtGui import QColor, QPalette

app = QApplication(sys.argv)


class Color(QWidget):
    def __init__(self, color):
        super().__init__()
        self.setAutoFillBackground(True)
        palette = self.palette()
        palette.setColor(QPalette.Window, QColor(color))
        self.setPalette(palette)


class Colors(QMainWindow):
    def __init__(self):
        super().__init__()
        v_l = QHBoxLayout()
        a = Color("red")
        b = Color("cyan")
        c = Color("yellow")
        d = Color("violet")
        v_l.addWidget(a)
        v_l.addWidget(b)
        v_l.addWidget(c)
        v_l.addWidget(d)
        q = Color("green")
        q.setLayout(v_l)

        q1 = Color("purple")

        l = QHBoxLayout()
        a1 = Color("#787475")
        b1 = Color("#e1e920")
        l.addWidget(a1)
        l.addWidget(b1)
        q2 = QWidget()
        q2.setLayout(l)

        v_l_new = QVBoxLayout()
        v_l_new.addWidget(q)
        v_l_new.addWidget(q1)
        v_l_new.addWidget(q2)
        wid = QWidget()
        wid.setLayout(v_l_new)
        self.setCentralWidget(wid)


window = Colors()
window.show()

sys.exit(app.exec_())