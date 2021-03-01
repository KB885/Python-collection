# Discount price
# In this challenge you must discount a price accoring to its value

# Constant price
price = 250

# We will use the if-elif case
if price >= 300: # If price is 300 or above
    price *= 0.7
elif price >= 200: # If price is between 200 and 300
    price *= 0.8
elif price >= 100: # if price is between 100 and 200
    price *= 0.9
elif price < 100 and price >= 0: # if price is less than 100
    price *= 0.95

# Print out the finale price
print(price)
