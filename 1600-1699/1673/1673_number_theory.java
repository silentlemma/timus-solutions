import java.util.ArrayList;
import java.util.Collections;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.Scanner;

public class Main {
    // enough for a deterministic test below 3.2 * 10^9
    static final long[] WITNESSES = {2, 3, 5, 7};
    static final int SHIFT = 32; // a memo key is rest << SHIFT | start

    static List<Long> primes = new ArrayList<>();
    static Map<Long, Long> memo = new HashMap<>();

    static long power(long base, long exp, long mod) {
        long result = 1;
        base %= mod;
        for (; exp > 0; exp >>= 1) {
            if ((exp & 1) == 1) {
                result = result * base % mod;
            }
            base = base * base % mod;
        }
        return result;
    }

    // Miller-Rabin with fixed witnesses, exact for these sizes
    static boolean isPrime(long n) {
        if (n < 2) {
            return false;
        }
        for (long p : WITNESSES) {
            if (n % p == 0) {
                return n == p;
            }
        }
        long d = n - 1;
        int s = 0;
        while (d % 2 == 0) {
            d /= 2;
            s++;
        }
        for (long a : WITNESSES) {
            long x = power(a, d, n);
            if (x == 1 || x == n - 1) {
                continue;
            }
            boolean composite = true;
            for (int i = 1; i < s && composite; i++) {
                x = x * x % n;
                composite = x != n - 1;
            }
            if (composite) {
                return false;
            }
        }
        return true;
    }

    // the smallest product of powers of primes from start on whose totient
    // is rest, or 0 if there is none
    static long least(long rest, int start) {
        if (rest == 1) {
            return 1;
        }
        long key = rest << SHIFT | start;
        Long known = memo.get(key);
        if (known != null) {
            return known;
        }
        long best = 0;
        for (int i = start; i < primes.size() && primes.get(i) - 1 <= rest; i++) {
            long p = primes.get(i);
            if (rest % (p - 1) != 0) {
                continue;
            }
            long part = rest / (p - 1);
            long pw = p;
            while (true) {
                long sub = least(part, i + 1);
                if (sub != 0 && (best == 0 || pw * sub < best)) {
                    best = pw * sub;
                }
                if (part % p != 0) {
                    break;
                }
                part /= p;
                pw *= p;
            }
        }
        memo.put(key, best);
        return best;
    }

    public static void main(String[] args) {
        long k = new Scanner(System.in).nextLong();
        // student j is admitted exactly when gcd(j, N) = 1, so K = phi(N); every
        // p - 1 over the primes of N divides K, so the candidates are d + 1, d | K
        List<Long> divs = new ArrayList<>();
        divs.add(1L);
        long rest = k;
        for (long p = 2; p * p <= rest; p++) {
            if (rest % p == 0) {
                int size = divs.size();
                long pw = 1;
                while (rest % p == 0) {
                    rest /= p;
                    pw *= p;
                    for (int i = 0; i < size; i++) {
                        divs.add(divs.get(i) * pw);
                    }
                }
            }
        }
        if (rest > 1) {
            int size = divs.size();
            for (int i = 0; i < size; i++) {
                divs.add(divs.get(i) * rest);
            }
        }
        Collections.sort(divs);
        for (long d : divs) {
            if (isPrime(d + 1)) {
                primes.add(d + 1);
            }
        }
        System.out.println(least(k, 0));
    }
}
