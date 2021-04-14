import datetime
today = datetime.date.today()
print(today)

birthday = datetime.date(2000, 6, 22)
print(birthday)
dayssinceBirth = (today-birthday).days
print(dayssinceBirth)
