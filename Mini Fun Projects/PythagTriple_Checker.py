## Display welcome message
print("Welcome to Kristen's Pythagorean Triangle Checker, sponsored by the Canadian House of Pizza and Garbage")

## Initialize variables
side = [0,0,0]
cont = True
#Function to take user input of three sides, sort by length, then check against equation for P triple
def checktrip():

        side[0] = int(input("Enter the length of one of the sides of the triangle: ")
               )
        side[1] = int(input ("Enter the length of the second side: ")
                 )
        side[2] = int(input("Enter the length of the last side: ")
                )

        list.sort(side)

        if ((side[0])^2) + ((side[1])^2) == ((side[2])^2):
         print("Yes, this triangle is a Pythagorean Triple")

        else: print("No, this triangle is not a Pythagorean Triple")

## Loop to enable as many iterations as user requires
while True:
    wishcont = str(input("Do you wish to check another triangle? Y/N: "))
    if wishcont == ("Y") or wishcont == ("y"):
        checktrip()
    else:
        print("Ok, thanks for using Kristen's Pythagorean Triple Checker, please remember to visit the Canadian House of Pizza and Garbage")
        break
