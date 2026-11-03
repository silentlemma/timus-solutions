#include <cstdio>
#include <vector>

const int LIMIT = 100000, BASE = 10, SMALL = BASE - 1;
const int REMAINDER = SMALL * (SMALL + 1) / 2;

int digit_sum(int value) {
    int sum = 0;
    while (value) {
        sum += value % BASE;
        value /= BASE;
    }
    return sum;
}

int main() {
    int remaining;
    scanf("%d", &remaining);
    std::vector<int> chosen;
    int value = LIMIT - 1;
    // The first ten thousand candidates have digit sum 270000 in total.
    // Thus this phase stops before any of the one-digit numbers are used.
    while (remaining > REMAINDER) {
        chosen.push_back(value);
        remaining -= digit_sum(value--);
    }
    // Distinct digits 1..9 can make every sum from zero through 45.
    for (int digit = SMALL; digit > 0; digit--)
        if (digit <= remaining) {
            chosen.push_back(digit);
            remaining -= digit;
        }
    printf("%d\n", static_cast<int>(chosen.size()));
    for (int number : chosen)
        printf("%d ", number);
    puts("");
}
