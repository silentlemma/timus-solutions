#include <cstdio>
#include <vector>

typedef long long i64;

// The largest value over all knights but one, from the two largest; -1 when
// there is no other knight, so a lone knight needs nothing.
struct TopTwo {
    i64 first = -1, second = -1;
    int where = -1;
    void add(i64 value, int index) {
        if (value > first) {
            second = first;
            first = value;
            where = index;
        } else if (value > second) {
            second = value;
        }
    }
    i64 without(int index) const { return index == where ? second : first; }
};

int main() {
    int n;
    scanf("%d", &n);
    std::vector<i64> a(n), d(n), g(n);
    TopTwo attack, shield;  // the strongest attack and shield each rival can afford
    for (int i = 0; i < n; i++) {
        scanf("%lld %lld %lld", &a[i], &d[i], &g[i]);
        attack.add(a[i] + g[i], i);
        shield.add(d[i] + g[i], i);
    }
    for (int i = 0; i < n; i++) {
        // The shield must exceed every rival's best attack and the attack must
        // reach every rival's best shield, whatever the rivals do.
        i64 needShield = attack.without(i) + 1 - d[i];
        i64 needAttack = shield.without(i) - a[i];
        i64 cost = (needShield > 0 ? needShield : 0) + (needAttack > 0 ? needAttack : 0);
        if (cost <= g[i]) {
            printf("%d\n", i + 1);
            return 0;
        }
    }
    puts("-1");
    return 0;
}
