#include <iostream>
#include <map>
#include <string>
#include <unordered_map>
#include <vector>
using namespace std;

// a max tree over cities: the best total, how many leaves reach it, and one
// of them
int size_ = 1;
vector<long long> best;
vector<int> countOf, where;

void add(int city, long long amount) {
    int i = city + size_;
    best[i] += amount;
    for (i /= 2; i; i /= 2) {
        int a = 2 * i, b = 2 * i + 1;
        if (best[a] != best[b]) {
            int w = best[a] > best[b] ? a : b;
            best[i] = best[w], countOf[i] = countOf[w], where[i] = where[w];
        } else {
            best[i] = best[a], countOf[i] = countOf[a] + countOf[b], where[i] = where[a];
        }
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n;
    if (!(cin >> n))
        return 0;
    vector<string> name(n), city(n);
    vector<long long> money(n);
    for (int i = 0; i < n; i++)
        cin >> name[i] >> city[i] >> money[i];
    int m, k;
    cin >> m >> k;
    vector<int> day(k);
    vector<string> who(k), to(k);
    for (int i = 0; i < k; i++)
        cin >> day[i] >> who[i] >> to[i];
    unordered_map<string, int> cityId;
    vector<string> cityName;
    auto id = [&](const string &c) {
        auto it = cityId.find(c);
        if (it != cityId.end())
            return it->second;
        cityName.push_back(c);
        return cityId[c] = cityName.size() - 1;
    };
    for (const string &c : city)
        id(c);
    for (const string &c : to)
        id(c);
    while (size_ < (int)cityName.size())
        size_ *= 2;
    best.assign(2 * size_, 0);
    countOf.assign(2 * size_, 1);
    where.assign(2 * size_, 0);
    for (int c = 0; c < size_; c++)
        where[size_ + c] = c;
    for (int i = size_ - 1; i > 0; i--)
        countOf[i] = countOf[2 * i] + countOf[2 * i + 1], where[i] = where[2 * i];
    unordered_map<string, int> home;
    unordered_map<string, long long> wealth;
    for (int i = 0; i < n; i++) {
        home[name[i]] = id(city[i]);
        wealth[name[i]] = money[i];
        add(home[name[i]], money[i]);
    }
    vector<long long> days(cityName.size());
    auto lead = [&](long long span) {
        if (span > 0 && countOf[1] == 1)  // a strict leader only
            days[where[1]] += span;
    };
    long long today = 1;
    for (int i = 0; i < k; i++) {
        // the moves of a day count from the next morning
        lead(day[i] + 1 - today);
        today = max(today, (long long)day[i] + 1);
        add(home[who[i]], -wealth[who[i]]);
        home[who[i]] = id(to[i]);
        add(home[who[i]], wealth[who[i]]);
    }
    lead(m + 1 - today);
    map<string, long long> answer;
    for (size_t c = 0; c < cityName.size(); c++)
        if (days[c])
            answer[cityName[c]] = days[c];
    for (const auto &[c, d] : answer)
        cout << c << ' ' << d << '\n';
}
