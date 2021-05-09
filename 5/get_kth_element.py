def max_heapify(arr: list, i: int, size: int):
    left = i*2 + 1
    right = left + 1
    largest = i
    if left < size and arr[i] < arr[left]:
        largest = left

    if right < size and arr[largest] < arr[right]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        max_heapify(arr, largest, size)


def heapify(arr: list, size: int):
    for i in range(size // 2, -1, -1):
        max_heapify(arr, i, size)


def heapsort(arr: list):
    size = len(arr)
    heapify(arr, size)
    while size > 0:
        max_heapify(arr, 0, size)
        arr[0], arr[size-1] = arr[size-1], arr[0]
        size -= 1


def get_kth_element(arr: list, k: int):
    heapsort(arr)
    return arr[k]


def solution():
    arr = list(map(int, input().split()))
    k = int(input())
    print(get_kth_element(arr, k))


if __name__ == '__main__':
    solution()
