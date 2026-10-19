#include <algorithm>
#include <array>
#include <iostream>

constexpr int MOVE_COUNT = 8;
constexpr int PIECE_COUNT = 5;
constexpr std::array<std::array<long long, 2>, MOVE_COUNT> MOVES{
    {{{-2, -1}}, {{-2, 1}}, {{-1, -2}}, {{-1, 2}}, {{1, -2}}, {{1, 2}}, {{2, -1}}, {{2, 1}}}};

std::array<long long, PIECE_COUNT> solve(long long n, long long x, long long y) {
    long long king = (1 + (x > 1) + (x < n)) * (1 + (y > 1) + (y < n)) - 1;
    long long knight = 0;
    for (auto move : MOVES) {
        long long nx = x + move[0], ny = y + move[1];
        if (1 <= nx && nx <= n && 1 <= ny && ny <= n)
            ++knight;
    }
    long long bishop = std::min(x - 1, y - 1) + std::min(x - 1, n - y) + std::min(n - x, y - 1) +
                       std::min(n - x, n - y);
    long long rook = 2 * (n - 1);
    return {king, knight, bishop, rook, rook + bishop};
}

int main() {
    long long n, x, y;
    std::cin >> n >> x >> y;
    auto answer = solve(n, x, y);
    const std::array<const char *, PIECE_COUNT> labels{"King", "Knight", "Bishop", "Rook", "Queen"};
    for (int i = 0; i < PIECE_COUNT; ++i)
        std::cout << labels[i] << ": " << answer[i] << '\n';
}
