#include <algorithm>
#include <cstdio>
#include <numeric>
#include <vector>

using namespace std;

int k;
vector<int> bound, radix, grundy;
vector<vector<int>> cutsOf; // legal cuts by edge length

int offset(const vector<int> &x) {
    int idx = 0;
    for (int i = 0; i < k; i++)
        idx += x[i] * radix[i];
    return idx;
}

// steps x through all tuples below dims, last axis fastest; false when done
bool advance(vector<int> &x, const vector<int> &dims) {
    int i = (int)dims.size() - 1;
    while (i >= 0 && ++x[i] == dims[i])
        x[i--] = 0;
    return i >= 0;
}

// the XOR over all parts for every tuple of cuts, last cut fastest: table
// holds the values of the parts by piece lengths, and each axis in turn is
// replaced by its cuts, a cut c of an edge d joining the pieces c - 1, d - c
vector<int> cutValues(vector<int> table, const vector<int> &dims) {
    vector<int> sizes = dims;
    for (int axis = k - 1; axis >= 0; axis--) {
        int inner = 1;
        for (int j = axis + 1; j < k; j++)
            inner *= sizes[j];
        int d = sizes[axis], span = d * inner;
        const vector<int> &cuts = cutsOf[d];
        vector<int> out;
        out.reserve(table.size() / d * cuts.size());
        for (size_t start = 0; start < table.size(); start += span)
            for (int c : cuts) {
                size_t low = start + (c - 1) * inner, high = start + (d - c) * inner;
                for (int j = 0; j < inner; j++)
                    out.push_back(table[low + j] ^ table[high + j]);
            }
        table.swap(out);
        sizes[axis] = cuts.size();
    }
    return table;
}

int main() {
    scanf("%d", &k);
    vector<int> edges(k);
    for (int &e : edges)
        scanf("%d", &e);
    if (k == 1) {
        // pieces of a segment of length d total d - 1, so by induction its
        // value is d mod 2, and from an odd length every cut wins
        puts(edges[0] % 2 ? "1\n1" : "2");
        return 0;
    }
    if (count(edges.begin(), edges.end(), 1) > 0) {
        // any cut empties a box with an edge of 1, so Alice cuts and wins
        printf("1\n");
        for (int i = 0; i < k; i++)
            printf("1%c", i + 1 < k ? ' ' : '\n');
        return 0;
    }
    // every ordering of a box's edges is stored with the same value, indexed
    // by a mixed radix over the sorted edges of the whole box
    bound = edges;
    sort(bound.begin(), bound.end());
    radix.assign(k, 1);
    for (int i = k - 2; i >= 0; i--)
        radix[i] = radix[i + 1] * (bound[i + 1] + 1);
    grundy.assign(radix[0] * (bound[0] + 1), 0); // boxes with an empty edge stay 0
    int longest = bound.back();
    cutsOf.assign(longest + 1, {});
    for (int d = 2; d <= longest; d++)
        for (int c = 1; c <= d; c++)
            if ((c > 1 && gcd(c - 1, d) == 1) || (d > c && gcd(d - c, d) == 1))
                cutsOf[d].push_back(c);
    // the boxes with sorted edges, smaller ones first
    vector<vector<int>> boxes;
    vector<int> box(k, 0);
    do {
        vector<int> b(k);
        for (int i = 0; i < k; i++)
            b[i] = box[i] + 1;
        if (is_sorted(b.begin(), b.end()))
            boxes.push_back(b);
    } while (advance(box, bound));
    stable_sort(boxes.begin(), boxes.end(), [](const vector<int> &a, const vector<int> &b) {
        return accumulate(a.begin(), a.end(), 0) < accumulate(b.begin(), b.end(), 0);
    });
    vector<int> seen(grundy.size() + 2, -1);
    int stamp = 0;
    for (vector<int> &b : boxes) {
        int g = 0;
        bool movable = true;
        for (int d : b)
            movable = movable && !cutsOf[d].empty();
        if (b[0] == 1)
            g = 1;
        else if (movable) {
            // the parts by piece lengths, a row along the last axis at a time
            vector<int> table, prefix(k, 0), head(b.begin(), b.end() - 1);
            do {
                int base = offset(prefix);
                table.insert(table.end(), grundy.begin() + base, grundy.begin() + base + b[k - 1]);
            } while (advance(prefix, head));
            stamp++;
            for (int v : cutValues(table, b))
                seen[v] = stamp;
            while (seen[g] == stamp)
                g++;
        }
        // only orderings within the bounds are ever looked up
        do {
            bool fits = true;
            for (int i = 0; i < k; i++)
                fits = fits && b[i] <= bound[i];
            if (fits)
                grundy[offset(b)] = g;
        } while (next_permutation(b.begin(), b.end()));
    }
    if (grundy[offset(bound)] == 0) {
        printf("2\n");
        return 0;
    }
    // the first winning cut in lexicographic order, in the input's order
    vector<int> table, x(k, 0), sorted(k);
    do {
        sorted = x;
        sort(sorted.begin(), sorted.end());
        table.push_back(grundy[offset(sorted)]);
    } while (advance(x, edges));
    vector<int> values = cutValues(table, edges), pos(k, 0);
    vector<int> counts(k);
    for (int i = 0; i < k; i++)
        counts[i] = cutsOf[edges[i]].size();
    for (int v : values) {
        if (v == 0) {
            printf("1\n");
            for (int i = 0; i < k; i++)
                printf("%d%c", cutsOf[edges[i]][pos[i]], i + 1 < k ? ' ' : '\n');
            return 0;
        }
        advance(pos, counts);
    }
}
