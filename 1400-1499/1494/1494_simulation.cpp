#include <cstdio>
#include <vector>

using namespace std;

int main() {
    int n;
    scanf("%d", &n);
    vector<int> taken(n);
    for (int &b : taken)
        scanf("%d", &b);
    // the pocket is a stack: roll the balls in order, and whenever the top
    // one is the next ball the inspector took out, take it out
    vector<int> pocket;
    int next = 0;
    for (int ball = 1; ball <= n; ball++) {
        pocket.push_back(ball);
        while (!pocket.empty() && next < n && pocket.back() == taken[next]) {
            pocket.pop_back();
            next++;
        }
    }
    puts(next == n ? "Not a proof" : "Cheater");
}
