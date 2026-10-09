#include <algorithm>
#include <cstdio>
#include <vector>

std::vector<int> digits(int v, int base) {
    std::vector<int> out;
    for (; v > 0; v /= base)
        out.push_back(v % base);
    std::reverse(out.begin(), out.end());
    return out;
}

bool fits(int x, int y, int base) {
    std::vector<int> dx = digits(x, base), dy = digits(y, base);
    size_t j = 0;
    for (size_t i = 0; i < dx.size() && j < dy.size(); i++)
        if (dx[i] == dy[j])
            j++;
    return j == dy.size();
}

int answer(int x, int y) {
    int base = 2;
    for (; (long long)base * base <= x; base++)
        if (fits(x, y, base))
            return base;
    // from here on x has two digits x / b and x % b, and y must be one of them
    int best = 0;
    int low = std::max(base, x / (y + 1) + 1);
    if (low <= x / y)
        best = low;
    // x % b == y means that b divides x - y and is larger than y
    int least = std::max(base, y + 1), n = x - y;
    for (int d = 1; d * d <= n; d++)
        if (n % d == 0)
            for (int b : {d, n / d})
                if (b >= least && (best == 0 || b < best))
                    best = b;
    return best;
}

int main() {
    int x, y;
    if (scanf("%d %d", &x, &y) != 2)
        return 0;
    int best = answer(x, y);
    if (best == 0)
        puts("No solution");
    else
        printf("%d\n", best);
}
