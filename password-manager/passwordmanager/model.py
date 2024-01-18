from pathlib import Path
from typing import Dict, TypeGuard
from passwordmanager import PASSFILE
import string
import random
import json


class PasswordModel:

    def __init__(self) -> None:
        self._filename = PASSFILE
        self._check_file()
        pass

    def _check_file(self):
        """ CHeck the existence of file. """
        if (not PASSFILE.parent.exists()) | (not PASSFILE.exists()):
            PASSFILE.parent.mkdir(exist_ok=True)
            PASSFILE.touch(exist_ok=True)
            PASSFILE.write_text("{}")
        return None

    def save_password(self, arg: Dict[str, str]):
        """ Save the password in the file. """
        password = {arg.get("website"): dict(
            email=arg.get("email", ""),
            password=arg.get("password", ""))}

        data: Dict = json.loads(PASSFILE.read_text())
        data.update(password)

        with open(self._filename, mode="w") as ofile:
            json.dump(data, ofile, indent=2)

        return None

    def generate_password(self) -> str:
        """ Password generators. """
        letters = random.choices(string.ascii_letters, k=random.randint(8, 10))
        numbers = random.choices(string.digits, k=random.randint(2, 4))
        symbols = random.choices(string.punctuation, k=random.randint(2, 4))
        password = [*letters, *numbers, *symbols]
        random.shuffle(password)
        return "".join(password)

    def search_password(self, key: str)->Dict[str, str]:
        """ Search for password in password file. """
        passwords:Dict = json.loads(PASSFILE.read_text())
        
        if key not in passwords.keys():
            raise Exception("Website not found in database")
        
        output:Dict = passwords[key]
        return output
