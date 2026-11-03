#include <cstdio>
#include <vector>

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
    int n = next_int();
    std::vector<int> votes(n);
    for (int i = 0; i < n; i++) {
        int start = i - (next_int() - 1);
        // -n<start<n, so a single correction replaces both modulo operations.
        if (start < 0)
            start += n;
        votes[start]++;
    }
    int best = 0;
    for (int i = 1; i < n; i++)
        if (votes[i] > votes[best])
            best = i;
    printf("%d\n", best + 1);
}
