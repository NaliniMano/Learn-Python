get_input=input("Enter a number")
nums=int(get_input)
if nums >= 100 :
    print("value greater than 100")
elif nums > 50 and nums <=99:
    print("Values between 50 to 99")
else:
    print("Value less than 50")

get_input2=input("Enter a year to find its leap year")
year=int(get_input2)
if (year % 4 == 0 and year % 100 !=0)or (year % 400==0):
    print("Its Leap Year!")
else:
    print("Not Leap year")