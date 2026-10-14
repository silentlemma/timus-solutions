#include <algorithm>
#include <cstdio>
#include <iostream>
#include <string>
#include <vector>
using namespace std;

const int MOD = 10007;
const int MOST = 512; // the product of the sizes is at most this

// the length of the arrays at each depth, ending with 0 for the empty ones
vector<int> sizes(const string &text) {
    vector<int> open, dims;
    for (char ch : text) {
        if (ch == '[') {
            if (!open.empty())
                open.back()++;
            open.push_back(0);
        } else if (ch == ']') {
            size_t depth = open.size() - 1;
            if (dims.size() <= depth)
                dims.resize(depth + 1, 0);
            dims[depth] = open.back();
            open.pop_back();
        }
    }
    return dims;
}

int main() {
    string text, line;
    while (getline(cin, line))
        text += line;
    vector<int> dims = sizes(text);
    if (dims.size() == 1) {
        printf("1\n");
        return 0;
    }
    // Stirling numbers of the second kind: ways to split m references into k objects
    vector<vector<int>> stirling(MOST + 1, vector<int>(MOST + 1, 0));
    stirling[0][0] = 1;
    for (int m = 1; m <= MOST; m++)
        for (int k = 1; k <= m; k++)
            stirling[m][k] = (stirling[m - 1][k - 1] + k * stirling[m - 1][k]) % MOD;
    // m references to empty arrays: any partition of them (Bell numbers)
    vector<int> ways(MOST + 1, 0);
    for (int m = 0; m <= MOST; m++) {
        long long sum = 0;
        for (int k = 0; k <= m; k++)
            sum += stirling[m][k];
        ways[m] = sum % MOD;
    }
    // the references at depth i number at most dims[0] * ... * dims[i - 1]
    vector<long long> slots = {1};
    for (size_t i = 0; i + 1 < dims.size(); i++)
        slots.push_back(slots.back() * dims[i]);
    for (int i = (int)dims.size() - 2; i >= 1; i--) {
        int width = dims[i];
        // m references to arrays of this depth: k distinct arrays, whose
        // k * width elements are configured one level down
        int upper = (int)min<long long>(MOST / width, slots[i]);
        vector<int> next(MOST + 1, 0);
        for (int m = 1; m <= upper; m++) {
            long long sum = 0;
            for (int k = 1; k <= m; k++)
                sum += (long long)stirling[m][k] * ways[k * width];
            next[m] = sum % MOD;
        }
        ways = next;
    }
    printf("%d\n", ways[dims[0]]);
}
