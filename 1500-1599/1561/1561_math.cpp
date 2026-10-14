#include <algorithm>
#include <iostream>
#include <string>
#include <vector>
using namespace std;

const string DAYS[] = {"Monday", "Tuesday",  "Wednesday", "Thursday",
                       "Friday", "Saturday", "Sunday"};
const int WEEK = 7;

int dayOf(const string &word) { return find(DAYS, DAYS + WEEK, word) - DAYS; }

int inverse(int x) {
    for (int y = 1; y < WEEK; y++)
        if (x * y % WEEK == 1)
            return y;
    return 0;
}

// a row of an echelon basis over the residues modulo 7, with a 1 at its
// first non-zero place
struct Row {
    int pivot;
    vector<int> coefficients;
    int right;
};

vector<Row> basis;

// subtract basis rows until no pivot of the basis stays non-zero
int reduce(vector<int> &v, int value) {
    for (const Row &row : basis) {
        int c = v[row.pivot];
        if (c == 0)
            continue;
        // the row is shorter if sorts appeared after it
        for (size_t i = row.pivot; i < row.coefficients.size(); i++)
            v[i] = ((v[i] - c * row.coefficients[i]) % WEEK + WEEK) % WEEK;
        value = ((value - c * row.right) % WEEK + WEEK) % WEEK;
    }
    return value;
}

int main() {
    int n, sorts = 0;
    cin >> n;
    bool crazy = false;
    for (int q = 0; q < n; q++) {
        string kind, word;
        cin >> kind;
        if (kind == "Add") {
            sorts++;
            continue;
        }
        // the numbers of the query up to its first weekday
        vector<int> v;
        while (cin >> word && dayOf(word) == WEEK)
            v.push_back(stoi(word) % WEEK);
        v.resize(max<size_t>(v.size(), sorts), 0);
        int start = dayOf(word);
        if (kind == "Learn") {
            cin >> word;
            if (crazy)
                continue;
            int value = reduce(v, ((dayOf(word) - start) % WEEK + WEEK) % WEEK);
            int pivot = find_if(v.begin(), v.end(), [](int c) { return c != 0; }) - v.begin();
            if (pivot == (int)v.size()) {
                crazy = value != 0;
                continue;
            }
            int scale = inverse(v[pivot]);
            for (int &c : v)
                c = c * scale % WEEK;
            Row row{pivot, v, value * scale % WEEK};
            basis.insert(upper_bound(basis.begin(), basis.end(), row,
                                     [](const Row &a, const Row &b) { return a.pivot < b.pivot; }),
                         row);
        } else if (crazy)
            cout << "Already crazy\n";
        else {
            int value = reduce(v, 0);
            if (any_of(v.begin(), v.end(), [](int c) { return c != 0; }))
                cout << "Don't know\n";
            else
                cout << DAYS[((start - value) % WEEK + WEEK) % WEEK] << "\n";
        }
    }
}
