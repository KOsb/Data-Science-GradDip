#print introduction
print("Welcome to Kristen's coin roll calculator, sponsered by the Canadian House of Pizza and Garbage."
      "You will be asked to enter the weight of all the coins you have, and provided with a estimate of the number of coin rolls you will need for each denomination")

def roll_calculator():
    #get the weight of total coins in each class
    pweight = int(input("Enter the total weight of pennies: "))
    nweight = int(input("Enter the total weight of nickels: "))
    dweight = int(input("Enter the total weight of dimes: "))
    qweight = int(input("Enter the total weight of quarters: "))
    #use the weight of individual coins to calculate the number of each coin (*_num)
    p_num = round(pweight/2.5)
    #use the weight of total coins to calculate the number of rolls needed (*rolls)
    prolls  = round(pweight/126)
    n_num = round(nweight/5)
    nrolls = round(nweight/199)
    d_num = round(dweight/2.268)
    drolls = round(dweight/113)
    q_num = round(qweight/5.67)
    qrolls = round(qweight/226)
    #use the total number of coins to calculate the value of all the money
    totalvalue = (p_num + (n_num*5) + (d_num *10) + (q_num*25))/100
    #print the totals
    print("You have approximately %s pennies and will need approximately %s roll(s) for pennies" %(p_num,prolls))
    print("You have approximately %s nickels and will need approximately %s roll(s) for nickels" % (n_num, nrolls))
    print("You have approximately %s dimes and will need approximately %s roll(s) for dimes" % (d_num, drolls))
    print("You have approximately %s quarters and will need approximately %s roll(s) for quarters" % (q_num, qrolls))
    print("The approximate total value of all your coins is $%s" %totalvalue)
roll_calculator()
while True:
    cont = input('Do you want to calculate another set of coins? (Y/N): ')
    if cont == 'Y' or cont == 'y':
        roll_calculator()
    else:
        print("Thank you for using Kristen's coin roll calculator, please remember to visit the Canadian House of Pizza and Garbage")
        break

