#include <algorithm>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>

using std::string;
using std::vector;

// the cards after which the second player loses the turn: 6, 7, ace, king
// of spades; the face-up card before the first move gets the next index
vector<string> skips;

struct Top {
    char value, suit, announced; // announced is 0 unless it is a queen
    int index;
};

bool covers(const string &card, const Top &top) {
    if (top.announced) {
        return card[1] == top.announced;
    }
    return card[1] == top.suit || card[0] == top.value;
}

vector<string> real;
string last;
int jokers;
vector<char> failed;

Top topOf(int k) { return {skips[k][0], skips[k][1], 0, k}; }

// the cards still to lay after top, or false; every card but the last must
// make the opponent skip, and the last may be anything
bool finish(int mask, int used, const Top &top, vector<string> &out) {
    int rest = real.size() - __builtin_popcount(mask) + jokers - used + !last.empty();
    if (rest == 1) {
        if (!last.empty()) {
            if (!covers(last, top)) {
                return false;
            }
            out.push_back(last[0] == 'Q' ? last + last[1] : last);
            return true;
        }
        if (used < jokers) {
            out.push_back(string("*2") + (top.announced ? top.announced : top.suit));
            return true;
        }
        for (int k = 0; k < (int)real.size(); k++) {
            if (!(mask >> k & 1)) {
                if (!covers(real[k], top)) {
                    return false;
                }
                out.push_back(real[k]);
                return true;
            }
        }
    }
    int key = (mask * (jokers + 1) + used) * (skips.size() + 1) + top.index;
    if (failed[key]) {
        return false;
    }
    for (int k = 0; k < (int)real.size(); k++) {
        if (!(mask >> k & 1) && covers(real[k], top)) {
            int s = 0;
            while (skips[s] != real[k]) {
                s++;
            }
            out.push_back(real[k]);
            if (finish(mask | 1 << k, used, topOf(s), out)) {
                return true;
            }
            out.pop_back();
        }
    }
    if (used < jokers) {
        for (int s = 0; s < (int)skips.size(); s++) {
            if (covers(skips[s], top)) {
                out.push_back("*" + skips[s]);
                if (finish(mask, used + 1, topOf(s), out)) {
                    return true;
                }
                out.pop_back();
            }
        }
    }
    failed[key] = 1;
    return false;
}

int main() {
    for (char v : string("67A")) {
        for (char s : string("SCDH")) {
            skips.push_back(string(1, v) + s);
        }
    }
    skips.push_back("KS");
    string line, word, faceUp;
    std::getline(std::cin, line);
    std::cin >> faceUp;
    faceUp = faceUp.substr(faceUp.find_first_not_of('*'));
    Top top = {faceUp[0], faceUp[1], faceUp[0] == 'Q' ? faceUp[2] : (char)0, (int)skips.size()};
    std::istringstream in(line);
    int others = 0;
    while (in >> word) {
        if (word == "*") {
            jokers++;
        } else if (std::find(skips.begin(), skips.end(), word) != skips.end()) {
            real.push_back(word);
        } else {
            last = word;
            others++;
        }
    }
    if (others > 1) {
        std::cout << "NO\n";
        return 0;
    }
    failed.assign((1 << real.size()) * (jokers + 1) * (skips.size() + 1), 0);
    vector<string> order;
    if (!finish(0, 0, top, order)) {
        std::cout << "NO\n";
        return 0;
    }
    std::cout << "YES\n";
    for (size_t k = 0; k < order.size(); k++) {
        std::cout << order[k] << (k + 1 < order.size() ? " " : "\n");
    }
}
