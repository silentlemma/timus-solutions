#include <cstdio>

int main() {
    int n;
    scanf("%d", &n);
    // every move adds two heaps, and the game ends when all heaps are ones
    long long moves = 0;
    for (int i = 0; i < n; i++) {
        int a;
        scanf("%d", &a);
        moves += (a - 1) / 2;
    }
    puts(moves % 2 == 1 ? "Daenerys" : "Stannis");
}
