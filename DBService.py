from typing import Type

from sqlalchemy.exc import IntegrityError

from extensions import db

Model = Type[db.Model]


class DBService:
    def __init__(self, flask_db):
        self.db = flask_db

    def add(self, model) -> Model:
        try:
            self.db.session.add(model)
            self.db.session.commit()
            return model
        except IntegrityError:
            self.rollback()

        return None

    def update(self, model) -> db.Model:
        try:
            self.db.session.merge(model)
            self.db.session.commit()
            return model
        except IntegrityError:
            self.rollback()

        return None

    def delete(self, model) -> bool:
        try:
            self.db.session.delete(model)
            self.db.session.commit()
            return True
        except IntegrityError:
            self.rollback()

        return False

    def commit(self):
        self.db.session.commit()

    def rollback(self):
        self.db.session.rollback()
