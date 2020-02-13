from typing import Type

from sqlalchemy.exc import IntegrityError

from extensions import db

Model = Type[db.Model]


class DBService:
    def __init__(self, flask_db):
        self.db = flask_db

    def add(self, model) -> Model:
        return self._commit(add=model)

    def update(self, model) -> db.Model:
        return self._commit(merge=model)

    def delete(self, model) -> bool:
        return self._commit(delete=model)

    def commit(self):
        self.db.session.commit()

    def rollback(self):
        self.db.session.rollback()

    def _commit(self,
                merge: Model = None,
                add: Model = None,
                delete: Model = None) -> Model:
        try:

            if merge:
                self.db.session.merge(merge)
            if add:
                self.db.session.add(add)
            if delete:
                self.db.session.delete(delete)

            self.commit()
        except IntegrityError:
            self.rollback()
            return None

        if merge:
            return merge
        if add:
            return add
        if delete:
            return delete

        return None
