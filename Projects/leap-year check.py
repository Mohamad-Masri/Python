year = int(input("input a year : "))

if(year % 4) == 0 :
    print("{0} is a leap-year".format(year))
else:
    print("{0} is not a leap-year".format(year))
