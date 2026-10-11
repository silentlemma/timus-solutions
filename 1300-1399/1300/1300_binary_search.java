import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

public class Main {
    static final long CENTS = 100;
    static final int DIGITS = 2;
    static List<Long> limits = new ArrayList<>(), rates = new ArrayList<>();
    static long topRate, bonusRate;
    static BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer words = new StringTokenizer("");

    static String next() throws IOException {
        while (!words.hasMoreTokens()) {
            String line = in.readLine();
            if (line == null)
                return "-1";
            words = new StringTokenizer(line);
        }
        return words.nextToken();
    }

    // a non-negative amount with at most two decimals, in cents
    static long cents(String token) {
        int dot = token.indexOf('.');
        String whole = dot < 0 ? token : token.substring(0, dot);
        String frac = (dot < 0 ? "" : token.substring(dot + 1)) + "00";
        long w = whole.isEmpty() ? 0 : Long.parseLong(whole);
        return w * CENTS + Long.parseLong(frac.substring(0, DIGITS));
    }

    // rate percent of an amount in cents, rounded half up to a cent
    static long percent(long amount, long rate) { return (amount * rate + CENTS / 2) / CENTS; }

    static long tax(long amount) {
        long raw = 0, previous = 0;
        for (int i = 0; i < limits.size(); i++) {
            long limit = limits.get(i), rate = rates.get(i);
            if (amount <= limit)
                return (raw + (amount - previous) * rate + CENTS / 2) / CENTS;
            raw += (limit - previous) * rate;
            previous = limit;
        }
        return (raw + (amount - previous) * topRate + CENTS / 2) / CENTS;
    }

    static long net(long gross) {
        long bonus = percent(gross, bonusRate);
        return gross - tax(gross) + bonus - tax(bonus);
    }

    // net never decreases as the salary grows, so the largest salary whose
    // net does not exceed the amount paid is found by bisection
    static long grossFor(long amount) {
        long lo = 0, hi = 1;
        while (net(hi) <= amount)
            hi *= 2;
        while (hi - lo > 1) {
            long mid = (lo + hi) / 2;
            if (net(mid) <= amount) {
                lo = mid;
            } else {
                hi = mid;
            }
        }
        return lo;
    }

    public static void main(String[] args) throws IOException {
        bonusRate = Long.parseLong(next());
        while (true) {
            long limit = cents(next()), rate = Long.parseLong(next());
            if (limit == 0) {
                topRate = rate;
                break;
            }
            limits.add(limit);
            rates.add(rate);
        }
        long total = 0, withheld = 0;
        for (String token = next(); !token.equals("-1"); token = next()) {
            long gross = grossFor(cents(token));
            total += gross;
            withheld += tax(gross) + tax(percent(gross, bonusRate));
        }
        long owed = tax(total) + tax(percent(total, bonusRate)) - withheld;
        long size = Math.abs(owed);
        System.out.printf("%s%d.%02d%n", owed < 0 ? "-" : "", size / CENTS, size % CENTS);
    }
}
