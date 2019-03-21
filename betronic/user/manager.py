import copy
from betronic.base.manager import BaseManager
from betronic.user.model import UserModel
from betronic.user.assistants.auth_assistant import AuthAssistant


class UserManager(BaseManager):

    def __init__(self, db):
        super().__init__(UserModel)
        self.db = db

    def register_user(self, args: dict):
        auth_assistant = AuthAssistant(self.db)
        data = copy.copy(args)
        user = auth_assistant.register(data)
        self.db.session.add(user)
        self.db.session.commit()
        return user
