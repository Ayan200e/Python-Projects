def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero!"
    return a / b

def km_to_miles(km):
    return km * 0.621371

def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def get_float_input(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def main():
    while True:
        print("\n--- Interactive Calculator & Unit Converter ---")
        print("1. Basic Arithmetic (+, -, *, /)")
        print("2. Unit Conversion (Km to Miles, Celsius to Fahrenheit)")
        print("3. Exit")
        
        choice = input("Choose an option (1-3): ").strip()
        
        if choice == '1':
            print("\nSelect Operation:")
            print("1. Add (+)")
            print("2. Subtract (-)")
            print("3. Multiply (*)")
            print("4. Divide (/)")
            
            op_choice = input("Enter choice (1-4): ").strip()
            if op_choice in ['1', '2', '3', '4']:
                num1 = get_float_input("Enter first number: ")
                num2 = get_float_input("Enter second number: ")
                
                if op_choice == '1':
                    print(f"Result: {num1} + {num2} = {add(num1, num2)}")
                elif op_choice == '2':
                    print(f"Result: {num1} - {num2} = {subtract(num1, num2)}")
                elif op_choice == '3':
                    print(f"Result: {num1} * {num2} = {multiply(num1, num2)}")
                elif op_choice == '4':
                    print(f"Result: {num1} / {num2} = {divide(num1, num2)}")
            else:
                print("Invalid operation choice.")
                
        elif choice == '2':
            print("\nSelect Conversion:")
            print("1. Kilometers to Miles")
            print("2. Celsius to Fahrenheit")
            
            conv_choice = input("Enter choice (1-2): ").strip()
            if conv_choice == '1':
                km = get_float_input("Enter distance in kilometers: ")
                print(f"Result: {km} km = {km_to_miles(km):.2f} miles")
            elif conv_choice == '2':
                c = get_float_input("Enter temperature in Celsius: ")
                print(f"Result: {c}°C = {celsius_to_fahrenheit(c):.2f}°F")
            else:
                print("Invalid conversion choice.")
                
        elif choice == '3':
            print("Exiting calculator. Goodbye!")
            break
        else:
            print("Invalid option. Please select 1, 2, or 3.")

if __name__ == "__main__":
    main()
