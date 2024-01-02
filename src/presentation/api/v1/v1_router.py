from fastapi import APIRouter
from .car_brand_router import car_brand_router
from .car_model_router import car_model_router
from .car_info_router import car_info_router


v1_router = APIRouter(prefix="/v1")

v1_router.include_router(router=car_model_router)
v1_router.include_router(router=car_brand_router)
v1_router.include_router(router=car_info_router)
