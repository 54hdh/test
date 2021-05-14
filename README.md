import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.Qsci import QsciScintilla, QsciLexerPython


if __name__ == "__main__":
    app = QApplication(sys.argv)
    font = QFont()
    font.setFamily('Courier')
    font.setFixedPitch(True)
    editor = QsciScintilla()
    editor.setFont(font)
    lexer = QsciLexerPython()
    lexer.setFont(font)
    editor.setLexer(lexer)
    editor.show()
    editor.setText(open(sys.argv[0]).read())
    app.exec_()