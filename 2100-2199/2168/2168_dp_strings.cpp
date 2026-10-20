#include <algorithm>
#include <array>
#include <iostream>
#include <string>
#include <utility>
#include <vector>

using namespace std;

constexpr int ALPHABET = 26;

class SuffixLcp {
    int length;
    int size;
    vector<int> rank;
    vector<int> tree;

  public:
    explicit SuffixLcp(const string &text) : length(static_cast<int>(text.size())), size(1) {
        const int total = length + 1;
        vector<int> symbol(total), order(total), group(total), shifted(total), next(total);
        vector<int> count(max(total, ALPHABET + 1));
        for (int i = 0; i < length; ++i) {
            symbol[i] = text[i] - 'a' + 1;
        }
        for (int value : symbol) {
            ++count[value];
        }
        for (int i = 1; i <= ALPHABET; ++i) {
            count[i] += count[i - 1];
        }
        for (int i = total - 1; i >= 0; --i) {
            order[--count[symbol[i]]] = i;
        }
        int classes = 1;
        for (int i = 1; i < total; ++i) {
            if (symbol[order[i]] != symbol[order[i - 1]]) {
                ++classes;
            }
            group[order[i]] = classes - 1;
        }
        for (int width = 1; width < total && classes < total; width *= 2) {
            fill(count.begin(), count.begin() + classes, 0);
            for (int i = 0; i < total; ++i) {
                shifted[i] = order[i] - width;
                if (shifted[i] < 0) {
                    shifted[i] += total;
                }
                ++count[group[shifted[i]]];
            }
            for (int i = 1; i < classes; ++i) {
                count[i] += count[i - 1];
            }
            for (int i = total - 1; i >= 0; --i) {
                order[--count[group[shifted[i]]]] = shifted[i];
            }
            classes = 1;
            next[order[0]] = 0;
            for (int i = 1; i < total; ++i) {
                int current = order[i];
                int previous = order[i - 1];
                if (group[current] != group[previous] ||
                    group[(current + width) % total] != group[(previous + width) % total]) {
                    ++classes;
                }
                next[current] = classes - 1;
            }
            group.swap(next);
        }
        rank.resize(length);
        for (int i = 0; i < length; ++i) {
            rank[order[i + 1]] = i;
        }
        vector<int> lcp(length);
        int matched = 0;
        for (int i = 0; i < length; ++i) {
            int position = rank[i];
            if (position == 0) {
                matched = 0;
                continue;
            }
            int previous = order[position];
            while (i + matched < length && previous + matched < length &&
                   text[i + matched] == text[previous + matched]) {
                ++matched;
            }
            lcp[position] = matched;
            if (matched > 0) {
                --matched;
            }
        }
        while (size < length) {
            size *= 2;
        }
        tree.assign(size * 2, length);
        for (int i = 0; i < length; ++i) {
            tree[size + i] = lcp[i];
        }
        for (int i = size - 1; i > 0; --i) {
            tree[i] = min(tree[i * 2], tree[i * 2 + 1]);
        }
    }

    int query(int first, int second) const {
        int left = rank[first];
        int right = rank[second];
        if (left > right) {
            swap(left, right);
        }
        left += size + 1;
        right += size + 1;
        int answer = length;
        while (left < right) {
            if (left % 2 == 1) {
                answer = min(answer, tree[left++]);
            }
            if (right % 2 == 1) {
                answer = min(answer, tree[--right]);
            }
            left /= 2;
            right /= 2;
        }
        return answer;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int length;
    string text;
    cin >> length >> text;
    SuffixLcp lcp(text);
    array<vector<pair<int, int>>, ALPHABET> starts;
    array<int, ALPHABET + 1> reach;
    reach.fill(-1);
    int active = ALPHABET + 1;
    int skipped = 0;

    // An optimal choice leaves at most one occurrence of each letter.
    for (int position = 0; position <= length; ++position) {
        while (active <= ALPHABET && reach[active] < position) {
            ++active;
        }
        if (position > 0) {
            skipped = min(skipped + 1, active);
        }
        if (position == length) {
            break;
        }
        int letter = text[position] - 'a';
        int farthest = position;
        for (auto iterator = starts[letter].rbegin(); iterator != starts[letter].rend();
             ++iterator) {
            if (text[iterator->first + farthest - position] != text[farthest]) {
                continue;
            }
            int end = position + lcp.query(iterator->first, position);
            if (end > farthest) {
                int cost = iterator->second;
                reach[cost] = max(reach[cost], end);
                active = min(active, cost);
                farthest = end;
            }
            if (farthest == length) {
                break;
            }
        }
        // Keep each strict improvement over all earlier starts with this letter.
        if (starts[letter].empty() || skipped < starts[letter].back().second) {
            starts[letter].emplace_back(position, skipped);
        }
    }
    cout << length - skipped << '\n';
}
