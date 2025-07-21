def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def celsius_to_kelvin(c):
    return c + 273.15

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

def fahrenheit_to_kelvin(f):
    return (f - 32) * 5/9 + 273.15

def kelvin_to_celsius(k):
    return k - 273.15

def kelvin_to_fahrenheit(k):
    return (k - 273.15) * 9/5 + 32

def main():
    print("🌡️ Temperature Converter")
    while True:
        print("\nChoose conversion type:")
        print("1. Celsius to Fahrenheit")
        print("2. Celsius to Kelvin")
        print("3. Fahrenheit to Celsius")
        print("4. Fahrenheit to Kelvin")
        print("5. Kelvin to Celsius")
        print("6. Kelvin to Fahrenheit")
        print("7. Exit")

        choice = input("Enter your choice (1-7): ")

        if choice == '7':
            print("Exiting program. Goodbye!")
            break

        temp = float(input("Enter the temperature value: "))

        if choice == '1':
            print(f"{temp}°C = {celsius_to_fahrenheit(temp):.2f}°F")
        elif choice == '2':
            print(f"{temp}°C = {celsius_to_kelvin(temp):.2f}K")
        elif choice == '3':
            print(f"{temp}°F = {fahrenheit_to_celsius(temp):.2f}°C")
        elif choice == '4':
            print(f"{temp}°F = {fahrenheit_to_kelvin(temp):.2f}K")
        elif choice == '5':
            print(f"{temp}K = {kelvin_to_celsius(temp):.2f}°C")
        elif choice == '6':
            print(f"{temp}K = {kelvin_to_fahrenheit(temp):.2f}°F")
        else:
            print("❌ Invalid choice. Please select between 1 and 7.")

if __name__ == "__main__":
    main()
