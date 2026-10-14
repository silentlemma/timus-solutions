#include <algorithm>
#include <cstdio>
#include <string>
#include <vector>
using namespace std;

const int LETTERS = 26;
typedef vector<int> Big; // base 26, lowest digit first

void trim(Big &x) {
    while (!x.empty() && x.back() == 0)
        x.pop_back();
}

Big mulAdd(const Big &x, int factor, int add) {
    Big r;
    long long carry = add;
    for (int d : x) {
        carry += (long long)d * factor;
        r.push_back(carry % LETTERS);
        carry /= LETTERS;
    }
    for (; carry; carry /= LETTERS)
        r.push_back(carry % LETTERS);
    trim(r);
    return r;
}

// the k-th password from 1: by length, then alphabetically, which is k written
// in bijective base 26 with digits a to z
string word(Big k) {
    string out;
    while (!k.empty()) {
        // k - 1, then its lowest digit is the letter and the rest goes on
        size_t i = 0;
        while (k[i] == 0)
            k[i++] = LETTERS - 1;
        k[i]--;
        out += char('a' + k[0]);
        k.erase(k.begin());
        trim(k);
    }
    reverse(out.begin(), out.end());
    return out;
}

int main() {
    int n, m;
    if (scanf("%d %d", &n, &m) != 2)
        return 0;
    // 26 + 26^2 + ... + 26^n is 11...10 in base 26
    Big total(n + 1, 1);
    total[0] = 0;
    Big share(total.size());
    long long rest = 0;
    for (int i = total.size() - 1; i >= 0; i--) {
        rest = rest * LETTERS + total[i];
        share[i] = rest / m;
        rest %= m;
    }
    trim(share);
    int extra = rest;
    // the first extra processors take one password more
    for (int i = 0; i < m; i++) {
        Big start = mulAdd(share, i, min(i, extra) + 1);
        Big end = mulAdd(share, i + 1, min(i + 1, extra));
        printf("%s-%s\n", word(start).c_str(), word(end).c_str());
    }
}
