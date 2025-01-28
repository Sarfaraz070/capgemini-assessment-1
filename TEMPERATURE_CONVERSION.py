
def fahrenheit_conversion(scale, value):
    if 'celsius' in scale.lower():
        fahrenheit = ((9 / 5) * value) + 32
        return f"{fahrenheit:.2f} Fahrenheit"
    elif 'kelvin' in scale.lower():
        fahrenheit = ((value - 273.15) * (9 / 5)) + 32
        return f"{fahrenheit:.2f} Fahrenheit"

def celsius_conversion(scale, value):
    if 'fahrenheit' in scale.lower():
        celsius = (value - 32) * (5 / 9)
        return f"{celsius:.2f} Celsius"
    elif 'kelvin' in scale.lower():
        celsius = value - 273.15
        return f"{celsius:.2f} Celsius"

def kelvin_conversion(scale, value):
    if 'celsius' in scale.lower():
        kelvin = value + 273.15
        return f"{kelvin:.2f} Kelvin"
    elif 'fahrenheit' in scale.lower():
        kelvin = (value - 32) * (5 / 9) + 273.15
        return f"{kelvin:.2f} Kelvin"

# Main program
conversion_type = input("Enter the type of conversion you need (e.g., 'Celsius to Fahrenheit'): ").lower()
temperature_value = float(input("Enter the temperature value: "))

if 'fahrenheit' in conversion_type and 'celsius' in conversion_type:
    print(celsius_conversion(conversion_type, temperature_value))
elif 'fahrenheit' in conversion_type and 'kelvin' in conversion_type:
    print(kelvin_conversion(conversion_type, temperature_value))
elif 'celsius' in conversion_type and 'fahrenheit' in conversion_type:
    print(fahrenheit_conversion(conversion_type, temperature_value))
elif 'celsius' in conversion_type and 'kelvin' in conversion_type:
    print(kelvin_conversion(conversion_type, temperature_value))
elif 'kelvin' in conversion_type and 'celsius' in conversion_type:
    print(celsius_conversion(conversion_type, temperature_value))
elif 'kelvin' in conversion_type and 'fahrenheit' in conversion_type:
    print(fahrenheit_conversion(conversion_type, temperature_value))
else:
    print("Invalid conversion type. Please try again.")