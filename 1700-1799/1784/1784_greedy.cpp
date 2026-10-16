#include <iostream>
#include <map>
#include <string>
#include <vector>

const int PILES = 4, RANKS = 13;

int main() {
    std::vector<std::vector<char>> suits(PILES, std::vector<char>(RANKS));
    for (auto &pile : suits) {
        for (char &suit : pile) {
            std::string card;
            if (!(std::cin >> card)) return 0;
            suit = card.back();
        }
    }
    int moves = 0;
    for (int level = 0; level + 1 < RANKS; level++) {
        // once the cards above level j sit in one-suit runs, the run ending at
        // level j of pile i must go onto the card one rank lower in its suit,
        // which lies at level j + 1 of pile target[i]
        std::map<char, int> holder;
        for (int k = 0; k < PILES; k++) holder[suits[k][level + 1]] = k;
        std::vector<int> target(PILES);
        for (int i = 0; i < PILES; i++) target[i] = holder[suits[i][level]];
        // every pile with a change of suit here needs one move, and each cycle
        // of such piles needs one more, to a new pile and back
        std::vector<bool> seen(PILES, false);
        for (int i = 0; i < PILES; i++) {
            if (target[i] == i || seen[i]) continue;
            moves++;
            for (int k = i; !seen[k]; k = target[k]) {
                seen[k] = true;
                moves++;
            }
        }
    }
    std::cout << moves << "\n";
    return 0;
}
