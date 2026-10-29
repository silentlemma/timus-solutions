#include <cmath>
#include <cstdio>

constexpr int MAX_INPUT = 256 * 1024;
constexpr unsigned long long SCALE = 10000;
constexpr double ROUNDING_OFFSET = 0.5;
char input[MAX_INPUT];

int main() {
    int end = 0;
    while (end < MAX_INPUT) {
        int count = static_cast<int>(fread(input + end, 1, MAX_INPUT - end, stdin));
        if (count == 0)
            break;
        end += count;
    }
    // the numbers are parsed from the end of the input backwards, so they come
    // out in the required order without an array of them
    while (end > 0) {
        while (end > 0 && input[end - 1] <= ' ')
            --end;
        int start = end;
        while (start > 0 && input[start - 1] > ' ')
            --start;
        if (start == end)
            break;
        unsigned long long value = 0;
        for (int i = start; i < end; ++i)
            value = value * 10 + input[i] - '0';
        // four decimals by hand: the root times 10^4, rounded, printed as the
        // integer part and the fraction, which is faster than printf("%.4f")
        double root = std::sqrt(static_cast<double>(value));
        auto scaled = static_cast<unsigned long long>(root * SCALE + ROUNDING_OFFSET);
        printf("%llu.%04llu\n", scaled / SCALE, scaled % SCALE);
        end = start;
    }
    return 0;
}
