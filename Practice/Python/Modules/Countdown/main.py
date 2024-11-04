import bday_messages

import datetime


date_today = datetime.date.today()
bday_date = datetime.date(2024, 12, 13)

time_difference = bday_date - date_today

if (str(date_today) == str(bday_date)):
	print(bday_messages.random_message)
else:
	print(f"My next birthday is {time_difference} days away!")

print(type(date_today), type(bday_date))