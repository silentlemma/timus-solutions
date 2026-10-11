#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <string>
#include <unordered_map>
#include <vector>

enum { NONE, PAWN, QUEEN, ROOK, BISHOP, KNIGHT };
const int PROMOTIONS[] = {QUEEN, ROOK, BISHOP, KNIGHT};
const int KING[8][2] = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}, {1, 1}, {1, -1}, {-1, 1}, {-1, -1}};
const int JUMPS[8][2] = {{1, 2}, {2, 1}, {2, -1}, {1, -2}, {-1, -2}, {-2, -1}, {-2, 1}, {-1, 2}};
// the double steps start from these rows, counted from 0
const int WHITE_START = 1, EN_PASSANT_ROW = 3;
// the king steps list the four straight directions before the four diagonal ones
const int FIRST_DIAGONAL = 4, DIRECTIONS = 8;
// a square is packed into 5 bits per coordinate in the memo keys
const int SHIFT = 5;

struct Move {
    int kind, bx, by, kx, ky;
};

// a white move: where the pawn lands and what is left of Black's pawn or piece
struct Option {
    int wx, wy, kind, bx, by;
};

int n;
std::unordered_map<long long, bool> memo;

static bool inside(int x, int y) { return x >= 0 && x < n && y >= 0 && y < n; }

// Squares the black piece can reach, ignoring the white pawn.
static void pieceMoves(int kind, int bx, int by, int kx, int ky,
                       std::vector<std::pair<int, int>> &out) {
    if (kind == KNIGHT) {
        for (auto &d : JUMPS) {
            int x = bx + d[0], y = by + d[1];
            if (inside(x, y) && !(x == kx && y == ky)) {
                out.push_back({x, y});
            }
        }
        return;
    }
    // the queen uses all eight rays, the rook the first four, the bishop the last four
    int from = kind == BISHOP ? FIRST_DIAGONAL : 0, to = kind == ROOK ? FIRST_DIAGONAL : DIRECTIONS;
    for (int r = from; r < to; r++) {
        int x = bx + KING[r][0], y = by + KING[r][1];
        while (inside(x, y) && !(x == kx && y == ky)) {
            out.push_back({x, y});
            x += KING[r][0];
            y += KING[r][1];
        }
    }
}

static bool whiteWins(int wx, int wy, int kind, int bx, int by, int kx, int ky);

// Whether White wins against every reply, Black to move.
static bool blackFails(int wx, int wy, int kind, int bx, int by, int kx, int ky) {
    if (std::max(std::abs(kx - wx), std::abs(ky - wy)) == 1) {
        return false; // the king takes the pawn
    }
    if (kind == PAWN && by - 1 == wy && std::abs(bx - wx) == 1) {
        return false;
    }
    std::vector<std::pair<int, int>> squares;
    if (kind != NONE && kind != PAWN) {
        pieceMoves(kind, bx, by, kx, ky, squares);
        for (auto &s : squares) {
            if (s.first == wx && s.second == wy) {
                return false;
            }
        }
    }
    std::vector<Move> moves;
    for (auto &d : KING) {
        int x = kx + d[0], y = ky + d[1];
        // the pawn attacks the two squares diagonally in front of it
        bool attacked = y == wy + 1 && std::abs(x - wx) == 1;
        if (inside(x, y) && !attacked && (kind == NONE || !(x == bx && y == by))) {
            moves.push_back({kind, bx, by, x, y});
        }
    }
    if (kind == PAWN) {
        int ahead = by - 1;
        auto free = [&](int y) { return !(bx == wx && y == wy) && !(bx == kx && y == ky); };
        if (ahead >= 0 && free(ahead)) {
            if (ahead == 0) {
                for (int p : PROMOTIONS) {
                    moves.push_back({p, bx, ahead, kx, ky});
                }
            } else {
                moves.push_back({PAWN, bx, ahead, kx, ky});
                if (by == n - 2 && free(by - 2)) {
                    moves.push_back({PAWN, bx, by - 2, kx, ky});
                }
            }
        }
    } else if (kind != NONE) {
        for (auto &s : squares) {
            moves.push_back({kind, s.first, s.second, kx, ky});
        }
    }
    if (moves.empty()) {
        return false; // nothing to move: the pawn has not promoted
    }
    for (auto &m : moves) {
        if (!whiteWins(wx, wy, m.kind, m.bx, m.by, m.kx, m.ky)) {
            return false;
        }
    }
    return true;
}

static bool whiteWins(int wx, int wy, int kind, int bx, int by, int kx, int ky) {
    long long key = kind;
    for (int v : {wx, wy, bx + 1, by + 1, kx, ky}) {
        key = key << SHIFT | v;
    }
    auto it = memo.find(key);
    if (it != memo.end()) {
        return it->second;
    }
    memo[key] = false;
    auto free = [&](int x, int y) {
        return !(x == kx && y == ky) && !(kind != NONE && x == bx && y == by);
    };
    std::vector<Option> options;
    if (free(wx, wy + 1)) {
        options.push_back({wx, wy + 1, kind, bx, by});
        if (wy == WHITE_START && free(wx, wy + 2)) {
            // a black pawn beside the landing square takes it en passant
            bool beside = kind == PAWN && by == EN_PASSANT_ROW && std::abs(bx - wx) == 1;
            if (!beside) {
                options.push_back({wx, wy + 2, kind, bx, by});
            }
        }
    }
    for (int dx : {-1, 1}) {
        if (kind != NONE && bx == wx + dx && by == wy + 1) {
            options.push_back({wx + dx, wy + 1, NONE, -1, -1});
        }
    }
    bool result = false;
    for (auto &o : options) {
        if (o.wy == n - 1 || blackFails(o.wx, o.wy, o.kind, o.bx, o.by, kx, ky)) {
            result = true;
            break;
        }
    }
    memo[key] = result;
    return result;
}

int main() {
    std::string w, b, k;
    std::cin >> n >> w >> b >> k;
    auto col = [](const std::string &s) { return s[0] - 'a'; };
    auto row = [](const std::string &s) { return std::stoi(s.substr(1)) - 1; };
    bool win = whiteWins(col(w), row(w), PAWN, col(b), row(b), col(k), row(k));
    puts(win ? "WHITE WINS" : "BLACK WINS");
}
