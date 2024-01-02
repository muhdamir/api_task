from fastapi import Depends

from persistence import CarInfoRepository

from .core import BaseService


class CarInfoService(
    BaseService[CarInfoRepository],
):
    def __init__(
        self,
        repository: CarInfoRepository = Depends(),
    ) -> None:
        super().__init__(repository)
