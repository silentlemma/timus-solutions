import java.io.*;
import java.util.*;

public class Main {
    // results of a position for the first player
    static final byte UNKNOWN = 0, WIN = 1, LOSE = 2, DRAW = 3;
    static final int INF = 65535;
    static final int SIDES = 4;
    static final int CELL = 3;
    static final int MOVES = 10;
    static final int PASS = 4;
    static final int SUICIDE = 9;
    static final int NONE = -1;
    // a rocket state: 0 still loaded, 1 fired out of the maze, w + 2 destroyed wall w
    static final int LOADED = 0;
    static final int FIRED = 1;
    static final int WALL_BASE = 2;
    // at most this many places move into a place: a step from each side, with or
    // without the chest picked up on the way, and a pass
    static final int MAX_PREDS = 2 * SIDES + 1;
    static final int SAW_WIN = 1, SAW_LOSE = 2, SAW_DRAW = 4;
    static final String DIRECTION = "8624"; // north, east, south, west as on a keypad
    static final String WALL_CHAR = "-|-|";
    static final int[] DR = {-1, 0, 1, 0}, DC = {0, 1, 0, -1};

    static int n, cells, walls, states, places;
    static int[][] side, step;
    static int start1, start2, chest;
    // a place: both cells, who holds the chest (0 nobody, 1 or 2) and whose turn
    static int[] cell1, cell2, holder, turnOf, valid;
    static byte[] resultAll; // by rocket states and place
    static char[] distAll;

    static int placeId(int c1, int c2, int h, int turn) {
        return ((c1 * cells + c2) * CELL + h) * 2 + turn;
    }

    static int slot(int s1, int s2, int place) { return (s1 * states + s2) * places + place; }

    static boolean wallStands(int w, int s1, int s2) {
        return w != NONE && s1 != w + WALL_BASE && s2 != w + WALL_BASE;
    }

    static boolean canPass(int from, int d, int s1, int s2) {
        int to = step[from][d];
        return to != NONE && !wallStands(side[from][d], s1, s2) &&
            !wallStands(side[to][(d + 2) % SIDES], s1, s2);
    }

    // the last move made by moveFrom: inside (to a place of the same rocket
    // states), or an outcome with its result and distance; missing when the
    // result is UNKNOWN and it is not inside
    static boolean mInside;
    static int mTo;
    static byte mResult;
    static int mDist;

    static void outcome(byte result, int to, int dist) {
        mInside = false;
        mTo = to;
        mResult = result;
        mDist = dist;
    }

    static byte winFor(int turn) { return turn == 0 ? WIN : LOSE; }

    static byte loseFor(int turn) { return turn == 0 ? LOSE : WIN; }

    // the move with a code (M8 M6 M2 M4 M5 S8 S6 S2 S4 S5) from a place
    static void moveFrom(int s1, int s2, int place, int code) {
        int turn = turnOf[place], h = holder[place];
        int cur = turn == 1 ? cell2[place] : cell1[place];
        int other = turn == 1 ? cell1[place] : cell2[place];
        outcome(UNKNOWN, 0, 0);
        if (code < PASS) {
            int d = code, next = step[cur][d];
            if (next == NONE) { // out of the maze, only with the chest
                if (h == turn + 1 && !wallStands(side[cur][d], s1, s2))
                    outcome(winFor(turn), 0, 0);
                return;
            }
            if (next == other || !canPass(cur, d, s1, s2))
                return;
            int nh = h == 0 && next == chest ? turn + 1 : h;
            mInside = true;
            mTo =
                turn == 0 ? placeId(next, cell2[place], nh, 1) : placeId(cell1[place], next, nh, 0);
            return;
        }
        if (code == PASS) {
            mInside = true;
            mTo = place ^ 1;
            return;
        }
        if ((turn == 0 ? s1 : s2) != LOADED)
            return;
        if (code == SUICIDE) {
            outcome(loseFor(turn), 0, 0);
            return;
        }
        // the flight of the rocket
        int d = code - PASS - 1, pos = cur, state;
        while (true) {
            if (wallStands(side[pos][d], s1, s2)) {
                state = side[pos][d] + WALL_BASE;
                break;
            }
            int next = step[pos][d];
            if (next == NONE) {
                state = FIRED;
                break;
            }
            int back = side[next][(d + 2) % SIDES];
            if (wallStands(back, s1, s2)) {
                state = back + WALL_BASE;
                break;
            }
            pos = next;
            if (pos == other) {
                outcome(winFor(turn), 0, 0);
                return;
            }
        }
        int at = turn == 0 ? slot(state, s2, place ^ 1) : slot(s1, state, place ^ 1);
        outcome(resultAll[at], place ^ 1, distAll[at]);
    }

    // buffers of one rocket state, reused
    static int[] moveTo, moveDist, predList, rest, needed, got, most, dist, order, heap;
    static boolean[] moveInside;
    static byte[] moveResult, res, seen, moveCount, predCount;
    static int orderSize, heapSize;

    static int saw(byte r) {
        return r == WIN ? SAW_WIN : r == LOSE ? SAW_LOSE : r == DRAW ? SAW_DRAW : 0;
    }

    static void settle(int place) {
        if (res[place] != UNKNOWN)
            return;
        boolean first = turnOf[place] == 0;
        if ((seen[place] & (first ? SAW_WIN : SAW_LOSE)) != 0)
            res[place] = first ? WIN : LOSE;
        else if (rest[place] == 0)
            res[place] = (seen[place] & SAW_DRAW) != 0 ? DRAW : first ? LOSE : WIN;
        else
            return;
        order[orderSize++] = place;
    }

    // a binary heap of events packed as distance * places + place
    static void push(int d, int place) {
        long key = (long)d * places + place;
        int i = heapSize++;
        while (i > 0 && heapKey(heap[(i - 1) / 2]) > key) {
            heap[i] = heap[(i - 1) / 2];
            i = (i - 1) / 2;
        }
        heap[i] = (int)key;
    }

    static long heapKey(int x) { return x; } // keys stay below 2^31

    static int pop() {
        int top = heap[0], x = heap[--heapSize], i = 0;
        while (2 * i + 1 < heapSize) {
            int c = 2 * i + 1;
            if (c + 1 < heapSize && heapKey(heap[c + 1]) < heapKey(heap[c]))
                c++;
            if (heapKey(heap[c]) >= heapKey(x))
                break;
            heap[i] = heap[c];
            i = c;
        }
        heap[i] = x;
        return top;
    }

    static void solve(int s1, int s2) {
        for (int place : valid) {
            moveCount[place] = 0;
            predCount[place] = 0;
            res[place] = UNKNOWN;
            seen[place] = 0;
            rest[place] = 0;
        }
        for (int place : valid)
            for (int code = 0; code < MOVES; code++) {
                moveFrom(s1, s2, place, code);
                if (!mInside && mResult == UNKNOWN)
                    continue;
                int k = place * MOVES + moveCount[place]++;
                moveTo[k] = mTo;
                moveInside[k] = mInside;
                moveResult[k] = mResult;
                moveDist[k] = mDist;
                if (mInside) {
                    predList[mTo * MAX_PREDS + predCount[mTo]++] = place;
                    rest[place]++;
                } else {
                    seen[place] |= saw(mResult);
                }
            }
        // the result by backward induction: a player wins as soon as one move
        // wins for her, loses when every move loses, and a cycle is a draw
        orderSize = 0;
        for (int place : valid)
            settle(place);
        for (int head = 0; head < orderSize; head++) {
            int u = order[head];
            for (int k = u * MAX_PREDS; k < u * MAX_PREDS + predCount[u]; k++) {
                int p = predList[k];
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
        for (byte kind : new byte[] {WIN, LOSE}) {
            heapSize = 0;
            for (int place : valid) {
                needed[place] = got[place] = most[place] = 0;
                if (res[place] != kind)
                    continue;
                for (int k = place * MOVES; k < place * MOVES + moveCount[place]; k++) {
                    boolean inside = moveInside[k];
                    if (inside ? res[moveTo[k]] == kind : moveResult[k] == kind) {
                        needed[place]++;
                        if (!inside && moveDist[k] < INF)
                            push(moveDist[k] + 1, place);
                    }
                }
            }
            while (heapSize > 0) {
                long key = heapKey(pop());
                int d = (int)(key / places), place = (int)(key % places);
                boolean done = false;
                if (turnOf[place] == 0) {
                    done = d < dist[place] && dist[place] == INF;
                    dist[place] = Math.min(dist[place], d);
                } else {
                    got[place]++;
                    most[place] = Math.max(most[place], d);
                    if (got[place] == needed[place] && most[place] < dist[place]) {
                        dist[place] = most[place];
                        done = true;
                    }
                }
                if (done)
                    for (int k = place * MAX_PREDS; k < place * MAX_PREDS + predCount[place]; k++)
                        if (res[predList[k]] == kind)
                            push(dist[place] + 1, predList[k]);
            }
        }
        for (int place : valid) {
            int at = slot(s1, s2, place);
            resultAll[at] = res[place];
            distAll[at] = (char)(res[place] == DRAW ? INF : dist[place]);
        }
    }

    static int strength(byte r) { return r == WIN ? 2 : r == DRAW ? 1 : 0; }

    public static void main(String[] args) throws IOException {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(in.readLine().trim());
        cells = n * n;
        char[][] board = new char[CELL * n][];
        for (int i = 0; i < CELL * n; i++) {
            String row = in.readLine();
            StringBuilder s = new StringBuilder(row == null ? "" : row);
            while (s.length() < CELL * n)
                s.append(' ');
            board[i] = s.toString().toCharArray();
        }
        side = new int[cells][SIDES];
        step = new int[cells][SIDES];
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
                char[] at = {board[CELL * r][CELL * c + 1], board[CELL * r + 1][CELL * c + 2],
                             board[CELL * r + 2][CELL * c + 1], board[CELL * r + 1][CELL * c]};
                for (int d = 0; d < SIDES; d++) {
                    side[cell][d] = at[d] == WALL_CHAR.charAt(d) ? walls++ : NONE;
                    int nr = r + DR[d], nc = c + DC[d];
                    step[cell][d] = 0 <= nr && nr < n && 0 <= nc && nc < n ? nr * n + nc : NONE;
                }
            }
        states = walls + WALL_BASE;
        places = cells * cells * CELL * 2;
        cell1 = new int[places];
        cell2 = new int[places];
        holder = new int[places];
        turnOf = new int[places];
        int count = 0;
        valid = new int[places];
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
                            valid[count++] = place;
                    }
        valid = Arrays.copyOf(valid, count);
        moveTo = new int[places * MOVES];
        moveDist = new int[places * MOVES];
        moveInside = new boolean[places * MOVES];
        moveResult = new byte[places * MOVES];
        moveCount = new byte[places];
        predList = new int[places * MAX_PREDS];
        predCount = new byte[places];
        res = new byte[places];
        seen = new byte[places];
        rest = new int[places];
        needed = new int[places];
        got = new int[places];
        most = new int[places];
        dist = new int[places];
        order = new int[places];
        heap = new int[places * MOVES * 2];
        resultAll = new byte[states * states * places];
        distAll = new char[states * states * places];
        // a shot only uses a rocket up, so states with fewer rockets come first
        for (int left = 0; left <= 2; left++)
            for (int s1 = 0; s1 < states; s1++)
                for (int s2 = 0; s2 < states; s2++)
                    if ((s1 == LOADED ? 1 : 0) + (s2 == LOADED ? 1 : 0) == left &&
                        !(s1 >= WALL_BASE && s1 == s2))
                        solve(s1, s2);
        int place = placeId(start1, start2, 0, 0);
        byte result = resultAll[slot(LOADED, LOADED, place)];
        if (result == DRAW) {
            System.out.println("Draw");
            return;
        }
        // the first move: the best result, then the fewest turns, then the order of codes
        int best = NONE, bestDist = INF;
        byte bestResult = UNKNOWN;
        for (int code = 0; code < MOVES; code++) {
            moveFrom(LOADED, LOADED, place, code);
            if (!mInside && mResult == UNKNOWN)
                continue;
            // a move leads to a table entry or ends the game at once (distance 0)
            byte r = mResult;
            int later = mDist;
            if (mInside) {
                int at = slot(LOADED, LOADED, mTo);
                r = resultAll[at];
                later = distAll[at];
            }
            int d = r == DRAW ? 0 : later == INF ? INF : later + 1;
            if (best == NONE || strength(r) > strength(bestResult) ||
                (strength(r) == strength(bestResult) && r != DRAW && d < bestDist)) {
                best = code;
                bestResult = r;
                bestDist = d;
            }
        }
        System.out.println((result == WIN ? "Win " : "Lose ") +
                           (int)distAll[slot(LOADED, LOADED, place)]);
        char dir = best == PASS || best == SUICIDE ? '5' : DIRECTION.charAt(best % (PASS + 1));
        System.out.println("" + (best <= PASS ? 'M' : 'S') + dir);
    }
}
