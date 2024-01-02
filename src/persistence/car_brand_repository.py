from domain.entities import CarBrand

from .core import BaseRepository


class CarBrandRepository(
    BaseRepository[CarBrand],
):
    entity = CarBrand
