#include <cstdio>
#include <vector>

using namespace std;

const long long BASE = 1000000000000000000LL; // a long number in limbs of 18 digits

// sum = a + b on limbs from the lowest
vector<long long> add(const vector<long long> &a, const vector<long long> &b) {
    vector<long long> sum;
    long long carry = 0;
    for (size_t i = 0; i < a.size() || i < b.size() || carry; i++) {
        long long v = carry + (i < a.size() ? a[i] : 0) + (i < b.size() ? b[i] : 0);
        sum.push_back(v % BASE);
        carry = v / BASE;
    }
    return sum;
}

int main() {
    int n;
    scanf("%d", &n);
    // numbers of length k without two zeros in a row: Fibonacci F(k + 2), so
    // F(2N) bars go into F(N) safes, and F(2N) = F(N) L(N) with Lucas L(N)
    vector<long long> a = {2}, b = {1}; // L(0), L(1)
    for (int i = 0; i < n; i++) {
        vector<long long> c = add(a, b);
        a.swap(b);
        b.swap(c);
    }
    printf("%lld", a.back());
    for (int i = (int)a.size() - 2; i >= 0; i--)
        printf("%018lld", a[i]);
    printf("\n");
}
