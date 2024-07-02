#Electricity Bill from Jan to Dec in Dictionary and find the total and Average
bill={
    'Jan':1000,
    'Feb':1200,
    'Mar':1500,
    'Apr':1300,
    'May':1500,
    'Jun':1700,
    'Jul':1200,
    'Aug':1800,
    'Sep':2000,
    'Oct':3500,
    'Nov':1100,
    'Dec':1500,

} 
total= sum(bill.values())
print(f"Total bill is {total}")
print(f"Average bill is {total/12}")