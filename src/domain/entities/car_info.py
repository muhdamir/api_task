from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey
from sqlalchemy.dialects.mysql import VARCHAR
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base

if TYPE_CHECKING:
    from .car_model import CarModel


class CarInfo(Base):
    __tablename__ = "car_info"

    car_info_id: Mapped[int] = mapped_column(primary_key=True)
    car_manufactured_year: Mapped[int] = mapped_column(nullable=False)
    car_mileage: Mapped[str] = mapped_column(VARCHAR(45), nullable=False)
    car_price: Mapped[float] = mapped_column(nullable=False)
    car_model_id: Mapped[int] = mapped_column(
        ForeignKey("car_model.car_model_id", ondelete="CASCADE")
    )

    # relationship
    car_model: Mapped["CarModel"] = relationship(back_populates="car_info")
