def evaluate(lst = [int(i) for i in input()]):
    x = 0
    y = 1
    for i in range(len(lst)):
        if lst[i] % 2 != 0:
            x = x + lst[i]
        elif lst[i] % 2 == 0:
            y = y * lst[i]
    return x - y
print(evaluate())
