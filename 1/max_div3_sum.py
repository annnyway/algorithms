from typing import List


def find_max_div3_sum(nums: List[int]) -> int:
    mod1 = [float('inf')] * 2
    mod2 = [float('inf')] * 2
    total = 0
    for num in nums:
        total += num
        if num % 3 == 1:
            if num < mod1[0]:
                t = mod1[0]
                mod1[0] = num
                mod1[1] = t
            elif num < mod1[1]:
                mod1[1] = num
        if num % 3 == 2:
            if num < mod2[0]:
                t = mod2[0]
                mod2[0] = num
                mod2[1] = t
            elif num < mod2[1]:
                mod2[1] = num

    if total % 3 == 0:
        return total

    elif total % 3 == 1 and mod1:
        if len(mod2) >= 2 and mod1[0] > mod2[0] + mod2[1]:
            return total - mod2[0] - mod2[1]
        return total - mod1[0]

    elif total % 3 == 2 and mod2:
        if len(mod1) >= 2 and mod2[0] > mod1[0] + mod1[1]:
            return total - mod1[0] - mod1[1]
        return total - mod2[0]

    return 0


# def find_max_div3_sum(numbers: List[int]) -> int:
#     # конечный автомат, но работает медленнее
#     # https://www.fatalerrors.org/a/1262-the-maximum-sum-divisible-by-three.html
#     state = [0, float('-inf'), float('-inf')]
#     for n in numbers:
#         temp = [0] * 3
#         for i in range(3):
#             temp[(i + n) % 3] = max(state[(i + n) % 3], state[i] + n)
#         state = temp
#     return state[0]


def solution():
    numbers = [int(x) for x in input().split()]
    max_div3_sum = find_max_div3_sum(numbers)
    print(max_div3_sum)


if __name__ == '__main__':
    solution()
