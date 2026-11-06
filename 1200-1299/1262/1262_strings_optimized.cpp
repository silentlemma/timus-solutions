#include <cctype>
#include <cstdio>

constexpr int LENGTHS[] = {0, 1, 2, 3, 2, 1, 2, 3, 4, 2};

int main() {
    int digit;
    do {
        digit = std::getchar();
    } while (std::isspace(digit));
    int total = 0;
    while (digit >= '0' && digit <= '9') {
        total += LENGTHS[digit - '0'];
        digit = std::getchar();
    }
    std::printf("%d\n", total);
}
