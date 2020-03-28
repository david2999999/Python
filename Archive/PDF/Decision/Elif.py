def main():
    milk_price = 1.50

    # You can create a chain of tests beginning with if ... : using elif ... : . elif ... : enables a
    # variety of conditions to be tested for but only if a prior condition wasn ’ t met. If you use a series of if
    # ... : statements they will all be executed. If you use an if ... : followed by an elif ... : , the
    # elif ... : will be evaluated only if the if ... : results in a False value:
    if milk_price < 1.25 :
        print("Buy two cartons of milk, they are on sale")
    elif milk_price < 2.00 :
        print("Buy one carton of milk, prices are normal")
    elif milk_price > 2.00:
        print("Go somewhere else, Milk cost too much here")


    # There is also a fall - through statement that you can insert to handle those cases where none of the prior
    # tests resulted in a True value: the else: statement. If none of the if ... : or elif ... :
    # statements have test conditions that evaluate to True , the else: clause is invoked:
    OJ_price = 2.50
    if OJ_price < 1.25:
        print("Buy one, I'm thirsty")
    elif OJ_price <= 2.00:
        print("Umm, sure, but I'll drink it slowly")
    else :
        print("I don't have enough money, never mind")

if __name__ == "__main__":
    main()