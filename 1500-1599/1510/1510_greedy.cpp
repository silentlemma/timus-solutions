#include <cstdio>

int main() {
    int n;
    scanf("%d", &n);
    // Boyer-Moore vote: a value met more often than all the others together
    // survives pairing every note with a different one
    long long leader = 0, lead = 0;
    for (int i = 0; i < n; i++) {
        long long value;
        scanf("%lld", &value);
        if (lead == 0)
            leader = value, lead = 1;
        else if (value == leader)
            lead++;
        else
            lead--;
    }
    printf("%lld\n", leader);
}
