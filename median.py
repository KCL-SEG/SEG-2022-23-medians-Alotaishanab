""""Median calculator."""
"""ENTER YOUR SOLUTION HERE!"""
numbers = []
median = 0
#Abdullah AlOtaishan

while True:
     try:
         print("Enter a list of numbers separated by commas: ")
         numbers = [float(value) for value in input().split(",")]
         numbers.sort()
         length = len(numbers)
         if length % 2 != 0:
             index = length / 2 - 0.5
             median = numbers[int(index)]
         if length % 2 == 0:
             index = length / 2
             foreal = index - 1
             first_number = numbers[int(index)]
             second_number = numbers[int(foreal)]
             total = first_number + second_number
             median = total / 2
     except ValueError:
         print("Some input could not be converted to a number!")
     else:
         break
print(numbers)
print(median)
