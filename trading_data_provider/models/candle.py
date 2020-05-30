from sqlalchemy import (
    Table,
    Column,
    ForeignKey,
    PrimaryKeyConstraint,
)
from sqlalchemy.types import DateTime, Float
from sqlalchemy.orm import mapper, relationship
from dataclasses import dataclass
from datetime import datetime
from trading_data_provider.models.provider import Provider
from trading_data_provider.models.metadata import metadata


candle_table = Table("candles", metadata,
    Column("date", DateTime(timezone=True), primary_key=True),
    Column("open", Float(precision=53)),
    Column("close", Float(precision=53)),
    Column("high", Float(precision=53)),
    Column("low", Float(precision=53)),
    Column("average", Float(precision=53)),
    Column("volume", Float(precision=53)),
    Column("provider_id", ForeignKey("provider.id"), primary_key=True),
)


@dataclass
class CandleData:
    date: datetime
    open: float
    close: float
    high: float
    low: float
    average: float
    volume: float


mapper(CandleData, candle_table, properties={
  'provider': relationship(Provider)
})
