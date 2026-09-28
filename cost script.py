from decimal import Decimal

#calculates the total cost of what you need and how much you will have left
while 1 == 1:
    #gets the cost of the product and how much money you have
    c = Decimal(input('how much is the thing you want to purchase   $'))
    m = Decimal(input('how much money do you have   $'))
    #calculats calculates how much money you will have or need
    cost = (c*Decimal(0)) - m
    rounded_cost = round(cost, 2)
    if rounded_cost > 0:
        print("you need $",rounded_cost,"more")
    elif rounded_cost < 0:
        print("you will have $",rounded_cost*-1,"left")
    

