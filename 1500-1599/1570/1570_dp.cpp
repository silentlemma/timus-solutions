#include <algorithm>
#include <cstdio>
#include <iostream>
#include <string>
#include <vector>
using namespace std;

const int SCALE = 1000;            // satiety has at most three digits after the point
const long long MOST_DISHES = 128; // more than the number of different dishes
const long long NONE = 1LL << 62;
const int DIGITS = 3;

int thousandths(const string &text) {
    size_t point = text.find('.');
    string whole = text.substr(0, point),
           part = point == string::npos ? "" : text.substr(point + 1);
    return stoi(whole) * SCALE + stoi((part + "000").substr(0, DIGITS));
}

int main() {
    int n, m;
    cin >> n >> m;
    vector<string> names(n);
    vector<int> price(n), fill(n);
    for (int i = 0; i < n; i++) {
        string f;
        cin >> names[i] >> price[i] >> f;
        fill[i] = thousandths(f);
    }
    int top = m * SCALE;
    // best[s]: the least cost, then the most different dishes, of an order with
    // satiety s, where s = top stands for top or more; one number holds both,
    // cost * MOST_DISHES - dishes, so that smaller is better
    vector<long long> best(top + 1, NONE), mine(top + 1);
    best[0] = 0;
    // per dish: whether the best order at s takes it, and in the orders
    // that take it, the satiety before the last plate and if that plate was the
    // first one, which leaves the orders without the dish
    vector<vector<char>> took(n, vector<char>(top + 1, 0)), first(n, vector<char>(top + 1, 0));
    vector<vector<int>> back(n, vector<int>(top + 1, 0));
    for (int i = 0; i < n; i++) {
        long long step = price[i] * MOST_DISHES;
        fill_n(mine.begin(), top + 1, NONE);
        for (int s = 0; s <= top; s++) {
            int t = min(top, s + fill[i]);
            if (best[s] < NONE && best[s] + step - 1 < mine[t])
                mine[t] = best[s] + step - 1, back[i][t] = s, first[i][t] = 1;
        }
        // more plates of the same dish, from lower satiety up
        for (int s = 0; s < top; s++) {
            int t = min(top, s + fill[i]);
            if (mine[s] < NONE && mine[s] + step < mine[t])
                mine[t] = mine[s] + step, back[i][t] = s, first[i][t] = 0;
        }
        for (int s = 0; s <= top; s++)
            if (mine[s] < best[s])
                best[s] = mine[s], took[i][s] = 1;
    }
    // walk back from the full order, dish by dish from the last one
    vector<int> plates(n, 0);
    int s = top;
    for (int i = n - 1; i >= 0; i--)
        if (took[i][s]) {
            bool done = false;
            while (!done) {
                plates[i]++;
                done = first[i][s];
                s = back[i][s];
            }
        }
    long long cost = 0;
    for (int i = 0; i < n; i++)
        cost += (long long)price[i] * plates[i];
    printf("%lld\n", cost);
    for (int i = 0; i < n; i++)
        if (plates[i])
            printf("%s %d\n", names[i].c_str(), plates[i]);
}
