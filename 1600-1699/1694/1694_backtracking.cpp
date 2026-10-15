#include <algorithm>
#include <cstdio>
#include <vector>

int k, longest;
std::vector<int> word;
std::vector<std::vector<long long>> counts;

// whether some k-repetition ends at the last letter of word
bool repetitionAtEnd() {
    int size = word.size();
    for (int block = 1; block * k <= size; block++) {
        int i = size - k * block;
        while (i < size - block && word[i] == word[i + block]) {
            i++;
        }
        if (i == size - block) {
            return true;
        }
    }
    return false;
}

// whether w^k has a k-repetition other than itself; w has none, and w^k
// repeats with period |w|, so only windows that start in the first copy
// and leave it need a look
bool properRepetition() {
    int size = word.size(), total = size * k;
    for (int block = 1; block <= size; block++) {
        int span = k * block;
        for (int start = 0; start < std::min(size, total - span + 1); start++) {
            if (start + span <= size || span == total) {
                continue;
            }
            int i = start, end = start + span - block;
            while (i < end && word[i % size] == word[(i + block) % size]) {
                i++;
            }
            if (i == end) {
                return true;
            }
        }
    }
    return false;
}

void extend(int distinct) {
    // w^k may fail while a longer w still works, so this only skips counting
    if (!word.empty() && !properRepetition()) {
        counts[word.size()][distinct]++;
    }
    if ((int)word.size() == longest) {
        return;
    }
    for (int c = 0; c <= distinct; c++) {
        word.push_back(c);
        // a k-repetition inside w is one inside the killer word too
        if (!repetitionAtEnd()) {
            extend(std::max(distinct, c + 1));
        }
        word.pop_back();
    }
}

int main() {
    int m, n;
    scanf("%d %d %d", &m, &k, &n);
    // a killer word is w repeated k times; whether it works does not depend
    // on which letters w uses, so count the words w with letters numbered in
    // order of first appearance, by their number of different letters
    longest = n / k;
    counts.assign(longest + 1, std::vector<long long>(longest + 1, 0));
    extend(0);
    long long total = 0;
    for (int length = 1; length <= longest; length++) {
        long long ways = 1;
        for (int distinct = 1; distinct <= length; distinct++) {
            ways *= std::max(m - distinct + 1, 0);
            total += counts[length][distinct] * ways;
        }
    }
    printf("%lld\n", total);
}
