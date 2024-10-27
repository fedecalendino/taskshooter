from pytz import UTC

from .trigger import MinuteTrigger, HourTrigger, DayTrigger

minutes_1 = MinuteTrigger(1)
minutes_5 = MinuteTrigger(5)
minutes_10 = MinuteTrigger(10)
minutes_15 = MinuteTrigger(15)
minutes_20 = MinuteTrigger(20)
minutes_30 = MinuteTrigger(30)
minutes_60 = MinuteTrigger(60)

hours_1 = HourTrigger(1)
hours_2 = HourTrigger(2)
hours_3 = HourTrigger(3)
hours_6 = HourTrigger(6)
hours_12 = HourTrigger(12)
hours_24 = HourTrigger(24)

utc_0000 = DayTrigger(hour=0, minute=0, tz=UTC)
utc_0600 = DayTrigger(hour=6, minute=0, tz=UTC)
utc_1200 = DayTrigger(hour=12, minute=0, tz=UTC)
utc_1800 = DayTrigger(hour=18, minute=0, tz=UTC)
utc_2359 = DayTrigger(hour=23, minute=59, tz=UTC)
