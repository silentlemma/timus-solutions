public class Main {
    static final int DIGITS = 10;

    public static void main(String[] args) throws Exception {
        long n = 0;
        int ch = System.in.read();
        while (ch <= ' ')
            ch = System.in.read();
        while (ch >= '0' && ch <= '9') {
            n = n * DIGITS + ch - '0';
            ch = System.in.read();
        }
        long[] count = new long[DIGITS];
        for (long place = 1; place <= n; place *= DIGITS) {
            long prefix = n / place, higher = prefix / DIGITS, current = prefix % DIGITS,
                 lower = n % place;
            for (int digit = 1; digit < DIGITS; digit++)
                count[digit] += higher * place + (digit < current    ? place
                                                  : digit == current ? lower + 1
                                                                     : 0);
            // Zero is written only when a nonzero prefix exists.
            if (higher > 0)
                count[0] += (higher - 1) * place + (current > 0 ? place : lower + 1);
        }
        StringBuilder out = new StringBuilder();
        for (long value : count)
            out.append(value).append('\n');
        System.out.print(out);
    }
}
