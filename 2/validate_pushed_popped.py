def validate_pushed_popped(pushed_seq: list, popped_seq: list):
    stack = []
    i = 0
    seq_length = len(pushed_seq)
    for pushed in pushed_seq:
        stack.append(pushed)
        while len(stack) > 0 and i < seq_length and stack[-1] == popped_seq[i]:
            stack.pop()
            i += 1
    return i == seq_length


def solution():
    pushed = list(map(int, input().split()))
    popped = list(map(int, input().split()))
    result = validate_pushed_popped(pushed, popped)
    print(result)


if __name__ == '__main__':
    solution()
