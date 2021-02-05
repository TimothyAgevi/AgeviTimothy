# WRITE YOUR CODE SOLUTION HERE
from datetime import date
date=date.today()
day=date.strftime("%A")[0:3]

mon_fri=["Mon","Tue","Wed","Thu","Fri"]

def get_fare(day):
  if day in mon_fri:
    return 100
  elif day == "Sat":
    return 60
  return 80


fare=get_fare(day)

print(f"""Date:{date}\nDay:{day}\nFare:{fare}""")    