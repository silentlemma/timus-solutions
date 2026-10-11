#include <cstdio>

const long long BASE = 3;

int main() {
    long long n, pay = 0, tip = 0;
    scanf("%lld", &n);
    // balanced ternary: digits 1 go into the payment, digits -1 into the tip
    for (long long power = 1; n > 0; power *= BASE) {
        if (n % BASE == 1) {
            pay += power;
            n--;
        } else if (n % BASE == BASE - 1) {
            tip += power;
            n++;
        }
        n /= BASE;
    }
    // no tip yet: add the smallest bill the payment lacks to both
    for (long long power = 1; tip == 0; power *= BASE) {
        if (pay / power % BASE == 0) {
            pay += power;
            tip = power;
        }
    }
    printf("%lld %lld\n", pay, tip);
}
