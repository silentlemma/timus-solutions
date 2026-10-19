#include <iostream>
#include <set>
#include <string>
#include <vector>

using namespace std;

const string UNKNOWN = "unknown";

// every block of size phrases is one language, and no language is used in
// two blocks
bool fits(const vector<string>& phrases, int size) {
    set<string> used;
    for (size_t start = 0; start < phrases.size(); start += size) {
        string lang;
        for (size_t i = start; i < start + size; i++) {
            if (phrases[i] == UNKNOWN) continue;
            if (lang.empty()) lang = phrases[i];
            if (phrases[i] != lang) return false;
        }
        if (lang.empty()) continue;
        if (!used.insert(lang).second) return false;
    }
    return true;
}

int main() {
    int n;
    cin >> n;
    vector<string> phrases(n);
    for (string& p : phrases) cin >> p;
    vector<int> counts;
    for (int k = 1; k <= n; k++)
        if (n % k == 0 && fits(phrases, n / k)) counts.push_back(k);
    if (counts.empty()) {
        cout << "Igor is wrong.\n";
        return 0;
    }
    for (size_t i = 0; i < counts.size(); i++)
        cout << counts[i] << (i + 1 < counts.size() ? " " : "\n");
    return 0;
}
