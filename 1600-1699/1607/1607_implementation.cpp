#include <cstdio>

int main() {
    int a, b, c, d;
    if (scanf("%d %d", &a, &b) != 2 || scanf("%d %d", &c, &d) != 2)
        return 0;
    int petya = a, driver = c;
    // the driver never asks less than Petya offers, and the other way round
    if (petya >= driver) {
        printf("%d\n", petya);
        return 0;
    }
    while (true) {
        petya += b;
        if (petya >= driver) {
            printf("%d\n", driver);
            return 0;
        }
        driver -= d;
        if (driver <= petya) {
            printf("%d\n", petya);
            return 0;
        }
    }
}
