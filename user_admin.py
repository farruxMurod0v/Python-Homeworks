import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QLabel, QVBoxLayout, QHBoxLayout, QMessageBox
import sqlite3

class AdminWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Admin Window')

        self.gmail_label = QLabel('Gmail:')
        self.gmail_input = QLineEdit()
        self.password_label = QLabel('Password:')
        self.password_input = QLineEdit()
        self.login_button = QPushButton('Login')
        self.login_button.clicked.connect(self.adminLogin)

        layout = QVBoxLayout()
        layout.addWidget(self.gmail_label)
        layout.addWidget(self.gmail_input)
        layout.addWidget(self.password_label)
        layout.addWidget(self.password_input)
        layout.addWidget(self.login_button)

        self.setLayout(layout)

    def adminLogin(self):
        gmail = self.gmail_input.text()
        password = self.password_input.text()

        # Check the admin credentials in the database
        # Replace 'admin_table' with the actual table name in your database
        conn = sqlite3.connect('your_database.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM admin_table WHERE gmail=? AND password=?", (gmail, password))
        result = cursor.fetchone()
        conn.close()

        if result:
            # Open the admin operations window
            admin_operations_window.show()
            self.close()
        else:
            QMessageBox.warning(self, 'Retry Error', 'Incorrect Gmail or Password. Please try again.')

class UserWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('User Window')

        self.gmail_label = QLabel('Gmail:')
        self.gmail_input = QLineEdit()
        self.password_label = QLabel('Password:')
        self.password_input = QLineEdit()
        self.login_button = QPushButton('Login')
        self.login_button.clicked.connect(self.userLogin)

        layout = QVBoxLayout()
        layout.addWidget(self.gmail_label)
        layout.addWidget(self.gmail_input)
        layout.addWidget(self.password_label)
        layout.addWidget(self.password_input)
        layout.addWidget(self.login_button)

        self.setLayout(layout)

    def userLogin(self):
        gmail = self.gmail_input.text()
        password = self.password_input.text()

        # Check the user credentials in the database
        # Replace 'user_table' with the actual table name in your database
        conn = sqlite3.connect('your_database.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM user_table WHERE gmail=? AND password=?", (gmail, password))
        result = cursor.fetchone()
        conn.close()

        if result:
            # Open the user operations window
            user_operations_window.show()
            self.close()
        else:
            QMessageBox.warning(self, 'Retry Error', 'Incorrect Gmail or Password. Please try again.')

class AdminOperationsWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Admin Operations Window')

        # Add widgets and functionality for admin operations here

class UserOperationsWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('User Operations Window')

        # Add widgets and functionality for user operations here

app = QApplication(sys.argv)

admin_window = AdminWindow()
user_window = UserWindow()
admin_operations_window = AdminOperationsWindow()
user_operations_window = UserOperationsWindow()

admin_window.show()

sys.exit(app.exec_())