n = int(open(0, "rb", buffering=0).read())
# Consecutive factors make this division exact before the final product.
answer = n * (n + 1) // 2 * (n + 2)
open(1, "wb", buffering=0).write((str(answer) + "\n").encode())
