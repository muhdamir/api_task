from typing import Annotated

from fastapi import APIRouter, Depends, Path

from application.services import CarModelService

car_model_router = APIRouter(
    prefix="/car_model",
    tags=["Car Model"],
)


@car_model_router.get("/")
def get_all_car_model(
    service: CarModelService = Depends(),
):
    """
    Get all car model name scraped from mudah.my
    """
    return service.get_all()


@car_model_router.get("/{car_model_id}")
def get_car_model_by_id(
    car_model_id: Annotated[
        int,
        Path(
            title="id of the model",
            gt=0,
        ),
    ],
    service: CarModelService = Depends(),
):
    """
    Get specific car model by id
    """
    return service.get_by_id(car_model_id)
