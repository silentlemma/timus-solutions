#include <cctype>
#include <iostream>
#include <map>
#include <set>
#include <string>
#include <utility>
#include <vector>

// a node: OR, AND, NOT, a constant or a register, with up to two children
enum Kind { OR, AND, NOT, CONST, REG };
struct Node {
    Kind kind;
    int left, right;
    char value;
};

std::vector<std::string> tokens;
std::vector<Node> nodes;
size_t pos = 0;

std::string peek() { return pos < tokens.size() ? tokens[pos] : ""; }

int add(Kind kind, int left, int right, char value) {
    nodes.push_back({kind, left, right, value});
    return (int)nodes.size() - 1;
}

int negation();

int conjunction();

// recursive descent: NOT binds tightest, OR loosest
int disjunction() {
    int node = conjunction();
    while (peek() == "OR") {
        pos++;
        node = add(OR, node, conjunction(), 0);
    }
    return node;
}

int conjunction() {
    int node = negation();
    while (peek() == "AND") {
        pos++;
        node = add(AND, node, negation(), 0);
    }
    return node;
}

int negation() {
    std::string word = tokens[pos++];
    if (word == "NOT")
        return add(NOT, negation(), -1, 0);
    if (word == "(") {
        int node = disjunction();
        pos++;
        return node;
    }
    if (word == "TRUE" || word == "FALSE")
        return add(CONST, -1, -1, word == "TRUE");
    return add(REG, -1, -1, word[0]);
}

bool value(int id, const std::map<char, bool> &reg) {
    const Node &node = nodes[id];
    switch (node.kind) {
    case OR:
        return value(node.left, reg) || value(node.right, reg);
    case AND:
        return value(node.left, reg) && value(node.right, reg);
    case NOT:
        return !value(node.left, reg);
    case CONST:
        return node.value;
    default:
        return reg.at(node.value);
    }
}

int main() {
    std::string expr;
    std::getline(std::cin, expr);
    for (size_t i = 0; i < expr.size();) {
        if (std::isalpha((unsigned char)expr[i])) {
            size_t j = i;
            while (j < expr.size() && std::isalpha((unsigned char)expr[j]))
                j++;
            tokens.push_back(expr.substr(i, j - i));
            i = j;
        } else {
            if (expr[i] == '(' || expr[i] == ')')
                tokens.push_back(std::string(1, expr[i]));
            i++;
        }
    }
    int root = disjunction();
    int n, m, k;
    std::cin >> n >> m >> k;
    std::set<std::pair<int, int>> forks;
    for (int i = 0; i < m; i++) {
        int x, y;
        std::cin >> x >> y;
        forks.insert({x, y});
    }
    std::map<std::pair<int, int>, char> switches;
    for (int i = 0; i < k; i++) {
        int x, y;
        char name;
        std::cin >> x >> y >> name;
        switches[{x, y}] = name;
    }
    std::map<char, bool> reg;
    for (char c = 'A'; c <= 'Z'; c++)
        reg[c] = false;
    int x = 0, y = 0, dx = 1, dy = 0;
    std::string out;
    while (-n <= x && x <= n && -n <= y && y <= n) {
        out += std::to_string(x) + " " + std::to_string(y) + "\n";
        auto sw = switches.find({x, y});
        if (sw != switches.end())
            reg[sw->second] = !reg[sw->second];
        if (forks.count({x, y})) {
            // TRUE turns right, FALSE turns left
            int ndx = value(root, reg) ? dy : -dy;
            int ndy = value(root, reg) ? -dx : dx;
            dx = ndx, dy = ndy;
        }
        x += dx, y += dy;
    }
    std::cout << out;
}
