#include <algorithm>
#include <cstdio>
using namespace std;

const int FREE = 6; // calls of up to six seconds cost nothing
const int MINUTE = 60;

int main() {
    long long n1, c1, n2, t, c2, n3;
    int k;
    if (scanf("%lld %lld", &n1, &c1) != 2 || scanf("%lld %lld", &n2, &t) != 2 ||
        scanf("%lld", &c2) != 1 || scanf("%lld", &n3) != 1 || scanf("%d", &k) != 1)
        return 0;
    long long minutes = 0;
    for (int i = 0; i < k; i++) {
        int mm, ss;
        if (scanf("%d:%d", &mm, &ss) != 2)
            return 0;
        int seconds = mm * MINUTE + ss;
        if (seconds > FREE)
            minutes += (seconds + MINUTE - 1) / MINUTE; // a started minute counts in full
    }
    printf("Basic:     %lld\n", n1 + c1 * minutes);
    printf("Combined:  %lld\n", n2 + c2 * max(0LL, minutes - t));
    printf("Unlimited: %lld\n", n3);
}
