#include <iostream>
#include <string>
#include <vector>

const int EDGE_FACTOR = 3; // a suffix automaton has fewer than 3N edges

struct State {
    int length, link, head;
};
struct Edge {
    int target, following;
    unsigned char letter;
};

struct Automaton {
    std::vector<State> states;
    std::vector<Edge> edges;

    int find(int state, unsigned char ch) const {
        // Each sparse outgoing list has at most the 26 alphabet letters.
        int edge = states[state].head;
        while (edge >= 0 && edges[edge].letter != ch)
            edge = edges[edge].following;
        return edge;
    }

    void add(int state, unsigned char ch, int target) {
        edges.push_back({target, states[state].head, ch});
        states[state].head = int(edges.size()) - 1;
    }

    explicit Automaton(const std::string &text) {
        states.reserve(2 * text.size() + 1);
        edges.reserve(EDGE_FACTOR * text.size());
        states.push_back({0, -1, -1});
        int last = 0;
        for (unsigned char ch : text) {
            int current = states.size();
            states.push_back({states[last].length + 1, 0, -1});
            int state = last;
            while (state >= 0 && find(state, ch) < 0) {
                add(state, ch, current);
                state = states[state].link;
            }
            if (state >= 0) {
                int target = edges[find(state, ch)].target;
                if (states[state].length + 1 == states[target].length)
                    states[current].link = target;
                else {
                    int clone = states.size();
                    states.push_back({states[state].length + 1, states[target].link, -1});
                    // Clone actual edges independently: later redirects can
                    // modify either state's transition destinations.
                    for (int edge = states[target].head; edge >= 0;) {
                        Edge old = edges[edge];
                        add(clone, old.letter, old.target);
                        edge = old.following;
                    }
                    while (state >= 0) {
                        int edge = find(state, ch);
                        if (edge < 0 || edges[edge].target != target)
                            break;
                        edges[edge].target = clone;
                        state = states[state].link;
                    }
                    states[target].link = states[current].link = clone;
                }
            }
            last = current;
        }
    }
};

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);
    int n;
    std::string first, second;
    std::cin >> n >> first >> second;
    Automaton a(first);
    int state = 0, run = 0, best = 0, end = 0;
    for (int i = 0; i < n; i++) {
        int edge = a.find(state, second[i]);
        while (state && edge < 0) {
            state = a.states[state].link;
            run = a.states[state].length;
            edge = a.find(state, second[i]);
        }
        if (edge >= 0) {
            state = a.edges[edge].target;
            run++;
        } else
            run = 0;
        if (run > best) {
            best = run;
            end = i + 1;
        }
    }
    std::cout << second.substr(end - best, best) << '\n';
}
