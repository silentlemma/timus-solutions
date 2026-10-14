#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <string>
#include <vector>

using namespace std;
typedef unsigned long long Mask; // a set of grid cells, one bit each (grid <= 8 x 8)

const int SIDES = 4;
const int MAXCELLS = 64;
const int NONE = -1;
const int INF = 1000000;
const double TIME_LIMIT = 4.6; // seconds of search before giving up
const int DR[] = {-1, 1, 0, 0}, DC[] = {0, 0, -1, 1};
const char STEP[] = "udlr";
const int OPP[] = {1, 0, 3, 2};
const int UP = 0, DOWN = 1, LEFT = 2, RIGHT = 3;

inline int low(Mask x) { return __builtin_ctzll(x); }
inline bool has(Mask m, int c) { return (m >> c) & 1; }
inline Mask bit(int c) { return 1ULL << c; }

clock_t started;
int rows, cols, cells;
Mask floorM, goalM, deadM, deadPullM, notFirstCol, notLastCol;
int nb[SIDES][MAXCELLS]; // the neighbour in a direction, NONE outside the grid
int startPlayer;
Mask startBoxes;
int floorCount, floorCell[MAXCELLS], floorIndex[MAXCELLS], goalCount;

// the player's area: the floor reachable from p around the boxes, as bit-parallel growth
Mask grow(Mask r) {
    return r | ((r << 1) & notFirstCol) | ((r >> 1) & notLastCol) | (r << cols) | (r >> cols);
}

Mask flood(Mask seed, Mask within) {
    for (Mask r = seed;;) {
        Mask x = grow(r) & within;
        if (x == r)
            return r;
        r = x;
    }
}

Mask reach(int p, Mask boxes) { return flood(bit(p), floorM & ~boxes); }

// a state: a bit per floor cell for the boxes, then the floor index of the
// lowest cell of the player's area
Mask packKey(Mask boxes, int player) {
    Mask k = 0;
    for (Mask b = boxes; b; b &= b - 1)
        k |= bit(floorIndex[low(b)]);
    return k | (Mask)floorIndex[player] << floorCount;
}

Mask keyBoxes(Mask key) {
    Mask b = 0;
    for (Mask k = key & (bit(floorCount) - 1); k; k &= k - 1)
        b |= bit(floorCell[low(k)]);
    return b;
}

int keyPlayer(Mask key) { return floorCell[key >> floorCount]; }

// A box is frozen when it can move along neither axis: a wall or a frozen box
// on either side, or dead squares on both sides. Boxes already found frozen
// count as walls while their neighbours are checked.
Mask frozenAsWall;
bool frozenOffGoal;

bool wallLike(int c) { return c < 0 || !has(floorM, c) || has(frozenAsWall, c); }

bool frozen(int x, Mask boxes);

bool axisBlocked(int x, int d1, int d2, Mask boxes) {
    int a = nb[d1][x], b = nb[d2][x];
    if (wallLike(a) || wallLike(b))
        return true;
    if (has(deadM, a) && has(deadM, b))
        return true;
    return (has(boxes, a) && frozen(a, boxes)) || (has(boxes, b) && frozen(b, boxes));
}

bool frozen(int x, Mask boxes) {
    Mask saved = frozenAsWall;
    frozenAsWall |= bit(x);
    bool f = axisBlocked(x, LEFT, RIGHT, boxes) && axisBlocked(x, UP, DOWN, boxes);
    frozenAsWall = saved;
    if (f && !has(goalM, x))
        frozenOffGoal = true;
    return f;
}

// the box just pushed to x froze a box that is not on a goal
bool freezeDeadlock(int x, Mask boxes) {
    frozenAsWall = 0;
    frozenOffGoal = false;
    return frozen(x, boxes) && frozenOffGoal;
}

// h: the sum of each box's push distance to its nearest target; boxes that
// cannot be matched to distinct reachable targets mean a deadlock
Mask canReach[2][MAXCELLS]; // [push or pull search][cell]: targets a box there can get to
int nearest[2][MAXCELLS];
int matchOf[MAXCELLS];
Mask boxTargets[MAXCELLS], visited;

bool augment(int i) {
    for (Mask m = boxTargets[i] & ~visited; m; m &= m - 1) {
        int j = low(m);
        visited |= bit(j);
        if (matchOf[j] < 0 || augment(matchOf[j])) {
            matchOf[j] = i;
            return true;
        }
    }
    return false;
}

int heuristic(Mask boxes, int dir) {
    int k = 0, h = 0;
    for (Mask b = boxes; b; b &= b - 1) {
        h += nearest[dir][low(b)];
        boxTargets[k++] = canReach[dir][low(b)];
    }
    fill(matchOf, matchOf + goalCount, NONE);
    for (int i = 0; i < k; i++) {
        visited = 0;
        if (!augment(i))
            return NONE;
    }
    return h;
}

struct Push {
    int box, dir;
};

// The pushes worth trying, or a deadlock. If every push of the boxes around
// a region the player cannot reach goes inward and can be made now, one of
// them is needed first, so only those are tried.
bool generatePushes(Mask boxes, Mask area, vector<Push> &out) {
    out.clear();
    for (Mask bb = boxes; bb; bb &= bb - 1) {
        int b = low(bb);
        for (int d = 0; d < SIDES; d++) {
            int s = nb[OPP[d]][b], t = nb[d][b];
            if (s >= 0 && t >= 0 && has(area, s) && has(floorM, t) && !has(boxes, t))
                out.push_back(Push{b, d});
        }
    }
    Mask unreached = floorM & ~boxes & ~area;
    vector<Push> best, candidates;
    size_t bestCount = out.size() + 1;
    while (unreached) {
        Mask corral = flood(unreached & (0 - unreached), floorM & ~boxes & ~area);
        unreached &= ~corral;
        Mask barrier = grow(corral) & boxes;
        if (!(corral & goalM) && (barrier & ~goalM) == 0)
            continue; // finished corral
        bool inward = true, ready = true;
        candidates.clear();
        for (Mask bb = barrier; bb && inward; bb &= bb - 1) {
            int b = low(bb);
            for (int d = 0; d < SIDES; d++) {
                int s = nb[OPP[d]][b], t = nb[d][b];
                // the player stands outside the corral and off the barrier
                if (s < 0 || !has(floorM, s) || has(corral, s) || has(barrier, s))
                    continue;
                if (t < 0 || !has(floorM, t) || has(barrier, t))
                    continue; // blocked for good
                if (!has(corral, t)) {
                    inward = false; // a push away from the corral
                    break;
                }
                if (has(area, s))
                    candidates.push_back(Push{b, d});
                else
                    ready = false;
            }
        }
        if (!inward)
            continue;
        if (ready && candidates.empty())
            return false; // unfinished, and no push can ever enter it
        if (ready && candidates.size() < bestCount) {
            bestCount = candidates.size();
            best = candidates;
        }
    }
    if (bestCount <= out.size())
        out = best;
    return true;
}

// One open-addressing table holds the states of both searches; pull-search
// keys carry PULLED. A slot keeps the key and the move that made it.
const Mask PULLED = 1ULL << 63;
const int TABLE_BITS = 22;
const unsigned TABLE = 1u << TABLE_BITS, TABLE_MASK = TABLE - 1;
const unsigned TABLE_FILL = TABLE / 100 * 88; // the most keys before the table counts as full
const unsigned char ROOT = 255;
const Mask GOLDEN = 0x9E3779B97F4A7C15ULL;
const int KEY_BITS = 64;
Mask tableKey[TABLE];
unsigned char tableMove[TABLE]; // floor index of the moved box * 4 + direction
unsigned keyCount;

unsigned slotOf(Mask key) { return (unsigned)((key * GOLDEN) >> (KEY_BITS - TABLE_BITS)); }

const long long PRESENT = -1, FULL = -2;

long long insertKey(Mask key) {
    unsigned h = slotOf(key);
    for (; tableKey[h]; h = (h + 1) & TABLE_MASK)
        if (tableKey[h] == key)
            return PRESENT;
    if (keyCount >= TABLE_FILL)
        return FULL;
    keyCount++;
    tableKey[h] = key;
    return h;
}

bool hasKey(Mask key) {
    for (unsigned h = slotOf(key); tableKey[h]; h = (h + 1) & TABLE_MASK)
        if (tableKey[h] == key)
            return true;
    return false;
}

unsigned findKey(Mask key) {
    unsigned h = slotOf(key);
    while (tableKey[h] != key)
        h = (h + 1) & TABLE_MASK;
    return h;
}

// Open lists: buckets by f = g + WEIGHT * h, each a stack threaded through the
// table slots (a slot is queued at most once), so the memory stays fixed.
const int BUCKETS = 4096;
const int G_BITS = 9;
const unsigned G_MASK = (1u << G_BITS) - 1;
const int WEIGHT = 3;
unsigned tableNext[TABLE]; // (next slot + 1) << G_BITS | g

struct Open {
    unsigned head[BUCKETS] = {}; // slot + 1, 0 when empty
    int lowest = BUCKETS;
    void push(unsigned slot, int g, int f) {
        f = min(f, BUCKETS - 1);
        tableNext[slot] = head[f] << G_BITS | (unsigned)min<int>(g, G_MASK);
        head[f] = slot + 1;
        lowest = min(lowest, f);
    }
    bool pop(unsigned &slot, int &g) {
        while (lowest < BUCKETS && !head[lowest])
            lowest++;
        if (lowest >= BUCKETS)
            return false;
        slot = head[lowest] - 1;
        head[lowest] = tableNext[slot] >> G_BITS;
        g = tableNext[slot] & G_MASK;
        return true;
    }
};
Open pushOpen, pullOpen;
const int PUSH_ROUNDS = 8, PULL_ROUNDS = 1; // expansions of each search per round

string walk(int from, int to, Mask boxes) {
    if (from == to)
        return "";
    int prev[MAXCELLS], queue[MAXCELLS], head = 0, tail = 0;
    fill(prev, prev + cells, -2);
    prev[from] = NONE;
    queue[tail++] = from;
    while (head < tail) {
        int x = queue[head++];
        if (x == to)
            break;
        for (int d = 0; d < SIDES; d++) {
            int y = nb[d][x];
            if (y < 0 || !has(floorM, y) || has(boxes, y) || prev[y] != -2)
                continue;
            prev[y] = x * SIDES + d;
            queue[tail++] = y;
        }
    }
    string s;
    for (int x = to; x != from; x = prev[x] / SIDES)
        s += STEP[prev[x] % SIDES];
    reverse(s.begin(), s.end());
    return s;
}

// the plan through the state key, which both searches reached (or which is solved)
string buildAnswer(Mask key) {
    vector<Push> pushes;
    for (Mask k = key;;) { // back from key to the start through the push search
        unsigned char move = tableMove[findKey(k)];
        if (move == ROOT)
            break;
        int b = floorCell[move / SIDES], d = move % SIDES, t = nb[d][b];
        pushes.push_back(Push{b, d});
        Mask boxes = (keyBoxes(k) & ~bit(t)) | bit(b);
        k = packKey(boxes, low(reach(nb[OPP[d]][b], boxes)));
    }
    reverse(pushes.begin(), pushes.end());
    if (keyBoxes(key) != goalM)
        for (Mask k = key;;) { // forward to the goal: each pull, undone, is a push
            unsigned char move = tableMove[findKey(k | PULLED)];
            if (move == ROOT)
                break;
            int x = floorCell[move / SIDES], d = move % SIDES, b = nb[d][x];
            pushes.push_back(Push{x, d});
            Mask boxes = (keyBoxes(k) & ~bit(x)) | bit(b);
            k = packKey(boxes, low(reach(x, boxes)));
        }
    string out;
    Mask boxes = startBoxes;
    int pos = startPlayer;
    for (const Push &p : pushes) {
        out += walk(pos, nb[OPP[p.dir]][p.box], boxes);
        out += (char)(STEP[p.dir] - 'a' + 'A');
        boxes = (boxes & ~bit(p.box)) | bit(nb[p.dir][p.box]);
        pos = p.box;
    }
    return out;
}

// For sets of k = 2..MOST cells, the player cells from which these boxes alone
// can be solved (a pull search from the goals) or reached (a push search from
// the start); a state with a failing subset is dead.
const int MOST = 4;
const int TRIO = 3;
const int BYTE_BITS = 8;
const int NEAR = 3; // sets of four only with boxes this close to the moved one
unsigned binom[MAXCELLS + 1][MOST + 2];
vector<unsigned char> seenSet;
vector<Mask> setTable[2][MOST + 1]; // [solvable or reachable][k][set]: player cells

unsigned setIndex(Mask boxes) { // the combinatorial number system
    unsigned index = 0;
    int i = 1;
    for (Mask b = boxes; b; b &= b - 1, i++)
        index += binom[floorIndex[low(b)]][i];
    return index;
}

bool firstVisit(Mask set, int area) {
    unsigned long long n = (unsigned long long)setIndex(set) * floorCount + floorIndex[area];
    unsigned char &c = seenSet[n / BYTE_BITS];
    if ((c >> (n % BYTE_BITS)) & 1)
        return false;
    c |= (unsigned char)(1 << (n % BYTE_BITS));
    return true;
}

void buildSetTable(int dir, int k) {
    seenSet.assign(((size_t)binom[floorCount][k] * floorCount + BYTE_BITS - 1) / BYTE_BITS, 0);
    vector<Mask> &table = setTable[dir][k];
    table.assign(binom[floorCount][k], 0);
    Mask *queue = tableKey;
    size_t head = 0, tail = 0;
    int at[MAXCELLS], n = 0;
    for (Mask c = dir ? startBoxes : goalM; c; c &= c - 1)
        at[n++] = low(c);
    int pick[MOST];
    for (int i = 0; i < k; i++)
        pick[i] = i;
    while (k <= n) { // every k of the start boxes or the goals
        Mask set = 0;
        for (int i = 0; i < k; i++)
            set |= bit(at[pick[i]]);
        if (dir) { // the player where it starts
            int area = low(reach(startPlayer, set));
            if (firstVisit(set, area))
                queue[tail++] = packKey(set, area);
        } else { // the player in any free area
            for (Mask rest = floorM & ~set; rest;) {
                Mask area = reach(low(rest), set);
                rest &= ~area;
                if (firstVisit(set, low(area)))
                    queue[tail++] = packKey(set, low(area));
            }
        }
        int i = k - 1;
        while (i >= 0 && pick[i] == n - k + i)
            i--;
        if (i < 0)
            break;
        pick[i]++;
        for (int j = i + 1; j < k; j++)
            pick[j] = pick[j - 1] + 1;
    }
    while (head < tail) {
        Mask key = queue[head++], boxes = keyBoxes(key);
        Mask area = reach(keyPlayer(key), boxes);
        table[setIndex(boxes)] |= area;
        for (Mask bb = boxes; bb; bb &= bb - 1) {
            int b = low(bb);
            for (int d = 0; d < SIDES; d++) {
                int x = nb[OPP[d]][b];
                if (x < 0 || !has(area, x))
                    continue;
                // a push from x moves the box to y; a pull to x moves the player to y
                int y = dir ? nb[d][b] : nb[OPP[d]][x], to = dir ? b : y;
                if (y < 0 || !has(floorM, y) || has(boxes, y))
                    continue;
                Mask moved = (boxes & ~bit(b)) | bit(dir ? y : x);
                int where = low(reach(to, moved));
                if (firstVisit(moved, where))
                    queue[tail++] = packKey(moved, where);
            }
        }
    }
    memset(tableKey, 0, sizeof(Mask) * tail);
}

bool setSolvable(int dir, Mask set, int k, int player) {
    return has(setTable[dir][k][setIndex(set)], player);
}

// every set of up to MOST boxes with the moved box t is in the table
bool setsOK(int dir, Mask boxes, int t, int player) {
    int other[MAXCELLS], n = 0, close[MAXCELLS], nc = 0;
    for (Mask b = boxes & ~bit(t); b; b &= b - 1) {
        int c = low(b);
        other[n++] = c;
        if (abs(c / cols - t / cols) <= NEAR && abs(c % cols - t % cols) <= NEAR)
            close[nc++] = c;
    }
    Mask bt = bit(t);
    for (int i = 0; i < n; i++)
        if (!setSolvable(dir, bt | bit(other[i]), 2, player))
            return false;
    for (int i = 0; i < n; i++)
        for (int j = i + 1; j < n; j++)
            if (!setSolvable(dir, bt | bit(other[i]) | bit(other[j]), TRIO, player))
                return false;
    for (int i = 0; i < nc; i++)
        for (int j = i + 1; j < nc; j++)
            for (int l = j + 1; l < nc; l++)
                if (!setSolvable(dir, bt | bit(close[i]) | bit(close[j]) | bit(close[l]), MOST,
                                 player))
                    return false;
    return true;
}

// Both expansions return the key of a state where the searches met (or a
// solved state), 0 if none yet; tableFull is set when the table is full.
bool tableFull;
vector<Push> pushes;

Mask expandPush(unsigned slot, int g) {
    g++;
    Mask key = tableKey[slot], boxes = keyBoxes(key);
    Mask area = reach(keyPlayer(key), boxes);
    if (!generatePushes(boxes, area, pushes))
        return 0;
    for (const Push &p : pushes) {
        int b = p.box, d = p.dir, t = nb[d][b];
        if (has(deadM, t))
            continue;
        Mask moved = (boxes & ~bit(b)) | bit(t);
        if (freezeDeadlock(t, moved))
            continue;
        Mask next = packKey(moved, low(reach(b, moved)));
        if (hasKey(next) || !setsOK(0, moved, t, b))
            continue;
        long long s = insertKey(next);
        if (s == PRESENT)
            continue;
        if (s == FULL) {
            tableFull = true;
            return 0;
        }
        tableMove[s] = (unsigned char)(floorIndex[b] * SIDES + d);
        if (moved == goalM || hasKey(next | PULLED))
            return next;
        int h = heuristic(moved, 0);
        if (h != NONE) // a deadlocked state stays in the table as visited
            pushOpen.push((unsigned)s, g, g + WEIGHT * h);
    }
    return 0;
}

Mask expandPull(unsigned slot, int g) {
    g++;
    Mask key = tableKey[slot] & ~PULLED, boxes = keyBoxes(key);
    Mask area = reach(keyPlayer(key), boxes);
    for (Mask bb = boxes; bb; bb &= bb - 1) {
        int b = low(bb);
        for (int d = 0; d < SIDES; d++) {
            // the player at x pulls the box from b to x and steps back to y
            int x = nb[OPP[d]][b];
            if (x < 0 || !has(area, x) || has(deadPullM, x))
                continue;
            int y = nb[OPP[d]][x];
            if (y < 0 || !has(floorM, y) || has(boxes, y))
                continue;
            Mask moved = (boxes & ~bit(b)) | bit(x);
            Mask next = packKey(moved, low(reach(y, moved)));
            if (hasKey(next | PULLED) || !setsOK(1, moved, x, y))
                continue;
            long long s = insertKey(next | PULLED);
            if (s == PRESENT)
                continue;
            if (s == FULL) {
                tableFull = true;
                return 0;
            }
            tableMove[s] = (unsigned char)(floorIndex[x] * SIDES + d);
            if (hasKey(next))
                return next;
            int h = heuristic(moved, 1);
            if (h != NONE)
                pullOpen.push((unsigned)s, g, g + WEIGHT * h);
        }
    }
    return 0;
}

double elapsed() { return double(clock() - started) / CLOCKS_PER_SEC; }

// The push search from the start and the pull search from the goal take
// turns until some state is in both.
Mask solve() {
    Mask root = packKey(startBoxes, low(reach(startPlayer, startBoxes)));
    tableMove[insertKey(root)] = ROOT;
    int h0 = heuristic(startBoxes, 0);
    if (h0 != NONE)
        pushOpen.push(findKey(root), 0, WEIGHT * h0);
    int hg = heuristic(goalM, 1);
    for (Mask rest = floorM & ~goalM; rest;) { // the boxes on the goals, the player anywhere
        Mask area = reach(low(rest), goalM);
        rest &= ~area;
        Mask key = packKey(goalM, low(area));
        long long s = insertKey(key | PULLED);
        if (s < 0)
            continue;
        tableMove[s] = ROOT;
        if (key == root)
            return key;
        if (hg != NONE)
            pullOpen.push((unsigned)s, 0, WEIGHT * hg);
    }
    const int CLOCK_EVERY = 128;
    for (long long round = 0;; round++) {
        if (round % CLOCK_EVERY == 0 && elapsed() > TIME_LIMIT)
            return 0;
        unsigned slot;
        int g;
        bool any = false;
        for (int i = 0; i < PUSH_ROUNDS && pushOpen.pop(slot, g); i++) {
            any = true;
            if (Mask k = expandPush(slot, g))
                return k;
            if (tableFull)
                return 0;
        }
        for (int i = 0; i < PULL_ROUNDS && pullOpen.pop(slot, g); i++) {
            any = true;
            if (Mask k = expandPull(slot, g))
                return k;
            if (tableFull)
                return 0;
        }
        if (!any)
            return 0;
    }
}

// push distances of a lone box: dist[target][cell] to bring a box from cell
// to the target (pull = false), or from the target to cell (pull = true)
int dist[2][MAXCELLS][MAXCELLS];

Mask boxDistances(Mask targets, int dir) {
    Mask unreachable = floorM;
    int j = 0;
    for (Mask tg = targets; tg; tg &= tg - 1, j++) {
        int *D = dist[dir][j], queue[MAXCELLS], head = 0, tail = 0;
        fill(D, D + MAXCELLS, INF);
        D[low(tg)] = 0;
        queue[tail++] = low(tg);
        while (head < tail) {
            int x = queue[head++];
            unreachable &= ~bit(x);
            for (int d = 0; d < SIDES; d++) {
                // a box pushed from y to x (the player behind y), or from x to y
                int y = dir ? nb[d][x] : nb[OPP[d]][x];
                int p = dir ? nb[OPP[d]][x] : (y < 0 ? NONE : nb[OPP[d]][y]);
                if (y < 0 || p < 0 || !has(floorM, y) || !has(floorM, p) || D[y] != INF)
                    continue;
                D[y] = D[x] + 1;
                queue[tail++] = y;
            }
        }
    }
    return unreachable;
}

int main() {
    started = clock();
    vector<string> lines;
    const int LINE = 256;
    char buf[LINE];
    while (fgets(buf, sizeof buf, stdin)) {
        string s(buf);
        while (!s.empty() && (s.back() == '\n' || s.back() == '\r' || s.back() == ' '))
            s.pop_back();
        lines.push_back(s);
    }
    // drop the empty rows and columns around the level
    while (!lines.empty() && lines.back().empty())
        lines.pop_back();
    while (!lines.empty() && lines[0].empty())
        lines.erase(lines.begin());
    size_t lead = string::npos;
    for (const string &line : lines)
        if (!line.empty())
            lead = min(lead, line.find_first_not_of(' '));
    for (string &line : lines)
        line = line.size() > lead ? line.substr(lead) : "";
    rows = lines.size();
    cols = 0;
    for (const string &line : lines)
        cols = max(cols, (int)line.size());
    cells = rows * cols;
    Mask wallM = 0;
    for (int r = 0; r < rows; r++)
        for (int c = 0; c < cols; c++) {
            char ch = c < (int)lines[r].size() ? lines[r][c] : ' ';
            int id = r * cols + c;
            if (ch == '#')
                wallM |= bit(id);
            if (ch == '.' || ch == '+' || ch == '*')
                goalM |= bit(id);
            if (ch == '$' || ch == '*')
                startBoxes |= bit(id);
            if (ch == '@' || ch == '+')
                startPlayer = id;
        }
    for (int i = 0; i < cells; i++) {
        for (int d = 0; d < SIDES; d++) {
            int r = i / cols + DR[d], c = i % cols + DC[d];
            nb[d][i] = r < 0 || r >= rows || c < 0 || c >= cols ? NONE : r * cols + c;
        }
        if (i % cols != 0)
            notFirstCol |= bit(i);
        if (i % cols != cols - 1)
            notLastCol |= bit(i);
    }
    // the floor: the cells the player reaches through non-walls; boxes on
    // goals walled off from the player never move and count as walls
    floorM = ~wallM & (cells == MAXCELLS ? ~0ULL : bit(cells) - 1);
    floorM = reach(startPlayer, 0);
    goalM &= floorM;
    startBoxes &= floorM;
    for (Mask f = floorM; f; f &= f - 1) {
        floorIndex[low(f)] = floorCount;
        floorCell[floorCount++] = low(f);
    }
    goalCount = __builtin_popcountll(goalM);
    deadM = boxDistances(goalM, 0);
    deadPullM = boxDistances(startBoxes, 1);
    for (int i = 0; i <= MAXCELLS; i++)
        for (int j = 0; j <= MOST + 1; j++)
            binom[i][j] = j == 0 ? 1 : i == 0 ? 0 : binom[i - 1][j - 1] + binom[i - 1][j];
    for (int k = 2; k <= MOST && k <= goalCount; k++)
        for (int dir = 0; dir < 2; dir++)
            buildSetTable(dir, k);
    for (int dir = 0; dir < 2; dir++)
        for (int c = 0; c < cells; c++) {
            nearest[dir][c] = INF;
            for (int j = 0; j < goalCount; j++) {
                if (dist[dir][j][c] < INF)
                    canReach[dir][c] |= bit(j);
                nearest[dir][c] = min(nearest[dir][c], dist[dir][j][c]);
            }
        }
    string answer;
    if (startBoxes != goalM) {
        Mask meet = solve();
        if (meet)
            answer = buildAnswer(meet);
    }
    printf("%s\n", answer.c_str());
}
