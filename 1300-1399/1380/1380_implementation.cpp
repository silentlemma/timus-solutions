#include <cstdlib>
#include <iostream>
#include <string>
#include <vector>

const int SIZE = 8;
const int PAWN = 1, KNIGHT = 2, BISHOP = 3, ROOK = 4, QUEEN = 5, KING = 6;
const int TO_FILE = 3, TO_RANK = 4; // a move reads like e2-e4

// row r is rank r + 1, column f is file a + f
int board[SIZE][SIZE];

bool inside(int f, int r) { return 0 <= f && f < SIZE && 0 <= r && r < SIZE; }

int sign(int x) { return (x > 0) - (x < 0); }

// can the piece on (f, r) move to (tf, tr), ignoring checks
bool reaches(int f, int r, int tf, int tr) {
    int piece = board[r][f], target = board[tr][tf];
    int side = sign(piece), kind = std::abs(piece);
    int df = tf - f, dr = tr - r;
    if ((df == 0 && dr == 0) || target * side > 0)
        return false;
    if (kind == PAWN) {
        int home = side > 0 ? 1 : SIZE - 2; // a pawn may step two squares from here
        if (df == 0 && target == 0)
            return dr == side || (dr == 2 * side && r == home && board[r + side][f] == 0);
        return std::abs(df) == 1 && dr == side && target * side < 0;
    }
    if (kind == KNIGHT)
        return std::abs(df * dr) == 2;
    if (kind == KING)
        return std::abs(df) <= 1 && std::abs(dr) <= 1;
    bool straight = df == 0 || dr == 0, diagonal = std::abs(df) == std::abs(dr);
    if (!((kind == BISHOP && diagonal) || (kind == ROOK && straight) ||
          (kind == QUEEN && (straight || diagonal))))
        return false;
    int sf = sign(df), sr = sign(dr);
    for (f += sf, r += sr; f != tf || r != tr; f += sf, r += sr)
        if (board[r][f])
            return false;
    return true;
}

// is any king of this side attacked
bool inCheck(int side) {
    for (int kr = 0; kr < SIZE; kr++)
        for (int kf = 0; kf < SIZE; kf++)
            if (board[kr][kf] == KING * side)
                for (int r = 0; r < SIZE; r++)
                    for (int f = 0; f < SIZE; f++)
                        if (board[r][f] * side < 0 && reaches(f, r, kf, kr))
                            return true;
    return false;
}

// makes the move if it is legal; `taken` gets the piece it took
bool legal(int side, int f, int r, int tf, int tr, int &taken) {
    if (!inside(f, r) || !inside(tf, tr) || board[r][f] * side <= 0 || !reaches(f, r, tf, tr))
        return false;
    taken = board[tr][tf];
    board[tr][tf] = board[r][f];
    board[r][f] = 0;
    if (inCheck(side)) {
        board[r][f] = board[tr][tf];
        board[tr][tf] = taken;
        return false;
    }
    return true;
}

bool hasMove(int side) {
    for (int r = 0; r < SIZE; r++)
        for (int f = 0; f < SIZE; f++)
            if (board[r][f] * side > 0)
                for (int tr = 0; tr < SIZE; tr++)
                    for (int tf = 0; tf < SIZE; tf++) {
                        int taken = 0;
                        if (legal(side, f, r, tf, tr, taken)) {
                            board[r][f] = board[tr][tf];
                            board[tr][tf] = taken;
                            return true;
                        }
                    }
    return false;
}

int main() {
    for (int r = SIZE - 1; r >= 0; r--)
        for (int f = 0; f < SIZE; f++)
            std::cin >> board[r][f];
    int count = 0;
    std::string who;
    std::cin >> count >> who;
    int side = who == "White" ? 1 : -1;
    std::string out;
    for (int i = 0; i < count; i++) {
        std::string move;
        std::cin >> move;
        int f = move[0] - 'a', r = move[1] - '1', tf = move[TO_FILE] - 'a',
            tr = move[TO_RANK] - '1';
        int taken = 0;
        if (!legal(side, f, r, tf, tr, taken)) {
            out += "Incorrect\n";
            break;
        }
        side = -side;
        bool check = inCheck(side), free = hasMove(side);
        out += !free ? (check ? "Mate\n" : "Draw\n") : (check ? "Check\n" : "Correct\n");
        if (!free)
            break;
    }
    out += "\n";
    for (int r = SIZE - 1; r >= 0; r--)
        for (int f = 0; f < SIZE; f++)
            out += std::to_string(board[r][f]) + (f + 1 < SIZE ? " " : "\n");
    std::cout << out;
    return 0;
}
