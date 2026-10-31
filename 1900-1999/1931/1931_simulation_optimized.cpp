#include <cstdio>

const int INPUT_BUFFER = 4096;
// refilling this small buffer keeps memory independent of the input size.
int nextInt() {
    static char buffer[INPUT_BUFFER];
    static int position = 0, size = 0;
    auto read = [&]() -> int {
        if (position == size) {
            size = static_cast<int>(std::fread(buffer, 1, INPUT_BUFFER, stdin));
            position = 0;
            if (size == 0)
                return EOF;
        }
        return buffer[position++];
    };
    int c = read();
    while (c != EOF && c != '-' && (c < '0' || c > '9'))
        c = read();
    int sign = 1;
    if (c == '-') {
        sign = -1;
        c = read();
    }
    int value = 0;
    while (c >= '0' && c <= '9') {
        value = value * 10 + c - '0';
        c = read();
    }
    return value * sign;
}

int main() {
    int n = nextInt(), championValue = nextInt();
    int champion = 0, best = 0, currentCount = 0, bestCount = 0;
    // each score is used once; n <= 100000 and scores <= 1000000000 fit int.
    for (int index = 1; index < n; ++index) {
        int value = nextInt();
        ++currentCount;
        if (currentCount > bestCount) {
            bestCount = currentCount;
            best = champion;
        }
        if (value < championValue) {
            championValue = value;
            champion = index;
            currentCount = 1;
        }
    }
    std::printf("%d\n", best + 1);
}
