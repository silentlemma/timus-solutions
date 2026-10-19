import java.io.BufferedInputStream;
import java.io.IOException;
import java.math.BigInteger;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Comparator;
import java.util.List;

public class Main {
    private static final int LIMIT = 100;
    private static final long MOD = 1000000007L;
    private static final BigInteger MOD_BIG = BigInteger.valueOf(MOD);

    private static class FastInput {
        private final BufferedInputStream input = new BufferedInputStream(System.in);

        int nextInt() throws IOException {
            int next = input.read();
            while (next <= ' ' && next != -1) {
                next = input.read();
            }
            if (next == -1) {
                return -1;
            }
            int value = 0;
            while (next > ' ') {
                value = value * 10 + next - '0';
                next = input.read();
            }
            return value;
        }
    }

    private static class Score {
        final BigInteger exact;
        final long residue;

        Score(BigInteger exact, long residue) {
            this.exact = exact;
            this.residue = residue;
        }
    }

    private static class Event {
        final Score value;
        final int color;
        final int amount;

        Event(Score value, int color, int amount) {
            this.value = value;
            this.color = color;
            this.amount = amount;
        }
    }

    private static Score valueAt(int color, int amount, int wild, int[] cards, int[] hand,
            int deck, int needed, int revealed, Score[][] ways) {
        int held = hand[0] + wild + hand[color] + amount;
        int good = cards[0] + cards[color] - held;
        if (held < needed || good > deck) {
            return new Score(BigInteger.ZERO, 0);
        }
        return ways[good][Math.min(revealed, held - needed)];
    }

    private static long power(long base, long exponent) {
        long result = 1;
        while (exponent > 0) {
            if (exponent % 2 == 1) {
                result = result * base % MOD;
            }
            base = base * base % MOD;
            exponent /= 2;
        }
        return result;
    }

    public static void main(String[] args) throws IOException {
        FastInput input = new FastInput();
        int colors = input.nextInt();
        if (colors == -1) {
            return;
        }
        int drawn = input.nextInt();
        int[] cards = new int[colors + 1];
        int[] hand = new int[colors + 1];
        int[] left = new int[colors + 1];
        for (int color = 0; color <= colors; color++) {
            cards[color] = input.nextInt();
        }
        int total = 0;
        for (int color = 0; color <= colors; color++) {
            hand[color] = input.nextInt();
            left[color] = cards[color] - hand[color];
            total += left[color];
        }
        int needed = input.nextInt();
        int revealed = input.nextInt();
        int deck = total - drawn;

        BigInteger[][] choose = new BigInteger[LIMIT + 1][LIMIT + 1];
        long[][] chooseMod = new long[LIMIT + 1][LIMIT + 1];
        for (int n = 0; n <= LIMIT; n++) {
            Arrays.fill(choose[n], BigInteger.ZERO);
            choose[n][0] = BigInteger.ONE;
            choose[n][n] = BigInteger.ONE;
            chooseMod[n][0] = 1;
            chooseMod[n][n] = 1;
            for (int j = 1; j < n; j++) {
                choose[n][j] = choose[n - 1][j - 1].add(choose[n - 1][j]);
                chooseMod[n][j] = (chooseMod[n - 1][j - 1] + chooseMod[n - 1][j]) % MOD;
            }
        }
        Score[][] ways = new Score[deck + 1][revealed + 1];
        for (int good = 0; good <= deck; good++) {
            BigInteger sum = BigInteger.ZERO;
            for (int bound = 0; bound <= revealed; bound++) {
                int other = revealed - bound;
                if (bound <= good && other <= deck - good) {
                    sum = sum.add(choose[good][bound].multiply(choose[deck - good][other]));
                }
                ways[good][bound] = new Score(sum, sum.mod(MOD_BIG).longValue());
            }
        }

        long answer = 0;
        int firstWild = Math.max(0, drawn - (total - left[0]));
        int lastWild = Math.min(left[0], drawn);
        for (int wild = firstWild; wild <= lastWild; wild++) {
            int remaining = drawn - wild;
            Score baseline = new Score(BigInteger.ZERO, 0);
            for (int color = 1; color <= colors; color++) {
                Score value = valueAt(color, 0, wild, cards, hand, deck, needed, revealed, ways);
                if (value.exact.compareTo(baseline.exact) > 0) {
                    baseline = value;
                }
            }
            List<Event> events = new ArrayList<>();
            for (int color = 1; color <= colors; color++) {
                for (int amount = 1; amount <= Math.min(left[color], remaining); amount++) {
                    Score value = valueAt(color, amount, wild, cards, hand, deck, needed,
                            revealed, ways);
                    if (value.exact.compareTo(baseline.exact) < 0) {
                        value = baseline;
                    }
                    events.add(new Event(value, color, amount));
                }
            }
            events.sort(new Comparator<Event>() {
                @Override
                public int compare(Event a, Event b) {
                    int comparison = a.value.exact.compareTo(b.value.exact);
                    if (comparison != 0) {
                        return comparison;
                    }
                    if (a.color != b.color) {
                        return Integer.compare(a.color, b.color);
                    }
                    return Integer.compare(a.amount, b.amount);
                }
            });

            // Each factor contains the draws admitted for one color so far.
            long[] dp = new long[remaining + 1];
            dp[0] = 1;
            int[] caps = new int[colors + 1];
            long conditional = baseline.residue * dp[remaining] % MOD;
            for (Event event : events) {
                int color = event.color;
                int amount = event.amount;
                long old = dp[remaining];
                long[] quotient = new long[remaining - amount + 1];
                long[] coefficients = chooseMod[left[color]];
                // Formal division removes the old factor, whose constant is one.
                for (int degree = 0; degree < quotient.length; degree++) {
                    long value = dp[degree];
                    for (int j = 1; j <= Math.min(caps[color], degree); j++) {
                        value = (value - coefficients[j] * quotient[degree - j] % MOD + MOD) % MOD;
                    }
                    quotient[degree] = value;
                }
                for (int degree = 0; degree < quotient.length; degree++) {
                    int index = degree + amount;
                    dp[index] = (dp[index] + coefficients[amount] * quotient[degree]) % MOD;
                }
                caps[color] = amount;
                long added = (dp[remaining] - old + MOD) % MOD;
                conditional = (conditional + event.value.residue * added) % MOD;
            }
            answer = (answer + chooseMod[left[0]][wild] * conditional) % MOD;
        }
        long denominator = chooseMod[total][drawn] * chooseMod[deck][revealed] % MOD;
        System.out.println(answer * power(denominator, MOD - 2) % MOD);
    }
}
