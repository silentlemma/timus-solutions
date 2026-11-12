#include <algorithm>
#include <cstdio>

constexpr int INPUT_SIZE = 8192;
char input[INPUT_SIZE];
int position = 0, length = 0;

int byte() {
    if (position == length) {
        length = fread(input, 1, INPUT_SIZE, stdin);
        position = 0;
        if (length == 0)
            return -1;
    }
    return input[position++];
}

long long number() {
    int c = byte();
    while (c >= 0 && c <= ' ')
        c = byte();
    int sign = 1;
    if (c == '-') {
        sign = -1;
        c = byte();
    }
    long long value = 0;
    while (c >= '0' && c <= '9') {
        value = value * 10 + c - '0';
        c = byte();
    }
    return sign * value;
}

constexpr long long HUNDRED = 100, STAND = 15 * HUNDRED, BOARD = 5 * HUNDRED;

long long hundredths() {
    int c = byte();
    while (c >= 0 && c <= ' ')
        c = byte();
    long long value = 0;
    while (c >= '0' && c <= '9') {
        value = value * 10 + c - '0';
        c = byte();
    }
    value *= HUNDRED;
    if (c == '.') {
        for (long long scale = HUNDRED / 10; scale > 0; scale /= 10) {
            c = byte();
            if (c < '0' || c > '9')
                break;
            value += (c - '0') * scale;
        }
    }
    return value;
}

int main() {
    long long n = number(), k = number();
    long long u = hundredths(), v = hundredths();
    long long ready = (k - 1) * v + STAND;
    long long best_floor = 1, best_time = (n - 1) * u;
    // ceil(n - ready/u) and its predecessor straddle the kink exactly.
    long long upper = n - ready / u;
    for (long long candidate : {2LL, n, upper - 1, upper}) {
        long long floor = std::clamp(candidate, 2LL, n);
        long long time = std::max((n - floor) * u, ready) + 2 * (floor - 1) * v + BOARD;
        if (time < best_time || (time == best_time && floor > best_floor)) {
            best_time = time;
            best_floor = floor;
        }
    }
    std::printf("%lld\n", best_floor);
}
