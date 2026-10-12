#include <cmath>
#include <cstdio>
#include <vector>

const int CEILING = 0, TURNIP = -1, FREE = -2;
const int ONE = 0, MASS = 1; // the turnip's weight of 1 and the unknown mass
const int FIELDS = 4;

int n;
std::vector<int> kind, x1, x2, up, parent, shift;
std::vector<bool> zero; // the whole group must have no tension

int rope(int i) { return 2 * i + 2; }   // tension in the rope over block i
int axle(int i) { return rope(i) + 1; } // tension in the rope at the axle of block i

// every tension is a power of two times the tension at the root of its
// group: value(x) = 2^shift[x] * value(root)
int find(int x) {
    if (parent[x] == x)
        return x;
    int root = find(parent[x]);
    shift[x] += shift[parent[x]];
    parent[x] = root;
    return root;
}

// value(x) = 2^k * value(y)
void tie(int x, int y, int k) {
    int rx = find(x), ry = find(y);
    if (rx == ry) {
        if (shift[x] != k + shift[y])
            zero[rx] = true;
        return;
    }
    parent[rx] = ry;
    shift[rx] = k + shift[y] - shift[x];
    zero[ry] = zero[ry] || zero[rx];
}

struct Port {
    int node, target;
    bool down;
};

// the two rope ends and the axle, with the way they leave the block; a
// first-type block hangs its rope ends down
std::vector<Port> ports(int i) {
    bool down = kind[i] == 1;
    return {{rope(i), x1[i], down}, {rope(i), x2[i], down}, {axle(i), up[i], !down}};
}

int main() {
    if (scanf("%d", &n) != 1)
        return 0;
    kind.resize(n);
    x1.resize(n);
    x2.resize(n);
    up.resize(n);
    for (int i = 0; i < n; i++) {
        if (scanf("%d %d %d %d", &kind[i], &x1[i], &x2[i], &up[i]) != FIELDS)
            return 0;
    }
    parent.resize(2 * n + 2);
    shift.assign(2 * n + 2, 0);
    zero.assign(2 * n + 2, false);
    for (int v = 0; v < 2 * n + 2; v++)
        parent[v] = v;
    for (int i = 0; i < n; i++) {
        tie(axle(i), rope(i), 1); // the axle holds both ends of the rope
        for (const Port &p : ports(i)) {
            if (p.target == TURNIP) {
                tie(p.node, ONE, 0);
            } else if (p.target == FREE) {
                tie(p.node, MASS, 0);
            } else if (p.target != CEILING) {
                // the other end leaves block target the opposite way
                for (const Port &q : ports(p.target - 1)) {
                    if (q.target == i + 1 && q.down != p.down) {
                        tie(p.node, q.node, 0);
                        break;
                    }
                }
            }
        }
    }
    int one = find(ONE), mass = find(MASS);
    if (zero[one])
        printf("No solution\n");
    else if (one == mass)
        printf("%.4f\n", std::ldexp(1.0, shift[MASS] - shift[ONE]));
    else if (zero[mass])
        printf("%.4f\n", 0.0);
    else
        printf("Any\n");
    return 0;
}
