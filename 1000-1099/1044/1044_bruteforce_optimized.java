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

    static final int DIGITS = 10;

    public static void main(String[] args) throws java.io.IOException {
        int n = (int)nextLong();
        int half = n / 2, limit = 1;
        for (int i = 0; i < half; i++) {
            limit *= DIGITS;
        }
        // ways[s]: how many halves (numbers below 10^half) have digit sum s
        long[] ways = new long[(DIGITS - 1) * half + 1];
        for (int x = 0; x < limit; x++) {
            int s = 0;
            for (int y = x; y > 0; y /= DIGITS) {
                s += y % DIGITS;
            }
            ways[s]++;
        }
        // the two halves are chosen independently with the same sum
        long total = 0;
        for (long w : ways) {
            total += w * w;
        }
        System.out.println(total);
    }
}
