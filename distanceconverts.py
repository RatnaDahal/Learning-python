#WAP to converts distance between km,miles and metres based on their user inputs
#Taking input as floats
 
a=float(input("Enter the numbers in km: "))
b=float(input("Enter the numbers in miles: "))
c=float(input("Enter the numbers in meters: "))

#Converting km into miles and vice-vers
d1=a*1.609344 
d2=b/1.609344

#converting km into metre and vice=vers
d3=a*1000
d4=c/1000

#converting miles into metre and vice=versa
d5=b*1609.34
d6=c/1609.34

print(f"length in km into miles is {d1}")
print(f"length in miles into km is {d2}")
print(f"length in km into metre is {d3}")
print(f"length in metre in km is{d4}")
print(f"length in miles in metre is {d5}")
print(f"length in metre in miles is {d6}")




