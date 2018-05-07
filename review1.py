
#always need except with try
try:
   number = int(input("Enter a number: "))
   result = number/0
except ValueError:
    print("Input is not valid!")
except ZeroDivisionError:
    print("Cannot divide by zero")
except:
    print("Something bad happened!")
finally:
    print("closing the resource!")