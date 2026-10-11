import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    static final int FIRST_SIZE = 4; // each bucket starts small and doubles
    static BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer words = new StringTokenizer("");

    static String next() throws IOException {
        while (!words.hasMoreTokens())
            words = new StringTokenizer(in.readLine());
        return words.nextToken();
    }

    public static void main(String[] args) throws IOException {
        int w = Integer.parseInt(next()), h = Integer.parseInt(next());
        int x = Integer.parseInt(next()), y = Integer.parseInt(next()),
            d = Integer.parseInt(next());
        boolean[] open = new boolean[w * h], wet = new boolean[w * h];
        for (int r = 0; r < h; r++) {
            String row = next();
            for (int c = 0; c < w; c++)
                open[r * w + c] = row.charAt(c) != '#';
        }
        // water reaches a cell that has a way to the surface without going down,
        // so search back from the top row: down, left and right
        int[] stack = new int[w * h];
        int top = 0;
        for (int c = 0; c < w; c++) {
            if (open[c]) {
                wet[c] = true;
                stack[top++] = c;
            }
        }
        while (top > 0) {
            int cell = stack[--top], r = cell / w, c = cell % w;
            int[] next = {r + 1 < h ? cell + w : -1, c > 0 ? cell - 1 : -1,
                          c + 1 < w ? cell + 1 : -1};
            for (int n : next) {
                if (n >= 0 && open[n] && !wet[n]) {
                    wet[n] = true;
                    stack[top++] = n;
                }
            }
        }
        // label: moves made under water since the last breath; an air pocket
        // resets it to 0, and no stretch under water may take more than D moves
        int start = (h - y) * w + (x - 1);
        int[] label = new int[w * h];
        java.util.Arrays.fill(label, d + 1);
        int[][] buckets = new int[d + 1][];
        int[] sizes = new int[d + 1];
        for (int i = 0; i <= d; i++)
            buckets[i] = new int[FIRST_SIZE];
        label[start] = 0;
        buckets[0][sizes[0]++] = start;
        for (int level = 0; level <= d;) {
            if (sizes[level] == 0) {
                level++;
                continue;
            }
            int cell = buckets[level][--sizes[level]];
            int here = label[cell];
            if (here != level)
                continue;
            int r = cell / w, c = cell % w;
            if (r == 0 && here + 1 <= d) {
                System.out.println("Can be rescued by himself");
                return;
            }
            int[] next = {r > 0 ? cell - w : -1, r + 1 < h ? cell + w : -1, c > 0 ? cell - 1 : -1,
                          c + 1 < w ? cell + 1 : -1};
            for (int n : next) {
                if (n < 0 || !open[n])
                    continue;
                int nl = 0;
                if (wet[n]) {
                    nl = here + 1;
                } else if (wet[cell] && here + 1 > d) {
                    continue;
                }
                if (nl <= d && nl < label[n]) {
                    label[n] = nl;
                    if (sizes[nl] == buckets[nl].length) {
                        buckets[nl] = java.util.Arrays.copyOf(buckets[nl], 2 * sizes[nl]);
                    }
                    buckets[nl][sizes[nl]++] = n;
                    if (nl < level)
                        level = nl;
                }
            }
        }
        System.out.println("Rescue operation required");
    }
}
