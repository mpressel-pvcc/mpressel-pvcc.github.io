#Name: Mike Pressel
#Purpose: This program finds the tuition & fees for PVCC students

import datetime

##########define variables#############
#Define tax rate and prices
TUITION_IN = 155
TUITION_OUT = 331.6
INST_FEE = 1.75
STU_ACT_FEE = 2.90
CAP_FEE = 23.5

# define global variables
residency = 1
num_credits = 0
tuition_amt = 0.0
inst_amount = 0.0
stu_act_amount = 0.0
cap_fee_amount = 0.0
total = 0.0
scholar_amt = 0.0
balance_owed = 0.0





######## define program functions ###########

def main() :
    more_data = True
    while more_data:
        get_user_data()
        perform_calculations()
        display_results()
        yesno = input("Do you want to process more data? (Y/N) : ")
        if yesno == "n" or yesno == "N":
            more_data = False
            print("Thank you for using our app.")

def get_user_data():
    global residency, num_credits, scholar_amt
    residency = int(input("Residency status:/n Enter a 1 for in-state or enter a 2 for out-of-state:  "))
    num_credits = int(input("Number of credits: "))
    scholar_amt = float(input("Amount of scholarship amount awarded: $"))

def perform_calculations():
    global tuition_amt, num_credits, inst_amount, stu_act_amount, cap_fee_amount, total, balance_owed, scholar_amt
    ####don't forget out or state###
    if residency == 2:
        tuition_amt = TUITION_OUT * num_credits
        cap_fee_amount = CAP_FEE * num_credits
    else :
         tuition_amt = TUITION_OUT * num_credits
         cap_fee_amount = 0
        
    inst_amount = num_credits * INST_FEE
    stu_act_amount = num_credits * STU_ACT_FEE
    total = tuition_amt + inst_amount + stu_act_amount + cap_fee_amount
    balance_owed = total - scholar_amt

def line() :
    return '-----------------------------------------'

def display_results() :
    print (line())
    print ('***Piedmont Virginia Community College***')
    print ('        Tuition and Fees Report')
    print (str(datetime.datetime.now()))
    print (line())
    print ('Number of credits taken: ' + str(num_credits))
    print (line())
    print ('Tuition            $ ' + format(tuition_amt,'8,.2f'))
    print ('Capital Fee        $ ' + format(cap_fee_amount,'8,.2f'))
    print ('Institution Fee    $ ' + format(inst_amount,'8,.2f'))
    print ('Activity Fee       $ ' + format(stu_act_amount,'8,.2f'))
    print(line())
    print ('Total              $ ' + format(total,'8,.2f'))
    print ('Scholarship        $ ' + format(scholar_amt,'8,.2f'))
    print(line())
    print ('Balance Owed       $ ' + format(balance_owed,'8,.2f'))
    print(line())
    
 ## Call on Main! ##   
main ()