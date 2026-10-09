#include <cstdio>
#include <vector>

const int BUFFER = 1 << 16, BASE = 10;

char buf[BUFFER];
size_t len = 0, pos = 0;

// the next byte of the input, or -1 at its end; the input is a few megabytes
int next_byte() {
    if (pos == len) {
        len = fread(buf, 1, BUFFER, stdin);
        pos = 0;
        if (len == 0)
            return -1;
    }
    return buf[pos++];
}

// the next digit, skipping spaces and line breaks
int next_digit() {
    int c = next_byte();
    while (c != -1 && (c < '0' || c > '9'))
        c = next_byte();
    return c - '0';
}

int main() {
    int n = 0, c = next_byte();
    while (c < '0' || c > '9')
        c = next_byte();
    for (; c >= '0' && c <= '9'; c = next_byte())
        n = n * BASE + (c - '0');
    // column sums from 0 to 18, then the carries from the last column up
    std::vector<char> out(n + 1, '\n');
    for (int i = 0; i < n; i++) {
        int a = next_digit();
        out[i] = (char)(a + next_digit());
    }
    int carry = 0;
    for (int i = n - 1; i >= 0; i--) {
        int t = out[i] + carry;
        carry = t / BASE;
        out[i] = (char)('0' + t % BASE);
    }
    fwrite(out.data(), 1, out.size(), stdout);
}
