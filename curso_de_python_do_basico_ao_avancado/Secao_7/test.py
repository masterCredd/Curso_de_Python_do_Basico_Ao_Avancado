import sys

from PySide6.QtWidgets import QApplication, QPushButton

app = QApplication(sys.argv)

botao = QPushButton('Texto do botão')
botao.setStyleSheet('font-size: 40px;')
botao.show()  # adiciona o Widget na hierarquia e exibe a janela


app.exec()  # o loop da aplicação
