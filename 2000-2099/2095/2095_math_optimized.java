public class Main {
    static final int FIRST = 2;
    static long quiet(long count) {
        long step = FIRST;
        while (count >= step) {
            long quotient = count / step, remainder = count - quotient * step;
            // Every step in this maximal group removes the same quotient.
            long jumps = remainder / (2 * quotient) + 1;
            count -= quotient * jumps;
            step += jumps;
        }
        return count;
    }
    static int nextInt() throws Exception {
        int c = System.in.read();
        while (c <= ' ')
            c = System.in.read();
        int value = 0;
        while (c >= '0' && c <= '9') {
            value = value * 10 + c - '0';
            c = System.in.read();
        }
        return value;
    }
    public static void main(String[] args) throws Exception {
        long left = nextInt(), right = nextInt();
        System.out.println(quiet(right) - quiet(left - 1));
    }
}
