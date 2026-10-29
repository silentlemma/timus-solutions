#include <cstdio>

int main() {
    int first, second;
    if (scanf("%d %d", &first, &second) != 2)
        return 0;
    // on night k the thief tries code k on lock 1 when k is even and on
    // lock 2 when k is odd
    puts(first % 2 == 0 || second % 2 == 1 ? "yes" : "no");
    return 0;
}
