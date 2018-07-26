def calc_profit_percent(selling_price, cost_price):
    return ((selling_price - cost_price) / cost_price) * 100


def calc_loss_profit(selling_price, cost_price):
    profit = calc_profit_percent(selling_price, cost_price)
    if profit < 0:
        print("Loss of {}%".format(abs(profit)))
    elif profit > 0:
        print("Profit of {}%".format(abs(profit)))
    else:
        print("Neither profit nor loss")


cp = int(input("Please enter cost price of product: "))
sp = int(input("Please enter selling price of product: "))

calc_loss_profit(sp, cp)