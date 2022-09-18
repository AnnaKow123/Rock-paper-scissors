from PyQt5.QtWidgets import *
import random

options=['kamień', 'papier', 'nożyce']
player2=random.choice(options)
rock, paper, scissors = options 

app=QApplication([])
window=QWidget()

button1=QPushButton(rock)
button2=QPushButton(paper)
button3=QPushButton(scissors)

def on_button_rock():
    alert = QMessageBox()
    if player2==rock:
        alert.setText('Komputer wybrał kamień. Remis')
    else:
        if player2==paper:
            alert.setText('Komputer wybrał papier. Komputer wygrał')
        else:
            alert.setText('Komputer wybrał nożyce. Wygrałeś!')
    alert.exec()

def on_button_paper():
    alert = QMessageBox()
    if player2==paper:
        alert.setText('Komputer wybrał papier. Remis')
    else:
        if player2==scissors:
            alert.setText('Komputer wybrał nożyce. Komputer wygrał')
        else:
            alert.setText('Komputer wybrał kamień. Wygrałeś!')
    alert.exec()

def on_button_scissors():
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
layout.addWidget(button1)
layout.addWidget(button2)
layout.addWidget(button3)
window.setLayout(layout)

window.show()
app.exec()

