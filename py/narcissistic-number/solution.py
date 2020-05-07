import functools

def narcissistic(value):
    total = 0

    for number in str(value):
        total += int(number) ** len(str(value))
    
    return total == value

print(narcissistic(371))
print(narcissistic(4887))
