# Write a pgm to check weather the given string/integer is palindrome or not
# IP: 12321
# OP: True

# IP: 12322
# OP: False

a = input("Enter a input string: ")

def isPalindrome(a):
    a = str(a)
    left, right = 0, len(a)-1

    while left<right:
        if a[left] != a[right]:
            return False
        left += 1
        right -= 1
    return True

print(isPalindrome(a))
