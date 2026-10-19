#include <algorithm>
#include <array>
#include <deque>
#include <iostream>
#include <string>
#include <utility>
#include <vector>

constexpr int ORIENTATIONS = 4;
using Point = std::pair<int, int>;

struct Transition {
    int player, mask, change, offset;
};

int minimum_passages(int rows, int columns, const std::vector<std::string> &scheme) {
    const int height = rows + 2, width = columns + 2, size = height * width;
    const std::array<Point, ORIENTATIONS> moves{{{-1, 0}, {0, 1}, {1, 0}, {0, -1}}};
    const std::array<int, ORIENTATIONS> offsets{{-width, 1, width, -1}};
    std::vector<unsigned char> outside(size), masks(size);
    std::vector<int> starts;
    for (int position = 0; position < size; ++position) {
        const int row = position / width, column = position % width;
        outside[position] = row == 0 || row == height - 1 || column == 0 || column == width - 1;
    }
    for (int row = 1; row <= rows; ++row) {
        for (int column = 1; column <= columns; ++column) {
            const int position = row * width + column, r = 2 * row - 1, c = 2 * column - 1;
            if (scheme[r][c] == '1' || scheme[r][c] == '2')
                starts.push_back(position);
            const std::array<char, ORIENTATIONS> walls{
                {scheme[r - 1][c], scheme[r][c + 1], scheme[r + 1][c], scheme[r][c - 1]}};
            for (int direction = 0; direction < ORIENTATIONS; ++direction)
                if (walls[direction] == '.')
                    masks[position] |= 1 << direction;
        }
    }
    for (int position = 0; position < size; ++position) {
        if (!outside[position])
            continue;
        const int row = position / width, column = position % width;
        for (int direction = 0; direction < ORIENTATIONS; ++direction) {
            const int nr = row + moves[direction].first, nc = column + moves[direction].second;
            if (nr < 0 || nr >= height || nc < 0 || nc >= width)
                continue;
            const int neighbor = nr * width + nc, opposite = (direction + 2) % ORIENTATIONS;
            if (outside[neighbor] || (masks[neighbor] & (1 << opposite)))
                masks[position] |= 1 << direction;
        }
    }
    const std::array<Point, ORIENTATIONS> relative{{{0, 1}, {1, -1}, {1, 0}, {1, 1}}};
    std::array<int, ORIENTATIONS> deltas{};
    std::array<std::vector<Transition>, ORIENTATIONS> transitions;
    for (int orientation = 0; orientation < ORIENTATIONS; ++orientation) {
        deltas[orientation] = relative[orientation].first * width + relative[orientation].second;
        for (int player = 0; player < 2; ++player) {
            for (int direction = 0; direction < ORIENTATIONS; ++direction) {
                std::array<Point, 2> positions{{{0, 0}, relative[orientation]}};
                positions[player].first += moves[direction].first;
                positions[player].second += moves[direction].second;
                if (positions[1] < positions[0])
                    std::swap(positions[0], positions[1]);
                const Point difference{positions[1].first - positions[0].first,
                                       positions[1].second - positions[0].second};
                const auto found = std::find(relative.begin(), relative.end(), difference);
                if (found == relative.end())
                    continue;
                const int next = static_cast<int>(found - relative.begin());
                const int shift = positions[0].first * width + positions[0].second;
                transitions[orientation].push_back({player, 1 << direction,
                                                    shift * ORIENTATIONS + next - orientation,
                                                    offsets[direction]});
            }
        }
    }
    std::sort(starts.begin(), starts.end());
    const int difference = starts[1] - starts[0];
    const int orientation =
        static_cast<int>(std::find(deltas.begin(), deltas.end(), difference) - deltas.begin());
    const int initial = starts[0] * ORIENTATIONS + orientation;
    std::vector<int> distance(size * ORIENTATIONS, -1);
    std::vector<unsigned char> finished(distance.size());
    std::deque<int> pending{initial};
    distance[initial] = 0;
    while (!pending.empty()) {
        const int state = pending.front();
        pending.pop_front();
        if (finished[state])
            continue;
        finished[state] = 1;
        const int current = distance[state], first = state / ORIENTATIONS;
        const int dir = state % ORIENTATIONS, second = first + deltas[dir];
        if (outside[first] && outside[second])
            return current;
        for (const Transition &action : transitions[dir]) {
            const int position = action.player == 0 ? first : second;
            if (!(masks[position] & action.mask))
                continue;
            const int neighbor = position + action.offset;
            const int cost = outside[position] && outside[neighbor] ? 0 : 1;
            const int following = state + action.change, candidate = current + cost;
            if (distance[following] == -1 || candidate < distance[following]) {
                distance[following] = candidate;
                if (cost == 0)
                    pending.push_front(following);
                else
                    pending.push_back(following);
            }
        }
    }
    return -1;
}

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);
    int rows, columns;
    std::cin >> rows >> columns;
    std::string line;
    std::getline(std::cin, line);
    std::vector<std::string> scheme(2 * rows + 1);
    for (std::string &drawing : scheme) {
        std::getline(std::cin, drawing);
        if (!drawing.empty() && drawing.back() == '\r')
            drawing.pop_back();
    }
    const int answer = minimum_passages(rows, columns, scheme);
    if (answer < 0)
        std::cout << "Death\n";
    else
        std::cout << answer << '\n';
}
