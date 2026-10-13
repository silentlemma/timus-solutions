#include <algorithm>
#include <iostream>
#include <numeric>
#include <string>

using namespace std;

const int FACES = 4;

int main() {
    string a, b;
    cin >> a >> b;
    int p[FACES];
    iota(p, p + FACES, 0);
    bool same = false;
    do {
        int inversions = 0;
        for (int i = 0; i < FACES; i++)
            for (int j = i + 1; j < FACES; j++)
                inversions += p[i] > p[j];
        // the rotations of a tetrahedron move its faces by exactly the even permutations
        if (inversions % 2 != 0)
            continue;
        bool match = true;
        for (int i = 0; i < FACES; i++)
            match = match && b[i] == a[p[i]];
        same = same || match;
    } while (next_permutation(p, p + FACES));
    cout << (same ? "equal" : "different") << endl;
}
