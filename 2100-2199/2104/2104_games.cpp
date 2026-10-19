#include <algorithm>
#include <iostream>
#include <string>

using namespace std;

constexpr int ALICE = 1, DRAW = 0, BOB = -1;
constexpr int NONE = 2;  // the strip still shows both colours

int winner(const string& top, const string& bottom) {
    for (char colour : {'A', 'B'})
        if (all_of(top.begin(), top.end(), [&](char c) { return c == colour; }) &&
            all_of(bottom.begin(), bottom.end(), [&](char c) { return c == colour; }))
            return colour == 'A' ? ALICE : BOB;
    return NONE;
}

// the result of optimal play from this strip with this player to move
int play(const string& top, const string& bottom, bool alice) {
    size_t n = top.size();
    if (n % 2) return DRAW;
    size_t half = n / 2;
    // folding brings the right half over or under the left one; the faces that
    // end up inside are hidden
    string upper = top.substr(half), lower = bottom.substr(half);
    reverse(upper.begin(), upper.end());
    reverse(lower.begin(), lower.end());
    pair<string, string> folds[] = {{top.substr(0, half), upper}, {lower, bottom.substr(0, half)}};
    int best = NONE;
    for (auto& [newTop, newBottom] : folds) {
        int result = winner(newTop, newBottom);
        if (result == NONE) result = play(newTop, newBottom, !alice);
        if (best == NONE || (alice ? result > best : result < best)) best = result;
        if (best == (alice ? ALICE : BOB)) break;
    }
    return best;
}

int main() {
    ios::sync_with_stdio(false);
    int n;
    string top, bottom;
    cin >> n >> top >> bottom;
    int result = play(top, bottom, true);
    cout << (result == ALICE ? "Alice" : result == BOB ? "Bob" : "Draw") << "\n";
}
