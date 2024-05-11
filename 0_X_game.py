import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QMessageBox

class TicTacToe(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Tic Tac Toe')
        self.setGeometry(100, 100, 300, 300)

        self.buttons = []
        self.turn = 'X'
        self.moves = 0
        self.winner = False

        layout = QVBoxLayout()

        for i in range(3):
            row = []
            for j in range(3):
                button = QPushButton('', self)
                button.clicked.connect(self.on_click)
                layout.addWidget(button)
                row.append(button)
            self.buttons.append(row)

        self.setLayout(layout)
        self.show()

    def on_click(self):
        button = self.sender()
        if button.text() == '' and not self.winner:
            button.setText(self.turn)
            self.moves += 1

            if (self.moves >= 5 and self.check_winner()):
                QMessageBox.information(self, 'Winner', f'Player {self.turn} wins!')
                self.winner = True
            elif (self.moves == 9 and not self.winner):
                QMessageBox.information(self, 'Draw', 'It\'s a draw!')
                self.winner = True

            if self.turn == 'X':
                self.turn = 'O'
            else:
                self.turn = 'X'

    def check_winner(self):
        for i in range(3):
            if (self.buttons[i][0].text() == self.buttons[i][1].text() == self.buttons[i][2].text() != '') or \
               (self.buttons[0][i].text() == self.buttons[1][i].text() == self.buttons[2][i].text() != ''):
                return True

        if (self.buttons[0][0].text() == self.buttons[1][1].text() == self.buttons[2][2].text() != '') or \
           (self.buttons[0][2].text() == self.buttons[1][1].text() == self.buttons[2][0].text() != ''):
            return True

        return False

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = TicTacToe()
    sys.exit(app.exec_())