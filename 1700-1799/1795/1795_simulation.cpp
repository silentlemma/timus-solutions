#include <deque>
#include <iostream>
#include <map>
#include <string>

struct Customer {
    std::string product;
    int wanted;
    int seen;  // the amount told at the last visit, -1 before the first
};

int main() {
    std::map<std::string, int> stock;
    int m;
    if (!(std::cin >> m)) return 0;
    for (int i = 0; i < m; i++) {
        int amount;
        std::string of, name;
        std::cin >> amount >> of >> name;
        stock[name] = amount;
    }
    int n;
    std::cin >> n;
    std::deque<Customer> line;
    for (int i = 0; i < n; i++) {
        int amount;
        std::string of, name;
        std::cin >> amount >> of >> name;
        line.push_back({name, amount, -1});
    }
    int minutes = 0;
    while (!line.empty()) {
        Customer c = line.front();
        line.pop_front();
        minutes++;
        int &left = stock[c.product];
        if (left >= c.wanted) {
            left -= c.wanted;
        } else if (left == c.seen) {
            left = 0;  // the same rest as before the call: take it all
        } else if (left > 0) {
            // let the next one forward and call home; if the next one is
            // the last of the line, it is Mark's turn
            c.seen = left;
            if (line.empty()) break;
            line.insert(line.begin() + 1, c);
        }
    }
    std::cout << minutes << "\n";
    return 0;
}
