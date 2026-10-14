#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <vector>
using namespace std;

const int TWO = 2, THREE = 3;
const unsigned long long LIMB = 1000000000; // nine decimal digits per limb
const int TWOS_PER_STEP = 29;               // 2^29 < LIMB
const int THREES_PER_STEP = 18;             // 3^18 < LIMB

// multiplies the little-endian number by a factor below LIMB
void multiply(vector<unsigned long long> &number, unsigned long long factor) {
    unsigned long long carry = 0;
    for (unsigned long long &limb : number) {
        unsigned long long cur = limb * factor + carry;
        limb = cur % LIMB;
        carry = cur / LIMB;
    }
    if (carry > 0)
        number.push_back(carry);
}

void multiplyPower(vector<unsigned long long> &number, int base, int exponent, int perStep) {
    while (exponent > 0) {
        int step = exponent < perStep ? exponent : perStep;
        unsigned long long factor = 1;
        for (int i = 0; i < step; i++)
            factor *= base;
        multiply(number, factor);
        exponent -= step;
    }
}

int main() {
    int n;
    if (scanf("%d", &n) != 1)
        return 0;
    vector<int> marks(n);
    for (int &x : marks)
        if (scanf("%d", &x) != 1)
            return 0;
    // a nonzero product is +-2^a 3^b: prefix counts of twos and threes
    vector<int> twos(n + 1, 0), threes(n + 1, 0);
    bool zero = false;
    for (int i = 0; i < n; i++) {
        twos[i + 1] = twos[i] + (abs(marks[i]) == TWO);
        threes[i + 1] = threes[i] + (abs(marks[i]) == THREE);
        zero = zero || marks[i] == 0;
    }
    double logTwo = log((double)TWO), logThree = log((double)THREE);
    bool found = false; // the exponents of the best positive product
    int bestA = 0, bestB = 0;
    int i = 0;
    while (i < n) {
        if (marks[i] == 0) {
            i++;
            continue;
        }
        // a run without zeros: |x| >= 1, so longer runs never shrink the size
        int j = i;
        vector<int> negatives;
        while (j < n && marks[j] != 0) {
            if (marks[j] < 0)
                negatives.push_back(j);
            j++;
        }
        vector<pair<int, int>> spans;
        if (negatives.size() % 2 == 0) {
            spans.push_back({i, j});
        } else {
            // drop the part up to the first negative or from the last one
            spans.push_back({negatives.front() + 1, j});
            spans.push_back({i, negatives.back()});
        }
        for (auto [lo, hi] : spans) {
            if (lo >= hi)
                continue;
            int a = twos[hi] - twos[lo], b = threes[hi] - threes[lo];
            if (!found || a * logTwo + b * logThree > bestA * logTwo + bestB * logThree) {
                found = true;
                bestA = a;
                bestB = b;
            }
        }
        i = j;
    }
    if (!found) {
        // all marks are zeros or lone negatives
        printf("%d\n", zero ? 0 : marks[0]);
        return 0;
    }
    vector<unsigned long long> number(1, 1);
    multiplyPower(number, TWO, bestA, TWOS_PER_STEP);
    multiplyPower(number, THREE, bestB, THREES_PER_STEP);
    printf("%llu", number.back());
    for (int k = (int)number.size() - 2; k >= 0; k--)
        printf("%09llu", number[k]);
    printf("\n");
}
