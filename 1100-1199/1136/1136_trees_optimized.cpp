#include <cstdio>

constexpr int MAX_MEMBERS = 3000;
// input positions are positive and below the array size, so 0 means none
int post[MAX_MEMBERS + 1], left[MAX_MEMBERS + 1], right[MAX_MEMBERS + 1];
int stack[MAX_MEMBERS], order[MAX_MEMBERS];

int main() {
    int n;
    if (scanf("%d", &n) != 1)
        return 0;
    for (int k = 1; k <= n; ++k)
        if (scanf("%d", &post[k]) != 1)
            return 0;
    // read backwards, the odd-session order gives every chairman, then the
    // right wing, then the left wing; a stack of the open chairmen rebuilds the
    // tree from that
    int size = 0;
    for (int k = n; k > 0; --k) {
        if (size > 0 && post[k] > post[stack[size - 1]]) {
            right[stack[size - 1]] = k;
        } else if (size > 0) {
            int parent = stack[--size];
            while (size > 0 && post[stack[size - 1]] > post[k])
                parent = stack[--size];
            left[parent] = k;
        }
        stack[size++] = k;
    }
    // the even-session order is the plain order root, left, right reversed
    size = 0;
    if (n > 0)
        stack[size++] = n;
    int count = 0;
    while (size > 0) {
        int node = stack[--size];
        order[count++] = post[node];
        if (right[node] != 0)
            stack[size++] = right[node];
        if (left[node] != 0)
            stack[size++] = left[node];
    }
    while (count > 0)
        printf("%d\n", order[--count]);
}
