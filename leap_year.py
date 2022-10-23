import calendar

#With the help of library
new_year = int(input("Please, enter your year: "))
if calendar.isleap(new_year) == True:
    print("Year is leap by lib")
else:
    print("Year is not leap by lib")


#by myself
is_leap  = (new_year % 4 == 0) and ((new_year % 100 != 0) or (new_year % 400 == 0))
if is_leap == True:
    print("Year is leap by myself")
else:
    print("Year is not leap by myself")