#include <algorithm>
#include <iostream>
#include <string>
#include <string_view>

struct Face {
    std::string_view cells;
    bool reversed = false;

    Face left() const {
        const auto half = cells.size() / 2;
        return {cells.substr(reversed ? half : 0, half), reversed};
    }

    Face right_reversed() const {
        const auto half = cells.size() / 2;
        return {cells.substr(reversed ? 0 : half, half), !reversed};
    }
};

constexpr int ALICE = 1, BOB = -1, DRAW = 0;

int play(Face top, Face bottom, bool alice);

int after_fold(Face face, bool top, bool next_alice) {
    // The two visible halves together contain exactly the chosen face.
    if (face.cells.find_first_not_of(face.cells.front()) == std::string_view::npos)
        return face.cells.front() == 'A' ? ALICE : BOB;
    const auto left = face.left();
    const auto right = face.right_reversed();
    return top ? play(left, right, next_alice) : play(right, left, next_alice);
}

int play(Face top, Face bottom, bool alice) {
    if (top.cells.size() % 2 != 0)
        return DRAW;
    const int first = after_fold(top, true, !alice);
    if (first == (alice ? ALICE : BOB))
        return first;
    const int second = after_fold(bottom, false, !alice);
    return alice ? std::max(first, second) : std::min(first, second);
}

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);
    int size;
    std::string top, bottom;
    if (!(std::cin >> size >> top >> bottom))
        return 0;
    const int result = play({top}, {bottom}, true);
    std::cout << (result == ALICE ? "Alice" : result == BOB ? "Bob" : "Draw") << '\n';
}
