import datetime_nepali

year=int(input("Enter Nepali Year: "))
month=int(input("Enter Nepali Month: "))
day=int(input("Enter Nepali Day: "))
date=datetime_nepali.date(year,month,day).to_datetime_date()
print(f"Engliah date is: {date}")




