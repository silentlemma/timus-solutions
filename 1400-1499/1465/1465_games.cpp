#include <cstdio>
#include <set>
#include <vector>

using namespace std;

const int LIMIT = 200; // the values repeat with PERIOD from 52 on, well below this
const int PERIOD = 34;
const int TAKE = 3; // a move takes up to three files out of play

int main() {
    long long n;
    scanf("%lld", &n);
    // Dawson's chess: a row of n files plays like the octal game 0.137, where
    // a move takes one file (only if it is all), two (leaving one row) or three
    // (leaving up to two rows); White, moving first, wins when the value is not 0
    vector<int> g(LIMIT + 1, 0);
    for (int size = 1; size <= LIMIT; size++) {
        set<int> seen;
        if (size == 1)
            seen.insert(0);
        if (size >= 2)
            seen.insert(g[size - 2]);
        for (int left = 0; left <= size - TAKE; left++)
            seen.insert(g[left] ^ g[size - TAKE - left]);
        while (seen.count(g[size]))
            g[size]++;
    }
    if (n > LIMIT)
        n = LIMIT - PERIOD + (n - LIMIT) % PERIOD;
    puts(g[n] ? "White" : "Black");
}
