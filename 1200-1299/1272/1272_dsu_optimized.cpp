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

const int MAX_ISLANDS = 10000;
// n <= 10000 makes this fixed parent array sufficient without heap allocation.
int parent[MAX_ISLANDS + 1];
int find(int v) {
    while (parent[v] != v)
        v = parent[v] = parent[parent[v]];
    return v;
}
int main() {
    int n = next_int(), k = next_int(), m = next_int();
    for (int i = 1; i <= n; i++)
        parent[i] = i;
    // tunnels are free; every bridge joins two of the remaining groups
    int groups = n;
    for (int i = 0; i < k; i++) {
        int a = find(next_int()), b = find(next_int());
        if (a != b) {
            parent[a] = b;
            groups--;
        }
    }
    // bridges cannot change the tunnel components, but all input is consumed.
    for (int i = 0; i < m; i++) {
        next_int();
        next_int();
    }
    printf("%d\n", groups - 1);
}
