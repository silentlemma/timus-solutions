#include <cstdio>

constexpr int MAX_SOLDIERS = 100000;

int main() {
    int n, k;
    scanf("%d %d", &n, &k);
    // a fenwick tree over the circle: 1 for a soldier still marching
    // initially every interval is full, so its count is lowbit(i) <= n <= 100000.
    static int tree[MAX_SOLDIERS + 1];
    for (int i = 1; i <= n; i++)
        tree[i] = i & -i;
    int top = 1;
    while (top * 2 <= n)
        top *= 2;
    for (int rank = 0, left = n; left > 0; left--) {
        // the soldier k places ahead, counting among those still marching
        rank = (rank + k - 1) % left;
        // descend to the (rank + 1)-th remaining soldier
        int pos = 0, need = rank + 1;
        for (int step = top; step > 0; step /= 2) {
            int next = pos + step;
            if (next <= n) {
                if (tree[next] < need) {
                    need -= tree[next];
                    pos = next;
                } else {
                    // this fenwick interval contains the soldier being removed.
                    tree[next]--;
                }
            }
        }
        printf("%d%c", pos + 1, left > 1 ? ' ' : '\n');
    }
}
