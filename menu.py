from fixnum_module import fixNum
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
        f.write(f"{num.a} {num.b}")

def get_sum():
    """Retrieves the last sum from the file"""
    try:
        with open("sum.txt", "r") as f:
            content = f.read().split()
            if len(content) == 2:
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
        print("1. Add numbers")
        print("2. Get power")
        print("3. Quit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
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
                
        elif choice == '2':
            num = get_number()
            while True:
                try:
                    n = int(input("Enter the power: "))
                    break
                except ValueError:
                    print("Invalid input. Enter an integer number.")
                    
            result = num.power(n)
            print(f"\n[Result] -> The result is {result}")
            
        elif choice == '3':
            print("Exiting application...")
            break

        else:
            print("Invalid choice, please select 1, 2, or 3.")
            continue

if __name__ == "__main__":
    menu()