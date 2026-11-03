#include <cstdio>

const int LIMIT = 100000, PERIOD = 3, BLOCK_REPEATS = 1024, BLOCK_SIZE = PERIOD * BLOCK_REPEATS;
const char LETTERS[] = "abc";
char block[BLOCK_SIZE];

int main() {
    int n;
    if (scanf("%d", &n) != 1)
        return 0;
    if (n == 1) {
        for (int first = 0; first < PERIOD; first++)
            printf("%c\n", LETTERS[first]);
        return 0;
    }
    if (PERIOD * (PERIOD - 1) * n > LIMIT) {
        puts("TOO LONG");
        return 0;
    }
    for (int first = 0; first < PERIOD; first++)
        for (int second = 0; second < PERIOD; second++)
            if (first != second) {
                int third = 0;
                while (third == first || third == second)
                    third++;
                char pattern[] = {LETTERS[first], LETTERS[second], LETTERS[third]};
                for (int i = 0; i < BLOCK_SIZE; i++)
                    block[i] = pattern[i % PERIOD];
                for (int left = n; left > 0;) {
                    int take = left < BLOCK_SIZE ? left : BLOCK_SIZE;
                    fwrite(block, 1, take, stdout);
                    left -= take;
                }
                putchar('\n');
            }
}
