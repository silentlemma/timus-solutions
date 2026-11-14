#include <bitset>
#include <cstdio>
#include <initializer_list>

const int MAX_FRIENDS = 100000;
const int BUFFER_SIZE = 1 << 15;

int number() {
    int c = getchar();
    while (c != EOF && c <= ' ')
        c = getchar();
    int value = 0;
    while (c >= '0' && c <= '9') {
        value = value * 10 + c - '0';
        c = getchar();
    }
    return value;
}

int main() {
    static char input[BUFFER_SIZE], output[BUFFER_SIZE];
    setvbuf(stdin, input, _IOFBF, sizeof input);
    setvbuf(stdout, output, _IOFBF, sizeof output);
    int n = number(), first = number(), previous = first;
    std::bitset<MAX_FRIENDS> falls;
    int count = 0;
    // The signed differences sum to zero. Mark just the edges with a drop.
    for (int edge = 0; edge < n; ++edge) {
        int current = edge + 1 < n ? number() : first;
        if (previous > current) {
            falls.set(edge);
            ++count;
        }
        previous = current;
    }
    if (count == 0) {
        falls.set(0);
        count = 1;
    }
    puts("YES");
    for (bool group : {true, false}) {
        printf("%d\n", group ? count : n - count);
        char separator = '\0';
        for (int edge = 0; edge < n; ++edge) {
            if (falls[edge] != group)
                continue;
            if (separator)
                putchar(separator);
            printf("%d", edge + 1);
            separator = ' ';
        }
        putchar('\n');
    }
}
