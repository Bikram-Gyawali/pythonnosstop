import calendar,datetime,time
print(calendar.weekheader(3))
# commment in python
print(calendar.firstweekday())

print(calendar.month(2021,4,3)) #the last paremtr is the length of the month
print(calendar.calendar(2021))

weekday=calendar.weekday(2000,4,9)
print(weekday)

isLeap=calendar.isleap(2020)
print(isLeap)

notleap=-1

if(isLeap):
    print("this year is leap year")