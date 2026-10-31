#include <algorithm>
#include <cstdio>

// coordinates fit int; pair sums below 10^16 require long long.
constexpr int MAX_POINTS = 100000;
// refilling handles arbitrary input length without retaining the whole input.
constexpr int BUFFER_SIZE = 4096;

int readInt() {
    static char buffer[BUFFER_SIZE];
    static int position = 0, length = 0;
    auto next = [&]() {
        if (position == length) {
            length = static_cast<int>(fread(buffer, 1, BUFFER_SIZE, stdin));
            position = 0;
            if (length == 0)
                return EOF;
        }
        return static_cast<int>(buffer[position++]);
    };
    int c = next();
    while (c != EOF && c <= ' ')
        c = next();
    int value = 0;
    while (c >= '0' && c <= '9') {
        value = value * 10 + c - '0';
        c = next();
    }
    return value;
}

// the sum of |a_i - a_j| over all pairs: in sorted order the i-th value
// is larger than the i values before it
long long pairSum(int *values, int size) {
    std::sort(values, values + size);
    long long total = 0, before = 0;
    for (int i = 0; i < size; i++) {
        total += static_cast<long long>(values[i]) * i - before;
        before += values[i];
    }
    return total;
}

int main() {
    int n = readInt();
    static int x[MAX_POINTS], y[MAX_POINTS];
    for (int i = 0; i < n; i++) {
        x[i] = readInt();
        y[i] = readInt();
    }
    // walking along the streets, a visit covers |dx| + |dy|
    long long pairs = static_cast<long long>(n) * (n - 1) / 2;
    printf("%lld\n", (pairSum(x, n) + pairSum(y, n)) / pairs);
}
