#include <algorithm>
#include <cstdio>
#include <vector>

// at most 29 transitions of absolute cost 32768 fit well below this sentinel.
const int INF = 1000000;

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
    int levels = nextInt();
    // the cheapest cost of reaching each planet of the current level
    std::vector<int> cost(1, 0);
    for (int level = 0; level < levels; level++) {
        int k = nextInt();
        std::vector<int> nxt(k, INF);
        for (int planet = 0; planet < k; planet++) {
            for (int src = nextInt(); src != 0; src = nextInt()) {
                int price = nextInt();
                if (cost[src - 1] < INF) {
                    nxt[planet] = std::min(nxt[planet], cost[src - 1] + price);
                }
            }
        }
        cost = nxt;
    }
    std::printf("%d\n", *std::min_element(cost.begin(), cost.end()));
}
