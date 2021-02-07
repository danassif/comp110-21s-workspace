"""A vaccination calculator."""

__author__ = "730329922"

# The datetime data type is imported from the datetime library.
# A datetime object models a specific date and time.
#
# Official Documentation: https://docs.python.org/3/library/datetime.html#datetime-objects
from datetime import datetime

# The timedelta data type is imported from the timedelta library.
# A timedelta object models a "time span", such as 1 day or 1 hour and 3 minutes.
# Subtracting two datetime objects will result in the timedelta between them.
# Adding a datetime and a timedelta will result in the datetime offset by the timedelta.
#
# Official Documentation: https://docs.python.org/3/library/datetime.html#datetime.timedelta
from datetime import timedelta

# Begin your solution here...

population: int = int(input("Population: "))
doses_administered: int = int(input("Doses administered: "))
doses_per_day: int = int(input("Doses per day: "))
target_percent_vaccinated: int = int(input("Target percent vaccinated: "))

number_of_people_who_need_vaccinated: float = ((target_percent_vaccinated * population) / 100)
number_of_people_after_doses_administered: float = (number_of_people_who_need_vaccinated - (doses_administered / 2))
number_of_days_left: float = (number_of_people_after_doses_administered / (doses_per_day / 2))

days_left_rounded = int(round(number_of_days_left))

number_days_left = timedelta = timedelta(days_left_rounded)

today: datetime = datetime.today()

days_left: datetime = today + number_days_left

converted_target = str(target_percent_vaccinated)
converted_days = str(days_left_rounded)
str(days_left.strftime("%B %d, %Y)"))

print("We will reach " + converted_target + "% vaccination in " + converted_days + " days, which falls on " + days_left.strftime("%B %d, %Y") + ".")