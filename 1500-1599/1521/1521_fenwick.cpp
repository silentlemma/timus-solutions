#include <cstdio>
#include <string>
#include <vector>

using namespace std;

int main() {
    int n, k;
    scanf("%d %d", &n, &k);
    // a Fenwick tree over the circle: 1 for a soldier still marching
    vector<int> tree(n + 1, 0);
    for (int i = 1; i <= n; i++) {
        tree[i]++;
        if (i + (i & -i) <= n)
            tree[i + (i & -i)] += tree[i];
    }
    int top = 1;
    while (top * 2 <= n)
        top *= 2;
    string out;
    for (int rank = 0, left = n; left > 0; left--) {
        // the soldier k places ahead, counting among those still marching
        rank = (rank + k - 1) % left;
        // descend to the (rank + 1)-th remaining soldier
        int pos = 0, need = rank + 1;
        for (int step = top; step > 0; step /= 2)
            if (pos + step <= n && tree[pos + step] < need) {
                pos += step;
                need -= tree[pos];
            }
        pos++;
        out += to_string(pos);
        out += left > 1 ? ' ' : '\n';
        for (int i = pos; i <= n; i += i & -i)
            tree[i]--;
    }
    fputs(out.c_str(), stdout);
}
