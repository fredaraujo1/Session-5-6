name = input("what is your name? ")
age = input("how old are you ")
age = int(age)
birth_year = 2023 - age

print(f"OMG ({name}, you are {age} years old so you were born in {birth_year} ")
print("OMG", name, ", you are", age, " years old so you were born in ", birth_year)

try:
    age1 = int(input("what is your age player 1?"))
    age2 = int(input("what is your age player 2?"))
    res = age1/age2
except ValueError:
    print("I am sorry, but that is not a valid number")
except ZeroDivisionError:
    print("I am sorry, but you cannot divide by zero")
except:
    print("I am sorry, but something went wrong")
else:
    print("player 1 is older than player 2 by a factor of", res)
finally:
    print("Thank you for playing")

    import random

    drinks = ["beer", "wine", "whiskey", "rum", "gin tonic", "vodka", "martini", "rakia"]
    try:
        age = int(input("How old are you? "))
        country = input("Where you living??")
    except ValueError:
        print("I am sorry, but that is not a valid number")

    else:
        # Do some sanity checks on age
        if age < 0 or age > 130:
            print("I am sorry, but your age cannot be negative or greater than 130")
        elif age < 18:
            print("I am sorry, too young to play this drinking game everywhere")
        elif age < 21 and country == "US":
            print("I am sorry, too young to play this drinking game in the US")
        else:
            drink = random.choice(drinks)
            print("Take a shot of ", drink, ". Thank you for playing, you are", age, "years old")

try:
    gross = float(input("Enter your salary: "))
    children = int(input("Enter the number of children you have: "))

except ValueError:
    print("Your salary or number of children must be expressed in a number format.")

else:
    if gross < 0:
        print("?")
    elif gross < 1000 and gross > 0:
        net = (0.9 + 0.01*children) * gross
        print("Your salary is ", net)
    elif gross < 2000 and gross >= 1000:
        net = (0.88+ 0.01*children) * gross
        print("Your salary is ", net)
    elif gross < 4000 and gross >= 2000:
        net = (0.86 + children*0.005) * gross
        print("Your salary is ", net)
    elif gross >= 4000:
        net = (0.82 + children*0.005) * gross
        print("Your salary is ", net)
