# different ways to reverse a string

# using slicing

# def reversed_string(s):
#     return s[::-1]
#
# original_string ="hello"
# reversed_string = reversed_string(original_string)
# print(reversed_string)

# def reversed_string(s):
#     return "".join(reversed(s))
#
# original_string = "hello"
# reversed_string = reversed_string(original_string)
# print(reversed_string)

# def reverse_string(s):
#     reversed_str = ""
#     for char in s:
#         reversed_str = char + reversed_str
#         if reversed_str == reversed(s):
#             print("palindrome")
#         else:
#             print("Not a palindrome")
#
# # Example usage:
# original_string = "hello"
# reverse_string(original_string) # Output: "olleh"

def palindrome(s):
    i, j= 0, len(s)-1

    while i<j:
        if s[i] != s[j]:
            return "Not a palindrome"
        i+=1
        j-=1
        return "palindrome"
result = palindrome("radar")
print(result)

