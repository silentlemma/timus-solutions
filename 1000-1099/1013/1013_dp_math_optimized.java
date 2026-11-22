import java.math.BigInteger;

public class Main {

    static final int BUFFER_SIZE = 1024, BYTE_MASK = 255;
    static final byte[] buffer = new byte[BUFFER_SIZE];
    static int position, available;

    static int read() throws java.io.IOException {
        if (position >= available) {
            available = System.in.read(buffer);
            position = 0;
            if (available <= 0)
                return -1;
        }
        return buffer[position++] & BYTE_MASK;
    }
    static long nextLong() throws java.io.IOException {
        int c = read();
        while (c >= 0 && c <= ' ')
            c = read();
        long value = 0;
        while (c >= '0' && c <= '9') {
            value = value * 10 + c - '0';
            c = read();
        }
        return value;
    }
    static BigInteger modulus, coefficient;

    static BigInteger[] multiply(BigInteger[] x, BigInteger[] y) {
        BigInteger product = x[0].multiply(y[0]);
        BigInteger constant = x[1].multiply(y[1]);
        BigInteger cross =
            x[0].add(x[1]).multiply(y[0].add(y[1])).subtract(product).subtract(constant);
        BigInteger shared = product.mod(modulus).multiply(coefficient);
        // x²=cx+c reduces every polynomial to a*x+b. This composition
        // needs four products and no modular inverses, even for even moduli.
        return new BigInteger[] {shared.add(cross).mod(modulus), shared.add(constant).mod(modulus)};
    }

    public static void main(String[] args) throws Exception {
        long n = nextLong();
        long base = nextLong();
        modulus = BigInteger.valueOf(nextLong());
        coefficient = BigInteger.valueOf(base - 1).mod(modulus);
        BigInteger[] power = {BigInteger.ZERO, BigInteger.ONE};
        BigInteger[] step = {BigInteger.ONE, BigInteger.ZERO};
        while (n > 0) {
            if ((n & 1) != 0)
                power = multiply(power, step);
            step = multiply(step, step);
            n >>= 1;
        }
        // A(0)=1 and A(1)=c, so a*x+b represents a*c+b for this sequence.
        System.out.println(power[0].multiply(coefficient).add(power[1]).mod(modulus));
    }
}
