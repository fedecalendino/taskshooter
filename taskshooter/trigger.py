from abc import ABC, abstractmethod
from datetime import datetime

from pytz import BaseTzInfo, UTC


class Trigger(ABC):
    @property
    @abstractmethod
    def description(self) -> str:
        raise NotImplementedError()

    @abstractmethod
    def check(self) -> bool:
        raise NotImplementedError()

    def __str__(self) -> str:
        return self.description


class MinuteTrigger(Trigger):
    def __init__(self, minutes: int, tz: BaseTzInfo = UTC):
        assert minutes > 0

        self.minutes: int = minutes
        self.tz: BaseTzInfo = tz

    @property
    def description(self) -> str:
        if self.minutes == 1:
            return "every minute"

        return "every {minutes} minutes".format(
            minutes=self.minutes,
        )

    def check(self) -> bool:
        now = datetime.now(self.tz)

        return now.minute % self.minutes == 0

    def __str__(self) -> str:
        return self.description


class HourTrigger(Trigger):
    def __init__(self, hours: int, tz: BaseTzInfo = UTC):
        assert hours > 0

        self.hours: int = hours
        self.tz: BaseTzInfo = tz

    @property
    def description(self) -> str:
        tz = self.tz.zone

        if self.hours == 1:
            return "every hour (tz={tz})".format(
                tz=tz,
            )

        return "every {hours} hours (tz={tz})".format(
            hours=self.hours,
            tz=tz,
        )

    def check(self) -> bool:
        now = datetime.now(self.tz)

        if now.minute != 0:
            return False

        return now.hour % self.hours == 0

    def __str__(self) -> str:
        return self.description


class DayTrigger(Trigger):
    def __init__(self, hour: int, minute: int, tz: BaseTzInfo = UTC):
        assert 0 <= hour < 24
        assert 0 <= minute < 60

        self.hour: int = hour
        self.minute: int = minute
        self.tz: BaseTzInfo = tz

    @property
    def description(self) -> str:
        return "every day @ {hour:02d}:{minute:02d} (tz={tz})".format(
            hour=self.hour,
            minute=self.minute,
            tz=self.tz.zone,
        )

    def check(self) -> bool:
        now = datetime.now(self.tz)

        return now.hour == self.hour and now.minute == self.minute
