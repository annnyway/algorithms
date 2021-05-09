import heapq

def get_kth_element(arr: list, k: int):
    heapq._heapify_max(arr)
    arr.sort(reverse=False)
    return arr[k]


def solution():
    arr = list(map(int, input().split()))
    k = int(input())
    print(get_kth_element(arr, k))


if __name__ == '__main__':
    solution()
