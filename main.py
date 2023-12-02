from PyQt6.QtWidgets import *

app = QApplication([])

window = QWidget()
lbl = QLabel("Скільки буде 2+2?")
ans1 = QRadioButton("4")
ans2 = QRadioButton("14")


main_line = QVBoxLayout()
main_line.addWidget(lbl)

h1 = QHBoxLayout()
h1.addWidget(ans1)
h1.addWidget(ans2)
main_line.addLayout(h1)
window.setLayout(main_line)



def true_var_1():
    msg = QMessageBox()
    msg.setText("Правильно")
    msg.exec()

ans1.clicked.connect(true_var_1)

window.show()
app.exec()