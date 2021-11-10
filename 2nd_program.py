# Assignment: create a function that returns multiple values (move all user inputs in one function)
apple_price = 20
orange_price = 25

apple = int(input(
      "Please enter the number of apples you want to buy: "))
orange = int(input(
        "Please enter the number of oranges you want to buy: "))

amount = ((apple*apple_price) +  # no. of apples and oranges are multiplied by their respective prices, then add together to get the total amount
          (orange*orange_price))
# this is the target final output
print("The total amount is Php" + str(amount) + ".00.")