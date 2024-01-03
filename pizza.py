def pizzabilling(pizzasize, number):

    bill = 0

    match (pizzasize):
        case "1":
            bill += 15*number
        case "2":
            bill += 10*number
        case "3":
            bill += 5*number
    return bill


def drink_bill(drink, number):

    bill = 0

    match (drink):
        case "1":
            bill += 10*number
        case "2":
            bill += 15*number
        case "3":
            bill += 5*number
    return bill


pizza_size = str(input("which pizza size do you want \n 1. for Large \n 2. for Medium \n 3. for Samll \n"))
no_pizza = int(input('number of pizzas do you want \n'))

drink = str(input("which drink size you want \n 1. for cola \n 2. for sprite \n 3. for orange \n"))
no_drink = int(input('number of drink you want \n'))
pizabill = pizzabilling(pizza_size, no_pizza)
drinkbill = drink_bill(drink, no_drink)

print(f" your pizza bill is {pizabill}$")
print(f" your drink bill is {drinkbill}$")
print(f" total bill  {drinkbill+pizabill}$")