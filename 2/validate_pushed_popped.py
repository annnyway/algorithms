def validate_pushed_popped(pushed: list, popped: list):
    stack = []
    j = 0
    seq_length = len(popped)
    for i in range(seq_length):
        stack.append(pushed[i])
        while len(stack) > 0 and j < seq_length and stack[-1] == popped[j]:
            stack.pop()
            j += 1
    return j == seq_length


def solution():
    pushed = list(map(int, input().split()))
    popped = list(map(int, input().split()))
    result = validate_pushed_popped(pushed, popped)
    print(result)


if __name__ == '__main__':
    solution()
