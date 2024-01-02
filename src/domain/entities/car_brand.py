from datetime import datetime
from typing import TYPE_CHECKING

from sqlalchemy import func
from sqlalchemy.dialects.mysql import VARCHAR
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base

if TYPE_CHECKING:
    from .car_model import CarModel


class CarBrand(Base):
    __tablename__ = "car_brand"

    car_brand_id: Mapped[int] = mapped_column(primary_key=True)
    car_brand_name: Mapped[str] = mapped_column(
        VARCHAR(45),
        nullable=False,
        unique=True,
    )
    car_brand_created_at: Mapped[datetime] = mapped_column(
        default=func.now(),  # pylint: disable=not-callable
    )
    car_brand_updated_at: Mapped[datetime] = mapped_column(
        default=func.now(),  # pylint: disable=not-callable
        onupdate=func.now(),  # pylint: disable=not-callable
    )

    # relationship
    car_models: Mapped[list["CarModel"]] = relationship(
        back_populates="car_brand",
        cascade="all, delete-orphan",
    )
