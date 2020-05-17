import datetime
import pytz

# Specific Date
specific_date = datetime.date(2020, 3, 23)
print("Specific Date: ", specific_date)

# Today's Date
today_date = datetime.date.today()
print("Today: ", today_date)
print(f"Today: Year-{today_date.year} Month-{today_date.month} Day-{today_date.day}")
print(f"Weekday-{today_date.weekday()} IsWeekDay-{today_date.isoweekday()}")

# Week After
time_delta = datetime.timedelta(days=7)
print(f"Date after 7 days: {today_date + time_delta}")

# Difference between 2 Days
birthday = datetime.date(2020, 12, 18)
print("Days remaining for my birthday:", (birthday - today_date).days)

# Time
specific_time = datetime.time(12, 30, 45, 100)
print("Specific Time: ", specific_time)

# Specific Date and Time
specific_date_time = datetime.datetime(2020, 3, 30, 12, 23, 45, 239)
print("Specific Date and Time: ", specific_date_time)

# Adding Hour
add_hour = datetime.timedelta(hours=12)
print("Add Hour: ", specific_date_time + add_hour)

# Timezone

datetime_today = datetime.datetime.today()
datetime_now = datetime.datetime.now()
# This doesn't have Timezone info
datetime_utc_now = datetime.datetime.utcnow()

print(datetime_today)
print(datetime_now)
print(datetime_utc_now)

# Specific Date and Time with Timezone
specific_date_time_tz = datetime.datetime(2020, 3, 30, 12, 23, 45, tzinfo=pytz.UTC)
print("Specific Date and Time with Timezone: ", specific_date_time_tz)

# Current Date Time with Timezone
datetime_now_tz = datetime.datetime.now(tz=pytz.UTC)
print("Current Date Time with Timezone:", datetime_now_tz)

datetime_utc_now_tz = datetime.datetime.utcnow().replace(tzinfo=pytz.UTC)
print("Date Time with UTC:", datetime_utc_now_tz)

# Get timezone maintained in pytz
for tz in pytz.all_timezones:
    print(tz)
