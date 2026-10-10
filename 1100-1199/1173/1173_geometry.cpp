#include <algorithm>
#include <cmath>
#include <cstdio>
#include <vector>

typedef long long ll;
// coordinates have at most three decimals, so in thousandths they are exact
// integers and every turn below is decided without rounding
const double SCALE = 1000;

struct Friend {
    ll x, y;
    int id;
};

ll exact() {
    double v;
    scanf("%lf", &v);
    return std::llround(v * SCALE);
}

int half(const Friend &p) { return p.y > 0 || (p.y == 0 && p.x > 0) ? 0 : 1; }

ll cross(const Friend &p, const Friend &q) { return p.x * q.y - p.y * q.x; }

int main() {
    ll hx = exact(), hy = exact();
    int n;
    scanf("%d", &n);
    std::vector<Friend> friends(n);
    for (auto &f : friends) {
        f.x = exact() - hx;
        f.y = exact() - hy;
        scanf("%d", &f.id);
    }
    std::sort(friends.begin(), friends.end(), [](const Friend &p, const Friend &q) {
        return half(p) != half(q) ? half(p) < half(q) : cross(p, q) > 0;
    });
    // consecutive friends by angle, joined in turn, never cross; the house
    // closes the loop across one angular gap, which must be the one wider
    // than half a turn if there is one
    int start = 0;
    for (int i = 0; i < n; i++) {
        if (cross(friends[(i + n - 1) % n], friends[i]) < 0) {
            start = i;
        }
    }
    printf("0\n");
    for (int k = 0; k < n; k++) {
        printf("%d\n", friends[(start + k) % n].id);
    }
    printf("0\n");
}
