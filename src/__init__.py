from .config import DBConnection
from .entities import Users as UsersModel

class insert_user(self, name):
    with DBConnection() as db:
        new_user = UsersModel(name = name)
        db.session.add(new_user)
        db.session.commit()

