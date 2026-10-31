#include <algorithm>
#include <cstdio>
#include <string>
#include <unordered_map>
#include <utility>
#include <vector>

const int NAME_SIZE = 21;
struct Person {
    int city;
    long long wealth;
};
std::unordered_map<std::string, int> ids;
std::vector<std::string> names;
std::vector<long long> totals, best;
std::vector<int> where, days;
int size = 1;

int cityId(const char *name) {
    auto found = ids.find(name);
    if (found != ids.end())
        return found->second;
    int id = static_cast<int>(names.size());
    ids.emplace(name, id);
    names.emplace_back(name);
    totals.push_back(0);
    return id;
}

// a max tree over cities: the best total and the one city that reaches it,
// or minus one when several cities do
void pull(int i) {
    int a = 2 * i, b = a + 1;
    best[i] = std::max(best[a], best[b]);
    // minus one denotes a tie, so a full multiplicity array is unnecessary.
    where[i] = best[a] == best[b] ? -1 : where[best[a] > best[b] ? a : b];
}

void add(int city, long long amount) {
    int i = size + city;
    best[i] += amount;
    for (i /= 2; i; i /= 2) {
        long long old = best[i];
        int winner = where[i];
        pull(i);
        // unchanged maxima and tie status cannot affect an ancestor.
        if (best[i] == old && where[i] == winner)
            break;
    }
}

int main() {
    int n;
    std::scanf("%d", &n);
    std::unordered_map<std::string, Person> people;
    // names have at most twenty letters, plus one terminating zero.
    char who[NAME_SIZE], city[NAME_SIZE];
    for (int i = 0; i < n; ++i) {
        long long wealth;
        std::scanf("%20s%20s%lld", who, city, &wealth);
        int id = cityId(city);
        people.emplace(who, Person{id, wealth});
        totals[id] += wealth;
    }
    int m, k;
    std::scanf("%d%d", &m, &k);
    // each move introduces at most one city; no move records need to be stored.
    while (size < static_cast<int>(names.size()) + k)
        size *= 2;
    best.assign(2 * size, 0);
    where.assign(2 * size, -1);
    days.assign(size, 0);
    for (int i = 0; i < size; ++i)
        where[size + i] = i;
    for (int i = 0; i < static_cast<int>(totals.size()); ++i)
        best[size + i] = totals[i];
    for (int i = size - 1; i; --i)
        pull(i);
    int today = 1;
    for (int i = 0; i < k; ++i) {
        int day;
        std::scanf("%d%20s%20s", &day, who, city);
        // a strict leader only; the moves of a day count from the next morning
        if (where[1] >= 0)
            days[where[1]] += day + 1 - today;
        today = day + 1;
        Person &person = people.find(who)->second;
        int to = cityId(city);
        if (person.city != to) {
            add(person.city, -person.wealth);
            add(to, person.wealth);
            person.city = to;
        }
    }
    if (where[1] >= 0)
        days[where[1]] += m + 1 - today;
    std::vector<int> leaders;
    for (int i = 0; i < static_cast<int>(names.size()); ++i)
        if (days[i])
            leaders.push_back(i);
    std::sort(leaders.begin(), leaders.end(), [](int a, int b) { return names[a] < names[b]; });
    for (int id : leaders)
        std::printf("%s %d\n", names[id].c_str(), days[id]);
}
