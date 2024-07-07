AVERAGE VALUE OF ITEMS

def calculate_average(weight1, num_purchases1, weight2, num_purchases2):
    total_value = (weight1 * num_purchases1) + (weight2 * num_purchases2)
    total_purchases = num_purchases1 + num_purchases2
    average_value = total_value / total_purchases
    return average_value

weight1 = int(input())
num_purchases1 = int(input())
weight2 = int(input())
num_purchases2 = int(input())
average_value = calculate_average(weight1, num_purchases1, weight2, num_purchases2)
print(int(average_value)


CELSIUS TOFAHRENHEIT

def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit
celsius = float(input())
fahrenheit = celsius_to_fahrenheit(celsius)
print(fahrenheit,"F")
