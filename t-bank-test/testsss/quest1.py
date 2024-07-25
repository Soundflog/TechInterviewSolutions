def can_distribute_tasks(max_day_time, tasks, k):
    current_sum = 0
    days_needed = 1  # Начинаем с первого дня

    for time in tasks:
        if current_sum + time > max_day_time:
            days_needed += 1
            current_sum = time
            if days_needed > k:
                return False
        else:
            current_sum += time

    return days_needed <= k


def find_min_max_day_time(n, k, tasks):
    low, high = max(tasks), sum(tasks)

    while low < high:
        mid = (low + high) // 2
        if can_distribute_tasks(mid, tasks, k):
            high = mid
        else:
            low = mid + 1

    return low


# Чтение входных данных
import sys

input = sys.stdin.read
data = input().strip().split()

n = int(data[0])
k = int(data[1])
tasks = list(map(int, data[2:]))

# Определение минимального максимального времени в день
result = find_min_max_day_time(n, k, tasks)

# Вывод результата
print(result)
