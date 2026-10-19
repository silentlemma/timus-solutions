#include <algorithm>
#include <cstdio>
#include <vector>

// character classes, ordered: the end, other characters, dot, at, letters
const int OTHER = 1, DOT = 2, AT = 3, LETTER = 4, ALPHABET = LETTER + 26;
const int BUFFER = 1 << 16;

// cyclic prefix doubling with counting sort; code ends with a 0
std::vector<int> suffixArray(const std::vector<int> &code) {
    int n = code.size();
    std::vector<int> order(n), cls(n), shifted(n), fresh(n), count(std::max(n, ALPHABET), 0);
    for (int c : code) count[c]++;
    for (int i = 1; i < ALPHABET; i++) count[i] += count[i - 1];
    for (int i = n - 1; i >= 0; i--) order[--count[code[i]]] = i;
    int classes = 1;
    for (int i = 1; i < n; i++) {
        if (code[order[i]] != code[order[i - 1]]) classes++;
        cls[order[i]] = classes - 1;
    }
    for (int shift = 1; shift < n && classes < n; shift *= 2) {
        for (int i = 0; i < n; i++) shifted[i] = (order[i] - shift + n) % n;
        std::fill(count.begin(), count.begin() + classes, 0);
        for (int p : shifted) count[cls[p]]++;
        for (int i = 1; i < classes; i++) count[i] += count[i - 1];
        for (int i = n - 1; i >= 0; i--) order[--count[cls[shifted[i]]]] = shifted[i];
        fresh[order[0]] = 0;
        classes = 1;
        for (int i = 1; i < n; i++) {
            int cur = order[i], prev = order[i - 1];
            if (cls[cur] != cls[prev] || cls[(cur + shift) % n] != cls[(prev + shift) % n]) {
                classes++;
            }
            fresh[cur] = classes - 1;
        }
        cls.swap(fresh);
    }
    order.erase(order.begin());
    return order;
}

int main() {
    std::vector<char> text;
    char buf[BUFFER];
    size_t got;
    while ((got = fread(buf, 1, sizeof buf, stdin)) > 0) text.insert(text.end(), buf, buf + got);
    int n = text.size();
    std::vector<int> code(n + 1, 0), letters(n + 1, 0);
    for (int i = 0; i < n; i++) {
        char ch = text[i];
        bool letter = ch >= 'a' && ch <= 'z';
        code[i] = letter ? LETTER + ch - 'a' : ch == '.' ? DOT : ch == '@' ? AT : OTHER;
        letters[i + 1] = letters[i] + letter;
    }
    // around an at sign, users start no earlier than just past the last other
    // character, at or double dot, and domains end no later than just before
    // the next of them
    std::vector<int> firstStart(n, 0), lastEnd(n, 0), nextAt(n, -1);
    int barrier = -1, twin = -1;
    for (int i = 0; i < n; i++) {
        if (code[i] == AT) firstStart[i] = std::max(barrier, twin) + 1;
        if (code[i] == DOT && i > 0 && code[i - 1] == DOT) twin = i;
        if (code[i] == OTHER || code[i] == AT) barrier = i;
    }
    barrier = twin = n;
    int upcoming = -1;
    for (int i = n - 1; i >= 0; i--) {
        if (code[i] == AT) lastEnd[i] = std::min(barrier, twin) - 1;
        if (code[i] == OTHER) upcoming = -1;
        nextAt[i] = upcoming;
        if (code[i] == DOT && i + 1 < n && code[i + 1] == DOT) twin = i + 1;
        if (code[i] == OTHER || code[i] == AT) barrier = i;
        if (code[i] == AT) upcoming = i;
    }
    std::vector<int> order = suffixArray(code), rank(n);
    for (int r = 0; r < n; r++) rank[order[r]] = r;
    // being an address is a property of the string alone, so every address
    // is counted once, at the first suffix in sorted order that starts with
    // it: only prefixes longer than the common part with the suffix before
    long long total = 0;
    int common = 0;
    for (int start = 0; start < n; start++) {
        int r = rank[start], lcp = 0;
        if (r == 0) {
            common = 0;
        } else {
            int other = order[r - 1];
            while (code[start + common] && code[start + common] == code[other + common]) common++;
            lcp = common;
        }
        if (common > 0) common--;
        if (code[start] < LETTER) continue;
        int at = nextAt[start];
        if (at < 0 || start < firstStart[at] || code[at - 1] < LETTER) continue;
        int end = lastEnd[at];
        if (at + 1 > end || code[at + 1] < LETTER) continue;
        int lo = std::max(start + lcp, at + 1);
        if (lo <= end) total += letters[end + 1] - letters[lo];
    }
    printf("%lld\n", total);
    return 0;
}
