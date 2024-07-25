# В компьютерной игре вам нужно собирать ресурсы на игровом поле размером n×m. Поле представлено двумерным
# массивом, где каждый элемент указывает количество ресурсов в данной клетке. Игрок может выбирать прямоугольные
# области на поле для сбора ресурсов.
#
# Ваша задача – помочь игроку быстро вычислять количество ресурсов в выбранных прямоугольных областях.
#
# Формат входных данных
# В первой строке идут два числа n и m (1≤n,m≤1000) — количество строк и столбцов на игровом поле соответственно.
#
# Далее следуют n строк, каждая из которых содержит m целых чисел — количество ресурсов в каждой клетке.
#
# Далее идет число (1≤q≤100000) – количество запросов. В следующих q строках следуют запросы, каждый из которых
# состоит из четырех чисел:  y_1, x_1, y_2, x_2 (1 ≤ x_1 ≤ x_2 ≤ n, 1 ≤ y_1 ≤ y_2 ≤ m), где (x_1, y_1) – координаты
# левого верхнего, а (x_2, y_2) – правого нижнего угла прямоугольной области.
#
# Формат выходных данных
# Для каждого запроса выведите одно число – суммарное количество ресурсов в указанной прямоугольной области.
#
# Пример данных
# Ввод
# 3 2
# 1 2
# 3 4
# 5 6
# 2
# 1 2 1 2
# 1 1 2 2
#
# Вывод
# 2
# 10
# def main():
#     import sys
#     input = sys.stdin.read
#     data = input().split()
#
#     idx = 0
#
#     # Read n and m
#     n = int(data[idx])
#     m = int(data[idx + 1])
#     idx += 2
#
#     # Read matrix
#     matrix = []
#     for i in range(n):
#         row = list(map(int, data[idx:idx + m]))
#         matrix.append(row)
#         idx += m
#
#     # Read number of queries
#     q = int(data[idx])
#     idx += 1
#
#     queries = []
#     for _ in range(q):
#         y1 = int(data[idx]) - 1
#         x1 = int(data[idx + 1]) - 1
#         y2 = int(data[idx + 2]) - 1
#         x2 = int(data[idx + 3]) - 1
#         queries.append((x1, y1, x2, y2))
#         idx += 4
#
#     # Compute prefix sums
#     prefix_sum = [[0] * (m + 1) for _ in range(n + 1)]
#
#     for i in range(1, n + 1):
#         for j in range(1, m + 1):
#             prefix_sum[i][j] = matrix[i - 1][j - 1] + prefix_sum[i - 1][j] + prefix_sum[i][j - 1] - prefix_sum[i - 1][
#                 j - 1]
#
#     # Answer queries
#     results = []
#     for x1, y1, x2, y2 in queries:
#         total = prefix_sum[x2 + 1][y2 + 1]
#         if x1 > 0:
#             total -= prefix_sum[x1][y2 + 1]
#         if y1 > 0:
#             total -= prefix_sum[x2 + 1][y1]
#         if x1 > 0 and y1 > 0:
#             total += prefix_sum[x1][y1]
#         results.append(total)
#
#     # Output results
#     for result in results:
#         print(result)
#
#
# if __name__ == "__main__":
#     main()

def compute_prefix_sum(matrix):
    n = len(matrix)
    m = len(matrix[0])

    # Создаем матрицу префиксных сумм
    prefix_sum = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            prefix_sum[i][j] = matrix[i - 1][j - 1] \
                               + prefix_sum[i - 1][j] \
                               + prefix_sum[i][j - 1] \
                               - prefix_sum[i - 1][j - 1]
    return prefix_sum


def query_sum(prefix_sum, x1, y1, x2, y2):
    return (prefix_sum[x2][y2]
            - prefix_sum[x1 - 1][y2]
            - prefix_sum[x2][y1 - 1]
            + prefix_sum[x1 - 1][y1 - 1])


def main():
    import sys
    input = sys.stdin.read
    data = input().split()

    index = 0

    n = int(data[index])
    m = int(data[index + 1])
    index += 2

    matrix = []
    for _ in range(n):
        row = list(map(int, data[index:index + m]))
        matrix.append(row)
        index += m

    # Compute prefix sums
    prefix_sum = compute_prefix_sum(matrix)

    q = int(data[index])
    index += 1

    results = []
    for _ in range(q):
        y1 = int(data[index])
        x1 = int(data[index + 1])
        y2 = int(data[index + 2])
        x2 = int(data[index + 3])
        index += 4

        result = query_sum(prefix_sum, x1, y1, x2, y2)
        results.append(result)

    print("\n".join(map(str, results)))


if __name__ == "__main__":
    main()
