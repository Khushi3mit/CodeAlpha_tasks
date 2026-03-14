# Predefined stock prices
stock_prices = {
    "AAPL": 188,
    "TSLA": 250,
    "GOOGL": 135,
    "AMZN": 145
}

portfolio = {}
total_value = 0

print("Stock Portfolio Tracker")

while True:
    stock = input("Enter stock name (or type 'done' to finish): ").upper()

    if stock == "DONE":
        break

    if stock not in stock_prices:
        print("Stock not available.")
        continue

    quantity = int(input("Enter quantity: "))
    portfolio[stock] = quantity

# Calculate total investment
for stock, quantity in portfolio.items():
    value = stock_prices[stock] * quantity
    total_value += value
    print(stock, "value:", value)

print("Total Investment Value:", total_value)

# Save result to file
with open("portfolio.txt", "w") as file:
    file.write("Total Investment Value: " + str(total_value))

print("Result saved in portfolio.txt")