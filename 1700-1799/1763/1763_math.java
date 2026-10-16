import java.util.Scanner;

public class Main {
    static final long MOD = 1000000009L;
    // with six sectors the jumps forward and back by three land on the same
    // sector, so that table is counted on its own
    static final long SIX = 6, SIX_WAYS = 12;
    // from seven sectors on the counts follow a linear recurrence of order 19,
    // found with the Berlekamp-Massey method from counts made by a search over
    // the sectors and checked on every table up to 200 sectors
    static final long FIRST_SECTORS = 7;
    static final String STEP_TEXT = "1 2 -1 1 -2 -1 -2 -3 3 -1 5 2 2 1 -2 0 -3 0 -1";
    static final String FIRST_TEXT = "46 144 110 312 290 670 706 1538 1732 3504 4288 8098 "
            + "10568 19044 26042 45222 64220 108382 158324";
    static long[] steps, first;

    static long[] parse(String text) {
        String[] words = text.trim().split("\\s+");
        long[] values = new long[words.length];
        for (int i = 0; i < words.length; i++) values[i] = Long.parseLong(words[i]);
        return values;
    }

    // the product of two polynomials modulo the recurrence's characteristic
    // polynomial x^k - sum of steps[j] x^(k-1-j)
    static long[] times(long[] p, long[] q) {
        int k = steps.length;
        long[] full = new long[2 * k - 1];
        for (int i = 0; i < k; i++) {
            if (p[i] == 0) continue;
            for (int j = 0; j < k; j++) full[i + j] = (full[i + j] + p[i] * q[j]) % MOD;
        }
        for (int i = 2 * k - 2; i >= k; i--) {
            if (full[i] == 0) continue;
            for (int j = 0; j < k; j++) {
                full[i - 1 - j] = ((full[i - 1 - j] + full[i] * steps[j]) % MOD + MOD) % MOD;
            }
        }
        return java.util.Arrays.copyOf(full, k);
    }

    public static void main(String[] args) {
        long n = new Scanner(System.in).nextLong();
        if (n == SIX) {
            System.out.println(SIX_WAYS);
            return;
        }
        steps = parse(STEP_TEXT);
        first = parse(FIRST_TEXT);
        int k = steps.length;
        // x^(n - 7) reduced by the recurrence gives the count as a mix of the
        // first k counts
        long[] power = new long[k], base = new long[k];
        power[0] = 1;
        base[1] = 1;
        for (long e = n - FIRST_SECTORS; e > 0; e >>= 1) {
            if ((e & 1) == 1) power = times(power, base);
            base = times(base, base);
        }
        long answer = 0;
        for (int i = 0; i < k; i++) answer = (answer + power[i] * first[i]) % MOD;
        System.out.println(answer);
    }
}
