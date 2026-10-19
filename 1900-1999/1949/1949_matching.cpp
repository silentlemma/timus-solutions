#include <iostream>
#include <string>
#include <vector>

struct Movie {
    int start, finish, count;
};

bool augment(int vertex, const std::vector<std::vector<bool>> &edges, std::vector<int> &own,
             std::vector<int> &other, const std::vector<bool> &active, std::vector<bool> &visited) {
    const int size = static_cast<int>(active.size());
    for (int target = 0; target < size; ++target) {
        if (!edges[vertex][target] || !active[target] || visited[target])
            continue;
        visited[target] = true;
        const int partner = other[target];
        if (partner < 0 || augment(partner, edges, own, other, active, visited)) {
            own[vertex] = target;
            other[target] = vertex;
            return true;
        }
    }
    return false;
}

std::string chooseMovies(const std::vector<Movie> &movies, int students) {
    const int size = static_cast<int>(movies.size());
    std::vector<std::vector<bool>> following(size, std::vector<bool>(size)), preceding = following;
    for (int first = 0; first < size; ++first) {
        for (int second = 0; second < size; ++second) {
            if (movies[first].finish <= movies[second].start &&
                movies[first].count <= movies[second].count) {
                following[first][second] = true;
                preceding[second][first] = true;
            }
        }
    }
    std::vector<int> left(size, -1), right(size, -1);
    std::vector<bool> active(size);
    int chosen = 0, matching = 0;
    std::string answer;
    for (int candidate = 0; candidate < size; ++candidate) {
        const auto oldLeft = left, oldRight = right;
        const int oldMatching = matching;
        std::vector<bool> visited(size);
        matching += augment(candidate, following, left, right, active, visited);
        active[candidate] = true;
        visited.assign(size, false);
        matching += augment(candidate, preceding, right, left, active, visited);
        if (chosen + 1 - matching <= students) {
            answer += '1';
            ++chosen;
        } else {
            answer += '0';
            active[candidate] = false;
            left = oldLeft;
            right = oldRight;
            matching = oldMatching;
        }
    }
    return answer;
}

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);
    int size, students;
    std::cin >> size >> students;
    std::vector<Movie> movies(size);
    for (auto &movie : movies)
        std::cin >> movie.start >> movie.finish >> movie.count;
    std::cout << chooseMovies(movies, students) << '\n';
    return 0;
}
