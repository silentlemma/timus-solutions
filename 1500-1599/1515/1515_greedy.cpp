#include <algorithm>
#include <cstdio>
#include <vector>

using namespace std;

int main() {
    int n;
    scanf("%d", &n);
    vector<long long> notes(n);
    for (long long &d : notes)
        scanf("%lld", &d);
    sort(notes.begin(), notes.end());
    // every sum from 1 to reach is made of the notes taken so far; a note
    // no larger than reach + 1 extends that to reach + note
    long long reach = 0;
    for (long long d : notes) {
        if (d > reach + 1)
            break;
        reach += d;
    }
    printf("%lld\n", reach + 1);
}
