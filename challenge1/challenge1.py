numbers = [10, 15, 3, 7]
k = 17
solution = False

for index, number in enumerate(numbers):
    result = k - number
    if (result in numbers) and (index > numbers.index(result)):
        solution = True

print(solution)
