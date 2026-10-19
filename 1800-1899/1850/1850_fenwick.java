import java.io.DataInputStream;
import java.io.IOException;
import java.util.Arrays;

public class Main {
    static final int BUFFER_SIZE = 1 << 16;
    static DataInputStream in = new DataInputStream(System.in);
    static byte[] buffer = new byte[BUFFER_SIZE];
    static int length;
    static int index;

    static int read() throws IOException {
        if (index == length) {
            length = in.read(buffer, 0, BUFFER_SIZE);
            index = 0;
            if (length <= 0) {
                return -1;
            }
        }
        return buffer[index++];
    }

    static int number() throws IOException {
        int c = read();
        while (c < '0' || c > '9') {
            c = read();
        }
        int v = 0;
        while (c >= '0' && c <= '9') {
            v = v * 10 + (c - '0');
            c = read();
        }
        return v;
    }

    static int lowerBound(int[] a, int key) {
        int lo = 0;
        int hi = a.length;
        while (lo < hi) {
            int mid = (lo + hi) >>> 1;
            if (a[mid] < key) {
                lo = mid + 1;
            } else {
                hi = mid;
            }
        }
        return lo;
    }

    public static void main(String[] args) throws IOException {
        int n = number();
        int s = number();
        int d = number();
        long[] packed = new long[n];
        for (int i = 0; i < n; i++) {
            long distance = number();
            packed[i] = (distance << Integer.SIZE) | number();
        }
        Arrays.sort(packed);
        int[] dist = new int[n];
        int[] race = new int[n];
        for (int i = 0; i < n; i++) {
            dist[i] = (int) (packed[i] >>> Integer.SIZE);
            race[i] = (int) packed[i];
        }
        // pieces of planets with gaps of at most d: the tourist moves only
        // inside a piece cut by the range [low, high]
        int[] piece = new int[n];
        int[] first = new int[n + 1];
        int pieces = 1;
        for (int i = 1; i < n; i++) {
            if (dist[i] - dist[i - 1] > d) {
                first[pieces++] = i;
            }
            piece[i] = pieces - 1;
        }
        first[pieces] = n;
        // head[i]: races from the start of i's piece to i; tail[i]: from i
        // to its end; whole[p]: races of piece p
        int[] head = new int[n];
        int[] tail = new int[n];
        int[] whole = new int[pieces];
        int[] mark = new int[s + 1];
        Arrays.fill(mark, -1);
        for (int p = 0; p < pieces; p++) {
            int seen = 0;
            for (int i = first[p]; i < first[p + 1]; i++) {
                if (mark[race[i]] != p) {
                    mark[race[i]] = p;
                    seen++;
                }
                head[i] = seen;
            }
            whole[p] = seen;
            seen = 0;
            for (int i = first[p + 1] - 1; i >= first[p]; i--) {
                if (mark[race[i]] != -2 - p) {
                    mark[race[i]] = -2 - p;
                    seen++;
                }
                tail[i] = seen;
            }
        }
        // sparse table of the largest whole piece over ranges of pieces
        int levels = Integer.SIZE - Integer.numberOfLeadingZeros(pieces);
        int[][] table = new int[levels][];
        table[0] = whole;
        for (int k = 1; k < levels; k++) {
            int step = 1 << (k - 1);
            table[k] = new int[pieces - 2 * step + 1];
            for (int i = 0; i < table[k].length; i++) {
                table[k][i] = Math.max(table[k - 1][i], table[k - 1][i + step]);
            }
        }
        int m = number();
        int[] answer = new int[m];
        // ranges inside one piece, packed as right * 2^32 + tourist, and
        // their left ends
        long[] inside = new long[m];
        int[] insideLeft = new int[m];
        int count = 0;
        for (int t = 0; t < m; t++) {
            int low = number();
            int high = number();
            int lo = lowerBound(dist, low);
            int hi = lowerBound(dist, high + 1) - 1;
            if (lo > hi) {
                continue;
            }
            if (piece[lo] == piece[hi]) {
                insideLeft[t] = lo;
                inside[count++] = ((long) hi << Integer.SIZE) | t;
            } else {
                int best = Math.max(tail[lo], head[hi]);
                int a = piece[lo] + 1;
                int b = piece[hi];
                if (a < b) {
                    int level = Integer.SIZE - 1 - Integer.numberOfLeadingZeros(b - a);
                    best = Math.max(best, table[level][a]);
                    best = Math.max(best, table[level][b - (1 << level)]);
                }
                answer[t] = best;
            }
        }
        // distinct races in a range: going right, count each race only at
        // its latest planet, in a Fenwick tree
        Arrays.sort(inside, 0, count);
        int[] tree = new int[n + 1];
        int[] latest = new int[s + 1];
        Arrays.fill(latest, -1);
        int j = 0;
        for (int i = 0; i < n; i++) {
            if (latest[race[i]] >= 0) {
                for (int k = latest[race[i]] + 1; k <= n; k += k & -k) {
                    tree[k]--;
                }
            }
            latest[race[i]] = i;
            for (int k = i + 1; k <= n; k += k & -k) {
                tree[k]++;
            }
            for (; j < count && (int) (inside[j] >>> Integer.SIZE) == i; j++) {
                int t = (int) inside[j];
                int total = 0;
                for (int k = i + 1; k > 0; k -= k & -k) {
                    total += tree[k];
                }
                for (int k = insideLeft[t]; k > 0; k -= k & -k) {
                    total -= tree[k];
                }
                answer[t] = total;
            }
        }
        StringBuilder out = new StringBuilder();
        for (int a : answer) {
            out.append(a).append('\n');
        }
        System.out.print(out);
    }
}
