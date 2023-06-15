"""
implement a program that prompts the user for a fraction, formatted as X/Y, wherein 
each of X and Y is an integer, and then outputs, as a percentage rounded to the nearest 
integer, how much fuel is in the tank. If, though, 1% or less remains, output E instead 
to indicate that the tank is essentially empty. And if 99% or more remains, output F instead 
to indicate that the tank is essentially full.
"""
def calculate_percentage(fraction):
    x, y = fraction.split('/')
    x = int(x)
    y = int(y)

    if x > y or y == 0:
        return None

    percentage = (x / y) * 100
    return percentage

def main():
    while True:
        try:
            fraction = input("Enter the fuel level as a fraction (X/Y): ")

            percentage = calculate_percentage(fraction)
            if percentage is None:
                print("Invalid input. Please try again.")
                continue

            if percentage <= 1:
                print("E")
            elif percentage >= 99:
                print("F")
            else:
                rounded_percentage = round(percentage)
                print("Fuel level:", rounded_percentage, "%")

            break

        except (ValueError, ZeroDivisionError):
            print("Invalid input. Please try again.")

# Call the main function
if __name__ == "__main__":
    main()