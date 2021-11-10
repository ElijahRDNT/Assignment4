# Assignment: create a function that returns multiple values (move all user inputs in one function)
try:
    
    def get_user_inputs(): 
        money_input = float(  # float is used to enable decimal points because money is the subject
            input("Please enter the amount of money you have: "))
        apple_input = float(  # float is used to enable decimal points because money is the subject if talking about price
            input("Please enter the price of an apple that you would like to buy: "))

        if(apple_input == 0.0):  # restricts user to enter 0.00 priced apples
            print("Sorry, we don't have apples that cost 0.00 pesos.")
            quit()  # prompt to terminate the program
        else:
            return money_input, apple_input    

    def final_output(moneyF, appleF):  # function for computation
        # this is converted to integer data type to avoid decimal places while flashing no. of apples
        max_apple = int(moneyF//appleF)
        change = moneyF % appleF

        # target final output
        print(
            f"You can buy {max_apple} apples and your change is {change:.2f} pesos.")

    money, apple = get_user_inputs()

    if(money < 0 or apple < 0):  # restricts the user to enter less than 0 inputs
        print("Error. Less than 0 inputs are invalid.")
    else:
        # prompts the system to execute the final_output function
        final_output(money, apple)

except ValueError:  # this will be executed if the input datatype is incorrect or the input is empty
    print("Invalid input. Please input a number.")