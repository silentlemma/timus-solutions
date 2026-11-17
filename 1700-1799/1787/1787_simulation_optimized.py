numbers = map(int, open(0, "rb").read().split())
capacity, minutes = next(numbers), next(numbers)
waiting = 0
for _ in range(minutes):
    waiting += next(numbers) - capacity
    if waiting < 0:
        waiting = 0
print(waiting)
