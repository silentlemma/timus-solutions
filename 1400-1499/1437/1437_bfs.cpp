#include <algorithm>
#include <cstdio>
#include <set>
#include <vector>

using namespace std;

const int CANS = 3;

int cap[CANS], sz[CANS];

int code(const int *v) { return (v[0] * sz[1] + v[1]) * sz[2] + v[2]; }

int main() {
    for (int &c : cap)
        scanf("%d", &c);
    for (int i = 0; i < CANS; i++)
        sz[i] = cap[i] + 1;
    // a state (x, y, z) as one number; every move leaves some can empty or full
    vector<char> seen(sz[0] * sz[1] * sz[2], 0);
    vector<int> queue = {0};
    seen[0] = 1;
    set<int> volumes;
    for (size_t head = 0; head < queue.size(); head++) {
        int s = queue[head], v[CANS] = {s / (sz[1] * sz[2]), s / sz[2] % sz[1], s % sz[2]};
        for (int mask = 1; mask < 1 << CANS; mask++) {
            int sum = 0;
            for (int i = 0; i < CANS; i++)
                if (mask >> i & 1)
                    sum += v[i];
            volumes.insert(sum);
        }
        for (int i = 0; i < CANS; i++)
            for (int j = -1; j < CANS; j++) {
                int w[CANS] = {v[0], v[1], v[2]};
                if (j < 0) { // fill can i from the pump up to the brim
                    w[i] = cap[i];
                } else if (i != j) { // pour i into j
                    int move = min(v[i], cap[j] - v[j]);
                    w[i] -= move;
                    w[j] += move;
                }
                int k = code(w);
                if (!seen[k]) {
                    seen[k] = 1;
                    queue.push_back(k);
                }
            }
    }
    volumes.erase(0);
    printf("%d\n", (int)volumes.size());
}
