from fastapi import Depends

from persistence import CarBrandRepository

from .core import BaseService


class CarBrandService(
    BaseService[CarBrandRepository],
):
    def __init__(
        self,
        repository: CarBrandRepository = Depends(),
    ) -> None:
        super().__init__(repository)
