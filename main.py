def is_palindrome(s):
    s = s.replace(" ", "").lower()
    return s == s[::-1]
input_str = input("Введіть рядок: ")
if is_palindrome(input_str):
    print("Введений рядок є паліндромом.")
else:
    print("Введений рядок не є паліндромом.")
