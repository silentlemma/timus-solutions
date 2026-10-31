import java.math.BigInteger;

public class Main {

    // these inputs contain only nonnegative integers; avoid scanner's regex machinery.
    static long nextLong() throws java.io.IOException {
        int c;
        do {
            c = System.in.read();
        } while (c >= 0 && c <= ' ');
        long value = 0;
        while (c >= '0' && c <= '9') {
            value = value * 10 + c - '0';
            c = System.in.read();
        }
        return value;
    }

    public static void main(String[] args) throws java.io.IOException {
        int n = (int)nextLong();
        // ordered choices of k different drinks: n (n - 1) ... (n - k + 1), for k from 2,
        // the sum for n = 21 needs more than 64 bits
        BigInteger total = BigInteger.ZERO, ways = BigInteger.valueOf(n);
        for (int k = 2; k <= n; k++) {
            ways = ways.multiply(BigInteger.valueOf(n - k + 1));
            total = total.add(ways);
        }
        System.out.println(total);
    }
}
