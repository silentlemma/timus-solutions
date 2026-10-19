#include <algorithm>
#include <cstdint>
#include <cstdio>
#include <numeric>
#include <vector>

using namespace std;

constexpr int BUFFER = 1 << 16;
constexpr int MAX_TOTAL = 1000000;
constexpr int BLOCK = 32;  // block size of the range maximum over the node lists

char inBuf[BUFFER], outBuf[BUFFER];
int inPos = 0, inLen = 0, outLen = 0;

int readChar() {
    if (inPos == inLen) {
        inLen = (int)fread(inBuf, 1, BUFFER, stdin);
        inPos = 0;
        if (inLen <= 0) return -1;
    }
    return inBuf[inPos++];
}

void writeChar(char c) {
    if (outLen == BUFFER) fwrite(outBuf, 1, outLen, stdout), outLen = 0;
    outBuf[outLen++] = c;
}

vector<char> pool;     // all words, one after another
vector<uint32_t> off;  // word i is pool[off[i], off[i + 1])

uint32_t len(uint32_t i) { return off[i + 1] - off[i]; }

uint32_t commonPrefix(uint32_t i, uint32_t j) {
    uint32_t k = 0, m = min(len(i), len(j));
    while (k < m && pool[off[i] + k] == pool[off[j] + k]) k++;
    return k;
}

uint32_t commonSuffix(uint32_t i, uint32_t j) {
    uint32_t k = 0, m = min(len(i), len(j));
    while (k < m && pool[off[i + 1] - 1 - k] == pool[off[j + 1] - 1 - k]) k++;
    return k;
}

// suffix tree of the words: node[off[i] + b - 1] is the node of the last b letters of word i,
// and the words below node u, by increasing number, are ids[start[u], start[u + 1])
vector<uint32_t> node, start, ids;
// maxima of word lengths over blocks of ids, with a sparse table over the blocks
vector<vector<uint32_t>> table;

uint32_t blockMax(size_t l, size_t r) {  // blocks l..r, l <= r
    int k = __lg(r - l + 1);
    return max(table[k][l], table[k][r + 1 - (1u << k)]);
}

uint32_t longest(size_t l, size_t r) {  // the longest word among ids[l, r)
    uint32_t best = 0;
    if (l >= r) return 0;
    size_t bl = l / BLOCK, br = (r - 1) / BLOCK;
    if (bl == br) {
        for (size_t k = l; k < r; k++) best = max(best, len(ids[k]));
        return best;
    }
    for (size_t k = l; k < (bl + 1) * BLOCK; k++) best = max(best, len(ids[k]));
    for (size_t k = br * BLOCK; k < r; k++) best = max(best, len(ids[k]));
    if (bl + 1 < br) best = max(best, blockMax(bl + 1, br - 1));
    return best;
}

void buildSuffixes(uint32_t n) {
    vector<uint32_t> order(n);
    iota(order.begin(), order.end(), 0);
    sort(order.begin(), order.end(), [](uint32_t i, uint32_t j) {
        uint32_t k = commonSuffix(i, j);
        if (k == len(i) || k == len(j)) return len(i) < len(j);
        return pool[off[i + 1] - 1 - k] < pool[off[j + 1] - 1 - k];
    });
    // nodes are numbered in the order the sorted reversed words open them
    node.assign(pool.size(), 0);
    vector<uint32_t> path(1, 0);
    uint32_t nodes = 0;
    for (uint32_t k = 0; k < n; k++) {
        uint32_t i = order[k], common = k ? commonSuffix(order[k - 1], i) : 0;
        path.resize(common + 1);
        while (path.size() <= len(i)) path.push_back(nodes++);
        for (uint32_t b = 1; b <= len(i); b++) node[off[i] + b - 1] = path[b];
    }
    vector<uint32_t>().swap(order);
    start.assign(nodes + 1, 0);
    for (uint32_t u : node) start[u + 1]++;
    for (uint32_t u = 0; u < nodes; u++) start[u + 1] += start[u];
    ids.resize(pool.size());
    for (uint32_t i = 0; i < n; i++)
        for (uint32_t b = 1; b <= len(i); b++) ids[start[node[off[i] + b - 1]]++] = i;
    for (uint32_t u = nodes; u > 0; u--) start[u] = start[u - 1];
    start[0] = 0;
    size_t blocks = (ids.size() + BLOCK - 1) / BLOCK;
    table.assign(1, vector<uint32_t>(blocks, 0));
    for (size_t k = 0; k < ids.size(); k++)
        table[0][k / BLOCK] = max(table[0][k / BLOCK], len(ids[k]));
    for (size_t h = 1; (size_t(1) << h) <= blocks; h++) {
        table.emplace_back(blocks - (size_t(1) << h) + 1);
        for (size_t k = 0; k < table[h].size(); k++)
            table[h][k] = max(table[h - 1][k], table[h - 1][k + (size_t(1) << (h - 1))]);
    }
}

// no other word has the first a and the last b letters of word i and room for both:
// the words with that prefix are the numbers [lo, hi]
bool unique(uint32_t i, uint32_t a, uint32_t b, uint32_t lo, uint32_t hi) {
    uint32_t u = node[off[i] + b - 1];
    auto from = ids.begin() + start[u], to = ids.begin() + start[u + 1];
    size_t l = lower_bound(from, to, lo) - ids.begin();
    size_t r = upper_bound(from, to, hi) - ids.begin();
    size_t self = lower_bound(from, to, i) - ids.begin();
    return max(longest(l, self), longest(self + 1, r)) < a + b;
}

int main() {
    uint32_t n = 0;
    pool.reserve(MAX_TOTAL);
    int c = readChar();
    while (c < '0' || c > '9') c = readChar();
    for (; c >= '0' && c <= '9'; c = readChar()) n = n * 10 + (c - '0');
    off.assign(n + 1, 0);
    for (uint32_t i = 0; i < n; i++) {
        while (c < 'a' || c > 'z') c = readChar();
        for (; c >= 'a' && c <= 'z'; c = readChar()) pool.push_back((char)c);
        off[i + 1] = (uint32_t)pool.size();
    }
    buildSuffixes(n);
    // last[off[i] + a - 1]: the last word sharing the first a letters of word i
    vector<uint32_t> last(pool.size()), run;
    for (uint32_t i = n; i-- > 0;) {
        uint32_t common = i + 1 < n ? commonPrefix(i, i + 1) : 0;
        run.resize(common + 1);
        run.resize(len(i) + 1, i);
        for (uint32_t a = 1; a <= len(i); a++) last[off[i] + a - 1] = run[a];
    }
    vector<uint32_t>().swap(run);
    vector<uint32_t> first;  // first[a]: the first word sharing the first a letters
    for (uint32_t i = 0; i < n; i++) {
        uint32_t m = len(i);
        uint32_t before = i ? commonPrefix(i - 1, i) : 0;
        uint32_t after = i + 1 < n ? commonPrefix(i, i + 1) : 0;
        first.resize(before + 1);
        first.resize(m + 1, i);
        // the whole word costs m; the shortest unique prefix with a dot costs one more
        uint32_t cost = m, kind = 0, bestA = 0, bestB = 0;
        uint32_t dot = max(before, after) + 1;
        if (dot + 1 < m) cost = dot + 1, kind = 1, bestA = dot;
        // with a hyphen: as the prefix gets shorter, the shortest unique suffix grows
        uint32_t b = 1;
        for (uint32_t a = m - 1; a >= 1; a--) {
            while (b <= m - a && !unique(i, a, b, first[a], last[off[i] + a - 1])) b++;
            if (b <= m - a && a + b + 1 < cost) cost = a + b + 1, kind = 2, bestA = a, bestB = b;
        }
        const char* w = pool.data() + off[i];
        if (kind == 0)
            for (uint32_t k = 0; k < m; k++) writeChar(w[k]);
        else
            for (uint32_t k = 0; k < bestA; k++) writeChar(w[k]);
        if (kind == 1) writeChar('.');
        if (kind == 2) {
            writeChar('-');
            for (uint32_t k = m - bestB; k < m; k++) writeChar(w[k]);
        }
        writeChar('\n');
    }
    fwrite(outBuf, 1, outLen, stdout);
}
