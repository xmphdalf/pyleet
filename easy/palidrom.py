"""Palidrom Number

Given an integer x, return true if x is a palindrome, and false otherwise.



Example 1:

Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.
Example 2:

Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:

Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.


Constraints:

-231 <= x <= 231 - 1


Follow up: Could you solve it without converting the integer to a string?
"""


def is_palindrome_with_string(x: int) -> bool:
    # if the number is negative, it is not a palindrome
    if x < 0:
        return False

    # convert the number to a string
    x_str = str(x)
    # check if the string is a palindrome
    return x_str == x_str[::-1]


def is_palindrome_without_string(x: int) -> bool:
    # if the number is negative, it is not a palindrome
    if x < 0:
        return False

    # get the number of digits
    original_x = x
    reversed_x = 0
    # reverse the number
    while x > 0:
        # get the last digit
        reversed_x = reversed_x * 10 + x % 10
        # remove the last digit
        x //= 10
    # check if the original number is equal to the reversed number
    return original_x == reversed_x


print("is_palindrome_with_string(121):", is_palindrome_with_string(121))
print("is_palindrome_with_string(-121):", is_palindrome_with_string(-121))
print("is_palindrome_with_string(10):", is_palindrome_with_string(10))
print("is_palindrome_without_string(121):", is_palindrome_without_string(121))
print("is_palindrome_without_string(-121):", is_palindrome_without_string(-121))
print("is_palindrome_without_string(10):", is_palindrome_without_string(10))
print("is_palindrome_without_string(12321):", is_palindrome_without_string(12321))
print("is_palindrome_without_string(-12321):", is_palindrome_without_string(-12321))
print("is_palindrome_without_string(123210):", is_palindrome_without_string(123210))
print("is_palindrome_without_string(-123210):", is_palindrome_without_string(-123210))
print("is_palindrome_without_string(1232100):", is_palindrome_without_string(1232100))
print("is_palindrome_without_string(-1232100):", is_palindrome_without_string(-1232100))
print("is_palindrome_without_string(12321000):", is_palindrome_without_string(12321000))
print(
    "is_palindrome_without_string(-12321000):", is_palindrome_without_string(-12321000)
)
print(
    "is_palindrome_without_string(123210000):", is_palindrome_without_string(123210000)
)
print(
    "is_palindrome_without_string(-123210000):",
    is_palindrome_without_string(-123210000),
)
