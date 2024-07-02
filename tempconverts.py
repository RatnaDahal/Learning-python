#Temperature Converter: Celcius,Fahrenheit,Kelvin
#taking inputs as floats
a=float(input("Enter the temperature in Celcius"))
b=float(input("Enter the temperature in Fahrenheit"))
c=float(input("Enter the temperature in Kelvin"))

#Fahrenheit to celcius and vice-versa
fah_to_cel=((b-32)*(5/9))
cel_to_fah=float(a*(9/5)+32)

#Celcius to kelvin and vice-versa
cel_to_kel=(a+273.15)
kel_to_cel=(c-273.15)

#Fahrenheit to kelvin and vice-versa
fah_to_kel=((b-32)*(5/9)+273.15)
kel_to_fah=((c-273.15)*(9/5)+32)

print(f"The teperature {a} celcius in fahrenheit is {cel_to_fah}")
print(f"The temperaturre{b}fahrenheit in celcius is {fah_to_cel}")
print(f"The temperature {a}celcius in kelvin is {cel_to_kel}")
print(f"The temperature {c}kelvin in celcius is {kel_to_cel}")
print(f"The temperature {c}kelvin in fahrenheit is {kel_to_fah}")
print(f"The temperature {b}fahrenheit in kelvin is {fah_to_kel}")
