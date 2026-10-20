#include <cstdio>
#include <vector>

constexpr int LIMIT = 2000000;  // the largest possible sum of two notes

std::vector<char> composite;
std::vector<int> odd, even;
std::vector<int> partner;  // the odd note matched to each even note, -1 if none
std::vector<char> visited;

bool augment(int u) {
    for (int v = 0; v < (int)even.size(); v++) {
        if (visited[v] || composite[odd[u] + even[v]]) continue;
        visited[v] = 1;
        if (partner[v] < 0 || augment(partner[v])) {
            partner[v] = u;
            return true;
        }
    }
    return false;
}

int main() {
    composite.assign(LIMIT + 1, 0);
    composite[0] = composite[1] = 1;
    for (long long i = 2; i * i <= LIMIT; i++)
        if (!composite[i])
            for (long long j = i * i; j <= LIMIT; j += i) composite[j] = 1;
    int n;
    scanf("%d", &n);
    int ones = 0;
    for (int i = 0; i < n; i++) {
        int c;
        scanf("%d", &c);
        if (c == 1) ones++;
        else if (c % 2) odd.push_back(c);
        else even.push_back(c);
    }
    // A prime sum is 2 = 1 + 1 or an odd prime, the sum of an odd and an even
    // note. So the surplus of odd notes must be paired as ones among themselves.
    int surplus = ones + (int)odd.size() - (int)even.size();
    if (surplus < 0 || surplus > ones) {
        puts("NO");
        return 0;
    }
    int onePairs = surplus / 2;
    for (int i = 0; i < ones - 2 * onePairs; i++) odd.push_back(1);
    partner.assign(even.size(), -1);
    for (int u = 0; u < (int)odd.size(); u++) {
        visited.assign(even.size(), 0);
        if (!augment(u)) {
            puts("NO");
            return 0;
        }
    }
    puts("YES");
    for (int i = 0; i < onePairs; i++) puts("1 1");
    for (int v = 0; v < (int)even.size(); v++) printf("%d %d\n", odd[partner[v]], even[v]);
    return 0;
}
