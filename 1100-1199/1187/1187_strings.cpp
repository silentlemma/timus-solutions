#include <algorithm>
#include <iostream>
#include <map>
#include <numeric>
#include <string>
#include <vector>

using std::string;
using std::vector;

const int WIDTH = 6, FULL = 100, NONE = -1, CODE = 3;

struct Question {
    string code, line;
    vector<char> answers;
    vector<string> lines;
};

// percents of total that round each value down or up and add up to 100:
// round all down, then raise the ones with the largest remainders
vector<int> shares(const vector<long long> &values, long long total) {
    vector<int> out(values.size(), NONE);
    if (total == 0) {
        return out;
    }
    vector<long long> rest(values.size());
    int sum = 0;
    for (size_t k = 0; k < values.size(); k++) {
        out[k] = FULL * values[k] / total;
        rest[k] = FULL * values[k] % total;
        sum += out[k];
    }
    vector<int> order(values.size());
    std::iota(order.begin(), order.end(), 0);
    std::stable_sort(order.begin(), order.end(), [&](int a, int b) { return rest[a] > rest[b]; });
    for (int k = 0; k < FULL - sum; k++) {
        out[order[k]]++;
    }
    return out;
}

string cell(const string &s) { return string(WIDTH - s.size(), ' ') + s; }

string percent(int p) { return cell(p == NONE ? "-" : std::to_string(p) + "%"); }

int main() {
    vector<string> lines;
    for (string line; std::getline(std::cin, line);) {
        if (!line.empty() && line.back() == '\r') {
            line.pop_back();
        }
        lines.push_back(line);
    }
    string survey = lines[0];
    size_t at = 1;
    vector<Question> questions;
    std::map<string, int> place;
    for (; lines[at] != "#"; at++) {
        if (lines[at][0] == ' ') {
            questions.back().answers.push_back(lines[at][1]);
            questions.back().lines.push_back(lines[at]);
        } else {
            place[lines[at].substr(0, CODE)] = questions.size();
            questions.push_back({lines[at].substr(0, CODE), lines[at], {}, {}});
        }
    }
    vector<string> results;
    for (at++; lines[at] != "#"; at++) {
        results.push_back(lines[at]);
    }
    bool started = false;
    for (at++; at < lines.size() && lines[at] != "#"; at++) {
        int p1 = place[lines[at].substr(0, CODE)], p2 = place[lines[at].substr(CODE + 1, CODE)];
        const Question &first = questions[p1], &second = questions[p2];
        int rows = first.answers.size(), cols = second.answers.size();
        // the table with its totals as one more column and one more row
        vector<vector<long long>> table(rows + 1, vector<long long>(cols + 1, 0));
        for (const string &line : results) {
            int r = std::find(first.answers.begin(), first.answers.end(), line[p1]) -
                    first.answers.begin();
            int c = std::find(second.answers.begin(), second.answers.end(), line[p2]) -
                    second.answers.begin();
            for (int i : {r, rows}) {
                for (int j : {c, cols}) {
                    table[i][j]++;
                }
            }
        }
        vector<vector<int>> byRow(rows + 1), byCol(rows + 1, vector<int>(cols + 1, NONE));
        for (int i = 0; i <= rows; i++) {
            vector<long long> part(table[i].begin(), table[i].end() - 1);
            byRow[i] = shares(part, table[i][cols]);
            byRow[i].push_back(table[i][cols] ? FULL : NONE);
        }
        for (int j = 0; j <= cols; j++) {
            vector<long long> part;
            for (int i = 0; i < rows; i++) {
                part.push_back(table[i][j]);
            }
            vector<int> got = shares(part, table[rows][j]);
            for (int i = 0; i < rows; i++) {
                byCol[i][j] = got[i];
            }
            byCol[rows][j] = table[rows][j] ? FULL : NONE;
        }
        if (started) {
            std::cout << "\n";
        }
        started = true;
        std::cout << survey << " - " << lines[at].substr(2 * CODE + 2) << "\n";
        for (const Question *q : {&first, &second}) {
            std::cout << q->line << "\n";
            for (const string &line : q->lines) {
                std::cout << line << "\n";
            }
        }
        std::cout << "\n" << string(WIDTH, ' ');
        for (char c : second.answers) {
            std::cout << cell(second.code + ":" + c);
        }
        std::cout << cell("TOTAL") << "\n";
        for (int i = 0; i <= rows; i++) {
            std::cout << cell(i < rows ? first.code + ":" + first.answers[i] : "TOTAL");
            for (long long v : table[i]) {
                std::cout << cell(std::to_string(v));
            }
            std::cout << "\n" << string(WIDTH, ' ');
            for (int p : byRow[i]) {
                std::cout << percent(p);
            }
            std::cout << "\n" << string(WIDTH, ' ');
            for (int p : byCol[i]) {
                std::cout << percent(p);
            }
            std::cout << "\n";
        }
    }
}
