from datetime import datetime, date

DATE_TIME = datetime.now()

DATE_NOW = DATE_TIME.date()

DATE_TIME_PAST = DATE_TIME.replace(year=DATE_TIME.year-1)

DATE_PAST = DATE_TIME_PAST.date()

print(DATE_NOW)

print(DATE_PAST)