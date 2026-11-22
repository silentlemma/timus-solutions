import java.util.Arrays;
public class Main {
    static final int RADIX = 1000000000, LIMB_DIGITS = 9, RATE_DIGITS = 2, DECIMAL_SCALE = 100;
    static final int BUFFER_SIZE = 1024, DECIMAL = 10;
    static final byte[] input = new byte[BUFFER_SIZE];
    static int position, available;
    static int read() throws java.io.IOException {
        if (position == available) {
            available = System.in.read(input);
            position = 0;
            if (available < 0)
                return -1;
        }
        return input[position++];
    }
    static int nextInt() throws java.io.IOException {
        int c = read();
        while (c >= 0 && c <= ' ')
            c = read();
        if (c == '+')
            c = read();
        int value = 0;
        while (c >= '0' && c <= '9') {
            value = value * DECIMAL + c - '0';
            c = read();
        }
        return value;
    }
    static int hundredths() throws java.io.IOException {
        int c = read();
        while (c >= 0 && c <= ' ')
            c = read();
        if (c == '+')
            c = read();
        int value = 0;
        while (c >= '0' && c <= '9') {
            value = value * DECIMAL + c - '0';
            c = read();
        }
        value *= DECIMAL_SCALE;
        if (c == '.') {
            int scale = DECIMAL_SCALE;
            for (c = read(); c >= '0' && c <= '9'; c = read()) {
                scale /= DECIMAL;
                value += (c - '0') * scale;
            }
        }
        return value;
    }
    static void answer(boolean yes) {
        if (yes) {
            System.out.write('Y');
            System.out.write('E');
            System.out.write('S');
        } else {
            System.out.write('N');
            System.out.write('O');
        }
        System.out.write('\n');
        System.out.flush();
    }
    static class Amount {
        int[] digits = new int[1];
        int size = 1;

        Amount() {}

        Amount(byte[] text, int length, int pad) {
            ensure((length + pad + LIMB_DIGITS - 1) / LIMB_DIGITS);
            size = 0;
            int value = 0, multiplier = 1, used = 0;
            for (int i = 0; i < pad; i++) {
                multiplier *= 10;
                used++;
            }
            for (int i = length - 1; i >= 0; i--) {
                if (text[i] < '0' || text[i] > '9')
                    continue;
                value += (text[i] - '0') * multiplier;
                if (++used == LIMB_DIGITS) {
                    digits[size++] = value;
                    value = 0;
                    multiplier = 1;
                    used = 0;
                } else {
                    multiplier *= 10;
                }
            }
            if (used != 0)
                digits[size++] = value;
            if (size == 0)
                size = 1;
            trim();
        }
        static Amount powerTen(int exponent) {
            Amount value = new Amount();
            int offset = exponent / LIMB_DIGITS, digit = 1;
            for (int i = 0; i < exponent % LIMB_DIGITS; i++)
                digit *= 10;
            value.ensure(offset + 1);
            value.size = offset + 1;
            value.digits[offset] = digit;
            return value;
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
                return size - value.size;
            for (int i = size - 1; i >= 0; i--)
                if (digits[i] != value.digits[i])
                    return digits[i] - value.digits[i];
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

    public static void main(String[] args) throws Exception {

        int n = nextInt(), m = nextInt(), start = nextInt() - 1;
        byte[] capital = new byte[BUFFER_SIZE];
        int length = 0, fractional = 0, c = read();
        boolean dot = false;
        while (c >= 0 && c <= ' ')
            c = read();
        while (c > ' ') {
            if (length == capital.length)
                capital = Arrays.copyOf(capital, 2 * capital.length);
            capital[length++] = (byte)c;
            if (c == '.')
                dot = true;
            else if (dot)
                fractional++;
            c = read();
        }
        int places = Math.max(RATE_DIGITS, fractional);
        Amount initial = new Amount(capital, length, places - fractional);
        if (initial.zero()) {
            answer(false);
            return;
        }
        Amount unit = Amount.powerTen(places - RATE_DIGITS);
        int[] parent = new int[n];
        for (int i = 0; i < n; i++)
            parent[i] = i;
        int[] from = new int[2 * m], to = new int[2 * m];
        int[] rates = new int[2 * m], fees = new int[2 * m];
        for (int i = 0; i < m; i++) {
            int a = nextInt() - 1, b = nextInt() - 1;
            int rab = hundredths();
            int cab = hundredths();
            int rba = hundredths();
            int cba = hundredths();
            parent[root(parent, a)] = root(parent, b);
            from[2 * i] = a;
            to[2 * i] = b;
            rates[2 * i] = rab;
            fees[2 * i] = cab;
            from[2 * i + 1] = b;
            to[2 * i + 1] = a;
            rates[2 * i + 1] = rba;
            fees[2 * i + 1] = cba;
        }
        int component = root(parent, start), count = 0;
        int[] index = new int[n];
        Arrays.fill(index, -1);
        for (int i = 0; i < n; i++)
            if (root(parent, i) == component)
                index[i] = count++;
        int kept = 0;
        for (int i = 0; i < 2 * m; i++)
            if (index[from[i]] >= 0) {
                from[kept] = index[from[i]];
                to[kept] = index[to[i]];
                rates[kept] = rates[i];
                fees[kept++] = fees[i];
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
                int source = from[i], destination = to[i];
                if (!reached[source])
                    continue;
                if (fees[i] == 0)
                    got.multiply(best[source], rates[i]);
                else {
                    cost.multiply(unit, fees[i]);
                    if (best[source].compare(cost) < 0)
                        continue;
                    got.subtract(best[source], cost);
                    got.multiply(got, rates[i]);
                }
                if (!next[destination] || after[destination].compare(got) < 0) {
                    after[destination].set(got);
                    next[destination] = true;
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
        answer(best[start].compare(initial) > 0 || changed);
    }
}
