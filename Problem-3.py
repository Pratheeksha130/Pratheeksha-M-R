# Problem-3: Print odd numbers up to a (or one less if a is even)
# Language: Python
# Author: Pratheeksha M R

a = int(input("Enter a number: "))

# If even, reduce a by 1 to avoid including it
if a % 2 == 0:
    a -= 1

for i in range(1, a + 1, 2):
    print(i, end=", ")
