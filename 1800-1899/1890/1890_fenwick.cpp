#include <iostream>
#include <string>
#include <vector>

using namespace std;
using int64 = long long;

class Fenwick {
    int n;
    vector<int64> linear, constant;

    void suffix_add(int index, int64 amount) {
        int64 weighted = amount * (index - 1);
        for (; index <= n; index += index & -index) {
            linear[index] += amount;
            constant[index] += weighted;
        }
    }

    int64 prefix_sum(int index) const {
        int64 coefficient = 0, offset = 0;
        for (int at = index; at > 0; at -= at & -at) {
            coefficient += linear[at];
            offset += constant[at];
        }
        return coefficient * index - offset;
    }

  public:
    explicit Fenwick(const vector<int64> &values)
        : n(static_cast<int>(values.size()) - 1), linear(n + 1), constant(n + 1) {
        for (int i = 1; i <= n; ++i) {
            int64 difference = values[i] - values[i - 1];
            linear[i] = difference;
            constant[i] = difference * (i - 1);
        }
        for (int i = 1; i <= n; ++i) {
            int ancestor = i + (i & -i);
            if (ancestor <= n) {
                linear[ancestor] += linear[i];
                constant[ancestor] += constant[i];
            }
        }
    }

    int64 point(int index) const {
        int64 result = 0;
        for (; index > 0; index -= index & -index)
            result += linear[index];
        return result;
    }

    int64 range_sum(int left, int length) const {
        return prefix_sum(left + length - 1) - prefix_sum(left - 1);
    }

    void add(int left, int length, int64 amount) {
        suffix_add(left, amount);
        suffix_add(left + length, -amount);
    }

    vector<int64> values() {
        // Undo the linear Fenwick build, then integrate the differences.
        for (int i = n; i > 0; --i) {
            int ancestor = i + (i & -i);
            if (ancestor <= n)
                linear[ancestor] -= linear[i];
        }
        for (int i = 1; i <= n; ++i)
            linear[i] += linear[i - 1];
        return linear;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n, q;
    cin >> n >> q;
    vector<int> parent(n), size(n, 1), tin(n, 1), cursor(n, 2);
    vector<int64> salary(n), initial(n + 1);
    cin >> salary[0];
    for (int vertex = 1; vertex < n; ++vertex)
        cin >> parent[vertex] >> salary[vertex];
    for (int vertex = n - 1; vertex > 0; --vertex)
        size[parent[vertex]] += size[vertex];
    // Reserve consecutive child blocks; every parent has a smaller number.
    for (int vertex = 1; vertex < n; ++vertex) {
        int boss = parent[vertex];
        tin[vertex] = cursor[boss];
        cursor[boss] += size[vertex];
        cursor[vertex] = tin[vertex] + 1;
    }
    for (int vertex = 0; vertex < n; ++vertex)
        initial[tin[vertex]] = salary[vertex];
    Fenwick tree(initial);
    for (int query = 0; query < q; ++query) {
        string kind;
        int vertex;
        int64 threshold, amount;
        cin >> kind >> vertex >> threshold >> amount;
        int left = tin[vertex];
        int length = kind == "employee" ? 1 : size[vertex];
        int64 total = length == 1 ? tree.point(left) : tree.range_sum(left, length);
        if (total < threshold * length)
            tree.add(left, length, amount);
    }
    auto final_salary = tree.values();
    for (int vertex = 0; vertex < n; ++vertex)
        cout << final_salary[tin[vertex]] << '\n';
}
