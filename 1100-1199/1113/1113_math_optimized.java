import java.math.BigInteger;

public class Main {
    static final long SCALE = 20000000;
    static long gcd(long a, long b) {
        while (b != 0) {
            long rest = a % b;
            a = b;
            b = rest;
        }
        return a;
    }
    static long nextLong() throws Exception {
        int c = System.in.read();
        while (c <= ' ')
            c = System.in.read();
        long value = 0;
        while (c >= '0' && c <= '9') {
            value = value * 10 + c - '0';
            c = System.in.read();
        }
        return value;
    }
    static long exactFloor(long load, long stage, long lower) {
        BigInteger num = BigInteger.ZERO, den = BigInteger.ONE;
        long factor = load * (2 * stage - 1);
        for (long i = 1; i < stage; i++) {
            long d = 2 * i - 1, r = factor % d;
            if (r == 0)
                continue;
            long g = gcd(d, den.mod(BigInteger.valueOf(d)).longValue());
            BigInteger scale = BigInteger.valueOf(d / g);
            num = num.multiply(scale).add(
                den.divide(BigInteger.valueOf(g)).multiply(BigInteger.valueOf(r)));
            den = den.multiply(scale);
        }
        // The interval is narrower than one: compare just the next integer.
        return lower + (num.compareTo(den.multiply(BigInteger.valueOf(lower + 1))) >= 0 ? 1 : 0);
    }
    static long lineCeiling(long distance, long load, long stage) {
        long factor = load * (2 * stage - 1),
             whole = (stage - 1) * load + (2 * stage - 1) * distance, lower = 0;
        for (long i = 1; i < stage; i++) {
            long d = 2 * i - 1;
            whole -= factor / d;
            lower += (factor % d) * SCALE / d;
        }
        long floor = lower / SCALE;
        if (stage > 1 && (lower + stage - 2) / SCALE != floor)
            floor = exactFloor(load, stage, floor);
        return whole - floor;
    }
    public static void main(String[] args) throws Exception {
        long distance = nextLong(), load = nextLong(), lower = 0, stage = 1;
        while (lower + load * SCALE / (2 * stage - 1) < distance * SCALE) {
            lower += load * SCALE / (2 * stage - 1);
            stage++;
        }
        // Both adjacent affine ceilings cover the possible one-stage overshoot.
        long answer = lineCeiling(distance, load, stage);
        if (stage > 1)
            answer = Math.max(answer, lineCeiling(distance, load, stage - 1));
        System.out.println(answer);
    }
}
