#include <cstdio>
#include <string>

const int BUF_SIZE = 1 << 16;
char buf[BUF_SIZE];
int len = 0, pos = 0;

int read_byte() {
    if (pos == len) {
        len = fread(buf, 1, BUF_SIZE, stdin);
        pos = 0;
        if (len <= 0)
            return -1;
    }
    return buf[pos++];
}

// skips separators and reads one non-negative number
int read_int() {
    int c = read_byte();
    while (c != -1 && (c < '0' || c > '9'))
        c = read_byte();
    int v = 0;
    for (; c >= '0' && c <= '9'; c = read_byte())
        v = v * 10 + c - '0';
    return v;
}

int main() {
    int n = read_int(), k = read_int();
    read_int();
    // removing an item changes the sum by 1..N and replacing one by -N+1..N-1,
    // never by a multiple of N + 1, so similar sets differ modulo N + 1
    std::string out = "YES\n";
    for (int i = 0; i < k; i++) {
        int count = read_int(), sum = 0;
        for (int j = 0; j < count; j++)
            sum += read_int();
        out += std::to_string(sum % (n + 1) + 1) + "\n";
    }
    fputs(out.c_str(), stdout);
}
