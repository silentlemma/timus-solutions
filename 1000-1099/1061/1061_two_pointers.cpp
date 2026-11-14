#include <cstdio>
#include <vector>

constexpr int MAX_DIGIT = 9;

int main() {
    int count, width;
    if (std::scanf("%d%d", &count, &width) != 2)
        return 0;
    if (width > count) {
        std::puts("0");
        return 0;
    }

    std::vector<unsigned char> digits(width);
    int slot = 0, unlocked = 0, sum = 0;
    int first = 0, minimum = MAX_DIGIT * width + 1;
    for (int position = 1; position <= count;) {
        const int state = std::getchar();
        if (state == EOF)
            return 0;
        if (state == '*') {
            unlocked = sum = slot = 0;
        } else if (state >= '0' && state <= '9') {
            const int digit = state - '0';
            // The slot holds the oldest digit once the window is full.
            if (unlocked == width)
                sum -= digits[slot];
            else
                ++unlocked;
            digits[slot] = digit;
            sum += digit;
            if (++slot == width)
                slot = 0;
            if (unlocked == width && sum < minimum) {
                first = position - width + 1;
                minimum = sum;
                if (minimum == 0)
                    break;
            }
        } else {
            continue;
        }
        ++position;
    }
    std::printf("%d\n", first);
}
