# Joshua Holliday
# July 1, 2026
# p4lab2.py
# Write a program that asks the user to enter an integer with a while loop and for loop together

"""
1. Get integer from user
2. Determine if integer is positive or negative
3. if number is positive, display multiplication table
4. if number is negative, tell user program cannot accept it
5. ask user to run again?
6. if yes, run program
7. if no, end program
"""

run_again = 'yes'

while run_again != "no":

    user_num = int(input("Enter an integer: "))
    print()

    if user_num >= 0:
        # display multiplication for that value and range (1-12)
        for item in range(1, 13):
            print(f"{user_num} * {item} = {user_num * item}")
            
    else: 
        print("This program does not handle negative number.")
        
    print()
    run_again = input("Would you like to run the program again? ")
    print()

# loop has broken. User entered 'no'
print("Program is ending....")