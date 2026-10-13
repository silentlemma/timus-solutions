#include <cstdio>
#include <initializer_list>

const int HALF = 1000, TICKETS = 1000000, BASE = 10;

int digitSum(int n) {
    int s = 0;
    for (; n > 0; n /= BASE)
        s += n % BASE;
    return s;
}

bool lucky(int n) { return digitSum(n / HALF) == digitSum(n % HALF); }

int main() {
    int number;
    scanf("%d", &number);
    // the sums differ by one, so the ticket is neither 000000 nor 999999
    // and both neighbours are six-digit tickets
    bool yes = false;
    for (int n : {number - 1, number + 1})
        if (n >= 0 && n < TICKETS && lucky(n))
            yes = true;
    puts(yes ? "Yes" : "No");
}
