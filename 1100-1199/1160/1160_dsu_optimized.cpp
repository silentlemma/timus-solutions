#include <algorithm>
#include <cstdint>
#include <cstdio>

// refills allow arbitrarily long input with only four kibibytes of storage.
const int INPUT_BUFFER = 4096;
char input_buffer[INPUT_BUFFER];
int input_pos = 0, input_len = 0;

int read_byte() {
    if (input_pos == input_len) {
        input_len = static_cast<int>(fread(input_buffer, 1, INPUT_BUFFER, stdin));
        input_pos = 0;
        if (input_len == 0)
            return EOF;
    }
    return input_buffer[input_pos++];
}

int next_int() {
    int c = read_byte();
    while (c != EOF && c <= ' ')
        c = read_byte();
    int value = 0;
    while (c >= '0' && c <= '9') {
        value = value * 10 + c - '0';
        c = read_byte();
    }
    return value;
}

const int MAX_HUBS = 1000, MAX_EDGES = 15000;
// hub numbers are at most 1000; length is at most a million and fits int.
struct Edge {
    int length;
    std::uint16_t a, b;
};
Edge edges[MAX_EDGES], chosen[MAX_HUBS];
int parent[MAX_HUBS + 1];

int find(int v) {
    while (parent[v] != v)
        v = parent[v] = parent[parent[v]];
    return v;
}
int main() {
    int n = next_int(), m = next_int();
    for (int i = 0; i < m; i++) {
        int a = next_int(), b = next_int(), length = next_int();
        edges[i] = {length, static_cast<std::uint16_t>(a), static_cast<std::uint16_t>(b)};
    }
    // in-place sorting avoids stable_sort's temporary edge array.
    std::sort(edges, edges + m, [](const Edge &a, const Edge &b) { return a.length < b.length; });
    for (int i = 1; i <= n; i++)
        parent[i] = i;
    int count = 0;
    for (int i = 0; i < m && count < n - 1; i++) {
        Edge e = edges[i];
        int a = find(e.a), b = find(e.b);
        if (a != b) {
            parent[a] = b;
            chosen[count++] = e;
        }
    }
    printf("%d\n%d\n", chosen[count - 1].length, count);
    for (int i = 0; i < count; i++)
        printf("%d %d\n", chosen[i].a, chosen[i].b);
}
