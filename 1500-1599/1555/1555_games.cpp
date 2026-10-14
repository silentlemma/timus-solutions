#include <cstdint>
#include <cstdio>
#include <iostream>
#include <queue>
#include <string>
#include <vector>

using namespace std;

// results of a position for the first player
enum Result : uint8_t { UNKNOWN, WIN, LOSE, DRAW };
const uint16_t INF = 65535;
const int SIDES = 4, CELL = 3, MOVES = 10, PASS = 4, SUICIDE = 9;
const int MAXN = 6;
// a rocket state: 0 still loaded, 1 fired out of the maze, w + 2 destroyed wall w
const int LOADED = 0, FIRED = 1, WALL_BASE = 2;
const int NONE = -1;
const char DIRECTION[] = "8624"; // north, east, south, west as on a keypad
const char WALL_CHAR[] = "-|-|";
const int DR[] = {-1, 0, 1, 0}, DC[] = {0, 1, 0, -1};

int n, cells, walls, states, places;
int side[MAXN * MAXN][SIDES]; // wall id on each side of a cell, or NONE
int step[MAXN * MAXN][SIDES]; // the neighbouring cell, or NONE
int start1, start2, chest;
// a place: both cells, who holds the chest (0 nobody, 1 or 2) and whose turn
vector<int> cell1, cell2, holder, turnOf, valid;
vector<uint8_t> resultAll; // by rocket states and place
vector<uint16_t> distAll;

int placeId(int c1, int c2, int h, int turn) { return ((c1 * cells + c2) * CELL + h) * 2 + turn; }
size_t slot(int s1, int s2, int place) { return ((size_t)s1 * states + s2) * places + place; }

bool wallStands(int w, int s1, int s2) {
    return w != NONE && s1 != w + WALL_BASE && s2 != w + WALL_BASE;
}

bool canPass(int from, int d, int s1, int s2) {
    int to = step[from][d];
    return to != NONE && !wallStands(side[from][d], s1, s2) &&
           !wallStands(side[to][(d + 2) % SIDES], s1, s2);
}

struct Move {
    bool inside; // to a place of the same rocket states
    int to;
    uint8_t result;
    uint16_t dist;
};

// the flight of a rocket: whether it hits the other player, else the new rocket state
bool fly(int from, int d, int other, int s1, int s2, int &state) {
    int pos = from;
    while (true) {
        if (wallStands(side[pos][d], s1, s2)) {
            state = side[pos][d] + WALL_BASE;
            return false;
        }
        int next = step[pos][d];
        if (next == NONE) {
            state = FIRED;
            return false;
        }
        if (wallStands(side[next][(d + 2) % SIDES], s1, s2)) {
            state = side[next][(d + 2) % SIDES] + WALL_BASE;
            return false;
        }
        pos = next;
        if (pos == other)
            return true;
    }
}

uint8_t winFor(int turn) { return turn == 0 ? WIN : LOSE; }
uint8_t loseFor(int turn) { return turn == 0 ? LOSE : WIN; }

// every move from a place under the rocket states, in the order M8 M6 M2 M4 M5
// S8 S6 S2 S4 S5; a missing move has inside false and result UNKNOWN
Move moveFrom(int s1, int s2, int place, int code) {
    int turn = turnOf[place], cur = turn ? cell2[place] : cell1[place];
    int other = turn ? cell1[place] : cell2[place], h = holder[place];
    Move none = {false, 0, UNKNOWN, 0};
    auto outside = [&](uint8_t r) { return Move{false, 0, r, 0}; };
    auto later = [&](int ns1, int ns2, int to) {
        size_t at = slot(ns1, ns2, to);
        return Move{false, to, resultAll[at], distAll[at]};
    };
    if (code < PASS) {
        int d = code, next = step[cur][d];
        if (next == NONE) // out of the maze, only with the chest
            return h == turn + 1 && !wallStands(side[cur][d], s1, s2) ? outside(winFor(turn))
                                                                      : none;
        if (next == other || !canPass(cur, d, s1, s2))
            return none;
        int nh = h == 0 && next == chest ? turn + 1 : h;
        int to = turn ? placeId(cell1[place], next, nh, 1 - turn)
                      : placeId(next, cell2[place], nh, 1 - turn);
        return Move{true, to, UNKNOWN, 0};
    }
    if (code == PASS)
        return Move{true, place ^ 1, UNKNOWN, 0};
    if ((turn == 0 ? s1 : s2) != LOADED)
        return none;
    if (code == SUICIDE)
        return outside(loseFor(turn));
    int state;
    if (fly(cur, code - PASS - 1, other, s1, s2, state))
        return outside(winFor(turn));
    return turn == 0 ? later(state, s2, place ^ 1) : later(s1, state, place ^ 1);
}

// buffers of one rocket state, reused; at most MAX_PREDS places move into a
// place: a step from each side, with or without the chest picked up on the
// way, and a pass
const int MAX_PREDS = 2 * SIDES + 1;
const uint8_t SAW_WIN = 1, SAW_LOSE = 2, SAW_DRAW = 4;
vector<Move> moveBuf;
vector<int> moveCount, predBuf, predCount, rest, needed, got, most, order;
vector<uint8_t> res, seen;
vector<uint16_t> dist;

uint8_t saw(uint8_t r) {
    return r == WIN ? SAW_WIN : r == LOSE ? SAW_LOSE : r == DRAW ? SAW_DRAW : 0;
}

void settle(int place) {
    if (res[place] != UNKNOWN)
        return;
    bool first = turnOf[place] == 0;
    if (seen[place] & (first ? SAW_WIN : SAW_LOSE))
        res[place] = first ? WIN : LOSE;
    else if (rest[place] == 0)
        res[place] = (seen[place] & SAW_DRAW) ? (uint8_t)DRAW : (uint8_t)(first ? LOSE : WIN);
    else
        return;
    order.push_back(place);
}

void solve(int s1, int s2) {
    for (int place : valid) {
        moveCount[place] = predCount[place] = rest[place] = 0;
        res[place] = UNKNOWN;
        seen[place] = 0;
    }
    for (int place : valid)
        for (int code = 0; code < MOVES; code++) {
            Move m = moveFrom(s1, s2, place, code);
            if (!m.inside && m.result == UNKNOWN)
                continue;
            moveBuf[place * MOVES + moveCount[place]++] = m;
            if (m.inside) {
                predBuf[m.to * MAX_PREDS + predCount[m.to]++] = place;
                rest[place]++;
            } else {
                seen[place] |= saw(m.result);
            }
        }
    // the result by backward induction: a player wins as soon as one move
    // wins for her, loses when every move loses, and a cycle is a draw
    order.clear();
    for (int place : valid)
        settle(place);
    for (size_t head = 0; head < order.size(); head++) {
        int u = order[head];
        for (int k = u * MAX_PREDS; k < u * MAX_PREDS + predCount[u]; k++) {
            int p = predBuf[k];
            if (res[p] == UNKNOWN) {
                rest[p]--;
                seen[p] |= saw(res[u]);
                settle(p);
            }
        }
    }
    for (int place : valid) {
        if (res[place] == UNKNOWN)
            res[place] = DRAW;
        dist[place] = INF;
    }
    // the number of turns: the first player takes the fewest, the second the
    // most, among the moves that keep the result
    for (uint8_t kind : {WIN, LOSE}) {
        priority_queue<pair<int, int>, vector<pair<int, int>>, greater<>> events;
        for (int place : valid) {
            needed[place] = got[place] = most[place] = 0;
            if (res[place] != kind)
                continue;
            for (int k = place * MOVES; k < place * MOVES + moveCount[place]; k++) {
                const Move &m = moveBuf[k];
                if (m.inside ? res[m.to] == kind : m.result == kind) {
                    needed[place]++;
                    if (!m.inside && m.dist < INF)
                        events.push({m.dist + 1, place});
                }
            }
        }
        while (!events.empty()) {
            auto [d, place] = events.top();
            events.pop();
            bool done = false;
            if (turnOf[place] == 0) {
                done = d < dist[place] && dist[place] == INF;
                if (d < dist[place])
                    dist[place] = d;
            } else {
                got[place]++;
                most[place] = max(most[place], d);
                if (got[place] == needed[place] && most[place] < dist[place]) {
                    dist[place] = most[place];
                    done = true;
                }
            }
            if (done)
                for (int k = place * MAX_PREDS; k < place * MAX_PREDS + predCount[place]; k++)
                    if (res[predBuf[k]] == kind)
                        events.push({dist[place] + 1, predBuf[k]});
        }
    }
    for (int place : valid) {
        size_t at = slot(s1, s2, place);
        resultAll[at] = res[place];
        distAll[at] = res[place] == DRAW ? INF : dist[place];
    }
}

int strength(uint8_t r) { return r == WIN ? 2 : r == DRAW ? 1 : 0; }

int main() {
    string line;
    getline(cin, line);
    n = stoi(line);
    cells = n * n;
    vector<string> board(CELL * n);
    for (string &row : board) {
        getline(cin, row);
        while (!row.empty() && (row.back() == '\r' || row.back() == '\n'))
            row.pop_back();
        row.resize(CELL * n, ' ');
    }
    for (int r = 0; r < n; r++)
        for (int c = 0; c < n; c++) {
            int cell = r * n + c;
            char mid = board[CELL * r + 1][CELL * c + 1];
            if (mid == '1')
                start1 = cell;
            else if (mid == '2')
                start2 = cell;
            else if (mid == '*')
                chest = cell;
            // the side characters of a cell: north, east, south, west
            char at[SIDES] = {board[CELL * r][CELL * c + 1], board[CELL * r + 1][CELL * c + 2],
                              board[CELL * r + 2][CELL * c + 1], board[CELL * r + 1][CELL * c]};
            for (int d = 0; d < SIDES; d++) {
                side[cell][d] = at[d] == WALL_CHAR[d] ? walls++ : NONE;
                int nr = r + DR[d], nc = c + DC[d];
                step[cell][d] = 0 <= nr && nr < n && 0 <= nc && nc < n ? nr * n + nc : NONE;
            }
        }
    states = walls + WALL_BASE;
    places = cells * cells * CELL * 2;
    cell1.resize(places);
    cell2.resize(places);
    holder.resize(places);
    turnOf.resize(places);
    for (int a = 0; a < cells; a++)
        for (int b = 0; b < cells; b++)
            for (int h = 0; h < CELL; h++)
                for (int turn = 0; turn < 2; turn++) {
                    int place = placeId(a, b, h, turn);
                    cell1[place] = a;
                    cell2[place] = b;
                    holder[place] = h;
                    turnOf[place] = turn;
                    if (a != b)
                        valid.push_back(place);
                }
    moveBuf.resize(places * MOVES);
    predBuf.resize(places * MAX_PREDS);
    for (vector<int> *v : {&moveCount, &predCount, &rest, &needed, &got, &most})
        v->resize(places);
    res.resize(places);
    seen.resize(places);
    dist.resize(places);
    resultAll.assign((size_t)states * states * places, UNKNOWN);
    distAll.assign((size_t)states * states * places, INF);
    // a shot only uses a rocket up, so states with fewer rockets come first
    for (int loaded = 0; loaded <= 2; loaded++)
        for (int s1 = 0; s1 < states; s1++)
            for (int s2 = 0; s2 < states; s2++)
                if ((s1 == LOADED) + (s2 == LOADED) == loaded && !(s1 >= WALL_BASE && s1 == s2))
                    solve(s1, s2);
    int place = placeId(start1, start2, 0, 0);
    uint8_t result = resultAll[slot(LOADED, LOADED, place)];
    if (result == DRAW) {
        printf("Draw\n");
        return 0;
    }
    // the first move: the best result, then the fewest turns, then the order of codes
    int bestCode = NONE;
    uint8_t bestResult = UNKNOWN;
    uint16_t bestDist = INF;
    for (int code = 0; code < MOVES; code++) {
        Move m = moveFrom(LOADED, LOADED, place, code);
        if (!m.inside && m.result == UNKNOWN)
            continue;
        // a move leads to a table entry or ends the game at once (distance 0)
        uint8_t r = m.result;
        uint16_t later = m.dist;
        if (m.inside) {
            size_t at = slot(LOADED, LOADED, m.to);
            r = resultAll[at];
            later = distAll[at];
        }
        uint16_t d = r == DRAW ? 0 : later == INF ? INF : later + 1;
        bool better = bestCode == NONE || strength(r) > strength(bestResult) ||
                      (strength(r) == strength(bestResult) && r != DRAW && d < bestDist);
        if (better) {
            bestCode = code;
            bestResult = r;
            bestDist = d;
        }
    }
    printf("%s %d\n", result == WIN ? "Win" : "Lose", distAll[slot(LOADED, LOADED, place)]);
    printf("%c%c\n", bestCode <= PASS ? 'M' : 'S',
           bestCode == PASS || bestCode == SUICIDE ? '5' : DIRECTION[bestCode % (PASS + 1)]);
}
