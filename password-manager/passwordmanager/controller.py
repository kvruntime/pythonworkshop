from typing import Dict
from PyQt6.QtWidgets import QDialog, QMessageBox
from passwordmanager.model import PasswordModel
from passwordmanager.pagemain import PageMain


class PasswordManagerController:

    def __init__(self, view: PageMain, model: PasswordModel) -> None:
        self._view = view
        self._model = model

        self._listen_events()
        pass

    def _listen_events(self):
        """ Listen all events. """
        self._view._button_add.clicked.connect(
            self.add_password)
        self._view._button_generate.clicked.connect(
            self._generate_password)
        self._view._button_search.clicked.connect(self._search_password)
        return None

    def add_password(self):
        obtained = self._view.retrieve_informations()

        for key in obtained.keys():
            if not obtained.get(key):
                self._on_empty_fields()
                return
        self._on_filled_fields(obtained)
        return None

    def _on_empty_fields(self):
        """ Called when user leave fields empty. """
        button = QMessageBox.warning(self._view,
                                     "Alert",
                                     """Please, fill all fields!""",
                                     buttons=QMessageBox.StandardButton.Ok)
        return None

    def _on_filled_fields(self, arg:Dict):
        """ Called when user enter fills all fields. """
        response = QMessageBox.question(self._view,
                                        "Save confirmation",
                                        "Are you sure ?",
                                        buttons=QMessageBox.StandardButton.Ok | QMessageBox.StandardButton.Cancel)
        if response == QMessageBox.StandardButton.Ok:
            self._view.wipeoff_textboxes()
            self._model.save_password(arg)
        else:
            pass
        return None
    
    def _generate_password(self):
        self._view._textbox_password.setText(str(self._model.generate_password()))
        return None
    
    
    def _search_password(self):
        """ Search for password. """
        key = self._view._textbox_website.text()
        key = "empty" if (key=="") else key
        
        try:
            data = self._model.search_password(key=key)
        except:
            QMessageBox.warning(self._view,
                                "Searching for password",
                                f"No data found for {key}",
                                QMessageBox.StandardButton.Ok)
            return
        email = data.get("email")
        password = data.get("password")
        QMessageBox.information(self._view,
                                "Searching result",
                                f"email: {email}\npassword: {password}",
                                QMessageBox.StandardButton.Ok)

        return None
