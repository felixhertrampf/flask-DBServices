from typing import Generic

from service.ModelService import ModelService, M
from service.PyOptional import PyOptional


class OptionalModelService(ModelService, Generic[M]):

    def get_latest(self) -> PyOptional[M]:
        return PyOptional[M](super().get_latest())

    def find_by(self, **kwargs) -> PyOptional[M]:
        return PyOptional[M](super().find_by(**kwargs))

    def add(self, model: M) -> PyOptional[M]:
        return PyOptional[M](super().add(model))

    def update(self, model: M) -> PyOptional[M]:
        return PyOptional(super().update(model))
