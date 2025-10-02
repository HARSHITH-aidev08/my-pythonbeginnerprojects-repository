unit = input("Is your temperature in Celsius or Fahrenheit (C or F): ")
temp = float(input("Enter your temperature: "))

if unit.upper() == "C":
    temp = round((9 * temp / 5) + 32, 1)
    print(f"The temperature in Fahrenheit is {temp}°F")

elif unit.upper() == "F":
    temp = round((temp - 32) * 5 / 9, 1)
    print(f"The temperature in Celsius is {temp}°C")

else:
    print(f"{unit} is not a valid unit.")
