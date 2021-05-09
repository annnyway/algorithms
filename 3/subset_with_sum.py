from itertools import combinations


def has_subset_with_sum_k(array: list, k: int) -> bool:
    for i in range(1, len(array)+1):
        for subset in combinations(array, i):
            if sum(subset) == k:
                return True
    return False


def solution():
    array = list(map(int, input().split()))
    k = int(input().strip())
    c = has_subset_with_sum_k(array, k)
    print(c)


if __name__ == '__main__':
    solution()