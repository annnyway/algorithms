from collections import deque


def calculate_stock_spans(prices: list) -> list:
    seq = deque()
    res = []
    for i, curr_price in enumerate(prices):
        seq.appendleft(curr_price)
        count = 0
        for elem in seq:
            if elem > curr_price:
                break
            count += 1

        if count == 0:
            count = 1

        res.append(count)

    return res


def solution():
    prices = list(map(int, input().split()))
    spans = calculate_stock_spans(prices)
    print(' '.join(map(str, spans)))


if __name__ == '__main__':
    solution()