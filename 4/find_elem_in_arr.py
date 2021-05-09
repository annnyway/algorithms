def find_elem(arr: list, left_idx: int, right_idx: int, elem: int) -> int:
    if right_idx > left_idx:
        left_elem = arr[left_idx]
        right_elem = arr[right_idx]
        if left_elem == elem:
            return left_idx
        if right_elem == elem:
            return right_idx

        # проверяем середину массива
        mid_idx = left_idx + (right_idx - left_idx) // 2
        mid_elem = arr[mid_idx]
        if mid_elem == elem:
            return mid_idx

        # проверяем левую часть
        if left_elem < mid_elem:
            if left_elem <= elem <= mid_elem:
                return find_elem(arr, left_idx, mid_idx, elem)
            else:
                return find_elem(arr, mid_idx, right_idx, elem)

        # проверяем правую часть
        if mid_elem < right_elem:
            if mid_elem <= elem <= right_elem:
                return find_elem(arr, mid_idx, right_idx, elem)
            else:
                return find_elem(arr, left_idx, mid_idx, elem)

    if left_idx == right_idx:
        return left_idx if arr[left_idx] == elem else -1

    return -1


def find_elem_in_arr(arr: list, elem: int) -> int:
    if len(arr) == 1:
        if arr[0] == elem:
            return 0
        return -1
    return find_elem(arr, 0, len(arr) - 1, elem)


def solution():
    arr = list(map(int, input().split()))
    elem = int(input().strip())
    index = find_elem_in_arr(arr, elem)
    print(index)


if __name__ == '__main__':
    solution()