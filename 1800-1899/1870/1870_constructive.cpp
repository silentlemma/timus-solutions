#include <cstdio>
#include <string>

using namespace std;

// 2 * 3: both must be invertible modulo n
const int BAD = 6;

int gcd(int a, int b) { return b ? gcd(b, a % b) : a; }

int main() {
    int n;
    if (scanf("%d", &n) != 1) return 0;
    if (gcd(n, BAD) != 1) {
        puts("No");
        return 0;
    }
    // queen i on row 2i: rows 2i, diagonals 3i and anti-diagonals i are all
    // different modulo n
    string out = "Yes\n";
    for (int i = 0; i < n; i++) {
        out += to_string(2LL * i % n + 1);
        out += i + 1 < n ? ' ' : '\n';
    }
    fputs(out.c_str(), stdout);
    return 0;
}
