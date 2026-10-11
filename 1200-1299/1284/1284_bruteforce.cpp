#include <algorithm>
#include <cstdio>
#include <set>
#include <utility>
#include <vector>

const int TOP = 101; // card values are 1..100
const int SUITS = 11;

int main() {
    int n;
    scanf("%d", &n);
    std::vector<std::pair<int, int>> cards(n);
    std::set<int> blueSet, yellowSet;
    for (auto &c : cards) {
        scanf("%d %d", &c.first, &c.second);
        (c.second % 2 ? blueSet : yellowSet).insert(c.second);
    }
    std::vector<int> blue(blueSet.begin(), blueSet.end()),
        yellow(yellowSet.begin(), yellowSet.end());
    // who starts: the larger colour group, or either when they are equal
    std::vector<std::pair<std::vector<int>, std::vector<int>>> starts;
    if (blue.size() >= yellow.size())
        starts.push_back({blue, yellow});
    if (yellow.size() >= blue.size())
        starts.push_back({yellow, blue});
    int best = 0;
    for (auto &[first, second] : starts) {
        std::vector<int> a = first;
        do {
            std::vector<int> b = second;
            do {
                int place[SUITS];
                for (size_t i = 0; i < a.size(); i++)
                    place[a[i]] = 2 * i;
                for (size_t i = 0; i < b.size(); i++)
                    place[b[i]] = 2 * i + 1;
                for (int sign : {1, -1}) {
                    // cards that stay form an increasing run of target ranks
                    std::vector<int> tails;
                    for (auto &[value, suit] : cards) {
                        int rank = place[suit] * TOP + sign * value;
                        auto it = std::lower_bound(tails.begin(), tails.end(), rank);
                        if (it == tails.end())
                            tails.push_back(rank);
                        else
                            *it = rank;
                    }
                    best = std::max(best, (int)tails.size());
                }
            } while (std::next_permutation(b.begin(), b.end()));
        } while (std::next_permutation(a.begin(), a.end()));
    }
    printf("%d\n", n - best);
}
