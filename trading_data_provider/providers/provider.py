import abc
from datetime import datetime, timedelta


class Provider:

    def __init__(self, ) -> None:
        self.id = None
        self.name = None

    @abc.abstractmethod
    def get_historical_candles(
        self,
        trade_pair: str,
        start_date: datetime,
        end_date: datetime,
        delta: timedelta
    ) -> None:
        pass
