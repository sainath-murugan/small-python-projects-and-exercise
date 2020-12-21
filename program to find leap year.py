## to find leap year
def leap_year(year):
  if year % 4 == 0 and year % 100 != 0:
    leap = "It is a leap year"
  elif year % 100 == 0 and year % 400 == 0:
    leap = "It is not a leap year"
  else:
    leap = "It is not a leap year"
    
  return leap
  
year = int(input())
print(leap_year(year))
