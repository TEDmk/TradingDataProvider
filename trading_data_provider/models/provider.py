from sqlalchemy import (
    Table,
    Column,
    ForeignKey,
    PrimaryKeyConstraint,
)
from sqlalchemy.orm import mapper
from sqlalchemy.types import String
from dataclasses import dataclass
import uuid
from trading_data_provider.models.type import GUID
from trading_data_provider.providers.provider import Provider
from trading_data_provider.models.metadata import metadata

provider_table = Table("provider", metadata,
    Column("id", GUID(), primary_key=True),
    Column("name", String())
)

mapper(Provider, provider_table)
