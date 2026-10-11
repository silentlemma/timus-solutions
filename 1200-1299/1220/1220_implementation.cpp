#include <cstdio>

// A stack is a chain of blocks of BLOCK values, the newest block first. Only
// the newest block of a stack can be partly full, so the blocks in use never
// exceed OPS / BLOCK + STACKS, which keeps everything well under 0.75 MB.
const int STACKS = 1000, OPS = 100000, BLOCK = 10;
const int BLOCKS = OPS / BLOCK + STACKS + 1;
const int NONE = -1, BASE = 10;
// small fixed buffers for reading and writing, cheap next to the blocks
const int BUFFER = 1 << 14, DIGITS = 12;

static int values[BLOCKS][BLOCK];
static short below[BLOCKS];   // the next older block of the same stack
static short top[STACKS + 1]; // the newest block of every stack
static int size[STACKS + 1];
static short freeBlock; // the first unused block, the rest chained after it

static char in[BUFFER], out[BUFFER];
static int inLen = 0, inPos = 0, outLen = 0;

static int readChar() {
    if (inPos == inLen) {
        inLen = (int)fread(in, 1, BUFFER, stdin);
        inPos = 0;
        if (inLen <= 0) {
            return EOF;
        }
    }
    return in[inPos++];
}

static int readInt() {
    int c = readChar();
    while (c < '0' || c > '9') {
        c = readChar();
    }
    int v = 0;
    while (c >= '0' && c <= '9') {
        v = v * BASE + (c - '0');
        c = readChar();
    }
    return v;
}

static void writeInt(int v) {
    if (outLen + DIGITS > BUFFER) {
        fwrite(out, 1, outLen, stdout);
        outLen = 0;
    }
    char digits[DIGITS];
    int k = 0;
    do {
        digits[k++] = (char)('0' + v % BASE);
        v /= BASE;
    } while (v > 0);
    while (k > 0) {
        out[outLen++] = digits[--k];
    }
    out[outLen++] = '\n';
}

static void push(int st, int v) {
    if (size[st] % BLOCK == 0) {
        short b = freeBlock;
        freeBlock = below[b];
        below[b] = top[st];
        top[st] = b;
    }
    values[top[st]][size[st] % BLOCK] = v;
    size[st]++;
}

static int pop(int st) {
    size[st]--;
    short b = top[st];
    int v = values[b][size[st] % BLOCK];
    if (size[st] % BLOCK == 0) {
        top[st] = below[b];
        below[b] = freeBlock;
        freeBlock = b;
    }
    return v;
}

int main() {
    for (int b = 0; b < BLOCKS; b++) {
        below[b] = (short)(b + 1 < BLOCKS ? b + 1 : NONE);
    }
    for (int st = 0; st <= STACKS; st++) {
        top[st] = NONE;
    }
    freeBlock = 0;
    int n = readInt();
    for (int i = 0; i < n; i++) {
        int c = readChar();
        while (c != 'U' && c != 'O') {
            c = readChar(); // PUSH has a U, POP an O, as their second letter
        }
        int st = readInt();
        if (c == 'U') {
            push(st, readInt());
        } else {
            writeInt(pop(st));
        }
    }
    fwrite(out, 1, outLen, stdout);
}
