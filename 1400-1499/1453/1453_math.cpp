#include <algorithm>
#include <cstdio>
#include <vector>

using namespace std;

const long long BASE = 1000000000; // a long number in decimal limbs of nine digits

// number = number * factor + add, on limbs from the lowest
void mulAdd(vector<long long> &number, int factor, long long add) {
    long long carry = add;
    for (auto &limb : number) {
        long long v = limb * factor + carry;
        limb = v % BASE;
        carry = v / BASE;
    }
    while (carry) {
        number.push_back(carry % BASE);
        carry /= BASE;
    }
}

int main() {
    int n, s;
    scanf("%d %d", &n, &s);
    vector<int> c(n);
    for (int &x : c)
        scanf("%d", &x);
    long long rook = (long long)n * (s - 1);
    if (n == 1) { // in one dimension a bishop moves exactly like a rook
        printf("%lld\n", rook);
        return 0;
    }
    // t bishop steps need room t on the chosen side of every coordinate
    vector<int> both(s, 0); // both[m]: coordinates with room m on each side
    int reach = s;          // beyond this some coordinate has no room
    for (int x : c) {
        both[min(s - x, x - 1)]++;
        reach = min(reach, max(s - x, x - 1));
    }
    vector<long long> count(n + 1, 0); // count[k]: lengths t with 2^k directions
    int k = n - both[0];
    for (int t = 1; t <= reach; t++) {
        count[k]++;
        k -= both[t];
    }
    vector<long long> ways = {0}; // the sum of count[k] 2^k, doubling from the top
    for (int j = n; j >= 0; j--)
        mulAdd(ways, 2, count[j]);
    mulAdd(ways, 1, rook);
    printf("%lld", ways.back());
    for (int i = (int)ways.size() - 2; i >= 0; i--)
        printf("%09lld", ways[i]);
    printf("\n");
}
