temp = float(input("enter the temperature in °C:"))
sun = input("is it sunny today ? (Yes/No):").lower()
is_sunny = sun == "yes"

if temp >= 28 and is_sunny:
    print("It was hot outside today")
    print("It is sunny")

elif temp < 0 and is_sunny:
    print("It was cold outside today")
    print("It is sunny")

elif 28 > temp > 0 and is_sunny:
    print("It was warm outside today")
    print("It is sunny")

elif temp >= 28 and not is_sunny:
    print("It was hot outside today")
    print("It is cloudy")

elif temp < 0 and not is_sunny:
    print("It was cold outside today")
    print("It is cloudy")

elif 28 > temp > 0 and not is_sunny:
    print("It was warm outside today")
    print("It is cloudy")
else :
    print("unable to determine the weather")
