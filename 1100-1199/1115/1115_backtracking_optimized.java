public class Main {

    static final int INPUT_SIZE = 1024, OUTPUT_SIZE = 1024, DIGITS = 10, DECIMAL = 10;
    static final byte[] input = new byte[INPUT_SIZE], output = new byte[OUTPUT_SIZE],
                        digits = new byte[DIGITS];
    static int position, available, used;
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
        int value = 0;
        while (c >= '0' && c <= '9') {
            value = value * DECIMAL + c - '0';
            c = read();
        }
        return value;
    }
    static void write(int c) {
        if (used == output.length) {
            System.out.write(output, 0, used);
            used = 0;
        }
        output[used++] = (byte)c;
    }
    static void number(int value) {
        if (value < 0) {
            write('-');
            value = -value;
        }
        int length = 0;
        do {
            digits[length++] = (byte)('0' + value % DECIMAL);
            value /= DECIMAL;
        } while (value != 0);
        while (length > 0)
            write(digits[--length]);
    }
    static void finish() { System.out.write(output, 0, used); }

    static final int BITS = 64, SEARCH_LIMIT = 256, ATTEMPTS = 128, RNG_MOD = 65536;
    static final int RNG_MULTIPLIER = 97, MAX_SHIP_LENGTH = 100;
    static int n, m, calls;
    static boolean limited;
    static int[] ships, rows, order, owner;
    static int[][] freeWorkspace;
    static long[][] workspace;

    static boolean has(long[] reach, int words, int index, int value) {
        return (reach[index * words + value / BITS] >>> (value % BITS) & 1) != 0;
    }
    static boolean pick(int pos, int[] free, int count, long[] reach, int words, int k, int need) {
        if (limited && ++calls > SEARCH_LIMIT)
            return false;
        if (need == 0)
            return fill(pos + 1);
        if (!has(reach, words, k, need))
            return false;
        int last = -1;
        for (int j = k; j < count; j++) {
            int length = ships[free[j]];
            if (length == last || length > need || !has(reach, words, j + 1, need - length))
                continue;
            last = length;
            owner[free[j]] = order[pos];
            if (pick(pos, free, count, reach, words, j + 1, need - length))
                return true;
            owner[free[j]] = -1;
            if (limited && calls > SEARCH_LIMIT)
                return false;
        }
        return false;
    }
    static boolean fill(int pos) {
        int[] free = freeWorkspace[pos];
        int count = 0;
        for (int i = 0; i < n; i++)
            if (owner[i] < 0)
                free[count++] = i;
        if (pos == m - 1) {
            int sum = 0;
            for (int i = 0; i < count; i++)
                sum += ships[free[i]];
            if (sum != rows[order[pos]])
                return false;
            for (int i = 0; i < count; i++)
                owner[free[i]] = order[pos];
            return true;
        }
        int total = 0;
        for (int q = pos; q < m; q++)
            total += rows[order[q]];
        int target = rows[order[pos]];
        for (int q = pos + 1; q < m; q++)
            target = Math.max(target, Math.min(rows[order[q]], total - rows[order[q]]));
        int words = target / BITS + 1, needed = (count + 1) * words;
        long[] reach = workspace[pos];
        if (reach == null || reach.length < needed)
            workspace[pos] = reach = new long[needed];
        else
            for (int i = 0; i < needed; i++)
                reach[i] = 0;
        reach[count * words] = 1;
        for (int k = count - 1; k >= 0; k--) {
            int current = k * words, previous = current + words;
            System.arraycopy(reach, previous, reach, current, words);
            int by = ships[free[k]], whole = by / BITS, bits = by % BITS;
            for (int i = words - 1; i >= whole; i--) {
                long value = reach[previous + i - whole] << bits;
                if (bits != 0 && i - whole > 0)
                    value |= reach[previous + i - whole - 1] >>> (BITS - bits);
                reach[current + i] |= value;
            }
        }
        for (int q = pos; q < m; q++)
            if (!has(reach, words, 0, Math.min(rows[order[q]], total - rows[order[q]])))
                return false;
        return pick(pos, free, count, reach, words, 0, rows[order[pos]]);
    }
    static void sortShips(int[] rank) {
        for (int i = 1; i < n; i++) {
            int value = ships[i], at = i;
            while (at > 0 && rank[ships[at - 1]] > rank[value]) {
                ships[at] = ships[at - 1];
                at--;
            }
            ships[at] = value;
        }
    }
    public static void main(String[] args) throws java.io.IOException {
        n = nextInt();
        m = nextInt();
        ships = new int[n];
        rows = new int[m];
        order = new int[m];
        owner = new int[n];
        workspace = new long[m][];
        freeWorkspace = new int[m][n];
        int[] rank = new int[MAX_SHIP_LENGTH + 1];
        for (int i = 0; i < n; i++) {
            ships[i] = nextInt();
            owner[i] = -1;
        }
        for (int i = 0; i <= MAX_SHIP_LENGTH; i++)
            rank[i] = MAX_SHIP_LENGTH - i;
        sortShips(rank);
        for (int i = 0; i < m; i++) {
            rows[i] = nextInt();
            int at = i;
            while (at > 0 && rows[order[at - 1]] > rows[i]) {
                order[at] = order[at - 1];
                at--;
            }
            order[at] = i;
        }
        int state = 1;
        for (int attempt = 0; attempt <= ATTEMPTS; attempt++) {
            calls = 0;
            limited = attempt < ATTEMPTS;
            if (fill(0))
                break;
            for (int i = m - 1; i > 0; i--) {
                state = (state * RNG_MULTIPLIER + 1) % RNG_MOD;
                int j = state % (i + 1), value = order[i];
                order[i] = order[j];
                order[j] = value;
            }
            for (int i = 0; i <= MAX_SHIP_LENGTH; i++)
                rank[i] = i;
            for (int i = MAX_SHIP_LENGTH; i > 1; i--) {
                state = (state * RNG_MULTIPLIER + 1) % RNG_MOD;
                int j = 1 + state % i, value = rank[i];
                rank[i] = rank[j];
                rank[j] = value;
            }
            sortShips(rank);
        }
        for (int row = 0; row < m; row++) {
            int count = 0;
            for (int i = 0; i < n; i++)
                if (owner[i] == row)
                    count++;
            number(count);
            write('\n');
            boolean first = true;
            for (int i = 0; i < n; i++)
                if (owner[i] == row) {
                    if (!first)
                        write(' ');
                    number(ships[i]);
                    first = false;
                }
            write('\n');
        }
        finish();
    }
}
