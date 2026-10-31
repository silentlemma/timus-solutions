#include <cstdio>

const int MOD = 1000000009, LOW = 100, HIGH = 1000, PAIRS = 100, WINDOW = 3;
int source[HIGH - LOW], target[HIGH - LOW];
// ways[t]: numbers of the length so far that end in the two digits t and
// whose every three neighbouring digits form a three-digit prime
int ways[PAIRS], next_ways[PAIRS];

int main() {
    int n;
    scanf("%d", &n);
    int count = 0;
    for (int p = LOW; p < HIGH; p++) {
        bool prime = true;
        for (int d = 2; d * d <= p; d++)
            if (p % d == 0) {
                prime = false;
                break;
            }
        if (prime) {
            source[count] = p / 10;
            target[count++] = p % PAIRS;
            ways[p % PAIRS]++;
        }
    }
    // reuse two arrays; two residues sum to less than 2 * mod, within signed int.
    for (int step = WINDOW; step < n; step++) {
        for (int &value : next_ways)
            value = 0;
        // a prime abc extends a number ending in ab (source) to one ending in bc (target)
        for (int i = 0; i < count; i++) {
            int &value = next_ways[target[i]];
            value += ways[source[i]];
            if (value >= MOD)
                value -= MOD;
        }
        for (int i = 0; i < PAIRS; i++)
            ways[i] = next_ways[i];
    }
    int total = 0;
    for (int value : ways) {
        total += value;
        if (total >= MOD)
            total -= MOD;
    }
    printf("%d\n", total);
}
