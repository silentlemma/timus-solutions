#include <array>
#include <bitset>
#include <iostream>
#include <string>
#include <vector>

constexpr int MAX_PEOPLE = 400;
using Claims = std::bitset<MAX_PEOPLE>;

std::vector<int> solve(const std::vector<std::string> &locations,
                       const std::vector<Claims> &claims) {
    int n = static_cast<int>(locations.size());
    std::vector<std::vector<int>> graph(n);
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < i; ++j) {
            if (locations[i] != locations[j] && (claims[i] & claims[j]).any()) {
                graph[i].push_back(j);
                graph[j].push_back(i);
            }
        }
    }
    std::vector<int> color(n, -1), answer;
    for (int start = 0; start < n; ++start) {
        if (color[start] != -1)
            continue;
        color[start] = 0;
        std::array<std::vector<int>, 2> sides;
        std::vector<int> pending{start};
        for (std::size_t at = 0; at < pending.size(); ++at) {
            int vertex = pending[at];
            sides[color[vertex]].push_back(vertex);
            for (int target : graph[vertex]) {
                if (color[target] == -1) {
                    color[target] = color[vertex] ^ 1;
                    pending.push_back(target);
                }
            }
        }
        const auto &chosen = sides[sides[0].size() <= sides[1].size() ? 0 : 1];
        answer.insert(answer.end(), chosen.begin(), chosen.end());
    }
    if (answer.empty())
        answer.push_back(0);
    return answer;
}

void run(std::istream &in, std::ostream &out) {
    int n;
    in >> n;
    std::vector<std::string> locations(n);
    std::vector<Claims> claims(n);
    for (int i = 0; i < n; ++i) {
        int count;
        in >> locations[i] >> count;
        claims[i].set(i);
        while (count--) {
            int person;
            in >> person;
            claims[i].set(person - 1);
        }
    }
    auto answer = solve(locations, claims);
    out << answer.size() << '\n';
    for (std::size_t i = 0; i < answer.size(); ++i)
        out << (i ? " " : "") << answer[i] + 1;
    out << '\n';
}

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);
    run(std::cin, std::cout);
    return 0;
}
