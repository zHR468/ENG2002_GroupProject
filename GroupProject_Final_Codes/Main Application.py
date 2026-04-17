from FixnumModule import fixNum
from FractionModule import Fraction
from FractionModule import fixed_pow
from FractionModule import fraconvert 
import math

def get_number():
    """Asks the user to enter a number in form of a and b"""
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
    docstring needed here
    creates a file and writes the sum in it to enable user add new numbers to this sum
    """
    f = open("sum.txt","w")
    #writes the a and b parts of the calculated sum into the file
    f.write(f"{num.a} {num.b}")
    f.close()

def get_sum():
    """
    docstring needed here
    """
    try:
        f = open("sum.txt","r")
        #assigns val
        a,b = f.read().split()
        f.close()
    
        return fixNum(int(a),b)
    except FileNotFoundError:
        return fixNum(0,'0')

def menu():
    """Main application loop"""
    while True:
        print("\n--- Fixed Point Calculator ---")
        print("[a] Addition of numbers")
        print("[b] Executing Integer-based Power Function")
        print("[c] Executing Fractional Power Function")
        print("[x] Quit")
        
        choice = input("Enter your choice: ")
        
        if choice == 'a':
            print("\nEnter the first number:")
            n1 = get_number()
            
            while True:
                print("\nEnter the second number:")
                n2 = get_number()

                result = n1.add(n2)
                print(f"\n[Result] -> {result} (a = {result.a}, b = {result.b})")
                
                save_sum(result)
                
                cont = input("Continue adding to this sum? (y/n): ")
                if cont.lower() != 'y':
                    break
                n1 = get_sum()
                
        elif choice == 'b':
            num = get_number()
            while True:
                try:
                    n = int(input("Enter the power: "))
                    break
                except ValueError:
                    print("Invalid input. Enter an integer number.")
                    
            result = num.power(n)
            print(f"\n[Result] -> The result is {result}")

        elif choice=='c':
            print("\n --- Fractional Power Mode ---")
            print("Enter base: ")
            base_num = get_number()

            print("Enter the exponent (fractional): ")
            exp_num= get_number()
            
            result = fixed_pow(base_num.a, str(base_num.b), exp_num.a, str(exp_num.b))
            if isinstance(result, tuple):
                print(f"Result is -> {result[0]}  {result[1]}")
                print(f"Estimation is -> {int(result[0].num/result[0].den)**(1/int(fraconvert(exp_num.a, str(exp_num.b)).den))}")
            else:
                print(f"Result is -> {result}")
                
            
                    
            
        elif choice == 'x':
            print("Exiting application...")
            break

        else:
            print("Invalid choice, please select a, b, or c or x.")
            

menu()
