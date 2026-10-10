import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.StreamTokenizer;
import java.util.Arrays;

public class Main {
    // the local search stops after this many improvements
    static final int ROUNDS = 20000;
    // an exact split of two generals may use at most this many bits of tables
    static final long SPLIT_BITS = 4000000;
    static final int WORD = 64;
    // a box is its value shifted by INDEX_BITS, plus its number
    static final int INDEX_BITS = 14;
    static final int INDEX_MASK = (1 << INDEX_BITS) - 1;
    // a general in a sort key is below GENERAL_BITS; values are at most TOP
    static final int GENERAL_BITS = 10;
    static final long TOP = 1000;

    // Only primitive arrays, allocated once where possible: under the 4 MB
    // limit, boxed numbers and short-lived tables make the heap grow too far.
    static long[] sums;
    static int[][] boxes; // sorted, per general
    static int[] sizes;
    static long[] reach = new long[(int)(SPLIT_BITS / WORD) + 1];
    static int[] items;

    static int lowerBound(int g, int key) {
        int lo = 0, hi = sizes[g];
        while (lo < hi) {
            int mid = (lo + hi) >>> 1;
            if (boxes[g][mid] < key) {
                lo = mid + 1;
            } else {
                hi = mid;
            }
        }
        return lo;
    }

    static void put(int g, int b) {
        if (sizes[g] == boxes[g].length) {
            boxes[g] = Arrays.copyOf(boxes[g], 2 * sizes[g] + 1);
        }
        int k = lowerBound(g, b);
        System.arraycopy(boxes[g], k, boxes[g], k + 1, sizes[g] - k);
        boxes[g][k] = b;
        sizes[g]++;
    }

    static int take(int g, int k) {
        int b = boxes[g][k];
        System.arraycopy(boxes[g], k + 1, boxes[g], k, sizes[g] - k - 1);
        sizes[g]--;
        return b;
    }

    // the move or swap of boxes from hi to lo that leaves the smallest gap
    // between the two, if it is smaller than now
    static boolean exchange(int hi, int lo) {
        long d = sums[hi] - sums[lo];
        if (d <= 1) {
            return false;
        }
        long best = d;
        int bestA = -1, bestB = -1, half = (int)(d / 2);
        int[] a = boxes[hi], b = boxes[lo];
        int na = sizes[hi], nb = sizes[lo];
        if (na > 1) {
            int k = lowerBound(hi, half << INDEX_BITS);
            for (int ia = Math.max(k - 1, 0); ia <= k && ia < na; ia++) {
                long t = a[ia] >> INDEX_BITS;
                if (t > 0 && t < d && Math.abs(d - 2 * t) < best) {
                    best = Math.abs(d - 2 * t);
                    bestA = ia;
                    bestB = -1;
                }
            }
        }
        for (int ia = 0; ia < na; ia++) {
            int va = a[ia] >> INDEX_BITS;
            if (ia > 0 && va == a[ia - 1] >> INDEX_BITS) {
                continue;
            }
            int k = lowerBound(lo, (va - half) << INDEX_BITS);
            for (int ib = Math.max(k - 1, 0); ib <= k && ib < nb; ib++) {
                long t = va - (b[ib] >> INDEX_BITS);
                if (t > 0 && t < d && Math.abs(d - 2 * t) < best) {
                    best = Math.abs(d - 2 * t);
                    bestA = ia;
                    bestB = ib;
                }
            }
        }
        if (bestA < 0) {
            return false;
        }
        int x = take(hi, bestA);
        sums[hi] -= x >> INDEX_BITS;
        sums[lo] += x >> INDEX_BITS;
        if (bestB >= 0) {
            int y = take(lo, bestB);
            put(hi, y);
            sums[hi] += y >> INDEX_BITS;
            sums[lo] -= y >> INDEX_BITS;
        }
        put(lo, x);
        return true;
    }

    static boolean has(int row, int words, long t) {
        return (reach[row * words + (int)(t / WORD)] >>> (t % WORD) & 1) == 1;
    }

    // the most even split of the boxes of hi and lo found by subset sums, if
    // it narrows their gap and leaves each general a box
    static boolean split(int hi, int lo) {
        int count = sizes[hi] + sizes[lo];
        long total = sums[hi] + sums[lo];
        int words = (int)(total / WORD) + 1;
        if ((long)(count + 1) * words * WORD > SPLIT_BITS) {
            return false;
        }
        System.arraycopy(boxes[hi], 0, items, 0, sizes[hi]);
        System.arraycopy(boxes[lo], 0, items, sizes[hi], sizes[lo]);
        Arrays.fill(reach, 0, words, 0);
        reach[0] = 1;
        for (int k = 0; k < count; k++) {
            int v = items[k] >> INDEX_BITS, shift = v / WORD, bits = v % WORD;
            int from = k * words, to = from + words;
            for (int w = 0; w < words; w++) {
                long moved = 0;
                if (w - shift >= 0) {
                    moved = reach[from + w - shift] << bits;
                    if (bits > 0 && w - shift - 1 >= 0) {
                        moved |= reach[from + w - shift - 1] >>> (WORD - bits);
                    }
                }
                reach[to + w] = reach[from + w] | moved;
            }
        }
        long t = total / 2;
        while (t > 0 && !has(count, words, t)) {
            t--;
        }
        if (t == 0 || total - 2 * t >= sums[hi] - sums[lo]) {
            return false;
        }
        int[] small = new int[count], big = new int[count];
        int ns = 0, nb = 0;
        long rest = t;
        for (int k = count - 1; k >= 0; k--) {
            if (!has(k, words, rest)) {
                small[ns++] = items[k];
                rest -= items[k] >> INDEX_BITS;
            } else {
                big[nb++] = items[k];
            }
        }
        if (ns == 0 || nb == 0) {
            return false;
        }
        Arrays.sort(small, 0, ns);
        Arrays.sort(big, 0, nb);
        boxes[hi] = big;
        sizes[hi] = nb;
        boxes[lo] = small;
        sizes[lo] = ns;
        sums[hi] = total - t;
        sums[lo] = t;
        return true;
    }

    public static void main(String[] args) throws IOException {
        StreamTokenizer in =
            new StreamTokenizer(new BufferedReader(new InputStreamReader(System.in)));
        in.nextToken();
        int n = (int)in.nval;
        in.nextToken();
        int m = (int)in.nval;
        in.nextToken();
        long limit = (long)in.nval;
        int[] value = new int[n];
        for (int i = 0; i < n; i++) {
            in.nextToken();
            value[i] = (int)in.nval;
        }
        items = new int[n];
        // largest boxes first, each to the general with the least gold so far
        // (the smaller number on ties)
        long[] order = new long[n];
        for (int i = 0; i < n; i++) {
            order[i] = (TOP - value[i]) << INDEX_BITS | i;
        }
        Arrays.sort(order);
        sums = new long[m];
        boxes = new int[m][];
        sizes = new int[m];
        for (int g = 0; g < m; g++) {
            boxes[g] = new int[1];
        }
        for (long key : order) {
            int i = (int)(key & INDEX_MASK), g = 0;
            for (int h = 1; h < m; h++) {
                if (sums[h] < sums[g]) {
                    g = h;
                }
            }
            put(g, value[i] << INDEX_BITS | i);
            sums[g] += value[i];
        }
        // then even out the richest and the poorest general against the others
        long[] up = new long[m], down = new long[m];
        int mask = (1 << GENERAL_BITS) - 1;
        for (int round = 0; round < ROUNDS; round++) {
            int hi = 0, lo = 0;
            for (int g = 0; g < m; g++) {
                if (sums[g] > sums[hi]) {
                    hi = g;
                }
                if (sums[g] < sums[lo]) {
                    lo = g;
                }
            }
            if (sums[hi] - sums[lo] <= limit) {
                break;
            }
            if (exchange(hi, lo)) {
                continue;
            }
            // generals from the poorest and from the richest, the smaller
            // number first among equals
            for (int g = 0; g < m; g++) {
                up[g] = sums[g] << GENERAL_BITS | g;
                down[g] = (sums[hi] - sums[g]) << GENERAL_BITS | g;
            }
            Arrays.sort(up);
            Arrays.sort(down);
            boolean moved = false;
            for (long key : up) {
                int g = (int)(key & mask);
                if (!moved && g != hi) {
                    moved = exchange(hi, g);
                }
            }
            for (long key : down) {
                int g = (int)(key & mask);
                if (!moved && g != lo) {
                    moved = exchange(g, lo);
                }
            }
            moved = moved || split(hi, lo);
            for (long key : up) {
                int g = (int)(key & mask);
                if (!moved && g != hi) {
                    moved = split(hi, g);
                }
            }
            for (long key : down) {
                int g = (int)(key & mask);
                if (!moved && g != lo) {
                    moved = split(g, lo);
                }
            }
            if (!moved) {
                break;
            }
        }
        long most = sums[0], least = sums[0];
        for (long s : sums) {
            most = Math.max(most, s);
            least = Math.min(least, s);
        }
        StringBuilder out = new StringBuilder().append(most - least).append('\n');
        for (int g = 0; g < m; g++) {
            int[] ids = new int[sizes[g]];
            for (int k = 0; k < ids.length; k++) {
                ids[k] = (boxes[g][k] & INDEX_MASK) + 1;
            }
            Arrays.sort(ids);
            for (int k = 0; k < ids.length; k++) {
                out.append(k > 0 ? " " : "").append(ids[k]);
            }
            out.append('\n');
        }
        System.out.print(out);
    }
}
