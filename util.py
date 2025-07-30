# Function that takes either a celsius or fahrenheit value
# value and converts to other units

def convert_temperature(temp, unit):
    if unit == "C":
        return (temp - 32) * 5.0 / 9.0
    elif unit == "F":
        return (temp * 9.0 / 5.0) + 32
    else:
        raise ValueError("Invalid target unit. Please use 'C' or 'F'.")
    