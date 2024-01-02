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


def drink(drink, number):

    bill = 0

    match (drink):
        case "cola":
            bill += 10*number
        case "sprite":
            bill += 15*number
        case "orange":
            bill += 5*number
    return bill


pizza_size = str(input("which pizza size do you want \n 1. for Large \n 2. for Medium \n 3. for Samll \n"))
no_pizza = int(input('number of pizzas do you want \n'))
pizabill = pizzabilling(pizza_size, no_pizza)
print(f" your pizza bill is {pizabill}$")