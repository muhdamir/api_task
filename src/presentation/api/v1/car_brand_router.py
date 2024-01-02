from fastapi import APIRouter, Depends, Path

from application.services import CarBrandService
from typing import Annotated

car_brand_router = APIRouter(
    tags=["Car Brand"],
    prefix="/car_brand",
)


@car_brand_router.get(
    "/",
)
def get_all_car_brand(
    service: CarBrandService = Depends(),
):
    """
    Get all car brand name scraped from mudah.my
    """
    return service.get_all()


@car_brand_router.get(
    "/{car_brand_id}",
)
def get_car_brand_by_id(
    car_brand_id: Annotated[int, Path(gt=0)],
    service: CarBrandService = Depends(),
):
    """
    Get a specific car brand
    """
    return service.get_by_id(id_=car_brand_id)
