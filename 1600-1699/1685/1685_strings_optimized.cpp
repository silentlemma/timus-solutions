#include <cstdio>
const int MAX_LENGTH = 20000;
// the line has at most 20000 ascii characters; leave room for cr, lf and the terminator.
const int LINE_END_SPACE = 3;
char text[MAX_LENGTH + LINE_END_SPACE], out[MAX_LENGTH];
int at;
void decode(int lo, int hi) {
    if (lo >= hi)
        return;
    int mid = (lo + hi - 1) / 2;
    out[mid] = text[at++];
    decode(lo, mid);
    decode(mid + 1, hi);
}
int main() {
    if (!fgets(text, sizeof text, stdin)) {
        putchar('\n');
        return 0;
    }
    int n = 0;
    while (text[n] && text[n] != '\r' && text[n] != '\n')
        n++;
    // the encoded text lists the middle of a range, then its left part,
    // then its right part: replay that order and put each letter back
    decode(0, n);
    fwrite(out, 1, n, stdout);
    putchar('\n');
}
