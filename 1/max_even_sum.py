from typing import List
import sys


def find_max_even_sum(numbers: List[int]) -> int:
    res = 0
    min_odd_number = sys.maxsize
    for number in numbers:
        res += number
        if number % 2 == 1 and number < min_odd_number:
            min_odd_number = number
    if res % 2 == 0:
        return res
    return res - min_odd_number


def solution():
    numbers = [int(x) for x in input().split()]
    max_even_sum = find_max_even_sum(numbers)
    print(max_even_sum)


if __name__ == '__main__':
    solution()
