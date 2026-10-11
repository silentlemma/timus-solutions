#include <algorithm>
#include <cstdio>
#include <vector>

const int NEVER = 1 << 30;
const int BOLT = -1, HEAL = 0; // spells; a teleport is its target square

int n, hpH, mpH, hpM, v, dH;
std::vector<int> bolt;
std::vector<std::vector<std::vector<int>>> need;

// where the monsters stop after moving from square p
int land(int p) { return p - 1 < v ? 1 : p - v; }

// the damage of a pack with h hit points that ends its move on p
int strike(int h, int p) { return p == 1 ? (h + hpM - 1) / hpM : 0; }

// the hit points a spell needs with m mana against h hit points on p
int cost(int m, int h, int p, int spell) {
    int cure = 0;
    if (spell == BOLT) {
        if (h <= bolt[p])
            return 1;
        h -= bolt[p];
    } else if (spell == HEAL) {
        cure = dH;
    } else {
        p = spell;
    }
    int q = land(p), rest = need[m - 1][h][q];
    if (rest == NEVER)
        return NEVER;
    int req = strike(h, q) + rest;
    if (!cure)
        return req;
    return req > hpH ? NEVER : std::max(1, req - cure);
}

int main() {
    int nM;
    scanf("%d %d %d %d %d %d %d", &n, &hpH, &mpH, &hpM, &nM, &v, &dH);
    bolt.assign(n + 1, 0);
    for (int p = 1; p <= n; p++)
        scanf("%d", &bolt[p]);
    int top = nM * hpM;
    // need[m][h][p] is the fewest hit points the hero needs at the start of
    // a turn with m mana against a pack of h hit points on square p; more
    // hit points never hurt, so this number decides every state
    need.assign(mpH + 1, std::vector<std::vector<int>>(top + 1, std::vector<int>(n + 1, NEVER)));
    for (int m = 1; m <= mpH; m++)
        for (int h = 1; h <= top; h++)
            for (int p = 1; p <= n; p++) {
                int best = NEVER;
                for (int s = BOLT; s <= n; s++)
                    best = std::min(best, cost(m, h, p, s));
                need[m][h][p] = best;
            }
    int hp = hpH, h = top, p = n;
    if (need[mpH][h][p] > hp) {
        puts("DEFEATED");
        return 0;
    }
    puts("VICTORIOUS");
    // replay: any spell whose need the hero meets keeps the win in reach
    for (int m = mpH; h > 0; m--) {
        int s = BOLT;
        while (cost(m, h, p, s) > hp)
            s++;
        if (s == BOLT) {
            puts("L");
            h -= bolt[p];
        } else if (s == HEAL) {
            puts("H");
            hp = std::min(hpH, hp + dH);
        } else {
            printf("T %d\n", s);
            p = s;
        }
        if (h > 0) {
            p = land(p);
            hp -= strike(h, p);
        }
    }
}
