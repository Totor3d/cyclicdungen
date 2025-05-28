

array = [[0 for _ in range(10)] for _ in range(10)]
result = draw_line(array, (1, 1), (8, 2))
for row in result:
    print(' '.join(map(str, row)))