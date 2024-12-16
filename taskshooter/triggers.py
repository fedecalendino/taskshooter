from pytz import UTC

from .trigger import MinuteTrigger, HourTrigger, DayTrigger

every_minute = MinuteTrigger(1)
every_2_minutes = MinuteTrigger(2)
every_3_minutes = MinuteTrigger(3)
every_5_minutes = MinuteTrigger(5)
every_6_minutes = MinuteTrigger(6)
every_10_minutes = MinuteTrigger(10)
every_12_minutes = MinuteTrigger(12)
every_15_minutes = MinuteTrigger(15)
every_20_minutes = MinuteTrigger(20)
every_30_minutes = MinuteTrigger(30)
every_60_minutes = MinuteTrigger(60)

every_hour = HourTrigger(1)
every_2_hours = HourTrigger(2)
every_3_hours = HourTrigger(3)
every_4_hours = HourTrigger(4)
every_6_hours = HourTrigger(6)
every_12_hours = HourTrigger(12)
every_24_hours = HourTrigger(24)

at_0000_utc = DayTrigger(hour=0, minute=0, tz=UTC)
at_0300_utc = DayTrigger(hour=3, minute=0, tz=UTC)
at_0600_utc = DayTrigger(hour=6, minute=0, tz=UTC)
at_0900_utc = DayTrigger(hour=9, minute=0, tz=UTC)
at_1200_utc = DayTrigger(hour=12, minute=0, tz=UTC)
at_1500_utc = DayTrigger(hour=15, minute=0, tz=UTC)
at_1800_utc = DayTrigger(hour=18, minute=0, tz=UTC)
at_2100_utc = DayTrigger(hour=21, minute=0, tz=UTC)
at_2359_utc = DayTrigger(hour=23, minute=59, tz=UTC)

at_midnight_utc = at_0000_utc
at_noon_utc = at_1200_utc

at_sod_utc = at_0000_utc
at_eod_utc = at_2359_utc
