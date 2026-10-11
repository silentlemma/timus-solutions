#include <cstdio>
#include <cstring>
#include <vector>

const int TOP = 1000000; // 10000.00 in cents
const int CENTS = 100;
const int WORD = 32;

// a price with at most two decimals, in cents
int cents(const char *s) {
    int whole = 0, frac = 0, digits = 0;
    bool after = false;
    for (; *s; s++) {
        if (*s == '.') {
            after = true;
        } else if (after) {
            if (digits < 2)
                frac = frac * 10 + (*s - '0');
            digits++;
        } else {
            whole = whole * 10 + (*s - '0');
        }
    }
    for (; digits < 2; digits++)
        frac *= 10;
    return whole * CENTS + frac;
}

int main() {
    // bids counted by price, indexed from the highest price down, so that
    // "at least X" is a Fenwick prefix sum
    std::vector<int> tree(TOP + 1, 0);
    long long sold = 0;
    char kind[WORD], price[WORD];
    while (scanf("%31s", kind) == 1 && strcmp(kind, "QUIT") != 0) {
        if (scanf("%31s", price) != 1)
            break;
        int r = TOP + 1 - cents(price);
        if (kind[0] == 'S') {
            long long k = 0;
            if (scanf("%lld", &k) != 1)
                break;
            long long count = 0;
            for (; r > 0; r &= r - 1)
                count += tree[r];
            sold += count < k ? count : k;
        } else {
            int step = kind[0] == 'B' ? 1 : -1;
            for (; r <= TOP; r += r & -r)
                tree[r] += step;
        }
    }
    // the exchange earns one cent per piece sold
    printf("%lld.%02lld\n", sold / CENTS, sold % CENTS);
    return 0;
}
