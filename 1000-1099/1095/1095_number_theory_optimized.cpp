#include <algorithm>
#include <array>
#include <cstdio>

constexpr int DIVISOR = 7;
constexpr int KEY_SIZE = 4;
constexpr int MAX_DIGITS = 20;
constexpr int KEY_SHIFT = 10000;

int main() {
    std::array<std::array<char, KEY_SIZE>, DIVISOR> suffix{};
    std::array<char, KEY_SIZE> order{'1', '2', '3', '4'};
    do {
        int remainder = 0;
        for (char digit : order)
            remainder = (remainder * 10 + digit - '0') % DIVISOR;
        suffix[remainder] = order;
    } while (std::next_permutation(order.begin(), order.end()));

    int count;
    if (std::scanf("%d", &count) != 1)
        return 0;
    while (count-- > 0) {
        char number[MAX_DIGITS + 1];
        if (std::scanf("%20s", number) != 1)
            return 0;
        char answer[MAX_DIGITS + 1];
        int length = 0, zeros = 0, remainder = 0;
        std::array<bool, KEY_SIZE> removed{};
        for (const char *digit = number; *digit; ++digit) {
            if (*digit == '0') {
                ++zeros;
            } else if (*digit >= '1' && *digit <= '4' && !removed[*digit - '1']) {
                removed[*digit - '1'] = true;
            } else {
                answer[length++] = *digit;
                remainder = (remainder * 10 + *digit - '0') % DIVISOR;
            }
        }
        const int needed = (DIVISOR - remainder * KEY_SHIFT % DIVISOR) % DIVISOR;
        for (char digit : suffix[needed])
            answer[length++] = digit;
        while (zeros-- > 0)
            answer[length++] = '0';
        answer[length] = '\0';
        std::puts(answer);
    }
}
