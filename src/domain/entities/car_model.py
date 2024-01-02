from datetime import datetime
from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey, UniqueConstraint, func
from sqlalchemy.dialects.mysql import VARCHAR
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base

if TYPE_CHECKING:
    from .car_brand import CarBrand
    from .car_info import CarInfo


class CarModel(Base):
    __tablename__ = "car_model"

    car_model_id: Mapped[int] = mapped_column(primary_key=True)
    car_model_name: Mapped[str] = mapped_column(VARCHAR(45), nullable=False)
    car_brand_id: Mapped[int] = mapped_column(
        ForeignKey("car_brand.car_brand_id", ondelete="CASCADE")
    )
    car_model_created_at: Mapped[datetime] = mapped_column(
        default=func.now(),  # pylint: disable=not-callable
    )
    car_model_updated_at: Mapped[datetime] = mapped_column(
        default=func.now(),  # pylint: disable=not-callable
        onupdate=func.now(),  # pylint: disable=not-callable
    )

    # relationship
    car_brand: Mapped["CarBrand"] = relationship(
        back_populates="car_models",
    )
    car_info: Mapped[list["CarInfo"]] = relationship(
        back_populates="car_model",
        cascade="all, delete-orphan",
    )

    __table_args__ = (
        UniqueConstraint(
            "car_model_name",
            "car_model_id",
        ),
    )
