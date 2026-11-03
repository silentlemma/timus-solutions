import java.io.IOException;
import java.util.Arrays;

public class Main {
    static final int RADIX = 1000000000, LIMB_DIGITS = 9, RATE_DIGITS = 2, DECIMAL_SCALE = 100;
    static final int BUFFER_SIZE = 4096;
    static final byte[] input = new byte[BUFFER_SIZE];
    static int position, available;

    static int read() throws IOException {
        if (position == available) {
            available = System.in.read(input);
            position = 0;
            if (available < 0)
                return -1;
        }
        return input[position++];
    }

    static String token() throws IOException {
        int c = read();
        while (c >= 0 && c <= ' ')
            c = read();
        StringBuilder text = new StringBuilder();
        while (c > ' ') {
            text.append((char)c);
            c = read();
        }
        return text.toString();
    }

    static String scaled(String text, int places) {
        if (text.startsWith("+"))
            text = text.substring(1);
        int dot = text.indexOf('.');
        int fractional = dot < 0 ? 0 : text.length() - dot - 1;
        StringBuilder result = new StringBuilder(text.replace(".", ""));
        for (int i = fractional; i < places; i++)
            result.append('0');
        return result.toString();
    }

    static class Amount {
        int[] digits = new int[1];
        int size = 1;

        Amount() {}

        Amount(String text) {
            ensure((text.length() + LIMB_DIGITS - 1) / LIMB_DIGITS);
            size = 0;
            for (int end = text.length(); end > 0; end -= LIMB_DIGITS)
                digits[size++] =
                    Integer.parseInt(text.substring(Math.max(0, end - LIMB_DIGITS), end));
            trim();
        }

        void ensure(int count) {
            if (digits.length < count)
                digits = Arrays.copyOf(digits, Math.max(count, 2 * digits.length));
        }

        void trim() {
            while (size > 1 && digits[size - 1] == 0)
                size--;
        }

        boolean zero() { return size == 1 && digits[0] == 0; }

        void set(Amount value) {
            ensure(value.size);
            System.arraycopy(value.digits, 0, digits, 0, value.size);
            size = value.size;
        }

        int compare(Amount value) {
            if (size != value.size)
                return Integer.compare(size, value.size);
            for (int i = size - 1; i >= 0; i--)
                if (digits[i] != value.digits[i])
                    return Integer.compare(digits[i], value.digits[i]);
            return 0;
        }

        void multiply(Amount value, int factor) {
            int count = value.size;
            ensure(count + 2);
            long carry = 0;
            // Limb*factor is below10^13. Consume each old limb before writing,
            // so destination==source multiplication is safe too.
            for (int i = 0; i < count; i++) {
                carry += (long)value.digits[i] * factor;
                digits[i] = (int)(carry % RADIX);
                carry /= RADIX;
            }
            size = count;
            while (carry != 0) {
                digits[size++] = (int)(carry % RADIX);
                carry /= RADIX;
            }
            trim();
        }

        void subtract(Amount a, Amount b) {
            ensure(a.size);
            long borrow = 0;
            for (int i = 0; i < a.size; i++) {
                long take = borrow + (i < b.size ? b.digits[i] : 0);
                if (a.digits[i] < take) {
                    digits[i] = (int)((long)RADIX + a.digits[i] - take);
                    borrow = 1;
                } else {
                    digits[i] = (int)(a.digits[i] - take);
                    borrow = 0;
                }
            }
            size = a.size;
            trim();
        }
    }

    static int root(int[] parent, int v) {
        while (parent[v] != v) {
            parent[v] = parent[parent[v]];
            v = parent[v];
        }
        return v;
    }

    static class Edge {
        int from, to, rate, fee;
        Edge(int from, int to, int rate, int fee) {
            this.from = from;
            this.to = to;
            this.rate = rate;
            this.fee = fee;
        }
    }

    public static void main(String[] args) throws Exception {
        int n = Integer.parseInt(token()), m = Integer.parseInt(token()),
            start = Integer.parseInt(token()) - 1;
        String text = token();
        int dot = text.indexOf('.');
        int places = Math.max(RATE_DIGITS, dot < 0 ? 0 : text.length() - dot - 1);
        Amount initial = new Amount(scaled(text, places));
        // Zero remains zero or makes the next exchange unaffordable.
        if (initial.zero()) {
            System.out.println("NO");
            return;
        }
        StringBuilder unitText = new StringBuilder("1");
        for (int i = RATE_DIGITS; i < places; i++)
            unitText.append('0');
        Amount unit = new Amount(unitText.toString());
        int[] parent = new int[n];
        for (int i = 0; i < n; i++)
            parent[i] = i;
        Edge[] edges = new Edge[2 * m];
        for (int i = 0; i < m; i++) {
            int a = Integer.parseInt(token()) - 1, b = Integer.parseInt(token()) - 1;
            int rab = Integer.parseInt(scaled(token(), RATE_DIGITS));
            int cab = Integer.parseInt(scaled(token(), RATE_DIGITS));
            int rba = Integer.parseInt(scaled(token(), RATE_DIGITS));
            int cba = Integer.parseInt(scaled(token(), RATE_DIGITS));
            parent[root(parent, a)] = root(parent, b);
            edges[2 * i] = new Edge(a, b, rab, cab);
            edges[2 * i + 1] = new Edge(b, a, rba, cba);
        }
        int component = root(parent, start), count = 0;
        int[] index = new int[n];
        Arrays.fill(index, -1);
        for (int i = 0; i < n; i++)
            if (root(parent, i) == component)
                index[i] = count++;
        int kept = 0;
        for (Edge edge : edges)
            if (index[edge.from] >= 0) {
                edge.from = index[edge.from];
                edge.to = index[edge.to];
                edges[kept++] = edge;
            }
        start = index[start];
        Amount[] best = new Amount[count], after = new Amount[count];
        for (int i = 0; i < count; i++) {
            best[i] = new Amount();
            after[i] = new Amount();
        }
        boolean[] reached = new boolean[count], next = new boolean[count];
        reached[start] = true;
        best[start].set(initial);
        Amount cost = new Amount(), got = new Amount();
        boolean changed = false;
        // Reuse owned limb buffers. Only previous-pass best values feed edges.
        // Compressing to the source component makes count passes sufficient.
        for (int pass = 0; pass < count; pass++) {
            for (int i = 0; i < count; i++)
                if (reached[i])
                    after[i].multiply(best[i], DECIMAL_SCALE);
            System.arraycopy(reached, 0, next, 0, count);
            changed = false;
            for (int i = 0; i < kept; i++) {
                Edge edge = edges[i];
                if (!reached[edge.from])
                    continue;
                if (edge.fee == 0)
                    got.multiply(best[edge.from], edge.rate);
                else {
                    cost.multiply(unit, edge.fee);
                    if (best[edge.from].compare(cost) < 0)
                        continue;
                    got.subtract(best[edge.from], cost);
                    got.multiply(got, edge.rate);
                }
                if (!next[edge.to] || after[edge.to].compare(got) < 0) {
                    after[edge.to].set(got);
                    next[edge.to] = true;
                    changed = true;
                }
            }
            Amount[] swap = best;
            best = after;
            after = swap;
            boolean[] flags = reached;
            reached = next;
            next = flags;
            unit.multiply(unit, DECIMAL_SCALE);
            initial.multiply(initial, DECIMAL_SCALE);
            if (best[start].compare(initial) > 0 || !changed)
                break;
        }
        System.out.println(best[start].compare(initial) > 0 || changed ? "YES" : "NO");
    }
}
