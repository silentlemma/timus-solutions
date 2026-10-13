#include <algorithm>
#include <cstdio>
#include <cstring>
#include <iostream>
#include <string>
#include <vector>

typedef unsigned long long u64;

const int PLAYERS = 3, SUITS = 4, RANKS = 8;
const char *RANK_NAMES[] = {"7", "8", "9", "10", "J", "Q", "K", "A"};
const char SUIT_NAMES[] = "SCDH";
const int CACHE_BITS = 20; // 8 MB of remembered positions, well inside 16 MB
const int SUIT_BITS = 14;  // an owner string of a suit fits in this many bits
const unsigned FULL_SUIT = (1u << RANKS) - 1;
const int KEY_BITS = 64;
const u64 GOLDEN = 0x9E3779B97F4A7C15ull;

// hand[p] holds player p's cards, suit s in bits 8 s .. 8 s + 7, rank upwards
unsigned hand[PLAYERS];
u64 cache[1 << CACHE_BITS];

// the suits play alike and only the order of the cards inside a suit
// matters, so a position is the sorted owner strings of the suits
u64 key(int leader) {
    unsigned code[SUITS];
    for (int s = 0; s < SUITS; s++) {
        unsigned v = 1;
        for (int r = 0; r < RANKS; r++)
            for (int p = 0; p < PLAYERS; p++)
                if (hand[p] >> (s * RANKS + r) & 1)
                    v = v * PLAYERS + p;
        code[s] = v;
    }
    std::sort(code, code + SUITS);
    u64 k = (u64)leader + 1;
    for (int s = 0; s < SUITS; s++)
        k = k << SUIT_BITS | code[s];
    return k;
}

bool survive(int leader);

// cards of player p worth trying: one from each run of touching cards,
// counting as touching two cards with no card of another player between
unsigned choices(int p, unsigned allowed, unsigned all) {
    unsigned out = 0;
    for (int c = 0; c < SUITS * RANKS; c++) {
        if (!(allowed >> c & 1))
            continue;
        int s = c / RANKS;
        unsigned below = all & ((1u << c) - 1) & (FULL_SUIT << (s * RANKS));
        if (below == 0)
            out |= 1u << c;
        else {
            unsigned top = below; // keep only the highest card below c
            while (top & (top - 1))
                top &= top - 1;
            if (!(hand[p] & top))
                out |= 1u << c;
        }
    }
    return out;
}

// plays the card of step `step` of a trick; the first player looks for
// any good card, the other two for any card that catches the first one
bool play(int leader, int step, int suit, int best, int bestPlayer, unsigned all) {
    int p = (leader + step) % PLAYERS;
    unsigned allowed = hand[p];
    if (step > 0 && (allowed & (FULL_SUIT << (suit * RANKS))))
        allowed &= FULL_SUIT << (suit * RANKS);
    unsigned options = choices(p, allowed, all);
    for (int c = 0; c < SUITS * RANKS; c++) {
        if (!(options >> c & 1))
            continue;
        int s = step == 0 ? c / RANKS : suit, b = best, bp = bestPlayer;
        if (step == 0 || (c / RANKS == suit && c > best)) {
            b = c;
            bp = p;
        }
        hand[p] &= ~(1u << c);
        bool ok =
            step + 1 < PLAYERS ? play(leader, step + 1, s, b, bp, all) : bp != 0 && survive(bp);
        hand[p] |= 1u << c;
        if (p == 0 && ok)
            return true;
        if (p != 0 && !ok)
            return false;
    }
    return p != 0;
}

// can the first player take no trick from here, whatever the others do
bool survive(int leader) {
    if (hand[0] == 0)
        return true;
    u64 k = key(leader);
    u64 slot = (k * GOLDEN) >> (KEY_BITS - CACHE_BITS);
    if (cache[slot] >> 1 == k)
        return cache[slot] & 1;
    bool result = play(leader, 0, 0, -1, -1, hand[0] | hand[1] | hand[2]);
    cache[slot] = k << 1 | (result ? 1 : 0);
    return result;
}

int main() {
    for (int p = 0; p < PLAYERS; p++)
        for (int i = 0; i < 10; i++) {
            std::string t;
            if (!(std::cin >> t))
                return 0;
            int s = (int)(strchr(SUIT_NAMES, t.back()) - SUIT_NAMES);
            int r = (int)(std::find(RANK_NAMES, RANK_NAMES + RANKS, t.substr(0, t.size() - 1)) -
                          RANK_NAMES);
            hand[p] |= 1u << (s * RANKS + r);
        }
    int leader = 0;
    if (!(std::cin >> leader))
        return 0;
    puts(survive(leader - 1) ? ";)" : ";(");
    return 0;
}
