import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QGridLayout

class TicTacToe(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.grid = QGridLayout()
        self.setLayout(self.grid)

        self.player = 'X'
        self.board = [['', '', ''], ['', '', ''], ['', '', '']]

        for i in range(3):
            for j in range(3):
                button = QPushButton('', self)
                button.clicked.connect(lambda _, i=i, j=j: self.onButtonClick(i, j))
                self.grid.addWidget(button, i, j)

        self.setWindowTitle('Tic Tac Toe')
        self.show()

    def onButtonClick(self, i, j):
        if self.board[i][j] == '':
            self.board[i][j] = self.player
            self.sender().setText(self.player)
            if self.checkWin():
                print(f'{self.player} wins!')
                sys.exit()
            elif all(self.board[i][j] != '' for row in self.board for cell in row):
                print('It\'s a tie!')
                sys.exit()
            else:
                self.player = 'O' if self.player == 'X' else 'X'

    def checkWin(self):
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != '':
                return True
            if self.board[0][i] == self.board[1][i] == self.board[2][i] != '':
                return True
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != '':
            return True
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != '':
            return True
        return False

if __name__ == '__main__':
    app = QApplication(sys.argv)
    game = TicTacToe()
    sys.exit(app.exec_())
