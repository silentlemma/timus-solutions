public class Main {
    static final int FIRST_ODD = 3, HIGHER_EXPONENT = 4, DECIMAL_SPACE = 24;
    static long nextLong() throws java.io.IOException {
        int c = System.in.read();
        while (c >= 0 && c <= ' ')
            c = System.in.read();
        boolean negative = c == '-';
        if (negative || c == '+')
            c = System.in.read();
        long value = 0;
        while (c >= '0' && c <= '9') {
            value = value * 10 - (c - '0');
            c = System.in.read();
        }
        return negative ? value : -value;
    }
    static int nextInt() throws java.io.IOException { return (int)nextLong(); }
    static long number() throws java.io.IOException { return nextLong(); }

    static int floorSqrt(long value) {
        long root = (long)Math.sqrt(value);
        while ((root + 1) * (root + 1) <= value)
            root++;
        while (root * root > value)
            root--;
        return (int)root;
    }

    static byte[] sieve(int limit) {
        int oddCount = (limit + 1) / 2;
        byte[] composite = new byte[oddCount];
        composite[0] = 1;
        for (int prime = FIRST_ODD; prime <= limit / prime; prime += 2)
            if (composite[prime / 2] == 0)
                for (int index = prime * prime / 2; index < oddCount; index += prime)
                    composite[index] = 1;
        return composite;
    }
    static int countPrimes(int lower, int upper, byte[] composite) {
        int answer = lower <= 2 && upper >= 2 ? 1 : 0;
        for (int value = Math.max(lower, FIRST_ODD) | 1; value <= upper; value += 2)
            if (composite[value / 2] == 0)
                answer++;
        return answer;
    }

    static boolean primeExponent(int value) {
        if (value < 2)
            return false;
        for (int divisor = 2; divisor <= value / divisor; divisor++)
            if (value % divisor == 0)
                return false;
        return true;
    }

    static long solve(long left, long right) {
        int limit = floorSqrt(right);
        byte[] composite = sieve(limit);
        long bad = countPrimes(floorSqrt(left - 1) + 1, limit, composite);
        int fourthRoot = floorSqrt(limit);
        for (int prime = 2; prime <= fourthRoot; prime += prime == 2 ? 1 : 2) {
            int index = prime >> 1;
            if (prime != 2 && composite[index] != 0)
                continue;
            long square = (long)prime * prime, power = square * square;
            int exponent = HIGHER_EXPONENT;
            while (true) {
                // Odd exponents >=3 have an even composite divisor count.
                if (power >= left && primeExponent(exponent + 1))
                    bad++;
                if (power > right / square)
                    break;
                power *= square;
                exponent += 2;
            }
        }
        return right - left + 1 - bad;
    }

    public static void main(String[] args) throws java.io.IOException {
        long left = number(), right = number(), answer = solve(left, right);
        byte[] output = new byte[DECIMAL_SPACE];
        int at = output.length;
        output[--at] = '\n';
        do {
            output[--at] = (byte)('0' + answer % 10);
            answer /= 10;
        } while (answer != 0);
        System.out.write(output, at, output.length - at);
    }
}
