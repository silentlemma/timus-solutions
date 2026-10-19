#include <cmath>
#include <cstdio>

const int BASE = 10;

// the chance that two random digits from first .. 9 plus the incoming
// carry reach 10
double carryChance(int first, int extra) {
    int hits = 0, total = 0;
    for (int a = first; a < BASE; a++) {
        for (int b = first; b < BASE; b++) {
            hits += a + b + extra >= BASE;
            total++;
        }
    }
    return double(hits) / total;
}

// the chance that one place with digits from first .. 9 shows a and b
double pairChance(int first, int a, int b) {
    int side = BASE - first;
    return (a == b ? 1.0 : 2.0) / (side * side);
}

int main() {
    int k;
    if (scanf("%d", &k) != 1) return 0;
    // every place costs one written digit and one sum; a carry costs a mark
    // and, unless it leaves the last place, one more second to add it in,
    // a carry out of the last place is written as a digit
    double expected = 2.0 * k, carry = 0;
    for (int place = 0; place < k; place++) {
        int first = place == k - 1 ? 1 : 0;
        carry = (1 - carry) * carryChance(first, 0) + carry * carryChance(first, 1);
        expected += 2 * carry;
    }
    // the first sum of two digits both above 1 takes a second more
    for (int a = 2; a < BASE; a++) {
        for (int b = a; b < BASE; b++) {
            double miss = std::pow(1 - pairChance(0, a, b), k - 1) * (1 - pairChance(1, a, b));
            expected += 1 - miss;
        }
    }
    printf("%.8f\n", expected);
    return 0;
}
