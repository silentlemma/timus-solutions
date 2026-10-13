#include <algorithm>
#include <iostream>
#include <set>
#include <string>
#include <vector>

using namespace std;

const int THREE = 3;
const int CARDS = 8, HAND = 3, SLEEVE = 6; // Sasha's, Dima's, then the sleeve
const int FIRST_FACE = 11;                 // J, Q, K, A rank from 11 to 14
const string FACES = "JQKA";
// combinations from the lowest: high card, pair, flush, straight,
// three of a kind, straight flush, three threes
enum { HIGH, PAIR, FLUSH, STRAIGHT, TRIPLE, STRAIGHT_FLUSH, THREE_THREES };

int rank_of(const string &card) {
    string name = card.substr(0, card.size() - 1);
    size_t face = FACES.find(name);
    return face != string::npos && name.size() == 1 ? FIRST_FACE + (int)face : stoi(name);
}

// a key that orders hands from the weakest to the strongest
vector<int> value(const vector<string> &hand) {
    vector<int> r;
    for (auto &c : hand)
        r.push_back(rank_of(c));
    sort(r.rbegin(), r.rend());
    bool flush = hand[0].back() == hand[1].back() && hand[1].back() == hand[2].back();
    bool straight = r[0] == r[1] + 1 && r[1] == r[2] + 1;
    if (r[0] == THREE && r[2] == THREE)
        return {THREE_THREES};
    if (straight && flush)
        return {STRAIGHT_FLUSH, r[0], r[1], r[2]};
    if (r[0] == r[2])
        return {TRIPLE, r[0], r[1], r[2]};
    if (straight)
        return {STRAIGHT, r[0], r[1], r[2]};
    if (flush)
        return {FLUSH, r[0], r[1], r[2]};
    if (r[0] == r[1])
        return {PAIR, r[0], r[2]};
    if (r[1] == r[2])
        return {PAIR, r[1], r[0]};
    return {HIGH, r[0], r[1], r[2]};
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    vector<string> card(CARDS);
    while (cin >> card[0]) {
        for (int i = 1; i < CARDS; i++)
            cin >> card[i];
        vector<string> sasha(card.begin(), card.begin() + HAND);
        vector<string> dima(card.begin() + HAND, card.begin() + SLEEVE);
        vector<string> usable;
        for (int i = SLEEVE; i < CARDS; i++)
            if (find(sasha.begin(), sasha.end(), card[i]) == sasha.end())
                usable.push_back(card[i]);
        // Dima's hands: as dealt, one card swapped, or two swapped for both
        vector<vector<string>> hands = {dima};
        for (auto &c : usable)
            for (int i = 0; i < HAND; i++) {
                vector<string> h = dima;
                h[i] = c;
                hands.push_back(h);
            }
        if (usable.size() == 2)
            for (int keep = 0; keep < HAND; keep++)
                hands.push_back({dima[keep], usable[0], usable[1]});
        vector<int> target = value(sasha);
        bool win = false, draw = false;
        for (auto &h : hands) {
            if ((int)set<string>(h.begin(), h.end()).size() != HAND)
                continue;
            vector<int> v = value(h);
            win = win || v > target;
            draw = draw || v == target;
        }
        cout << (win ? "Dima" : draw ? "Artyom" : "Sasha") << "\n";
    }
}
