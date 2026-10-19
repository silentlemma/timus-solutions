#include <algorithm>
#include <iostream>
#include <sstream>
#include <string>
#include <unordered_map>
#include <vector>

using namespace std;

const vector<string> STREETS = {"preflop", "flop", "turn", "river"};

struct Game {
    vector<int> stacks, bets;
    vector<bool> folded, pending;
    int count, dealer, current, street = 0, cursor;

    Game(vector<int> initial, int button, int small, int big, int ante)
        : stacks(initial), bets(initial.size()), folded(initial.size()), pending(initial.size()),
          count(static_cast<int>(initial.size())), dealer(button), current(big) {
        for (int &stack : stacks) {
            stack = max(0, stack - ante);
        }
        int small_seat = count == 2 ? dealer : (dealer + 1) % count;
        int big_seat = (small_seat + 1) % count;
        for (auto post : {pair<int, int>{small_seat, small}, {big_seat, big}}) {
            int paid = min(stacks[post.first], post.second);
            stacks[post.first] -= paid;
            bets[post.first] = paid;
        }
        reset_pending();
        cursor = (big_seat + 1) % count;
    }

    void reset_pending() {
        for (int seat = 0; seat < count; ++seat) {
            pending[seat] = !folded[seat] && stacks[seat] > 0;
        }
    }

    void deal() {
        ++street;
        current = 0;
        fill(bets.begin(), bets.end(), 0);
        reset_pending();
        cursor = (dealer + 1) % count;
    }

    void play(int seat, const string &action, int paid) {
        if (action == "folds") {
            folded[seat] = true;
        } else {
            stacks[seat] -= paid;
            bets[seat] += paid;
            if (bets[seat] > current) {
                current = bets[seat];
                reset_pending();
            }
        }
        pending[seat] = false;
        cursor = (seat + 1) % count;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int small, big, ante, count, dealer, bot;
    cin >> small >> big >> ante >> count >> dealer >> bot;
    --dealer;
    --bot;
    string target_name;
    cin >> target_name;
    int target =
        static_cast<int>(find(STREETS.begin(), STREETS.end(), target_name) - STREETS.begin());
    vector<string> names(count);
    vector<int> initial(count);
    unordered_map<string, int> indices;
    for (int seat = 0; seat < count; ++seat) {
        cin >> names[seat] >> initial[seat];
        indices[names[seat]] = seat;
    }
    Game game(initial, dealer, small, big, ante);
    int known;
    cin >> known;
    string line;
    getline(cin, line);
    for (int step = 0; step < known; ++step) {
        getline(cin, line);
        istringstream input(line);
        string name, action;
        input >> name >> action;
        if (name == "dealing") {
            game.deal();
            continue;
        }
        int seat = indices[name];
        int paid = 0;
        if (action == "raises") {
            int increase, total;
            string to;
            input >> increase >> to >> total;
            paid = total - game.bets[seat];
        } else if (action == "calls" || action == "bets") {
            input >> paid;
        }
        game.play(seat, action, paid);
    }
    vector<int> final(count);
    for (int &stack : final) {
        cin >> stack;
    }
    vector<string> answer;
    while (true) {
        if (none_of(game.pending.begin(), game.pending.end(), [](bool value) { return value; })) {
            game.deal();
            answer.push_back("dealing " + STREETS[game.street]);
        }
        while (!game.pending[game.cursor]) {
            game.cursor = (game.cursor + 1) % count;
        }
        int seat = game.cursor;
        if (seat == bot && game.street == target && game.stacks == final) {
            break;
        }
        int paid = game.stacks[seat] - final[seat];
        // A completed street cannot contain a raise after the bot's last action.
        if (game.street < target && seat != bot) {
            paid = min(paid, game.current - game.bets[seat]);
        }
        int total = game.bets[seat] + paid;
        string action, text;
        if (paid == 0) {
            action = total == game.current ? "checks" : "folds";
            text = action;
        } else if (game.current == 0) {
            action = "bets";
            text = "bets " + to_string(paid);
        } else if (total > game.current) {
            action = "raises";
            text = "raises " + to_string(total - game.current) + " to " + to_string(total);
        } else {
            action = "calls";
            text = "calls " + to_string(paid);
        }
        answer.push_back(names[seat] + " " + text);
        game.play(seat, action, paid);
    }
    cout << answer.size() << '\n';
    for (const string &action : answer) {
        cout << action << '\n';
    }
}
