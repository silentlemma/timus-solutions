#include <algorithm>
#include <array>
#include <iostream>
#include <memory>
#include <string>
#include <unordered_set>
#include <utility>
#include <vector>

constexpr int LETTERS = 26;
constexpr int ALPHABET = LETTERS + 1;
constexpr int NO_STATE = -1;

struct State {
    std::array<int, ALPHABET> next{};
    int length = 0;
    int link = NO_STATE;
    int negative;
    int favorite;
    int missing = 1;
    std::unique_ptr<std::unordered_set<int>> documents;

    State(int negative_limit, int position_limit)
        : negative(negative_limit), favorite(position_limit) {}
};

class Automaton {
  public:
    std::vector<State> states;

    Automaton(int total_length, int team_count)
        : team_limit(team_count), position_limit(total_length) {
        states.reserve(2 * total_length + 1);
        add_state(0);
    }

    int extend(int last, int character) {
        int target = states[last].next[character];
        if (target != 0) {
            if (states[target].length == states[last].length + 1) {
                return target;
            }
            int clone = clone_state(target, states[last].length + 1);
            redirect(last, character, target, clone);
            states[target].link = clone;
            return clone;
        }

        int current = add_state(states[last].length + 1);
        int parent = last;
        while (parent != NO_STATE && states[parent].next[character] == 0) {
            states[parent].next[character] = current;
            parent = states[parent].link;
        }
        if (parent == NO_STATE) {
            states[current].link = 0;
        } else {
            target = states[parent].next[character];
            if (states[target].length == states[parent].length + 1) {
                states[current].link = target;
            } else {
                int clone = clone_state(target, states[parent].length + 1);
                redirect(parent, character, target, clone);
                states[target].link = clone;
                states[current].link = clone;
            }
        }
        return current;
    }

  private:
    int team_limit;
    int position_limit;

    int add_state(int length) {
        int index = static_cast<int>(states.size());
        states.emplace_back(team_limit, position_limit);
        states.back().length = length;
        return index;
    }

    int clone_state(int source, int length) {
        int clone = add_state(length);
        states[clone].next = states[source].next;
        states[clone].link = states[source].link;
        return clone;
    }

    void redirect(int parent, int character, int target, int replacement) {
        while (parent != NO_STATE && states[parent].next[character] == target) {
            states[parent].next[character] = replacement;
            parent = states[parent].link;
        }
    }
};

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);

    int team_count;
    std::cin >> team_count;
    std::vector<std::string> names(team_count);
    std::vector<bool> positive(team_count);
    int total_length = 0;
    int maximum_length = 0;
    for (int team = 0; team < team_count; ++team) {
        std::cin >> names[team];
        positive[team] = names[team].back() == '+';
        if (positive[team]) {
            names[team].pop_back();
        }
        int length = static_cast<int>(names[team].size());
        total_length += length;
        maximum_length = std::max(maximum_length, length);
    }

    Automaton automaton(total_length, team_count);
    auto &states = automaton.states;
    std::vector<int> positive_times;
    for (int team = 0; team < team_count; ++team) {
        int document = static_cast<int>(positive_times.size());
        if (positive[team]) {
            positive_times.push_back(team);
        }
        int last = 0;
        int position = 0;
        for (char character : names[team]) {
            int letter = character == '_' ? LETTERS : character - 'a';
            last = automaton.extend(last, letter);
            State &state = states[last];
            if (team == 0) {
                state.favorite = std::min(state.favorite, position);
            } else if (positive[team]) {
                if (!state.documents) {
                    state.documents = std::make_unique<std::unordered_set<int>>();
                }
                state.documents->insert(document);
            } else {
                state.negative = std::min(state.negative, team);
            }
            ++position;
        }
    }
    positive_times.push_back(team_count);

    std::vector<int> counts(maximum_length + 1);
    for (const State &state : states) {
        ++counts[state.length];
    }
    for (int length = 1; length <= maximum_length; ++length) {
        counts[length] += counts[length - 1];
    }
    std::vector<int> order(states.size());
    for (int index = 0; index < static_cast<int>(states.size()); ++index) {
        order[--counts[states[index].length]] = index;
    }

    const std::pair<int, int> absent(total_length + 1, total_length);
    std::vector<std::pair<int, int>> best(team_count + 1, absent);
    for (int index = static_cast<int>(order.size()) - 1; index > 0; --index) {
        State &state = states[order[index]];
        if (state.documents) {
            while (state.documents->count(state.missing) != 0) {
                ++state.missing;
            }
        }
        State &parent = states[state.link];
        if (state.favorite != total_length) {
            int length = parent.length + 1;
            int left = state.favorite - length + 1;
            int expiration = std::min(state.negative, positive_times[state.missing]);
            best[expiration] = std::min(best[expiration], std::make_pair(length, left));
        }

        // Suffix-link subtrees contain exactly the occurrences of each state.
        parent.negative = std::min(parent.negative, state.negative);
        parent.favorite = std::min(parent.favorite, state.favorite);
        parent.missing = std::max(parent.missing, state.missing);
        if (state.documents) {
            if (!parent.documents || parent.documents->size() < state.documents->size()) {
                parent.documents.swap(state.documents);
            }
            if (state.documents) {
                parent.documents->insert(state.documents->begin(), state.documents->end());
                state.documents.reset();
            }
        }
    }

    std::pair<int, int> answer = absent;
    std::vector<std::pair<int, int>> answers(team_count);
    for (int team = team_count - 1; team >= 0; --team) {
        answer = std::min(answer, best[team + 1]);
        answers[team] = answer;
    }
    for (const auto &result : answers) {
        if (result == absent) {
            std::cout << "-1 -1\n";
        } else {
            std::cout << result.second << ' ' << result.second + result.first - 1 << '\n';
        }
    }
}
