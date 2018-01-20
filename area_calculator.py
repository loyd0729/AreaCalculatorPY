from math import pi
from time import sleep
from datetime import datetime
now = datetime.now()
hint = "Don't forget to include the correct units! \nExiting..."
option = input("Enter C for Circle or T for Triangle: ").upper()

print("Calculator started...")
print('%s/%s/%s ' '%s:%s' % (now.month, now.day, now.year, now.hour, now.minute))
sleep(1)

if option == 'C':
  radius = float(input("Enter radius: "))
  area = pi * radius ** 2
  print("The pie is baking...")
  sleep(1)
  print("%.2f" % (area))

elif option == 'T':
  base = float(input("Enter base: "))
  height = float(input("Enter height: "))
  area = base * height / 2
  print("Uni Bi Tri...") 
  print(hint)
  sleep(1)
  print("%.2f" % (area))
  
else:
  print("You entered garbage! Exiting...")
  sleep(3)