#include <algorithm>
#include <cstdio>
#include <string>
#include <vector>

using namespace std;

constexpr int BUFFER = 1 << 16;
constexpr int DIGITS = 16;
char buffer[BUFFER];
int length = 0, position = 0;

int read_char() {
    if (position == length) {
        length = int(fread(buffer, 1, BUFFER, stdin));
        position = 0;
        if (length <= 0) return -1;
    }
    return buffer[position++];
}

long long read_int() {
    int c = read_char();
    while (c < '0') c = read_char();
    long long v = 0;
    for (; c >= '0'; c = read_char()) v = v * 10 + (c - '0');
    return v;
}

int main() {
    int n = int(read_int());
    vector<long long> t(n);
    for (auto& v : t) v = read_int();
    int q = int(read_int());
    vector<int> x(q);
    int most = 0;
    for (auto& v : x) most = max(most, v = int(read_int()));
    // tent of height t at every odd multiple of t; the envelope of all
    // tents is the answer, and centres beyond 2 * most never matter
    int limit = 2 * most;
    vector<int> height(limit + 1, 0);
    sort(t.begin(), t.end());
    t.erase(unique(t.begin(), t.end()), t.end());
    for (long long v : t) {
        if (v >= most) {
            // still climbing at every query: a tent at most of height most
            height[most] = max(height[most], most);
            continue;
        }
        int w = int(v);
        for (int c = w; c <= limit; c += 2 * w) height[c] = max(height[c], w);
    }
    // best[x] = max over c of height[c] - |x - c|, by two sweeps
    vector<int> best(height);
    for (int i = 1; i <= limit; ++i) best[i] = max(best[i], best[i - 1] - 1);
    for (int i = limit - 1; i >= 0; --i) best[i] = max(best[i], best[i + 1] - 1);
    string out;
    out.reserve(size_t(q) * DIGITS);
    char digits[DIGITS];
    for (int v : x) {
        int len = snprintf(digits, sizeof digits, "%d\n", best[v]);
        out.append(digits, size_t(len));
    }
    fwrite(out.data(), 1, out.size(), stdout);
}
