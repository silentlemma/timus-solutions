import java.math.BigInteger;

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

    static final int THREE = 3, FOUR = 4;

    public static void main(String[] args) throws java.io.IOException {
        int n = next();
        // threes are best: a 4 or more splits into parts with a larger product, and
        // three 2s lose to two 3s; a leftover 1 joins a 3 to make 2 + 2
        if (n < FOUR) {
            System.out.println(n);
            return;
        }
        int threes = n / THREE, rest = n % THREE;
        if (rest == 1) {
            threes--;
            rest = FOUR;
        }
        BigInteger product = BigInteger.valueOf(THREE).pow(threes);
        System.out.println(product.multiply(BigInteger.valueOf(Math.max(rest, 1))));
    }
}
