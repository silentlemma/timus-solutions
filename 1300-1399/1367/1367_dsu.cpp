#include <algorithm>
#include <iostream>
#include <set>
#include <string>
#include <tuple>
#include <vector>

std::vector<int> parent;

int find(int x) {
    while (parent[x] != x) {
        parent[x] = parent[parent[x]];
        x = parent[x];
    }
    return x;
}

void unite(int a, int b) {
    a = find(a);
    b = find(b);
    if (a != b)
        parent[a] = b;
}

int main() {
    std::vector<std::string> pic;
    std::string line;
    while (std::getline(std::cin, line)) {
        if (!line.empty() && line.back() == '\r')
            line.pop_back();
        pic.push_back(line);
    }
    while (!pic.empty() && pic.back().empty())
        pic.pop_back();
    int h = (int)pic.size(), w = 0;
    for (const std::string &row : pic)
        w = std::max(w, (int)row.size());
    // walls run along the middle lines of the cells, so the four quarters
    // around a corner of the grid always meet: the corners are the places
    // an agent can be, and a cell joins some of its four corners
    int side = w + 1;
    parent.resize((size_t)(h + 1) * side);
    for (size_t i = 0; i < parent.size(); i++)
        parent[i] = (int)i;
    std::vector<std::tuple<int, int, int>> secrets; // row, minus column, top-left corner
    for (int r = 0; r < h; r++) {
        int top = r * side, bottom = (r + 1) * side;
        for (int c = 0; c < (int)pic[r].size(); c++) {
            char ch = pic[r][c];
            if (ch == '.') {
                unite(top + c, top + c + 1);
                unite(top + c, bottom + c);
                unite(top + c, bottom + c + 1);
            } else if (ch == '-') { // keeps the upper and the lower pair apart
                unite(top + c, top + c + 1);
                unite(bottom + c, bottom + c + 1);
            } else if (ch == '|') { // keeps the left and the right pair apart
                unite(top + c, bottom + c);
                unite(top + c + 1, bottom + c + 1);
            } else if (ch == '#') { // numbered from the right within a row
                secrets.emplace_back(r, -c, top + c);
            }
        }
    }
    std::sort(secrets.begin(), secrets.end());
    // an agent may not pass through a secret, so two secrets are joined when
    // some corner of one shares a region with some corner of the other
    std::vector<std::set<int>> regions;
    for (const auto &s : secrets) {
        int corner = std::get<2>(s);
        regions.push_back(
            {find(corner), find(corner + 1), find(corner + side), find(corner + side + 1)});
    }
    std::string out;
    for (const auto &a : regions) {
        for (const auto &b : regions) {
            bool shared = false;
            for (int v : a)
                shared = shared || b.count(v) > 0;
            out += shared ? '1' : '0';
        }
        out += '\n';
    }
    std::cout << out;
    return 0;
}
