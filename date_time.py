from datetime import datetime, timezone
from zoneinfo import ZoneInfo

# strftime — date → string
now = datetime.now()
formatted = now.strftime("%Y-%m-%d %H:%M:%S")
print(formatted)

# strptime — string → date
date_time = datetime.strptime("2023-01-01 12:00:00", "%Y-%m-%d %H:%M:%S")
print(date_time)


# TIMEZONE

# timezone UTC
dt = datetime.strptime("2023-01-01 12:00:00", "%Y-%m-%d %H:%M:%S")
dt = dt.replace(tzinfo=timezone.utc)

# convert to Warsaw
dt_pl = dt.astimezone(ZoneInfo("Europe/Warsaw"))

print(dt_pl)

# --- FORMAT ---
# %Y – year (e.g. 2026)
# %m – month (01–12)
# %d – day of the month (01–31)
# %H – hour (24-hour format, 00–23)
# %M – minute (00–59)
# %S – second (00–59)
