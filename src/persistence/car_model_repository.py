from domain.entities import CarModel

from .core import BaseRepository


class CarModelRepository(
    BaseRepository[CarModel],
):
    entity = CarModel
