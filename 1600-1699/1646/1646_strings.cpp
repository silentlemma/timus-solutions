#include <iostream>
#include <string>
#include <vector>
using namespace std;

const long long MOD = 1000000007;

struct Sample {
    long long count;    // occurrences mod MOD; the string can be 2^100 long
    string head, tail;  // its first and last letters
};

string pattern;
size_t edge;  // letters kept at each end of a sample

long long occurrences(const string &text) {
    long long found = 0;
    for (size_t i = 0; i + pattern.size() <= text.size(); i++)
        found += text.compare(i, pattern.size(), pattern) == 0;
    return found;
}

string head(const string &s) {
    return s.substr(0, edge);
}

string tail(const string &s) {
    return s.size() > edge ? s.substr(s.size() - edge) : s;
}

int main() {
    string first, second;
    int m;
    cin >> pattern >> first >> second >> m;
    edge = pattern.size() - 1;
    vector<Sample> samples;
    for (const string &s : {first, second})
        samples.push_back({occurrences(s), head(s), tail(s)});
    for (int k = 0; k < m; k++) {
        int i, j;
        cin >> i >> j;
        Sample a = samples[i - 1], b = samples[j - 1];
        // every new occurrence crosses the seam, so it lies in these letters
        long long seam = occurrences(a.tail + b.head);
        long long count = (a.count + b.count + seam) % MOD;
        samples.push_back({count, head(a.head + b.head), tail(a.tail + b.tail)});
    }
    cout << samples.back().count << '\n';
}
