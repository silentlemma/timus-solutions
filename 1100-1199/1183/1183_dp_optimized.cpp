#include <cstdio>
#include <cstring>

const int MAX_LENGTH = 100;
unsigned char cost[MAX_LENGTH + 1][MAX_LENGTH + 1];
char text[MAX_LENGTH + 2], output[2 * MAX_LENGTH + 1];
int used;

bool pair(char a, char b) { return (a == '(' && b == ')') || (a == '[' && b == ']'); }

void build(int i, int j) {
    if (i == j)
        return;
    if (j == i + 1) {
        bool round = text[i] == '(' || text[i] == ')';
        output[used++] = round ? '(' : '[';
        output[used++] = round ? ')' : ']';
    } else if (pair(text[i], text[j - 1]) && cost[i][j] == cost[i + 1][j - 1]) {
        output[used++] = text[i];
        build(i + 1, j - 1);
        output[used++] = text[j - 1];
    } else {
        for (int k = i + 1; k < j; k++)
            if (cost[i][j] == cost[i][k] + cost[k][j]) {
                build(i, k);
                build(k, j);
                return;
            }
    }
}

int main() {
    if (!fgets(text, sizeof(text), stdin))
        text[0] = 0;
    int n = std::strlen(text);
    while (n && (text[n - 1] == '\n' || text[n - 1] == '\r' || text[n - 1] == ' '))
        n--;
    for (int i = 0; i < n; i++)
        cost[i][i + 1] = 1;
    for (int length = 2; length <= n; length++)
        for (int i = 0; i + length <= n; i++) {
            int j = i + length, best = 1 + cost[i + 1][j];
            if (pair(text[i], text[j - 1]))
                best = cost[i + 1][j - 1];
            // A balanced result has even length; no cost beats length%2.
            for (int k = i + 1; k < j && best > length % 2; k++)
                if (cost[i][k] + cost[k][j] < best)
                    best = cost[i][k] + cost[k][j];
            cost[i][j] = best;
        }
    // Optimal transitions can be recovered from costs alone.
    build(0, n);
    output[used++] = '\n';
    fwrite(output, 1, used, stdout);
}
