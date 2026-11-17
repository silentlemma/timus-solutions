HALF = 1000


def digit_sum(number):
    total = 0
    while number:
        total += number % 10
        number //= 10
    return total


def lucky(number):
    return digit_sum(number // HALF) == digit_sum(number % HALF)


number = int(input())
# The input guarantee makes both neighbours valid six-digit tickets.
print("Yes" if lucky(number - 1) or lucky(number + 1) else "No")
