from typing import Annotated

from fastapi import APIRouter, Depends, Path

from application.services import CarInfoService

Service = Annotated[CarInfoService, Depends(CarInfoService)]
Id = Annotated[int, Path(gt=0)]

car_info_router = APIRouter(
    prefix="/car_info",
    tags=["Car Info"],
)


@car_info_router.get("/")
def get_all_car_info(service: Service):
    return service.get_all()


@car_info_router.get("/{car_info_id}")
def get_car_info_by_id(service: Service, car_info_id: Id):
    return service.get_by_id(id_=car_info_id)
