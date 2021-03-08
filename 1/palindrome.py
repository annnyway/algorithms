def is_palindrome(number: int) -> bool:
    if number < 10:
        return True
    input_number = number
    reverse = 0
    while number > 0:
        last_digit = number % 10
        reverse = (reverse * 10) + last_digit
        number = number // 10
    if reverse == input_number:
        return True
    else:
        return False


def solution():
    a = int(input('Вход: '))
    c = is_palindrome(a)
    print('Выход:', c)


if __name__ == '__main__':
    solution()
