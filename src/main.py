
from utils import square, is_even, celsius_to_fahrenheit, greet


def main():
    name = input("Enter your name: ")
    print(greet(name))

    number = int(input("Enter a number: "))

    print("Square:", square(number))

    if is_even(number):
        print("The number is even.")
    else:
        print("The number is odd.")

    fahrenheit = celsius_to_fahrenheit(number)
    print("Temperature in Fahrenheit:", fahrenheit)


if __name__ == "__main__":
    main()
