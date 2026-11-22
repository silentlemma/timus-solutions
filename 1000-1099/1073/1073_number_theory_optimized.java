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

    // Lagrange: every number is a sum of four squares, and Legendre: exactly the
    // numbers 4^a (8b + 7) need all four
    static final int MOST = 4;
    static final int POWER = 4;
    static final int MODULUS = 8;
    static final int REST = 7;

    static boolean isSquare(int v) {
        int r = (int)Math.round(Math.sqrt(v));
        return r * r == v;
    }

    static int count(int n) {
        if (isSquare(n)) {
            return 1;
        }

        while (n % POWER == 0)
            n /= POWER;
        if (n % MODULUS == REST)
            return MOST;
        // Removing powers of four preserves the minimum number of squares.
        // A monotone pair scan needs no square root for each candidate.
        int left = 1, right = (int)Math.sqrt(n);
        while (left <= right) {
            int sum = left * left + right * right;
            if (sum == n)
                return 2;
            if (sum < n)
                left++;
            else
                right--;
        }
        return MOST - 1;
    }

    public static void main(String[] args) throws java.io.IOException {
        System.out.println(count(next()));
    }
}
