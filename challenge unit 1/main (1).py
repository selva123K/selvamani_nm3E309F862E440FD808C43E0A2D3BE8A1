#python programm to check if year is a leap year or not
year=1999
if(year % 400==0) and (year % 100==0):
  print("{0}is a leap year".format(year))
else:
  print("{0} is not a leap year".format(year))
