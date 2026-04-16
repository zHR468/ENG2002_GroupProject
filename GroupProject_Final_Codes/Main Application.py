from FixnumModule import fixNum

def get_number():
    """Asks the user to enter a number in form of a and b"""
    while True:
        try:
            a = int(input("Enter the integer part (a): "))
            b = input("Enter the fractional part (b): ")
            int(b) # validate that b is a number

            if a > 0:
                b = b.lstrip('-')
                
            return fixNum(a, b)
        except Exception as e:
            print(f"Invalid input, an error occured: {e}. Enter numbers only.")

def save_sum(num):
    """Saves the current sum to a file (Fixed: using 'with' for safe file handling)"""
    with open("sum.txt", "w") as f:
        f.write(f"{num.a} {num.b} {num.b_original_len}")

def get_sum():
    """Retrieves the last sum from the file"""
    try:
        with open("sum.txt", "r") as f:
            content = f.read().split()
            if len(content) == 3:
                a, b, DecLen = content
                PreOutput = fixNum(int(a), b)
                PreOutput.b_original_len = int(DecLen)
                return PreOutput
            elif len(content) == 2:
                a, b = content
                return fixNum(int(a), b)
            else:
                return fixNum(0, '0')
    except FileNotFoundError:
        return fixNum(0, '0')

def menu():
    """Main application loop"""
    while True:
        print("\n--- Fixed Point Calculator ---")
        print("[a] Addition of numbers")
        print("[b] Executing Power function")
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
                    if n < 0:
                        print("Invalid input. Enter an integer number >= 0.")
                        continue
                    break
                except ValueError:
                    print("Invalid input. Enter an integer number.")
                    
            result = num.power(n)
            print(f"\n[Result] -> The result is {result}")
            
        elif choice == 'x':
            print("Exiting application...")
            break

        else:
            print("Invalid choice, please select 1, 2, or 3.")
            continue

menu()
