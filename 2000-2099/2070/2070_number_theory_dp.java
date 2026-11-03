import java.io.InputStreamReader;
import java.io.StreamTokenizer;

public class Main {
    static final int FOURTH_ROOT_LIMIT = 1000, FIRST_HIGHER_EXPONENT = 4;

    static int floorSqrt(long value) {
        long root = (long)Math.sqrt(value);
        while ((root + 1) * (root + 1) <= value)
            root++;
        while (root * root > value)
            root--;
        return (int)root;
    }

    static int primeCount(int n) {
        if (n < 2)
            return 0;
        int root = floorSqrt(n);
        int[] small = new int[root + 1], large = new int[root + 1];
        for (int i = 1; i <= root; i++) {
            small[i] = i - 1;
            large[i] = n / i - 1;
        }
        for (int prime = 2; prime <= root; prime++) {
            if (small[prime] == small[prime - 1])
                continue;
            int before = small[prime - 1], square = prime * prime;
            // g(v) counts survivors after smaller primes. Remove multiples
            // whose remaining factor is at least this prime.
            for (int i = 1; i <= Math.min(root, n / square); i++) {
                int reduced = n / i / prime;
                int count = reduced <= root ? small[reduced] : large[n / reduced];
                large[i] -= count - before;
            }
            // Descending values preserve the previous-prime layer.
            for (int value = root; value >= square; value--)
                small[value] -= small[value / prime] - before;
        }
        return large[1];
    }

    public static void main(String[] args) throws Exception {
        StreamTokenizer input = new StreamTokenizer(new InputStreamReader(System.in));
        input.nextToken();
        long left = (long)input.nval;
        input.nextToken();
        long right = (long)input.nval;
        long bad = primeCount(floorSqrt(right)) - primeCount(floorSqrt(left - 1));
        boolean[] composite = new boolean[FOURTH_ROOT_LIMIT + 1];
        composite[0] = composite[1] = true;
        for (int p = 2; p * p <= FOURTH_ROOT_LIMIT; p++)
            if (!composite[p])
                for (int multiple = p * p; multiple <= FOURTH_ROOT_LIMIT; multiple += p)
                    composite[multiple] = true;
        // k+1 prime and k>=2 implies even k. Beyond squares p^4<=R,
        // so a sieve to the fourth root supplies all remaining bases.
        for (int prime = 2; prime <= FOURTH_ROOT_LIMIT; prime++) {
            if (composite[prime])
                continue;
            long square = (long)prime * prime;
            if (square > right / square)
                break;
            long power = square * square;
            int exponent = FIRST_HIGHER_EXPONENT;
            while (true) {
                if (power >= left && !composite[exponent + 1])
                    bad++;
                if (power > right / square)
                    break;
                power *= square;
                exponent += 2;
            }
        }
        System.out.println(right - left + 1 - bad);
    }
}
