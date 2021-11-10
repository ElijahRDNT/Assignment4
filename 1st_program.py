# Assignment: create a function that returns multiple values (move all user inputs in one function)
def get_user_inputs():  # function for collecting inputs
    name_l = input("Please enter you name: ")
    age_l = input("Please enter your age in years: ")
    address_l = input("Please enter your address: ")
    return name_l, age_l, address_l  # returned 3 inputs


def display(name, age, address):  # the values of inputs are passed to be used inside the function
    print("\nHi, my name is " + name + ". I am " + age +  # this is the final output if the inputs are acceptable
          " years old and I live in " + address + ".")


# this function contains validation for age input such as the data type or value
def age_validation(nameF, ageF, addressF):
    try:  # the system will try the set of codes under "try". If can't be executed, it will proceed to "except"
        age_int = int(ageF)

        if(age_int <= 0):  # age input that is less than or equal to zero is invalid
            print("\nInvalid age.")
        else:
            # prompts the system to execute the display() function
            display(nameF, ageF, addressF)

    # this will be executed if the age can't be converted into an integer type (ex. if the input is in letters)
    except ValueError:
        print("\nError. Only whole numbers are accepted for age.")


# the inputs from get_user_input() function stored in 3 variables
name_g, age_g, address_g = get_user_inputs()

if(name_g == "" or age_g == "" or address_g == ""):  # empty inputs are also restricted
    print("\nEmpty input is invalid.")
else:
    # this prompts the system to execute the codes under age_validation function
    age_validation(name_g, age_g, address_g)
