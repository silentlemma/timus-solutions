import java.io.IOException;

public class Main {
    static final int BASE = 10;

    static long choose(int n, int k) {
        long result = 1;
        for (int i = 1; i <= k; i++) {
            result = result * (n - i + 1) / i;
        }
        return result;
    }

    static long equalSums(int digits) {
        if (digits == 0) {
            return 1;
        }
        int target = (BASE - 1) * digits;
        int variables = 2 * digits;
        long count = 0;
        // Complement the digits of one group, then exclude values outside the digit range.
        for (int excluded = 0; excluded <= target / BASE; excluded++) {
            int sum = target - BASE * excluded;
            long ways = choose(variables, excluded) * choose(sum + variables - 1, variables - 1);
            count += excluded % 2 == 0 ? ways : -ways;
        }
        return count;
    }

    public static void main(String[] args) throws IOException {
        int ch = System.in.read();
        while (ch >= 0 && ch <= ' ') {
            ch = System.in.read();
        }
        int size = 0;
        while (ch >= '0' && ch <= '9') {
            size = size * BASE + ch - '0';
            ch = System.in.read();
        }
        int half = size / 2;
        System.out.println(equalSums(half / 2) * equalSums((half + 1) / 2));
    }
}
