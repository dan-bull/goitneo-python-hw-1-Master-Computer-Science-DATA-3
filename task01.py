from collections import defaultdict
from datetime import datetime, timedelta

def get_birthdays_per_week(users):
    next_monday = datetime.today().date() + timedelta(days=(7 - datetime.weekday(datetime.today().date())) % 7)
    today = next_monday
    birthdays = defaultdict(list)

    for user in users:
        name = user["name"]
        birthday = user["birthday"].date()
        birthday_this_year = birthday.replace(year=today.year)

        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)

        delta_days = (birthday_this_year - today).days

        if delta_days < 7:
            weekday = (today + timedelta(days=delta_days)).strftime("%A")
            if weekday in ["Saturday", "Sunday"]:
                weekday = "Monday"
            birthdays[weekday].append(name)

    return birthdays

users_sample = [
  {"name": "Mark Sunday", "birthday": datetime(1984, 3, 2)},
  {"name": "Jan Koum", "birthday": datetime(1976, 2, 27)},
  {"name": "Bill Gates", "birthday": datetime(1955, 2, 25)},
  {"name": "Bill Gates", "birthday": datetime(1955, 2, 25)},
  {"name": "Jan Koum", "birthday": datetime(1976, 2, 27)},
  {"name": "Mark Zuckerberg", "birthday": datetime(1984, 3, 1)},
]

birthdays_per_week = get_birthdays_per_week(users_sample)

for weekday, names in birthdays_per_week.items():
    print(f"{weekday}: {', '.join(names)}")
