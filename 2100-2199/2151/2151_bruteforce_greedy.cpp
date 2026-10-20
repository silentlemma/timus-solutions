#include <array>
#include <iostream>
#include <string>

constexpr int SUITS = 3;
constexpr int RANKS = 9;
constexpr int TYPES = SUITS * RANKS;
constexpr int HAND_SIZE = 14;
constexpr int TRIPLE_SIZE = 3;
constexpr int PAIR_SIZE = 2;

using Counts = std::array<int, TYPES>;

bool triples(Counts counts) {
    for (int tile = 0; tile < TYPES; ++tile) {
        // Three equal sequences can be replaced with three triplets.
        int runs = counts[tile] % TRIPLE_SIZE;
        if (runs == 0) {
            continue;
        }
        if (tile % RANKS > RANKS - TRIPLE_SIZE || counts[tile + 1] < runs ||
            counts[tile + 2] < runs) {
            return false;
        }
        counts[tile + 1] -= runs;
        counts[tile + 2] -= runs;
    }
    return true;
}

bool winning(const Counts &counts) {
    int pair_suit = -1;
    for (int suit = 0; suit < SUITS; ++suit) {
        int total = 0;
        for (int rank = 0; rank < RANKS; ++rank) {
            total += counts[suit * RANKS + rank];
        }
        int remainder = total % TRIPLE_SIZE;
        if (remainder == PAIR_SIZE && pair_suit == -1) {
            pair_suit = suit;
        } else if (remainder != 0) {
            return false;
        }
    }
    if (pair_suit == -1) {
        return false;
    }
    for (int rank = 0; rank < RANKS; ++rank) {
        int tile = pair_suit * RANKS + rank;
        if (counts[tile] >= PAIR_SIZE) {
            Counts rest = counts;
            rest[tile] -= PAIR_SIZE;
            if (triples(rest)) {
                return true;
            }
        }
    }
    return false;
}

std::string classify(Counts counts) {
    if (winning(counts)) {
        return "Tsumo";
    }
    for (int removed = 0; removed < TYPES; ++removed) {
        if (counts[removed] == 0) {
            continue;
        }
        --counts[removed];
        for (int added = 0; added < TYPES; ++added) {
            if (added == removed) {
                continue;
            }
            // A replacement may produce five identical tiles.
            ++counts[added];
            bool ready = winning(counts);
            --counts[added];
            if (ready) {
                return "Tenpai";
            }
        }
        ++counts[removed];
    }
    return "Noten";
}

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);
    Counts counts{};
    for (int i = 0; i < HAND_SIZE; ++i) {
        std::string tile;
        std::cin >> tile;
        int rank = tile[0] - '1';
        int suit = tile[1] - 'a';
        ++counts[suit * RANKS + rank];
    }
    std::cout << classify(counts) << '\n';
}
