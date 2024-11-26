# EX 1

def calculate_area_triangle(base, height):
    area = (base * height) / 2
    return area

print('Exercise 1:', calculate_area_triangle(10, 5)) 

# EX 2

def simple_interest(principal, rate, time):
    interest = (principal * rate * time) / 100
    return interest

print('Exercise 2:', simple_interest(1000, 5, 2))

# EX 3

def apply_discount(price, discount):
    discount = (discount / 100) * price
    new_price = price - discount
    return new_price

print('Exercise 3:', apply_discount(100, 25))

# EX 4

def convert_temperature(temperature, unit):
    if unit == 'C':
        fahrenheit = (temperature * 9/5) + 32
        return fahrenheit
    elif unit == 'F':
        celsius = (temperature - 32) * 5/9
        return celsius

print('Exercise 4: Convert 0°C to Fahrenheit:', convert_temperature(0, 'C'))
print('Exercise 4: Convert 32°F to Celsius:', convert_temperature(32, 'F'))

# EX 5

def sum_to(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total

print('Exercise 5:', sum_to(6))

# EX 6

def largest(a, b, c):
    return max(a, b, c)

print('Exercise 6:', largest(1, 2, 3))

# EX 7

def calculate_tip(bill_amount, tip_percentage):
    tip_amount = (tip_percentage / 100) * bill_amount
    return tip_amount

print('Exercise 7:', calculate_tip(50, 20))

# EX 8

def product(a, b, c):
    return a * b * c

print('Exercise 8:', product(2, 5, 5))

# EX 9

def basicCalculator(num1, num2, operation):
    if operation == "add":
        return num1 + num2
    elif operation == "subtract":
        return num1 - num2
    elif operation == "multiply":
        return num1 * num2
    elif operation == "divide":
        return num1 / num2
    else:
        return "Invalid operation"

print('Exercise 9 Result:', basicCalculator(10, 5, "subtract"))