# Assignment: create a function that returns multiple values (move all user inputs in one function)
def get_user_inputs(): 
    money_input = float(  # float is used to enable decimal points because money is the subject
        input("Please enter the amount of money you have: "))
    apple_input = float(  # float is used to enable decimal points because money is the subject if talking about price
        input("Please enter the price of an apple that you would like to buy: "))
    return money_input, apple_input    

def final_output(moneyF, appleF):  # function for computation
    # this is converted to integer data type to avoid decimal places while flashing no. of apples
    max_apple = int(moneyF//appleF)
    change = moneyF % appleF

    print(
    "You can buy " + str(max_apple) + " apples and your change is " + str(change) + " pesos.")

money, apple = get_user_inputs()
final_output(money, apple)