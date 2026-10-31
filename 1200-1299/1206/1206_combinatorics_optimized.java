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

    static final int FIRST = 36, OTHER = 55;

    public static void main(String[] args) throws java.io.IOException {
        int k = (int)nextLong();
        // no position may carry: 36 pairs of leading digits with a sum of at
        // most 9, and 55 pairs of digits from 0 in every other position
        BigInteger count = BigInteger.valueOf(OTHER).pow(k - 1).multiply(BigInteger.valueOf(FIRST));
        System.out.println(count);
    }
}
