#include <algorithm>
#include <cstdio>
#include <numeric>
#include <vector>

using namespace std;

const int CAMEL = 1;

struct Animal {
    int a, b, kind; // a ray from the origin, reduced by the gcd
};

long long cross(const Animal &p, const Animal &q) {
    return (long long)p.a * q.b - (long long)p.b * q.a;
}

int main() {
    int n;
    scanf("%d", &n);
    vector<Animal> animals(n);
    bool origin = false;
    for (auto &x : animals) {
        scanf("%d %d %d", &x.a, &x.b, &x.kind);
        int g = gcd(x.a, x.b);
        if (g == 0)
            origin = true; // nobody can judge an animal at the origin
        else
            x.a /= g, x.b /= g;
    }
    if (origin) {
        puts("-1");
        return 0;
    }
    // rays by angle, counterclockwise from the A axis
    sort(animals.begin(), animals.end(),
         [](const Animal &p, const Animal &q) { return cross(p, q) > 0; });
    vector<pair<int, int>> experts;
    for (int i = 0; i + 1 < n; i++) {
        const Animal &p = animals[i], &q = animals[i + 1];
        if (cross(p, q) == 0) {
            if (p.kind != q.kind) {
                puts("-1"); // every expert judges a whole ray alike
                return 0;
            }
            continue;
        }
        if (p.kind == q.kind)
            continue;
        // a line along p + q passes strictly between the two rays
        int x = p.a + q.a, y = p.b + q.b, g = gcd(x, y);
        x /= g, y /= g;
        experts.push_back(p.kind == CAMEL ? make_pair(y, -x) : make_pair(-y, x));
    }
    if (experts.size() % 2 == 0) {
        // an odd count avoids ties; one more expert votes for the first kind
        int s = animals[0].kind == CAMEL ? 1 : -1;
        experts.push_back({s, s});
    }
    printf("%d\n", (int)experts.size());
    for (auto &e : experts)
        printf("%d %d\n", e.first, e.second);
}
