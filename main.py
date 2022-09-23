from PyQt5.QtWidgets import (QDialog, QLabel, QPushButton, QMessageBox, QVBoxLayout, QApplication)
import random

options=['kamień', 'papier', 'nożyce']
player2=random.choice(options)
rock, paper, scissors = options 

class WidgetGallery(QDialog):
    def __init__(self, parent=None):
        super(WidgetGallery, self).__init__(parent)

        self.setWindowTitle('Gra kamień, papier, nożyce')
        message=QLabel('<h3>Witaj w grze papier, kamień, nożyce</h3>', self)

        button1=QPushButton(rock)
        button2=QPushButton(paper)
        button3=QPushButton(scissors)

        def on_button_rock(self):
            alert = QMessageBox()
            if player2==rock:
                alert.setText('Komputer wybrał kamień. Remis')
            else:
                if player2==paper:
                    alert.setText('Komputer wybrał papier. Komputer wygrał')
                else:
                    alert.setText('Komputer wybrał nożyce. Wygrałeś!')
            alert.exec()

        def on_button_paper(self):
            alert = QMessageBox()
            if player2==paper:
                alert.setText('Komputer wybrał papier. Remis')
            else:
                if player2==scissors:
                    alert.setText('Komputer wybrał nożyce. Komputer wygrał')
                else:
                    alert.setText('Komputer wybrał kamień. Wygrałeś!')
            alert.exec()

        def on_button_scissors(self):
            alert = QMessageBox()
            if player2==scissors:
                alert.setText('Komputer wybrał nożyce. Remis')
            else:
                if player2==rock:
                    alert.setText('Komputer wybrał kamień. Komputer wygrał')
                else:
                    alert.setText('Komputer wybrał papier. Wygrałeś!')
            alert.exec()

        button1.clicked.connect(on_button_rock)
        button2.clicked.connect(on_button_paper)
        button3.clicked.connect(on_button_scissors)

        layout=QVBoxLayout()
        layout.addWidget(message)
        layout.addWidget(button1)
        layout.addWidget(button2)
        layout.addWidget(button3)
        self.setLayout(layout)


if __name__ == '__main__':
    import sys
    
    app=QApplication(sys.argv)
    window=WidgetGallery()
    window.show()
    app.exec()

