def calculate_stock_spans(prices: list) -> list:
    res = []
    stack = []

    res.append(1)
    stack.append(0)

    for i in range(1, len(prices)):
        while prices[i] >= prices[stack[-1]]:  # пока текущая цена больше цены на вершине стека
            stack.pop()                        # снимаем со стека верхний индекс
            if len(stack) == 0:
                break

        if len(stack) > 0:              # если стек не пустой
            res.append(i - stack[-1])   # добавляем индекс текущей цены - индекс цены на вершине стека
        else:
            res.append(i + 1)           # если стек пусстой - значит, цена росла до сих пор, прибавляем + 1

        # проходимся по индексам цен и добавляем их в стэк
        stack.append(i)

    return res


def solution():
    prices = list(map(int, input().split()))
    spans = calculate_stock_spans(prices)
    print(' '.join(map(str, spans)))


if __name__ == '__main__':
    solution()