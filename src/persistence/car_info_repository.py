from domain.entities import CarInfo

from .core import BaseRepository


class CarInfoRepository(
    BaseRepository[CarInfo],
):
    entity = CarInfo
