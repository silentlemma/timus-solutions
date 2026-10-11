#include <iostream>
#include <map>
#include <string>
#include <utility>
#include <vector>

int people = 0;
std::vector<int> adj;
std::vector<int> callerOf; // callee of each caller already busy, or -1

bool place(int person, int informed, int &seen) {
    for (int caller = 0; caller < people; caller++) {
        if ((adj[person] >> caller & 1) && (informed >> caller & 1) && !(seen >> caller & 1)) {
            seen |= 1 << caller;
            if (callerOf[caller] < 0 || place(callerOf[caller], informed, seen)) {
                callerOf[caller] = person;
                return true;
            }
        }
    }
    return false;
}

// who calls whom so that every person in fresh is called by a different
// informed neighbour; empty if that cannot be done
std::vector<std::pair<int, int>> calls(int informed, int fresh) {
    callerOf.assign(people, -1);
    for (int person = 0; person < people; person++) {
        int seen = 0;
        if ((fresh >> person & 1) && !place(person, informed, seen))
            return {};
    }
    std::vector<std::pair<int, int>> plan;
    for (int caller = 0; caller < people; caller++) {
        if (callerOf[caller] >= 0)
            plan.push_back({caller, callerOf[caller]});
    }
    return plan;
}

int main() {
    int n = 0, m = 0;
    std::cin >> n >> m;
    std::map<std::string, int> index;
    std::vector<std::string> names;
    auto id = [&](const std::string &name) {
        if (!index.count(name)) {
            index[name] = (int)names.size();
            names.push_back(name);
        }
        return index[name];
    };
    std::vector<std::pair<int, int>> edges(m);
    for (auto &e : edges) {
        std::string a, b;
        std::cin >> a >> b;
        int ia = id(a);
        e = {ia, id(b)};
    }
    std::string leader;
    std::cin >> leader;
    int start = 1 << id(leader);
    people = (int)names.size();
    adj.assign(people, 0);
    for (auto &e : edges) {
        adj[e.first] |= 1 << e.second;
        adj[e.second] |= 1 << e.first;
    }
    int full = (1 << people) - 1;
    // breadth-first search over the sets of people who know the news
    std::vector<int> from(full + 1, -1);
    std::vector<std::vector<std::pair<int, int>>> how(full + 1);
    std::vector<int> queue = {start};
    from[start] = start;
    for (size_t head = 0; head < queue.size() && from[full] < 0; head++) {
        int informed = queue[head], reach = 0;
        for (int p = 0; p < people; p++) {
            if (informed >> p & 1)
                reach |= adj[p];
        }
        reach &= ~informed;
        for (int fresh = reach; fresh > 0; fresh = (fresh - 1) & reach) {
            int next = informed | fresh;
            if (from[next] >= 0)
                continue;
            std::vector<std::pair<int, int>> plan = calls(informed, fresh);
            if (!plan.empty()) {
                from[next] = informed;
                how[next] = plan;
                queue.push_back(next);
            }
        }
    }
    std::vector<int> path;
    for (int state = full; state != start; state = from[state])
        path.push_back(state);
    std::cout << path.size() << "\n";
    for (auto it = path.rbegin(); it != path.rend(); ++it) {
        std::cout << how[*it].size() << "\n";
        for (auto &call : how[*it])
            std::cout << names[call.first] << " " << names[call.second] << "\n";
    }
    return 0;
}
