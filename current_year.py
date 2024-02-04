# Print today's year, month and day.

from datetime import date
today=date.today()
print("Current day: ", today.day)
print("Current month: ", today.month)
print("Current year: ", today.year)