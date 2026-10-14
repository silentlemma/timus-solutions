import java.util.*;

public class Main {
    static final long MOD = 1000000009;
    static final int LOW = 100, HIGH = 1000; // the three-digit numbers
    static final int PAIRS = 100;            // the last two digits
    static final int BASE = 10;
    static final int WINDOW = 3; // neighbouring digits that form a prime

    public static void main(String[] args) {
        int n = new Scanner(System.in).nextInt();
        List<Integer> primes = new ArrayList<>();
        for (int p = LOW; p < HIGH; p++) {
            boolean prime = true;
            for (int d = 2; d * d <= p; d++)
                if (p % d == 0)
                    prime = false;
            if (prime)
                primes.add(p);
        }
        // ways[t]: numbers of the length so far that end in the two digits t and
        // whose every three neighbouring digits form a three-digit prime
        long[] ways = new long[PAIRS];
        for (int p : primes)
            ways[p % PAIRS]++;
        for (int step = WINDOW; step < n; step++) {
            long[] next = new long[PAIRS];
            // a prime abc extends a number ending in ab to one ending in bc
            for (int p : primes)
                next[p % PAIRS] = (next[p % PAIRS] + ways[p / BASE]) % MOD;
            ways = next;
        }
        long total = 0;
        for (long w : ways)
            total = (total + w) % MOD;
        System.out.println(total);
    }
}
