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


def solution():
    arr = list(map(int, input().split()))
    i = check_rotation(arr, 0, len(arr)-1)
    print(i)


if __name__ == '__main__':
    solution()