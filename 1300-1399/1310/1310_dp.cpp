#include <cstdio>
#include <cstring>
#include <string>
#include <vector>

typedef unsigned long long u64;

const u64 BASE = 1000000000; // a limb holds nine decimal digits
const int LIMB_DIGITS = 9;
const int TEN = 10;
const int WORD = 512;
const int FIELDS = 4; // L, M, K and the code

// a non-negative number as limbs of nine decimal digits, lowest first
struct Big {
    std::vector<u64> d;
};

Big parse(const std::string &s) {
    Big x;
    for (int end = (int)s.size(); end > 0; end -= LIMB_DIGITS) {
        int start = end > LIMB_DIGITS ? end - LIMB_DIGITS : 0;
        u64 limb = 0;
        for (int i = start; i < end; i++)
            limb = limb * TEN + (s[i] - '0');
        x.d.push_back(limb);
    }
    while (!x.d.empty() && x.d.back() == 0)
        x.d.pop_back();
    return x;
}

void add(Big &a, const Big &b) {
    if (a.d.size() < b.d.size())
        a.d.resize(b.d.size(), 0);
    u64 carry = 0;
    for (size_t i = 0; i < a.d.size(); i++) {
        u64 sum = a.d[i] + (i < b.d.size() ? b.d[i] : 0) + carry;
        a.d[i] = sum % BASE;
        carry = sum / BASE;
    }
    if (carry)
        a.d.push_back(carry);
}

bool less(const Big &a, const Big &b) {
    if (a.d.size() != b.d.size())
        return a.d.size() < b.d.size();
    for (size_t i = a.d.size(); i-- > 0;) {
        if (a.d[i] != b.d[i])
            return a.d[i] < b.d[i];
    }
    return false;
}

// a -= b, where a >= b
void subtract(Big &a, const Big &b) {
    u64 borrow = 0;
    for (size_t i = 0; i < a.d.size(); i++) {
        u64 take = (i < b.d.size() ? b.d[i] : 0) + borrow;
        borrow = a.d[i] < take;
        a.d[i] = a.d[i] + (borrow ? BASE : 0) - take;
    }
    while (!a.d.empty() && a.d.back() == 0)
        a.d.pop_back();
}

int main() {
    int length = 0, top = 0, k = 0;
    char word[WORD];
    if (scanf("%d %d %d %511s", &length, &top, &k, word) != FIELDS)
        return 0;
    Big n = parse(word);
    // ways[i][r]: how many ways i registers can hold values 1..M with a sum
    // that leaves remainder r modulo K
    std::vector<std::vector<Big>> ways(length + 1, std::vector<Big>(k));
    ways[0][0].d.push_back(1);
    for (int i = 1; i <= length; i++) {
        for (int v = 1; v <= top; v++) {
            for (int r = 0; r < k; r++)
                add(ways[i][(r + v) % k], ways[i - 1][r]);
        }
    }
    int total = 0;
    for (int pos = 0; pos < length; pos++) {
        int left = length - pos - 1;
        // try the values in increasing order and skip whole blocks of states
        for (int v = 1; v <= top; v++) {
            const Big &block = ways[left][((-(total + v)) % k + k) % k];
            if (less(n, block)) {
                printf(pos ? " %d" : "%d", v);
                total += v;
                break;
            }
            subtract(n, block);
        }
    }
    printf("\n");
    return 0;
}
