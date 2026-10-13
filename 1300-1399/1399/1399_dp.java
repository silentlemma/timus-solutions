import java.io.IOException;
import java.util.Arrays;

public class Main {
    static final int ROUNDS = 300000; // large neighbourhood search rounds
    static final int SHARE = 50;      // the first threshold is the first cost over this
    static final int MOST = 8;        // at most this many random items removed at once

    static final int BUFFER_SIZE = 65536;
    static final int KINDS = 3;          // removal kinds: random items, a whole trip, one client
    static final int UNREACHED = 0xFFFF; // no path yet in the subset table

    // xorshift64 from a fixed seed: the same numbers in every language
    static final long SEED = 88172645463325252L;
    static final int SHIFT_A = 13, SHIFT_B = 7, SHIFT_C = 17;

    static class Reader {
        final byte[] buffer = new byte[BUFFER_SIZE];
        int position, length;

        int read() throws IOException {
            if (position == length) {
                length = System.in.read(buffer);
                position = 0;
                if (length < 0)
                    return -1;
            }
            return buffer[position++];
        }

        int nextInt() throws IOException {
            int c;
            do {
                c = read();
            } while (c <= ' ');
            int value = 0;
            while (c > ' ') {
                value = value * 10 + c - '0';
                c = read();
            }
            return value;
        }
    }

    static long rngState = SEED;

    static int below(int k) {
        rngState ^= rngState << SHIFT_A;
        rngState ^= rngState >>> SHIFT_B;
        rngState ^= rngState << SHIFT_C;
        // Divide the nonnegative upper bits, then restore the low bit.
        int value = 2 * (int)((rngState >>> 1) % k) + (int)(rngState & 1);
        return value < k ? value : value - k;
    }

    static int m, n, cap;
    static int[][] dist;
    static int[] weight, client;
    static char[] tour; // the shortest round through each set of clients
    // Store only feasible subsets and their endpoints, in increasing client order.
    static char[] path;
    static int[] start;

    static int slot(int s, int j) { return start[s] + Integer.bitCount(s & ((1 << j) - 1)); }

    static int[] trip; // the trip of each item
    static int[] load = new int[0], clients = new int[0];
    static int[] perClient;
    static int trips; // trips in use, emptied ones included
    static long cost;

    static void put(int i, int t) {
        if (t == trips)
            trips++;
        trip[i] = t;
        load[t] += weight[i];
        if (perClient[t * m + client[i]]++ == 0) {
            cost -= tour[clients[t]];
            clients[t] |= 1 << client[i];
            cost += tour[clients[t]];
        }
    }

    static void take(int i) {
        int t = trip[i];
        load[t] -= weight[i];
        if (--perClient[t * m + client[i]] == 0) {
            cost -= tour[clients[t]];
            clients[t] &= ~(1 << client[i]);
            cost += tour[clients[t]];
        }
        trip[i] = -1;
    }

    // the cheapest place for item i, an existing trip or a new one: the first
    // trip that costs no more than a new one, so that emptied trips are reused
    static void insertBest(int i) {
        int fresh = trips, best = fresh, bit = 1 << client[i], extra = tour[bit];
        for (int t = 0; t < fresh; t++) {
            if (load[t] + weight[i] > cap)
                continue;
            int d = tour[clients[t] | bit] - tour[clients[t]];
            if (d < extra || (d == extra && best == fresh)) {
                extra = d;
                best = t;
                if (extra == 0)
                    break;
            }
        }
        put(i, best);
    }

    public static void main(String[] args) throws IOException {
        Reader in = new Reader();
        m = in.nextInt();
        n = in.nextInt();
        cap = in.nextInt();
        dist = new int[m + 1][m + 1];
        for (int i = 0; i <= m; i++)
            for (int j = 0; j <= m; j++)
                dist[i][j] = in.nextInt();
        weight = new int[n];
        client = new int[n];
        boolean[] active = new boolean[m];
        int[] minimum = new int[m];
        Arrays.fill(minimum, cap + 1);
        int totalWeight = 0, lightest = cap + 1, second = cap + 1;
        for (int i = 0; i < n; i++) {
            weight[i] = in.nextInt();
            client[i] = in.nextInt() - 1;
            active[client[i]] = true;
            minimum[client[i]] = Math.min(minimum[client[i]], weight[i]);
            totalWeight += weight[i];
            if (weight[i] < lightest) {
                second = lightest;
                lightest = weight[i];
            } else {
                second = Math.min(second, weight[i]);
            }
        }
        int[] original = new int[m], remap = new int[m];
        int countActive = 0;
        for (int j = 0; j < m; j++)
            if (active[j]) {
                remap[j] = countActive;
                original[countActive++] = j + 1;
            }
        int[][] reduced = new int[countActive + 1][countActive + 1];
        int[] minWeight = new int[countActive], clientWeight = new int[countActive];
        for (int j = 0; j < countActive; j++) {
            int c = original[j];
            minWeight[j] = minimum[c - 1];
            reduced[0][j + 1] = dist[0][c];
            reduced[j + 1][0] = dist[c][0];
            for (int k = 0; k < countActive; k++)
                reduced[j + 1][k + 1] = dist[c][original[k]];
        }
        for (int i = 0; i < n; i++) {
            client[i] = remap[client[i]];
            clientWeight[client[i]] += weight[i];
        }
        dist = reduced;
        m = countActive;
        // Held-Karp over the clients: shortest walks from the depot through every subset
        int full = 1 << m;
        start = new int[full + 1];
        // Initially the tour table holds minimum loads, consumed in subset order.
        tour = new char[full];
        for (int s = 1; s < full; s++) {
            int bit = Integer.lowestOneBit(s);
            tour[s] = (char)(tour[s ^ bit] + minWeight[Integer.numberOfTrailingZeros(bit)]);
            start[s + 1] = start[s];
            if (tour[s] <= cap)
                start[s + 1] += Integer.bitCount(s);
        }
        path = new char[start[full]];
        int[][] into = new int[m][m]; // into[k][j]: from client j to client k
        for (int k = 0; k < m; k++)
            for (int j = 0; j < m; j++)
                into[k][j] = dist[j + 1][k + 1];
        // a walk through t ending at k comes from a walk through t without k:
        // all of those lie together, so the table is read and written in order
        for (int t = 1; t < full; t++) {
            if (tour[t] > cap) {
                tour[t] = 0;
                continue;
            }
            int best = UNREACHED, at = start[t];
            for (int ks = t; ks != 0; ks &= ks - 1, at++) {
                int k = Integer.numberOfTrailingZeros(ks), s = t ^ 1 << k;
                int v = UNREACHED;
                if (s == 0) {
                    v = dist[0][k + 1];
                } else {
                    int[] row = into[k];
                    int from = start[s];
                    for (int js = s; js != 0; js &= js - 1, from++) {
                        int w = path[from] + row[Integer.numberOfTrailingZeros(js)];
                        if (w < v)
                            v = w;
                    }
                }
                path[at] = (char)v;
                best = Math.min(best, v + dist[k + 1][0]);
            }
            tour[t] = (char)best;
        }
        // a first plan by cheapest insertion; then rounds of removing some items
        // and putting them back in the cheapest places, undone when the cost grows
        // by more than a threshold that falls to zero
        load = new int[n];
        clients = new int[n];
        perClient = new int[n * m];
        trip = new int[n];
        Arrays.fill(trip, -1);
        for (int i = 0; i < n; i++)
            insertBest(i);
        int[] bestTrip = trip.clone(), removed = new int[n], oldTrip = new int[n];
        long bestCost = cost, start = cost;
        long lower = 0;
        for (int c = 0; c < m; c++)
            lower = Math.max(lower, 2L * dist[0][c + 1] *
                             ((clientWeight[c] + cap - 1) / cap));
        if (trips == 1 || totalWeight <= cap || lightest + second > cap)
            lower = cost;
        int rounds = cost == lower ? 0 : ROUNDS;
        for (int round = 0; round < rounds; round++) {
            long before = cost;
            int size = 0;
            int kind = below(KINDS), count = 1 + below(Math.min(n, MOST));
            int pick = below(n), target = kind == 1 ? trip[pick] : client[pick];
            for (int i = 0; i < n; i++)
                if ((kind == 1 && trip[i] == target) || (kind == 2 && client[i] == target)) {
                    removed[size] = i;
                    oldTrip[size++] = trip[i];
                }
            for (int k = 0; kind == 0 && k < count; k++) {
                int i = below(n);
                boolean seen = false;
                for (int r = 0; r < size; r++)
                    seen |= removed[r] == i;
                if (!seen) {
                    removed[size] = i;
                    oldTrip[size++] = trip[i];
                }
            }
            for (int k = 0; k < size; k++)
                take(removed[k]);
            for (int k = size - 1; k > 0; k--) {
                int r = below(k + 1), a = removed[k], b = oldTrip[k];
                removed[k] = removed[r];
                removed[r] = a;
                oldTrip[k] = oldTrip[r];
                oldTrip[r] = b;
            }
            for (int k = 0; k < size; k++)
                insertBest(removed[k]);
            long threshold = start * (ROUNDS - round) / ROUNDS / SHARE;
            if (cost > before + threshold) {
                for (int k = 0; k < size; k++)
                    take(removed[k]);
                for (int k = 0; k < size; k++)
                    put(removed[k], oldTrip[k]);
            }
            if (cost < bestCost) {
                bestCost = cost;
                bestTrip = trip.clone();
            }
        }
        // rebuild the best plan and print its non-empty trips, each route
        // recovered from the subset table
        int count = 0;
        for (int t : bestTrip)
            count = Math.max(count, t + 1);
        trips = count;
        load = new int[count];
        clients = new int[count];
        perClient = new int[count * m];
        cost = 0;
        for (int i = 0; i < n; i++)
            put(i, bestTrip[i]);
        StringBuilder out = new StringBuilder();
        int used = 0;
        for (int t = 0; t < count; t++)
            if (clients[t] != 0)
                used++;
        out.append(used).append("\n\n");
        long total = 0;
        int[] route = new int[m];
        for (int t = 0; t < count; t++) {
            if (clients[t] == 0)
                continue;
            boolean first = true;
            for (int i = 0; i < n; i++)
                if (trip[i] == t) {
                    out.append(first ? "" : " ").append(i + 1);
                    first = false;
                }
            out.append('\n').append(load[t]).append('\n');
            int s = clients[t], length = tour[s], last = -1;
            for (int j = 0; j < m && last < 0; j++)
                if ((s >> j & 1) == 1 && path[slot(s, j)] + dist[j + 1][0] == length)
                    last = j;
            int routeSize = 0;
            while (s != 0) {
                route[routeSize++] = original[last];
                int prev = -1, rest = s & ~(1 << last);
                for (int j = 0; j < m && rest != 0 && prev < 0; j++)
                    if ((rest >> j & 1) == 1 &&
                        path[slot(rest, j)] + dist[j + 1][last + 1] == path[slot(s, last)])
                        prev = j;
                s = rest;
                last = prev;
            }
            out.append('0');
            for (int k = routeSize - 1; k >= 0; k--)
                out.append(' ').append(route[k]);
            out.append(" 0\n").append(length).append("\n\n");
            total += length;
        }
        out.append(total).append('\n');
        System.out.write(out.toString().getBytes("US-ASCII"));
    }
}
