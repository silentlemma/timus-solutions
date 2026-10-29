#include <cstdio>

// scanf and printf instead of iostream, which needs less memory
int main() {
    int harry, larry;
    if (scanf("%d %d", &harry, &larry) != 2)
        return 0;
    // the last can was shot by both, so each missed the other's count minus one
    printf("%d %d\n", larry - 1, harry - 1);
    return 0;
}
