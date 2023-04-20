#Michael Pressel
#Prog Purpose: This program creates a receipt for a pizza order.

# formatting time to YYYY-MM-DD HH:MM:SS
import datetime
current_time = str(datetime.datetime.now()).split('.')[0]

############ define global variables ###########
#define tax rate and prices (constants)
SMALL = 9.99
MEDIUM = 12.99
LARGE = 14.99
XLARGE = 17.99

SALES_TAX = .055

#define global variables
size = "n"
num_pizzas = 0
cost = 0
tax = 0
total = 0
price = 0

############ define program functions ##########
def main() :
    more_data = True #Loop to ask to process more data
    while more_data:#Loop to ask to process more data
        get_user_data()
        perform_calculations()
        print_receipt()
        yesno = input("\nWould you like to process more data?  (Y/N): ")#Loop to ask to proccess more data
        if yesno == "n" or yesno == "N":
            more_data = False
            print("Thank you for using our app!")

def get_user_data() :
    global size, num_pizzas
    size = (input("What size pizza did you order? (S)mall, (M)edium, (L)arge, (X)tra-Large "))[0]
    num_pizzas = int(input("Number of pizzas ordered: "))

def perform_calculations() :
    global price, cost, total, tax
    match size:
        case "s":
            price = SMALL
        case "S":
            price = SMALL
        case "m":
            price = MEDIUM
        case "M":
            price = MEDIUM
        case "l":
            price = LARGE
        case "L":
            price = LARGE
        case "x":
            price = XLARGE
        case "X":
            price = XLARGE 

            
    cost = num_pizzas * price
    tax = cost * SALES_TAX
    total = cost + tax


def print_receipt() :
    print ('\n----------------------------------------')###added \n to provide a space between last user input and displayed results
    print ('******* Palermo Pizza *******')
    print ('Your neighborhood pizza shop')
    print ('    ' + current_time)
    print ('----------------------------------------')
    print ('Pizzas ordered:  ' + str(num_pizzas) + " " + str(size))
    print ('----------------------------------------')
    print ('Pizza Cost       $' + format(cost, '10,.2f'))
    print ('Sales Tax        $' + format(tax, '10,.2f'))
    print ('----------------------------------------')
    print ('total            $ ' + format(total, '10,.2f'))
    
    

######## call on main program to execute ######
main()
