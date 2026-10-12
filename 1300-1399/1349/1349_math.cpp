#include <cstdio>

int main() {
    int n = 0;
    if (scanf("%d", &n) != 1)
        return 0;
    // by Fermat's last theorem only the first and second powers have answers
    if (n == 1)
        printf("1 2 3\n");
    else if (n == 2)
        printf("3 4 5\n");
    else
        printf("-1\n");
    return 0;
}
