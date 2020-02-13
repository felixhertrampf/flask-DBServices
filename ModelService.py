from typing import List, Generic, TypeVar, Optional

from sqlalchemy.sql.expression import func

from extensions import db
from service.DBService import DBService

M = TypeVar('M', bound=db.Model)


class ModelService(DBService, Generic[M]):

    def __init__(self, flask_db, model: M):
        super().__init__(flask_db)
        self.model = model

    def get(self):
        return self.model

    def count(self, **kwargs) -> int:
        if len(kwargs) == 0:
            return self.db.session.query(self.model).count()

        return self.model.query.filter_by(**kwargs).count()

    def existsBy(self, **kwargs) -> bool:
        return self.model.query.filter_by(**kwargs).count() == 1

    def get_latest(self) -> M:
        return self.db.session.query(self.model).order_by(self.model.id.desc()).first()

    def find_by(self, **kwargs) -> M:
        return self.model.query.filter_by(**kwargs).first()

    def find_all_by(self, **filters) -> List[M]:
        return self.model.query.filter_by(**filters).all()

    def find_all_ordered(self, order):
        return self.db.session.query(self.model).order_by(order).all()

    def delete_by(self, **kwargs) -> bool:
        return self._commit(delete=self.model.query.filter_by(**kwargs).first())

    def get_all(self) -> List[M]:
        return self.model.query.all()

    def get_random(self) -> Optional[M]:
        return self.db.session.query(self.model).order_by(func.random()).first()
