#include <cstdint>
#include <cstdio>

using u32 = uint32_t;
const int LIMIT = 32768;
const int BUFFER_SIZE = 8192;
const int NUMBER_RESERVE = 16;
const u32 MOD_FOUR = 4;
const u32 MOD_EIGHT = 8;
const u32 CLASS_THREE = 3;
const u32 CLASS_FIVE = 5;
const int NUMBER_DIGITS = 5;

u32 power(u32 base, u32 exponent, u32 modulus) {
    u32 result = 1;
    for (; exponent; exponent >>= 1, base = base * base % modulus)
        if (exponent & 1)
            result = result * base % modulus;
    return result;
}

u32 root(u32 a, u32 p, uint16_t *cache) {
    if (p == 2)
        return 1;
    if (p % MOD_FOUR == CLASS_THREE) {
        u32 r = power(a, (p + 1) / MOD_FOUR, p);
        return r * r % p == a ? r : 0;
    }
    if (p % MOD_EIGHT == CLASS_FIVE) {
        u32 r = power(a, (p + CLASS_THREE) / MOD_EIGHT, p);
        if (r * r % p != a) {
            if (!cache[p])
                cache[p] = static_cast<uint16_t>(power(2, (p - 1) / MOD_FOUR, p));
            r = r * cache[p] % p;
        }
        return r * r % p == a ? r : 0;
    }
    u32 q = p - 1, s = 0;
    while (!(q & 1)) {
        q >>= 1;
        ++s;
    }
    // One power yields r and t with r²=a*t; no separate Euler test is needed.
    u32 b = power(a, (q - 1) / 2, p), r = a * b % p, t = r * b % p, c = 0;
    while (t != 1) {
        u32 i = 0, square = t;
        while (square != 1 && i < s) {
            square = square * square % p;
            ++i;
        }
        if (i == s)
            return 0;
        if (!c) {
            if (!cache[p]) {
                u32 z = 2;
                while (power(z, (p - 1) / 2, p) != p - 1)
                    ++z;
                cache[p] = static_cast<uint16_t>(power(z, q, p));
            }
            c = cache[p];
        }
        b = c;
        for (u32 j = 0; j < s - i - 1; ++j)
            b = b * b % p;
        c = b * b % p;
        r = r * b % p;
        t = t * c % p;
        s = i;
    }
    return r;
}

struct Reader {
    unsigned char data[BUFFER_SIZE];
    int position = 0, length = 0;
    int byte() {
        if (position == length) {
            length = int(fread(data, 1, sizeof(data), stdin));
            position = 0;
            if (!length)
                return 0;
        }
        return data[position++];
    }
    u32 number() {
        int c = byte();
        while (c && c <= ' ')
            c = byte();
        u32 value = 0;
        while (c >= '0' && c <= '9') {
            value = value * 10 + c - '0';
            c = byte();
        }
        return value;
    }
};

struct Writer {
    char data[BUFFER_SIZE];
    int used = 0;
    void flush() {
        fwrite(data, 1, used, stdout);
        used = 0;
    }
    void number(u32 value) {
        char digits[NUMBER_DIGITS];
        int length = 0;
        do {
            digits[length++] = char('0' + value % 10);
            value /= 10;
        } while (value);
        while (length)
            data[used++] = digits[--length];
    }
    void answer(u32 r, u32 p) {
        if (used + NUMBER_RESERVE > BUFFER_SIZE)
            flush();
        if (!r) {
            const char *message = "No root\n";
            while (*message)
                data[used++] = *message++;
            return;
        }
        if (p == 2) {
            data[used++] = '1';
            data[used++] = '\n';
            return;
        }
        u32 other = p - r;
        if (r > other) {
            u32 swap = r;
            r = other;
            other = swap;
        }
        number(r);
        data[used++] = ' ';
        number(other);
        data[used++] = '\n';
    }
};

int main() {
    Reader in;
    Writer out;
    static uint16_t cache[LIMIT];
    u32 count = in.number();
    while (count--) {
        u32 a = in.number(), p = in.number();
        out.answer(root(a % p, p, cache), p);
    }
    out.flush();
}
