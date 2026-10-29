#include <cstdio>

// scanf and printf instead of iostream, which needs less memory
int main() {
    int count;
    long long capacity;
    if (scanf("%d %lld", &count, &capacity) != 2)
        return 0;
    long long unused = 0, survivors = 0;
    for (int i = 0; i < count; ++i) {
        long long amount;
        scanf("%lld", &amount);
        if (amount > capacity)
            unused += amount - capacity;
        else
            survivors += capacity - amount;
    }
    printf("%lld %lld\n", unused, survivors);
}
