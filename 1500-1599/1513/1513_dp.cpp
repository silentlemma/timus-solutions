#include <cstdint>
#include <cstdio>
#include <vector>

using namespace std;

typedef vector<int64_t> Big; // base 10^9 limbs, the lowest first
const int64_t LIMB = 1000000000;
const int DIGITS = 9;

// 2 x - y for y <= 2 x
Big twiceMinus(const Big &x, const Big &y) {
    Big out(x.size() + 1, 0);
    int64_t carry = 0;
    for (size_t i = 0; i < out.size(); i++) {
        int64_t v = carry + (i < x.size() ? 2 * x[i] : 0) - (i < y.size() ? y[i] : 0);
        carry = v < 0 ? -1 : v / LIMB;
        out[i] = v < 0 ? v + LIMB : v % LIMB;
    }
    while (out.size() > 1 && out.back() == 0)
        out.pop_back();
    return out;
}

int main() {
    int n, k;
    scanf("%d %d", &n, &k);
    // count[i + 1]: lines of i words with no more than k lemons in a row,
    // with count[0] = 1 standing for length -1
    vector<Big> count = {{1}, {1}};
    for (int i = 1; i <= n; i++) {
        // a valid line of i words is a valid line of i - 1 words plus a word,
        // except those ending in exactly k + 1 lemons after a banana
        Big drop = i > k ? count[i - k - 1] : Big{0};
        count.push_back(twiceMinus(count[i], drop));
    }
    const Big &answer = count[n + 1];
    printf("%lld", (long long)answer.back());
    for (int i = (int)answer.size() - 2; i >= 0; i--)
        printf("%0*lld", DIGITS, (long long)answer[i]);
    printf("\n");
}
