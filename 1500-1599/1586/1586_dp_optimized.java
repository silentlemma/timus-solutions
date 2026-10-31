public class Main {

    // a single small integer is read byte by byte; no scanner or buffer is needed.
    static int next() throws java.io.IOException {
        int c = System.in.read();
        while (c != -1 && c <= ' ')
            c = System.in.read();
        int value = 0;
        while (c >= '0' && c <= '9') {
            value = value * 10 + c - '0';
            c = System.in.read();
        }
        return value;
    }

    static final int MOD = 1000000009, LOW = 100, HIGH = 1000, PAIRS = 100, WINDOW = 3;
    public static void main(String[] args) throws java.io.IOException {
        int n = next(), count = 0;
        int[] source = new int[HIGH - LOW], target = new int[HIGH - LOW];
        // ways[t]: numbers of the length so far that end in the two digits t and
        // whose every three neighbouring digits form a three-digit prime
        int[] ways = new int[PAIRS], nextWays = new int[PAIRS];
        for (int p = LOW; p < HIGH; p++) {
            boolean prime = true;
            for (int d = 2; d * d <= p; d++)
                if (p % d == 0) {
                    prime = false;
                    break;
                }
            if (prime) {
                source[count] = p / 10;
                target[count++] = p % PAIRS;
                ways[p % PAIRS]++;
            }
        }
        // reuse two primitive arrays; two residues sum to less than signed int's limit.
        for (int step = WINDOW; step < n; step++) {
            java.util.Arrays.fill(nextWays, 0);
            // a prime abc extends a number ending in ab (source) to one ending in bc (target)
            for (int i = 0; i < count; i++) {
                int value = nextWays[target[i]] + ways[source[i]];
                if (value >= MOD)
                    value -= MOD;
                nextWays[target[i]] = value;
            }
            int[] swap = ways;
            ways = nextWays;
            nextWays = swap;
        }
        int total = 0;
        for (int value : ways) {
            total += value;
            if (total >= MOD)
                total -= MOD;
        }
        System.out.println(total);
    }
}
