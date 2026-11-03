#include <algorithm>
#include <cstdio>
#include <vector>
using namespace std;
const int BUFFER = 1 << 14;
const long long INF = 1LL << 60;
char buffer[BUFFER];
int position, available;
int readByte() {
    if (position == available) {
        available = (int)fread(buffer, 1, BUFFER, stdin);
        position = 0;
        if (!available)
            return EOF;
    }
    return buffer[position++];
}
int nextInt() {
    int c = readByte(), value = 0;
    while (c <= ' ')
        c = readByte();
    while (c >= '0' && c <= '9') {
        value = value * 10 + c - '0';
        c = readByte();
    }
    return value;
}
char nextKind() {
    int c = readByte();
    while (c <= ' ')
        c = readByte();
    char kind = (char)c;
    while (readByte() > ' ') {
    }
    return kind;
}
int main() {
    int n = nextInt(), m = nextInt();
    vector<int> head(n, -1), to(m), link(m), weight(m);
    vector<char> kind(m);
    for (int i = 0; i < m; i++) {
        int x = nextInt() - 1;
        to[i] = nextInt() - 1;
        weight[i] = nextInt();
        kind[i] = nextKind();
        link[i] = head[x];
        head[x] = i;
    }
    vector<long long> clean(n, INF), dirty(n, INF);
    clean[0] = 0;
    for (int v = 0; v < n; v++) {
        long long licensed = clean[v], pirated = dirty[v];
        for (int edge = head[v]; edge != -1; edge = link[edge]) {
            int y = to[edge], cost = weight[edge];
            if (kind[edge] == 'P')
                dirty[y] = min(dirty[y], min(licensed, pirated) + cost);
            else {
                clean[y] = min(clean[y], licensed + cost);
                if (kind[edge] == 'C')
                    dirty[y] = min(dirty[y], pirated + cost);
            }
        }
    }
    long long answer = min(clean[n - 1], dirty[n - 1]);
    if (answer == INF)
        puts("Offline");
    else
        printf("Online\n%lld\n", answer);
}
