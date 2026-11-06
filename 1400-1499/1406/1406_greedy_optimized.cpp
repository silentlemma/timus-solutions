#include <algorithm>
#include <cstdio>
#include <cstring>

constexpr int MAX_DIGITS = 2000;
constexpr int MAX_DIGIT = 9;

int main() {
    char digits[MAX_DIGITS + 1];
    if (std::scanf("%2000s", digits) != 1) {
        return 0;
    }
    const int size = static_cast<int>(std::strlen(digits));
    int tail_sum = 0;
    for (int pivot = size - 1; pivot >= 0; --pivot) {
        if (digits[pivot] != '9' && tail_sum > 0) {
            ++digits[pivot];
            --tail_sum;
            // Concentrate the remaining sum at the right end of the suffix.
            for (int i = size - 1; i > pivot; --i) {
                const int digit = std::min(MAX_DIGIT, tail_sum);
                digits[i] = static_cast<char>('0' + digit);
                tail_sum -= digit;
            }
            std::puts(digits);
            return 0;
        }
        tail_sum += digits[pivot] - '0';
    }
    std::puts("-1");
}
