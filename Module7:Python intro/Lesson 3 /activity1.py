city = input("Enter your city name:") #By default, input is always a string
print(f"Wow! {city} is a great place to live!")

temp = float(input("Enter the current temperature in Celsius:"))
# print(type(temp))

if temp > 35:
    print("Warning:It is very hot today!")

if temp > 25:
    print("Great day to go outside")    
else:
    print("Grab a jacket before you go out")

if temp > 35:
    print("scorching hot!")
elif temp > 25:
    print("Warm and sunny")
elif temp > 15:
    print("Cool and breezy")
else :  
    print("COLD!") 
if city.lower() =="abu dhabi":
    print("You live i UAE")
elif city.lower() == "hisar":
    print("You live in India") 

import datetime
import calendar
now = datetime.datetime.now()
print(now) 
formatted = now.strftime("%d %B,%Y")
print(formatted) 
print(calendar.month(now.year,now.month))                        
                                                      