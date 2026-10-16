#include <iostream>
#include <string>
#include <unordered_map>
#include <utility>
#include <vector>

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);
    int groups, pots;
    if (!(std::cin >> groups >> pots)) return 0;
    // each team is an edge from its pot to its party; a colouring of the
    // edges with one colour per group, never repeated at a vertex, is an
    // answer
    std::vector<std::string> team(groups * pots);
    std::vector<int> pot(groups * pots), party(groups * pots);
    std::unordered_map<std::string, int> partyId;
    std::vector<int> size;
    for (int e = 0; e < groups * pots; e++) {
        std::string name;
        std::cin >> team[e] >> name;
        auto it = partyId.find(name);
        if (it == partyId.end()) {
            it = partyId.emplace(name, (int)size.size()).first;
            size.push_back(0);
        }
        pot[e] = e / groups;
        party[e] = it->second;
        size[party[e]]++;
    }
    for (int s : size) {
        if (s > groups) {
            std::cout << "No\n";
            return 0;
        }
    }
    // atPot[u * groups + c], atParty[v * groups + c]: the edge of colour c
    std::vector<int> atPot(pots * groups, -1), atParty(size.size() * groups, -1);
    std::vector<int> colour(groups * pots, -1), path;
    auto paint = [&](int e, int c) {
        colour[e] = c;
        atPot[pot[e] * groups + c] = e;
        atParty[party[e] * groups + c] = e;
    };
    for (int e = 0; e < groups * pots; e++) {
        int u = pot[e], v = party[e], a = 0, b = 0;
        while (atPot[u * groups + a] != -1) a++;
        while (atParty[v * groups + b] != -1) b++;
        // colour a is free at the pot and b at the party; swap a and b along
        // the path from the pot that alternates b and a, which cannot reach
        // the party, and b becomes free at both ends
        path.clear();
        int at = u, want = b;
        bool onPot = true;
        while (a != b) {
            int next = onPot ? atPot[at * groups + want] : atParty[at * groups + want];
            if (next == -1) break;
            path.push_back(next);
            at = onPot ? party[next] : pot[next];
            onPot = !onPot;
            want = want == a ? b : a;
        }
        for (int f : path) {
            atPot[pot[f] * groups + colour[f]] = -1;
            atParty[party[f] * groups + colour[f]] = -1;
        }
        for (int f : path) paint(f, colour[f] == a ? b : a);
        paint(e, b);
    }
    std::vector<std::vector<int>> members(groups, std::vector<int>(pots));
    for (int e = 0; e < groups * pots; e++) members[colour[e]][pot[e]] = e;
    std::string out = "Yes\n";
    for (const auto &group : members) {
        out += "\n";
        for (int e : group) out += team[e] + "\n";
    }
    std::cout << out;
    return 0;
}
