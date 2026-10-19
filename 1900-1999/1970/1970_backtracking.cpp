#include <array>
#include <cstdint>
#include <iostream>
#include <stdexcept>
#include <utility>
#include <vector>

constexpr int kPieceSide = 4;
constexpr int kGridSide = 3;
constexpr int kPieceCount = kGridSide * kGridSide;
constexpr int kTurns = 4;
constexpr int kStateCount = kTurns * kPieceCount;
constexpr int kPixels = kPieceSide * kPieceSide;
constexpr int kStride = kPieceSide - 1;
constexpr int kBoardSide = kGridSide * kStride + 1;
using Piece = std::array<int, kPixels>;
using Mask = std::uint64_t;
using Domains = std::array<Mask, kPieceCount>;

struct Solver {
    std::array<Piece, kStateCount> states{};
    std::array<Mask, kPieceCount> masks{};
    std::array<std::array<Mask, kStateCount>, kTurns> compatible{};
    std::array<std::vector<std::pair<int, int>>, kPieceCount> neighbors;
    std::array<int, kPieceCount> placement{};

    bool search(const Domains &domains, int remaining) {
        if (remaining == 0)
            return true;
        int slot = -1, best = kStateCount + 1;
        for (int i = 0; i < kPieceCount; ++i) {
            if (placement[i] >= 0)
                continue;
            int count = __builtin_popcountll(domains[i]);
            if (count < best || (count == best && neighbors[i].size() > neighbors[slot].size())) {
                slot = i;
                best = count;
            }
        }
        Mask choices = domains[slot];
        while (choices != 0) {
            int state = __builtin_ctzll(choices);
            choices &= choices - 1;
            placement[slot] = state;
            Mask unused = ~masks[state / kTurns];
            Domains following = domains;
            for (auto &domain : following)
                domain &= unused;
            for (auto [direction, adjacent] : neighbors[slot])
                if (placement[adjacent] < 0)
                    following[adjacent] &= compatible[direction][state];
            bool possible = true;
            for (int i = 0; i < kPieceCount; ++i)
                if (placement[i] < 0 && following[i] == 0)
                    possible = false;
            if (possible && search(following, remaining - 1))
                return true;
            placement[slot] = -1;
        }
        return false;
    }

    std::array<std::array<int, kBoardSide>, kBoardSide>
    assemble(const std::array<Piece, kPieceCount> &pieces) {
        Mask initial = 0;
        for (int index = 0; index < kPieceCount; ++index) {
            Piece current = pieces[index];
            for (int turn = 0; turn < kTurns; ++turn) {
                int state = index * kTurns + turn;
                states[state] = current;
                masks[index] |= Mask{1} << state;
                bool duplicate = false;
                for (int previous = index * kTurns; previous < state; ++previous)
                    duplicate = duplicate || states[previous] == current;
                if (!duplicate && (index != 0 || turn == 0))
                    initial |= Mask{1} << state;
                Piece rotated{};
                for (int r = 0; r < kPieceSide; ++r)
                    for (int c = 0; c < kPieceSide; ++c)
                        rotated[r * kPieceSide + c] =
                            current[(kPieceSide - 1 - c) * kPieceSide + r];
                current = rotated;
            }
        }
        std::array<std::array<std::array<int, kPieceSide>, kTurns>, kStateCount> edges{};
        for (int state = 0; state < kStateCount; ++state)
            for (int i = 0; i < kPieceSide; ++i) {
                edges[state][0][i] = states[state][i];
                edges[state][1][i] = states[state][i * kPieceSide + kPieceSide - 1];
                edges[state][2][i] = states[state][(kPieceSide - 1) * kPieceSide + i];
                edges[state][kTurns - 1][i] = states[state][i * kPieceSide];
            }
        for (int direction = 0; direction < kTurns; ++direction)
            for (int first = 0; first < kStateCount; ++first)
                for (int second = 0; second < kStateCount; ++second)
                    if (first / kTurns != second / kTurns &&
                        edges[first][direction] == edges[second][(direction + 2) % kTurns])
                        compatible[direction][first] |= Mask{1} << second;
        constexpr std::array<int, kTurns> dr{-1, 0, 1, 0}, dc{0, 1, 0, -1};
        for (int slot = 0; slot < kPieceCount; ++slot)
            for (int direction = 0; direction < kTurns; ++direction) {
                int r = slot / kGridSide + dr[direction];
                int c = slot % kGridSide + dc[direction];
                if (0 <= r && r < kGridSide && 0 <= c && c < kGridSide)
                    neighbors[slot].emplace_back(direction, r * kGridSide + c);
            }
        placement.fill(-1);
        Domains domains{};
        domains.fill(initial);
        if (!search(domains, kPieceCount))
            throw std::runtime_error("The guaranteed arrangement was not found");
        std::array<std::array<int, kBoardSide>, kBoardSide> board{};
        for (int slot = 0; slot < kPieceCount; ++slot)
            for (int r = 0; r < kPieceSide; ++r)
                for (int c = 0; c < kPieceSide; ++c)
                    board[slot / kGridSide * kStride + r][slot % kGridSide * kStride + c] =
                        states[placement[slot]][r * kPieceSide + c];
        return board;
    }
};

int main() {
    std::array<Piece, kPieceCount> pieces{};
    for (auto &piece : pieces)
        for (int &value : piece)
            std::cin >> value;
    Solver solver;
    for (const auto &row : solver.assemble(pieces)) {
        for (int column = 0; column < kBoardSide; ++column)
            std::cout << (column ? " " : "") << row[column];
        std::cout << '\n';
    }
}
