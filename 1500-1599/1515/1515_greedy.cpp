#include <cstdio>

using namespace std;

int main() {
    int n;
    scanf("%d", &n);
    // every sum from 1 to reach is made of the notes taken so far; a note
    // no larger than reach + 1 extends that to reach + note
    long long reach = 0;
    for (int i = 0; i < n; i++) {
        long long d;
        scanf("%lld", &d);
        if (d > reach + 1)
            break;
        reach += d;
    }
    printf("%lld\n", reach + 1);
}
