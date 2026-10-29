#include <cstdio>

// the numbers are parsed by hand with getchar, without iostream
long long readInt() {
    int c;
    do {
        c = getchar();
    } while (c != EOF && c <= ' ');
    long long value = 0;
    while (c >= '0' && c <= '9') {
        value = value * 10 + c - '0';
        c = getchar();
    }
    return value;
}

int main() {
    long long x = readInt(), y = readInt(), total = readInt();
    long long a = x < total ? x : total;
    long long b = total - a;
    if (b > y)
        puts("Impossible");
    else
        printf("%lld %lld\n", a, b);
}
