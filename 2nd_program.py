# Assignment: create a function that returns multiple values (move all user inputs in one function)
# constant values are placed at the top so it won't be disrupted while editting the whole program
apple_price = 20
orange_price = 25

print("\nFRUIT              PRICE")
print("Apple  =========> Php20.00")
print("Orange =========> Php25.00")    
                
def get_user_input():  # function for collecting inputs
    apple_l = input(
        "\n\nPlease enter the number of apples you want to buy: ")
    orange_l = input(
        "Please enter the number of oranges you want to buy: ")
    return apple_l, orange_l


# function for computation and printing of target final output
def final_output(applesP, orangesP):
    amount = ((applesP*apple_price) +  # no. of apples and oranges are multiplied by their respective prices, then add together to get the total amount
              (orangesP*orange_price))
    # this is the target final output
    print("The total amount is Php" + str(amount) + ".00.")


apples_g, oranges_g = get_user_input()

try:  # the system will try the set of codes under "try". If can't be executed, it will proceed to "except"

    apples, oranges = int(apples_g), int(oranges_g)

    if(apples < 0 or oranges < 0):  # restricts the user to enter less than 0 inputs
        print("Invalid order. Less than 0 inputs are not accepted.")
    else:
        # if the input is correct, this prompts the final_output function to be executed
        final_output(apples, oranges)

except ValueError:  # this is executed if the data type of the input is unacceptable
    print("Error. Please enter whole numbers.")
