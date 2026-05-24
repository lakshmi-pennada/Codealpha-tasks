# 1. Setup 5 available stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "AMZN": 175,
    "MSFT": 420,
    "NVDA": 900
}

print("Available stocks: AAPL ($180), TSLA ($250), AMZN ($175), MSFT ($420), NVDA ($900)")

# 2. Get input from the user
ticker = input("Enter stock name: ").upper().strip()
quantity = int(input("Enter how many shares you own: "))

# 3. Calculate total value
price_per_share = stock_prices[ticker]
total_value = quantity * price_per_share

# 4. Display the results
result_text = f"Your {quantity} shares of {ticker} are worth: ${total_value}"
print("\n" + result_text)

# 5. Save the result to a text file
with open("portfolio.txt", "w") as file:
    file.write(result_text)

print("Saved to portfolio.txt!")