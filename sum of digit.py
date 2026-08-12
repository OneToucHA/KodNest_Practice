number = int(input())
sum_of_digits = 0

# Extract and add each digit using a while loop
while number > 0:
    digit = number % 10
    sum_of_digits += digit
    number = number // 10

print(f"Sum of Digits: {sum_of_digits}")