#include <algorithm>
#include <cstdio>
#include <string>
#include <vector>

using namespace std;

const int RECORD = 64; // room for the 50 letters

int main() {
    int n;
    scanf("%d", &n);
    vector<int> weights(n);
    for (int &w : weights)
        scanf("%d", &w);
    sort(weights.begin(), weights.end());
    static char buf[RECORD];
    scanf("%s", buf);
    string record = buf;
    // the weights in use always form a block of the sorted list whose
    // neighbours stand on opposite pans, so the pan of the largest one wins,
    // and a change adds a new largest weight, any other step a new smallest
    int changes = 0;
    for (int i = 1; i < n; i++)
        changes += record[i] != record[i - 1];
    int low = n - 1 - changes, high = low;
    char lowSide = record[0], highSide = record[0];
    printf("%d %c\n", weights[low], record[0]);
    for (int i = 1; i < n; i++) {
        if (record[i] != record[i - 1]) {
            highSide = highSide == 'L' ? 'R' : 'L';
            printf("%d %c\n", weights[++high], highSide);
        } else {
            lowSide = lowSide == 'L' ? 'R' : 'L';
            printf("%d %c\n", weights[--low], lowSide);
        }
    }
}
