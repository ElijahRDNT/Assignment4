#Assignment: create a function that returns multiple values (move all user inputs in one function)
def get_user_inputs():
    name_l = input("Please enter you name: ")
    age_l = input("Please enter your age in years: ")
    address_l = input("Please enter your address: ")
    return name_l, age_l, address_l

def display(name, age, address):
    print("\nHi, my name is " + name + ". I am " + age +  # this is the final output
            " years old and I live in " + address + ".")

name_g, age_g, address_g = get_user_inputs()
display(name_g, age_g, address_g)