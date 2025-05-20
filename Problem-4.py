# Problem-4: Count numbers divisible by 1 to 9
# Author: Pratheeksha M R


input_str = input("Enter numbers separated by commas: ")

# Convert the input string to a list of integers
numbers = list(map(int, input_str.split(",")))

# Create a dictionary to count divisible numbers for 1 to 9
count = {}

for i in range(1, 10):
    count[i] = 0
    for num in numbers:
        if num % i == 0:
            count[i] += 1


print(count)
