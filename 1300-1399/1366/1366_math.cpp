#include <cstdio>
#include <vector>

const unsigned BASE = 1000000000; // nine decimal digits per limb

int main() {
    int n = 0;
    if (scanf("%d", &n) != 1)
        return 0;
    // derangements: d(1) = 0 and d(k) = k d(k - 1) + (-1)^k, kept as limbs
    // from the lowest; d(k) >= 1 for k >= 2, so subtracting 1 never underflows
    std::vector<unsigned> count(1, 0);
    for (int k = 2; k <= n; k++) {
        unsigned long long carry = 0;
        for (unsigned &limb : count) {
            unsigned long long cur = (unsigned long long)limb * k + carry;
            limb = (unsigned)(cur % BASE);
            carry = cur / BASE;
        }
        while (carry) {
            count.push_back((unsigned)(carry % BASE));
            carry /= BASE;
        }
        if (k % 2 == 0) {
            size_t i = 0;
            while (++count[i] == BASE) {
                count[i++] = 0;
                if (i == count.size())
                    count.push_back(0);
            }
        } else {
            size_t i = 0;
            while (count[i] == 0)
                count[i++] = BASE - 1;
            count[i]--;
            if (count.size() > 1 && count.back() == 0)
                count.pop_back();
        }
    }
    printf("%u", count.back());
    for (size_t i = count.size() - 1; i-- > 0;)
        printf("%09u", count[i]);
    printf("\n");
    return 0;
}
