rounds = int(input())
prefectures = [input().split()[1] for _ in range(1 << rounds)]
prefectures.sort()
largest = run = 0
previous = ""
# Sorting makes each prefecture one run, avoiding a separate hash-table entry.
for prefecture in prefectures:
    run = run + 1 if prefecture == previous else 1
    if run > largest:
        largest = run
    previous = prefecture
print(rounds - (largest - 1).bit_length())
