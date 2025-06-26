# Find the missing and repeated number

arr = eval(input("Enter the array: "))
print("Array:", arr)

n = len(arr)
expected_sum = n * (n + 1) // 2
expected_square_sum = n * (n + 1) * (2 * n + 1) // 6

actual_sum = sum(arr)
actual_square_sum = sum(x * x for x in arr)

diff = actual_sum - expected_sum
square_diff = actual_square_sum - expected_square_sum

sum_xy = square_diff // diff

x = (diff + sum_xy) // 2
y = x - diff

print(f"Repeating : {x}")
print(f"Missing   : {y}")
