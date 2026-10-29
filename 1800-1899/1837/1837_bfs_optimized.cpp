#include <cstdio>
#include <map>
#include <string>
#include <vector>

int main() {
    constexpr int TEAM_SIZE = 3;
    constexpr int MAX_NAME = 20;
    int teams;
    std::scanf("%d", &teams);
    // every name gets a number; the ordered map keeps the output sorted
    std::map<std::string, int> ids;
    std::vector<std::vector<int>> mates;
    for (int t = 0; t < teams; ++t) {
        int team[TEAM_SIZE];
        for (int &id : team) {
            // names are at most MAX_NAME letters, so a fixed buffer is enough
            char name[MAX_NAME + 1];
            std::scanf("%20s", name);
            auto entry = ids.emplace(name, static_cast<int>(ids.size()));
            id = entry.first->second;
            if (entry.second)
                mates.emplace_back();
        }
        for (int a : team)
            for (int b : team)
                if (a != b)
                    mates[a].push_back(b);
    }
    // breadth-first search from the champion over shared teams
    std::vector<int> distance(ids.size(), -1);
    std::vector<int> queue;
    queue.reserve(ids.size());
    auto source = ids.find("Isenbaev");
    if (source != ids.end()) {
        distance[source->second] = 0;
        queue.push_back(source->second);
    }
    // a vertex is marked when it is queued, so repeated teams add no work
    for (std::size_t head = 0; head < queue.size(); ++head) {
        int current = queue[head];
        for (int next : mates[current]) {
            if (distance[next] == -1) {
                distance[next] = distance[current] + 1;
                queue.push_back(next);
            }
        }
    }
    for (const auto &entry : ids) {
        std::printf("%s ", entry.first.c_str());
        int value = distance[entry.second];
        if (value == -1)
            std::puts("undefined");
        else
            std::printf("%d\n", value);
    }
}
