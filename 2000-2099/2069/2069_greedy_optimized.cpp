#include <algorithm>
#include <cstdio>

const int BUFFER_SIZE = 4096;
unsigned char input[BUFFER_SIZE];
int position, available;

int read() {
    if (position == available) {
        available = fread(input, 1, BUFFER_SIZE, stdin);
        position = 0;
        if (!available)
            return -1;
    }
    return input[position++];
}

int next_int() {
    int c = read();
    while (c <= ' ')
        c = read();
    int value = 0;
    while (c >= '0' && c <= '9') {
        value = value * 10 + c - '0';
        c = read();
    }
    return value;
}

int main() {
    int n = next_int(), m = next_int();
    int first_v = next_int(), last_v = first_v, max_v = first_v;
    for (int i = 1; i < n; i++) {
        last_v = next_int();
        max_v = std::max(max_v, last_v);
    }
    int first_h = next_int(), last_h = first_h, max_h = first_h;
    for (int i = 1; i < m; i++) {
        last_h = next_int();
        max_h = std::max(max_h, last_h);
    }
    // Both directions and an incident street at each endpoint are necessary.
    // Qualifying horizontal and vertical streets form a connected cross-grid.
    printf("%d\n", std::min({max_v, max_h, std::max(first_v, first_h), std::max(last_v, last_h)}));
}
