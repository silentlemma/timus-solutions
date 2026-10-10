#include <algorithm>
#include <cstdio>
#include <vector>

int main() {
    int n;
    scanf("%d", &n);
    // the teacher's dates come sorted, so each of the student's dates is
    // looked up by binary search, counting repeats every time
    std::vector<int> known(n);
    for (int &year : known) {
        scanf("%d", &year);
    }
    int m, count = 0;
    scanf("%d", &m);
    for (int i = 0; i < m; i++) {
        int year;
        scanf("%d", &year);
        count += std::binary_search(known.begin(), known.end(), year);
    }
    printf("%d\n", count);
}
