from fastapi import Depends

from persistence import CarModelRepository

from .core import BaseService


class CarModelService(
    BaseService[CarModelRepository],
):
    def __init__(
        self,
        repository: CarModelRepository = Depends(),
    ) -> None:
        super().__init__(repository)
