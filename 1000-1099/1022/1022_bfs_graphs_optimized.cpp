#include <cstdio>

const int MAX_MEMBERS = 100;
// n <= 100: one byte per possible relation takes only about ten kibibytes.
bool children[MAX_MEMBERS + 1][MAX_MEMBERS + 1];
int parents[MAX_MEMBERS + 1], order[MAX_MEMBERS];

int main() {
    int n;
    scanf("%d", &n);
    for (int v = 1; v <= n; v++) {
        int c;
        while (scanf("%d", &c) == 1 && c != 0) {
            if (!children[v][c]) {
                children[v][c] = true;
                parents[c]++;
            }
        }
    }
    int size = 0;
    for (int v = 1; v <= n; v++)
        if (parents[v] == 0)
            order[size++] = v;
    for (int i = 0; i < size; i++) {
        int v = order[i];
        for (int c = 1; c <= n; c++)
            if (children[v][c] && --parents[c] == 0)
                order[size++] = c;
    }
    for (int i = 0; i < size; i++)
        printf("%d%c", order[i], i + 1 == size ? '\n' : ' ');
}
