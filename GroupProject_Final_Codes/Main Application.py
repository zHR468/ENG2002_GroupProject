"""
BIRUNGI MARY GORETTI ABWOOLI - 25100607D
"""
from FixnumModule import fixNum
from FractionModule import Fraction
from FractionModule import fixed_pow
from FractionModule import fraconvert 
import math

def get_number():
    """Asks the user to enter a number in form of a and b
    uses try except to ensure that the user enters valid input without crashing the program
    a while loop is used until the correct input is entered"""
    while True:#loop runs until valid input is entered. 
        try:
            a = int(input("Enter the integer part (a): "))#a is an integer
            b = input("Enter the fractional part (b): ")# fractional part is maintained as a string
            int(b) # validate that b can be converted into an integer

            if a > 0:#if a is positive, b must be negative
                b = b.lstrip('-')
                
            return fixNum(a, b)#returns a fixNum object and exits the loop and function
        except Exception as e:
            print(f"Invalid input, an error occured: {e}. Enter numbers only.")#prompts user again when invalid input is entered

def save_sum(num):
    """
    Saves the results into a text file 'sum.txt'
    Allows user to continue adding numbers to previous result by saving previous result
    the file is overwritten every time with the latest result
    """
    f = open("sum.txt","w")#opens file in write mode and overwrites previous content
    #writes the a and b parts of the calculated sum into the file separated by a space
    f.write(f"{num.a} {num.b}")
    f.close()#closes the file to save changes

def get_sum():
    """
    reads previously saved result from sum.txt
    Allows cummulative addition by retrieving the last stored result
    Returns a fixNum object from the file data
    if the file does not exist, return a default value of 0.0 instead of crashing
    """
    try:
        f = open("sum.txt","r")#opens the file in read mode
        #assigns stored values to a and b after splitting along the space that separates them
        a,b = f.read().split()
        f.close()
    
        return fixNum(int(a),b)
    except FileNotFoundError:#if the file does not exist, return a default value of 0.0 instead of crashing
        return fixNum(0,'0')

def menu():
    """Main application loop"""
    while True:#Continuous loop
        print("\n--- Fixed Point Calculator ---")
        print("[a] Addition of numbers")
        print("[b] Executing Integer-based Power Function")
        print("[c] Executing Fractional Power Function")
        print("[x] Quit")
        #Menu is printed as above
        choice = input("Enter your choice: ").lower()#The choice of the user is asked
        
        if choice == 'a': #Addition function for two fixed numbers
            print("\nEnter the first number:")
            n1 = get_number()# By using get_number function it retrieves the first number
            
            while True:
                print("\nEnter the second number:")
                n2 = get_number()# By using get_number once again, receives the second nummber from the user

                result = n1.add(n2)#Adds the number 
                print(f"\n[Result] -> {result} (a = {result.a}, b = {result.b})")
                
                save_sum(result)# Saves the result into the results.txt file for further need
                
                cont = input("Continue adding to this sum? (y/n): ")#Asks user if they would like to add the current addition into the sum for further use
                if cont.lower() != 'y':#If no, then the algorithm breaks 
                    break
                n1 = get_sum()#Gives the sum as a result
                
        elif choice == 'b':#Power function where the power are consist of integers
            num = get_number()# Get base number by using get_number function
            while True:
                try:
                    n = int(input("Enter the power: "))#Gets the integer power
                    break
                except ValueError:#In case of a wrong input exist in power entry, the algorithm raises error. 
                    print("Invalid input. Enter an integer number.")
                    
            result = num.power(n)# Calculate power by using power method defined in the fixNum class
            print(f"\n[Result] -> The result is {result}")

        elif choice=='c':#Fractional Power mode
            print("\n --- Fractional Power Mode ---")
            print("Enter base: ")
            base_num = get_number()#Get the base by using get_number function from Fixnum Class

            print("Enter the exponent (fractional): ")
            exp_num= get_number()#Gets the fractional exponent
            
            result = fixed_pow(base_num.a, str(base_num.b), exp_num.a, str(exp_num.b)) #Calculates fractional power by using power() function from Fraction Class which makes base.b and exp.b as strings for result
            if isinstance(result, tuple):#The result is retrieved as tuple
                print(f"Result is -> {result[0]}  {result[1]}")#The exact value division is the output
                print(f"Estimation is -> {int(result[0].num/result[0].den)**(1/int(result[1].lstrip('to the power of 1/')))}")#Provides an estimation where exact value division is a long number and output is a float-point numnber.
                print(result[0].num/result[0].den)
                print(1/int(result[1].lstrip('to the power of 1/')))
            else:#If result is a single value
                print(f"Result is -> {result}")#
                
            
                    
            
        elif choice == 'x':#Quit 
            print("Exiting application...")
            break #Breaks the loop and quits

        else:# In case of wrong input entry the algorithm raises error and redirects to the menu for correct choice
            print("Invalid choice, please select a, b, or c or x.")
            
#Menu starts from here.
menu()
