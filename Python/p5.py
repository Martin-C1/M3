#Martin C
#Oct 10, 2024

fahrenheit= float(input("enter the temperature in fahrenheit:"))
#This is where the calculation happens
celsius= (fahrenheit - 32) * 5/9
if fahrenheit <30:
    print(f"That's cold! In Norway you would say it is {celsius:.2f} degrees C.")
elif 30 <= fahrenheit <= 70:
    print(f"That's Balmy! In Japan you would say it is {celsius:.2f} degrees C.")
else:
    print(f"That's hot! In Brazil you would say it is {celsius:.2f} degrees C.")
#program that asks for temperature in fahrenheit, calculates the temperature in celsius, then replies based on the temperature
