def merge_sorted_arrs(old: list, new: list) -> list:
    sorted_arr = old + new
    old_idx, new_idx = 0, 0
    i = 0
    old_len = len(old)
    new_len = len(new)
    while i < len(sorted_arr):
        if old_idx >= old_len:
            sorted_arr[i:] = new[new_idx:]
            break

        if new_idx >= new_len:
            sorted_arr[i:] = old[old_idx:]
            break

        if old[old_idx] > new[new_idx]:
            sorted_arr[i] = new[new_idx]
            new_idx += 1
            i += 1
            continue
        else:
            sorted_arr[i] = old[old_idx]
            old_idx += 1
            i += 1

    return sorted_arr


def merge_k_sorted(arrs: list) -> list:
    if len(arrs) == 0:
        return []
    left, right = 0, len(arrs) - 1
    while right > 0:
        if left >= right:
            left = 0
        else:
            arrs[left] = merge_sorted_arrs(arrs[left], arrs[right])
            left += 1
            right -= 1
    return arrs[0]


def solution():
    # arrs = read_multiline_input() # эта функция уже написана
    arrs = [
        [3, 5, 7, 7],
        [3, 4, 6, 9, 10],
        [1, 1, 2, 3, 11],
        [5],
        [0, 0, 100],
        [],
    ]
    merged = merge_k_sorted(arrs)
    print(' '.join([str(el) for el in merged]))


if __name__ == '__main__':
    solution()