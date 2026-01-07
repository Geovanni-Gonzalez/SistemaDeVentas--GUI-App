from .repository import Repository
from .models import Usuario

class AuthController:
    def __init__(self):
        self.repo = Repository("usuarios.txt")

    def login(self, username, password):
        users = self.repo.load_all(Usuario.from_string)
        for user in users:
            if user.username == username and user.password == password:
                return user
        return None
