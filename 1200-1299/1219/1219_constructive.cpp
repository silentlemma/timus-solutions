#include <cstdio>
#include <string>
#include <vector>

const int LETTERS = 26, ORDER = 3, LENGTH = 1000000;

std::vector<int> a(LETTERS *ORDER), cycle;

// A de Bruijn sequence: every word of ORDER letters once around the cycle.
static void gen(int t, int p) {
    if (t > ORDER) {
        if (ORDER % p == 0) {
            cycle.insert(cycle.end(), a.begin() + 1, a.begin() + p + 1);
        }
        return;
    }
    a[t] = a[t - p];
    gen(t + 1, p);
    for (int j = a[t - p] + 1; j < LETTERS; j++) {
        a[t] = j;
        gen(t + 1, t);
    }
}

int main() {
    gen(1, 1);
    // repeating the cycle keeps every window of three letters a cyclic window
    // of it, so each triple, pair and letter appears almost equally often
    std::string out(LENGTH, ' ');
    for (int i = 0; i < LENGTH; i++) {
        out[i] = (char)('a' + cycle[i % cycle.size()]);
    }
    puts(out.c_str());
}
