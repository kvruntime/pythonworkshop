from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *
from tmyapp import TmyApp
# from todoapp import TodoApp

# App = TodoApp
App = TmyApp

app=QApplication([])
app.setApplicationDisplayName(App.AppName)
app.setApplicationName(App.AppName)
app.setApplicationVersion(App.AppVersion)
w=App()
w.show()
app.exec()