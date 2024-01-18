from typing import Dict
from PyQt6.QtGui import QIcon, QPixmap
from PyQt6.QtWidgets import (QGridLayout, QLabel, QLineEdit, QMainWindow, QPushButton, 
                             QWidget)


from passwordmanager import IMAGE



class PageMain(QMainWindow):

    def __init__(self):
        super().__init__()
        self._central_ui = QWidget()
        self.setCentralWidget(self._central_ui)
        self.setWindowTitle("Password Manager")
        self.setWindowIcon(QIcon(str(IMAGE)))
        # self.setMinimumSize(QSize(500, 500))

        self._init_ui()
        pass

    def _init_ui(self):
        layout = QGridLayout(self._central_ui)
        self._label_image = QLabel()
        image = QPixmap(str(IMAGE))
        self._label_image.setPixmap(image)

        label_website = QLabel(self.tr("Website"))
        label_username = QLabel(self.tr("Email/Username"))
        label_password = QLabel(self.tr("Password"))

        self._textbox_website = QLineEdit()
        self._textbox_email = QLineEdit()
        self._textbox_email.setText("victorespoir.dev@gmail.com")
        self._textbox_password = QLineEdit()

        self._button_search = QPushButton(self.tr("Search"))
        self._button_generate = QPushButton(self.tr("Generate Password"))
        self._button_add = QPushButton(self.tr("Add"))

        # positionning
        layout.addWidget(self._label_image, 0, 1, 1, 1)
        layout.addWidget(label_website, 1, 0, 1, 1)
        layout.addWidget(label_username, 2, 0, 1, 1)
        layout.addWidget(label_password, 3, 0, 1, 1)
        layout.addWidget(self._textbox_website, 1, 1, 1, 1)
        layout.addWidget(self._textbox_email, 2, 1, 1, 2)
        layout.addWidget(self._textbox_password, 3, 1, 1, 1)
        layout.addWidget(self._button_search, 1,2,1,1)
        layout.addWidget(self._button_generate, 3,2,1,1)
        layout.addWidget(self._button_add, 4,1,1,2)
        return None
    
    def retrieve_informations(self)->Dict[str, str]:
        website = self._textbox_website.text()
        email = self._textbox_email.text()
        password = self._textbox_password.text()
        output:Dict[str, str] = dict(website=website, email=email, password=password)
        return output
    
    def wipeoff_textboxes(self):
        self._textbox_website.setText("")
        self._textbox_password.setText("")
        return None


