import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.Scanner;
import java.util.TreeMap;

public class Main {
    static final long MOD = 1000000000;
    static final int OPEN = 1, CLOSE = 2; // plugs are brackets: the two ends of one path
    static final int BITS = 2;            // a plug state keeps two bits per plug
    static final int MASK = (1 << BITS) - 1;
    static int width;

    static int get(int code, int k) { return code >> (BITS * k) & MASK; }

    static int with(int code, int k, int v) {
        return (code & ~(MASK << (BITS * k))) | v << (BITS * k);
    }

    // the bracket matching plug k: rightwards for an opening one, leftwards otherwise
    static int partner(int code, int k) {
        int step = get(code, k) == OPEN ? 1 : -1, depth = 0;
        for (int j = k;; j += step) {
            if (get(code, j) == get(code, k))
                depth++;
            else if (get(code, j) != 0)
                depth--;
            if (depth == 0)
                return j;
        }
    }

    static void add(Map<Integer, Long> to, int key, long ways) { to.merge(key, ways, Long::sum); }

    // run one row of cells over a plug state and return the states it can leave
    // below; plug c is the left plug of cell c, plug c + 1 its upper plug
    static Map<Integer, Long> rowMoves(int start, boolean last) {
        Map<Integer, Long> states = new HashMap<>();
        states.put(start << BITS, 1L);
        for (int c = 0; c < width; c++) {
            Map<Integer, Long> next = new HashMap<>();
            for (Map.Entry<Integer, Long> e : states.entrySet()) {
                int p = e.getKey();
                long ways = e.getValue();
                int left = get(p, c), up = get(p, c + 1);
                if (left == 0 && up == 0) {
                    if (c + 1 < width && !last) // a new path turning right and down
                        add(next, with(with(p, c, OPEN), c + 1, CLOSE), ways);
                } else if (left != 0 && up != 0) {
                    int q = p;
                    if (left == OPEN && up == CLOSE) {
                        // closing the cycle: only at the very last cell, with nothing else open
                        if (last && c == width - 1 && with(with(p, c, 0), c + 1, 0) == 0)
                            add(next, 0, ways);
                        continue;
                    }
                    if (left == OPEN && up == OPEN)
                        q = with(q, partner(q, c + 1), OPEN);
                    else if (left == CLOSE && up == CLOSE)
                        q = with(q, partner(q, c), CLOSE);
                    add(next, with(with(q, c, 0), c + 1, 0), ways);
                } else {
                    int plug = left + up;
                    if (!last)
                        add(next, with(with(p, c, plug), c + 1, 0), ways);
                    if (c + 1 < width)
                        add(next, with(with(p, c, 0), c + 1, plug), ways);
                }
            }
            states = next;
        }
        Map<Integer, Long> result = new TreeMap<>();
        for (Map.Entry<Integer, Long> e : states.entrySet())
            if (get(e.getKey(), width) == 0)
                result.put(e.getKey(), e.getValue() % MOD);
        return result;
    }

    static long[][] multiply(long[][] a, long[][] b) {
        int n = a.length;
        long[][] c = new long[n][n];
        for (int i = 0; i < n; i++)
            for (int k = 0; k < n; k++)
                if (a[i][k] != 0)
                    for (int j = 0; j < n; j++)
                        c[i][j] = (c[i][j] + a[i][k] * b[k][j]) % MOD;
        return c;
    }

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        width = in.nextInt();
        long height = in.nextLong();
        // every plug state that a row can leave behind, reached from the empty one
        Map<Integer, Integer> index = new HashMap<>();
        List<Integer> order = new ArrayList<>();
        index.put(0, 0);
        order.add(0);
        for (int i = 0; i < order.size(); i++)
            for (int t : rowMoves(order.get(i), false).keySet())
                if (!index.containsKey(t)) {
                    index.put(t, order.size());
                    order.add(t);
                }
        int size = order.size();
        long[][] step = new long[size][size], power = new long[size][size];
        for (int i = 0; i < size; i++) {
            power[i][i] = 1;
            for (Map.Entry<Integer, Long> e : rowMoves(order.get(i), false).entrySet())
                step[i][index.get(e.getKey())] = e.getValue();
        }
        // the first height - 1 rows by fast powering, then the last row that closes the cycle
        for (long e = height - 1; e > 0; e >>= 1) {
            if ((e & 1) == 1)
                power = multiply(power, step);
            step = multiply(step, step);
        }
        long total = 0;
        for (int i = 0; i < size; i++) {
            Long closed = rowMoves(order.get(i), true).get(0);
            if (closed != null)
                total = (total + power[0][i] * closed) % MOD;
        }
        System.out.println(2 * total % MOD); // every cycle can be walked in two directions
    }
}
