#include <cstdio>
#include <vector>
using namespace std;

int main() {
    int n;
    if (scanf("%d", &n) != 1)
        return 0;
    vector<int> numbers(n);
    for (int &x : numbers)
        if (scanf("%d", &x) != 1)
            return 0;
    // each run of equal numbers is said as its length and then the number
    bool first = true;
    for (int i = 0; i < n;) {
        int j = i;
        while (j < n && numbers[j] == numbers[i])
            j++;
        printf(first ? "%d %d" : " %d %d", j - i, numbers[i]);
        first = false;
        i = j;
    }
    printf("\n");
}
