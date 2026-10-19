#include <cstdint>
#include <iostream>
#include <limits>
#include <vector>

using namespace std;

constexpr int WORD_BITS = numeric_limits<uint64_t>::digits;

int select_bit(uint64_t word, int rank) {
    int position = 0;
    for (int half = WORD_BITS / 2; half > 0; half >>= 1) {
        uint64_t mask = (uint64_t{1} << half) - 1;
        int count = __builtin_popcountll(word & mask);
        if (rank >= count) {
            rank -= count;
            word >>= half;
            position += half;
        } else {
            word &= mask;
        }
    }
    return position;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n, k;
    cin >> n >> k;
    int buckets = (n + WORD_BITS - 1) / WORD_BITS;
    vector<uint64_t> alive(buckets, numeric_limits<uint64_t>::max());
    vector<int> tree(buckets + 1);
    for (int i = 1; i <= buckets; ++i) tree[i] = WORD_BITS * (i & -i);
    int tail = n % WORD_BITS;
    if (tail != 0) {
        alive.back() = (uint64_t{1} << tail) - 1;
        tree.back() -= WORD_BITS - tail;
    }
    int jump = 1;
    while ((jump << 1) <= buckets) jump <<= 1;
    int rank = 0, answer = 0;
    for (int round = 1, remaining = n; remaining > 0; ++round, --remaining) {
        rank = (rank + k - 1) % remaining;
        int bucket = 0, local_rank = rank;
        for (int step = jump; step > 0; step >>= 1) {
            int next = bucket + step;
            if (next <= buckets && tree[next] <= local_rank) {
                bucket = next;
                local_rank -= tree[next];
            }
        }
        int position = select_bit(alive[bucket], local_rank);
        int soldier = bucket * WORD_BITS + position + 1;
        answer ^= round > soldier ? round - soldier : soldier - round;
        alive[bucket] &= ~(uint64_t{1} << position);
        for (int i = bucket + 1; i <= buckets; i += i & -i) --tree[i];
    }
    cout << answer << '\n';
}
