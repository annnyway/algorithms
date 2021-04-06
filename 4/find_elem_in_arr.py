def check_rotation(arr: list, left_id: int, right_id: int) -> int:
    if left_id < right_id:
        # берем индекс середины массива
        i = left_id + (right_id - left_id) // 2

        # если среднее значение меньше значений слева и справа, то возвращаем индекс
        if arr[i] < arr[i-1] and arr[i] < arr[i+1]:
            return i

        # если левое значение больше среднего, то проверяем в левом подмассиве
        if arr[left_id] > arr[i]:
            return check_rotation(arr, left_id, i-1)

        # если следующий за серединой элемент больше правого, то проверяем в правом подмассиве
        elif arr[i+1] > arr[right_id]:
            return check_rotation(arr, i+1, right_id)

        else:
            # проверяем пограничную ситуацию: например [..., 6, 1, ...]
            if arr[i] > arr[i+1]:
                return i+1
            # иначе тут сдвига нет
            else:
                return 0

    else:
        return len(arr)-1


def binary_search(arr: list, left_id: int, right_id: int, elem: int) -> int:
    if right_id >= left_id:
        mid = left_id + (right_id - left_id) // 2
        if arr[mid] == elem:
            return mid
        elif arr[mid] > elem:
            return binary_search(arr, left_id, mid - 1, elem)
        else:
            return binary_search(arr, mid + 1, right_id, elem)
    else:
        return -1


def find_elem_in_arr(arr: list, elem: int) -> int:
    i = -1

    if len(arr) == 1:
        if arr[0] == elem:
            return 0
        else:
            return i

    if arr[0] < elem < arr[-1]:
        i = binary_search(arr, 0, len(arr), elem)
    else:
        shift = check_rotation(arr, 0, len(arr) - 1)
        left_arr = arr[:shift]
        right_arr = arr[shift:]
        if elem >= left_arr[0]:
            return binary_search(left_arr, 0, len(left_arr)-1, elem)
        elif elem >= right_arr[0]:
            i = binary_search(right_arr, 0, len(right_arr)-1, elem)
            if i != -1:
                return len(left_arr) + i

    return i

def solution():
    arr = list(map(int, input().split()))
    elem = int(input().strip())
    index = find_elem_in_arr(arr, elem)
    print(index)


if __name__ == '__main__':
    solution()