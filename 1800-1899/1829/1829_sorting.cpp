#include <algorithm>
#include <cstdint>
#include <cstdio>
#include <vector>

const int ADDRESS_BITS = 32;
const int64_t FULL = (int64_t(1) << ADDRESS_BITS) - 1;

struct Block {
    int64_t lo, hi, gate;
};

const int BYTE = 8;
const int LONGEST = 15;  // characters in a dotted address

// a dotted address read byte by byte
int64_t address() {
    char text[LONGEST + 1];
    scanf("%15s", text);
    int64_t value = 0, part = 0;
    for (char *c = text;; c++) {
        if (*c == '.' || *c == 0) {
            value = value << BYTE | part;
            part = 0;
            if (*c == 0) return value;
        } else {
            part = part * 10 + (*c - '0');
        }
    }
}

// each row covers one aligned block of addresses, and two blocks are
// nested or apart; sweeping them by start, larger first, with a stack of
// open blocks cuts the line into pieces routed by the innermost one
std::vector<Block> pieces(std::vector<Block> blocks) {
    std::sort(blocks.begin(), blocks.end(), [](const Block &x, const Block &y) {
        return x.lo != y.lo ? x.lo < y.lo : x.hi > y.hi;
    });
    blocks.push_back({FULL + 1, FULL + 1, -1});
    std::vector<Block> out, stack;
    int64_t pos = 0;
    // adjacent pieces with one gateway merge, so equal routing gives
    // equal lists
    auto emit = [&](int64_t lo, int64_t hi, int64_t gate) {
        if (lo > hi) return;
        if (!out.empty() && out.back().hi + 1 == lo && out.back().gate == gate) {
            out.back().hi = hi;
        } else {
            out.push_back({lo, hi, gate});
        }
    };
    for (const Block &b : blocks) {
        while (!stack.empty() && stack.back().hi < b.lo) {
            Block top = stack.back();
            stack.pop_back();
            emit(pos, top.hi, top.gate);
            pos = top.hi + 1;
        }
        if (!stack.empty()) emit(pos, b.lo - 1, stack.back().gate);
        pos = b.lo;
        stack.push_back(b);
    }
    return out;
}

int main() {
    std::vector<Block> tables[2];
    for (auto &table : tables) {
        int count;
        if (scanf("%d", &count) != 1) return 0;
        std::vector<Block> blocks;
        for (int i = 0; i < count; i++) {
            int64_t d = address(), m = address(), g = address();
            blocks.push_back({d & m, (d & m) | (FULL ^ m), g});
        }
        table = pieces(blocks);
    }
    bool same = tables[0].size() == tables[1].size();
    for (size_t i = 0; same && i < tables[0].size(); i++) {
        const Block &x = tables[0][i], &y = tables[1][i];
        same = x.lo == y.lo && x.hi == y.hi && x.gate == y.gate;
    }
    puts(same ? "YES" : "NO");
    return 0;
}
