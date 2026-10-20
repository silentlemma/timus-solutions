#include <cstdio>
#include <string>
#include <vector>

int main() {
    int n;
    scanf("%d", &n);
    std::vector<long long> a(n);
    for (auto &x : a) scanf("%lld", &x);
    // Around the circle the rises and the falls cancel out, so the
    // conversations where the next friend is less interesting sum to the same
    // as those where the next one is more interesting; equal neighbours add 0.
    std::vector<int> falls, rises, ties;
    for (int i = 0; i < n; i++) {
        long long next = a[(i + 1) % n];
        if (a[i] > next) falls.push_back(i + 1);
        else if (a[i] < next) rises.push_back(i + 1);
        else ties.push_back(i + 1);
    }
    if (falls.empty()) {
        // every difference is 0: one conversation against all the others
        falls.push_back(ties.back());
        ties.pop_back();
    }
    for (int x : ties) rises.push_back(x);
    std::string out = "YES\n";
    for (auto *part : {&falls, &rises}) {
        out += std::to_string(part->size()) + "\n";
        for (size_t i = 0; i < part->size(); i++)
            out += std::to_string((*part)[i]) + (i + 1 < part->size() ? " " : "\n");
    }
    fputs(out.c_str(), stdout);
    return 0;
}
