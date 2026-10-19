HOSTS = 2  # Marshall and Lily
UNLUCKY = 13
PRICE = 100
PLUS = "+one"


def main():
    n = int(input())
    people = HOSTS
    for _ in range(n):
        people += 2 if input().strip().endswith(PLUS) else 1
    if people == UNLUCKY:
        people += 1  # a dummy takes the extra seat
    print(people * PRICE)


main()
