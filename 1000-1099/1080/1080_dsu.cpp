#include <cstdio>

const int MAX_COUNTRIES = 98;
int parent[MAX_COUNTRIES], sizes[MAX_COUNTRIES];
unsigned char parity[MAX_COUNTRIES];

int find(int v) {
    if (parent[v] != v) {
        int old = parent[v];
        parent[v] = find(old);
        parity[v] ^= parity[old];
    }
    return parent[v];
}

int main() {
    int n;
    if (scanf("%d", &n) != 1)
        return 0;
    for (int v = 0; v < n; v++) {
        parent[v] = v;
        sizes[v] = 1;
    }
    // parity stores child/parent color XOR. Each edge must have XOR=1.
    for (int a = 0; a < n; a++) {
        int b;
        while (scanf("%d", &b) == 1 && b) {
            b--;
            int ra = find(a), rb = find(b);
            if (ra == rb) {
                if (parity[a] == parity[b]) {
                    puts("-1");
                    return 0;
                }
            } else {
                if (sizes[ra] < sizes[rb]) {
                    int tmp = ra;
                    ra = rb;
                    rb = tmp;
                }
                parent[rb] = ra;
                parity[rb] = parity[a] ^ parity[b] ^ 1;
                sizes[ra] += sizes[rb];
            }
        }
    }
    find(0);
    int first = parity[0];
    char answer[MAX_COUNTRIES + 1];
    for (int v = 0; v < n; v++) {
        find(v);
        answer[v] = '0' + (parity[v] ^ first);
    }
    answer[n] = 0;
    puts(answer);
}
