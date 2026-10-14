#include <algorithm>
#include <array>
#include <cstdio>
#include <map>
using namespace std;

const int SHOOTERS = 3;
const int AIR = -1; // a shot into the air
const int INDEX_SUM = 0 + 1 + 2;
const double EPS = 1e-12; // survival chances closer than this count as equal

typedef array<double, SHOOTERS> Chances;

double acc[SHOOTERS];
array<int, SHOOTERS> order;

// the most accurate living opponent of all three; the earlier one on a tie
int strongest(int shooter) {
    int best = -1;
    for (int i = 0; i < SHOOTERS; i++)
        if (i != shooter && (best < 0 || acc[i] > acc[best]))
            best = i;
    return best;
}

// two left, first to shoot: first wins p / (p + q - p q)
Chances duel(int first, int second) {
    double p = acc[first], q = acc[second];
    Chances c = {0, 0, 0};
    c[first] = p / (p + q - p * q);
    c[second] = 1 - c[first];
    return c;
}

// the duel left after a hit, with the next living shooter first
Chances afterHit(int turn, int killed) {
    int first = order[(turn + 1) % SHOOTERS];
    if (first == killed)
        first = order[(turn + 2) % SHOOTERS];
    return duel(first, INDEX_SUM - killed - first);
}

// chances when all three live and order[turn] shoots; A never misses, so the
// shooting stops at A's turn at the latest
Chances three(int turn) {
    int shooter = order[turn];
    if (shooter == 0)
        return afterHit(turn, strongest(shooter));
    double p = acc[shooter];
    Chances miss = three((turn + 1) % SHOOTERS);
    map<int, Chances> outcomes = {{AIR, miss}};
    double best = miss[shooter];
    for (int target = 0; target < SHOOTERS; target++) {
        if (target == shooter)
            continue;
        Chances hit = afterHit(turn, target), mixed;
        for (int i = 0; i < SHOOTERS; i++)
            mixed[i] = p * hit[i] + (1 - p) * miss[i];
        outcomes[target] = mixed;
        best = max(best, mixed[shooter]);
    }
    // on a tie the strongest opponent is shot, then A, B, C, then the air
    for (int choice : {strongest(shooter), 0, 1, 2, AIR})
        if (outcomes.count(choice) && outcomes[choice][shooter] >= best - EPS)
            return outcomes[choice];
    return miss;
}

int main() {
    if (scanf("%lf %lf", &acc[0], &acc[1]) != 2 || scanf("%lf", &acc[2]) != 1)
        return 0;
    order = {0, 1, 2};
    Chances total = {0, 0, 0};
    int orders = 0;
    do {
        Chances c = three(0);
        for (int i = 0; i < SHOOTERS; i++)
            total[i] += c[i];
        orders++;
    } while (next_permutation(order.begin(), order.end()));
    printf("%.5f %.5f %.5f\n", total[0] * (1.0 / orders), total[1] * (1.0 / orders),
           total[2] * (1.0 / orders));
}
