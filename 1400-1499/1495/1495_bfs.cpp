#include <algorithm>
#include <cstdio>
#include <string>
#include <vector>

using namespace std;

const int LONGEST = 30, BASE = 10;
const int DIGITS[] = {1, 2};

int main() {
    int n;
    scanf("%d", &n);
    // breadth-first search over remainders: shorter numbers come first, and
    // within one length the queue keeps numeric order, so the first number
    // to reach a remainder is the smallest one with it
    vector<int> parent(n, -2), digit(n, 0), length(n, 0), queue;
    queue.reserve(n);
    for (int d : DIGITS) {
        int r = d % n;
        if (parent[r] == -2) {
            parent[r] = -1, digit[r] = d, length[r] = 1;
            queue.push_back(r);
        }
    }
    for (size_t head = 0; head < queue.size() && parent[0] == -2; head++) {
        int r = queue[head];
        if (length[r] == LONGEST)
            continue;
        for (int d : DIGITS) {
            int s = (int)(((long long)r * BASE + d) % n);
            if (parent[s] == -2) {
                parent[s] = r, digit[s] = d, length[s] = length[r] + 1;
                queue.push_back(s);
            }
        }
    }
    if (parent[0] == -2) {
        puts("Impossible");
        return 0;
    }
    string out;
    for (int r = 0; r != -1; r = parent[r])
        out += char('0' + digit[r]);
    reverse(out.begin(), out.end());
    puts(out.c_str());
}
