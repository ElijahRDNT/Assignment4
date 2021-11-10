# Assignment: create a function that returns multiple values (move all user inputs in one function)
apple_price = 20
orange_price = 25

def get_user_input():  # function for collecting inputs
    apple_l = int(input(
        "Please enter the number of apples you want to buy: "))
    orange_l = int(input(
            "Please enter the number of oranges you want to buy: "))
    return apple_l, orange_l

def final_output(applesP, orangesP):
    amount = ((applesP*apple_price) +  # no. of apples and oranges are multiplied by their respective prices, then add together to get the total amount
            (orangesP*orange_price))
    # this is the target final output
    print("The total amount is Php" + str(amount) + ".00.")

apples_g, oranges_g = get_user_input()
final_output(apples_g, oranges_g)