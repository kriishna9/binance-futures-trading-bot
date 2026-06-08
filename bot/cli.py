from bot.orders import place_market_order, place_limit_order

order_type = input("Order Type (MARKET/LIMIT): ").upper()
symbol = input("Symbol: ").upper()
side = input("Side (BUY/SELL): ").upper()
quantity = float(input("Quantity: "))

if order_type == "MARKET":
    response = place_market_order(symbol, side, quantity)

elif order_type == "LIMIT":
    price = float(input("Price: "))
    response = place_limit_order(
        symbol,
        side,
        quantity,
        price
    )

else:
    print("Invalid Order Type")
    exit()

print("\nOrder Placed Successfully!")
print(response)