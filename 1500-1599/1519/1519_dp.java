import java.io.*;
import java.util.*;

public class Main {
    static final long OPEN = 1, CLOSE = 2; // the ends of a path piece, matched like brackets
    static final long FLIP = OPEN ^ CLOSE; // turns one end into the other
    static final int BITS = 2;             // bits per plug
    static final long MASK = 3;

    // the plug matching the bracket at pos, searching towards step
    static int partner(long state, int pos, int step) {
        for (int depth = 0;; pos += step) {
            long v = state >> (BITS * pos) & MASK;
            if (v == OPEN)
                depth += step;
            else if (v == CLOSE)
                depth -= step;
            if (depth == 0)
                return pos;
        }
    }

    static void add(HashMap<Long, Long> map, long state, long count) {
        map.merge(state, count, Long::sum);
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken()), m = Integer.parseInt(st.nextToken());
        boolean[][] free = new boolean[n + 1][m + 1];
        int last = 0;
        for (int i = 0; i < n;) {
            String row = br.readLine().trim();
            if (row.isEmpty())
                continue;
            for (int j = 0; j < m; j++)
                if (row.charAt(j) == '.') {
                    free[i][j] = true;
                    last = i * m + j;
                }
            i++;
        }
        // a state holds m + 1 plugs: plug j is the left side of the current cell
        // when j is its column, plug j + 1 its upper side; the rest are the lower
        // sides of the row above or this row
        HashMap<Long, Long> ways = new HashMap<>();
        ways.put(0L, 1L);
        long total = 0;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                HashMap<Long, Long> next = new HashMap<>(ways.size() * 2);
                int sl = BITS * j, su = BITS * (j + 1);
                long clear = ~(MASK << sl) & ~(MASK << su);
                boolean down = free[i + 1][j], right = free[i][j + 1];
                for (Map.Entry<Long, Long> e : ways.entrySet()) {
                    long state = e.getKey(), count = e.getValue();
                    long left = state >> sl & MASK, up = state >> su & MASK, base = state & clear;
                    if (!free[i][j]) {
                        if (left == 0 && up == 0)
                            add(next, state, count);
                    } else if (left == 0 && up == 0) {
                        if (down && right)
                            add(next, base | OPEN << sl | CLOSE << su, count);
                    } else if (left == 0 || up == 0) {
                        long end = left | up;
                        if (down)
                            add(next, base | end << sl, count);
                        if (right)
                            add(next, base | end << su, count);
                    } else if (left == up) {
                        // two openings or two closings: the far end of one of the
                        // joined pieces changes its kind
                        int far = left == OPEN ? partner(state, j + 1, 1) : partner(state, j, -1);
                        add(next, base ^ FLIP << (BITS * far), count);
                    } else if (left == CLOSE) {
                        add(next, base, count);
                    } else if (i * m + j == last && base == 0) {
                        total += count; // the loop closes on the last free cell
                    }
                }
                ways = next;
            }
            // the next row starts with an empty left plug
            HashMap<Long, Long> shifted = new HashMap<>(ways.size() * 2);
            for (Map.Entry<Long, Long> e : ways.entrySet())
                add(shifted, e.getKey() << BITS, e.getValue());
            ways = shifted;
        }
        System.out.println(total);
    }
}
