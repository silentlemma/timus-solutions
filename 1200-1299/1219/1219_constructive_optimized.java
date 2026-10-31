import java.io.IOException;

public class Main {
    static final int LETTERS = 26, ORDER = 3, LENGTH = 1000000;
    // one cycle has exactly 26^3 letters; reuse it instead of holding a million bytes.
    static final int CYCLE_LENGTH = LETTERS * LETTERS * LETTERS;
    static int[] a = new int[ORDER + 1];
    static byte[] cycle = new byte[CYCLE_LENGTH];
    static int size = 0;

    // a de bruijn sequence: every word of order letters once around the cycle.
    static void gen(int t, int p) {
        if (t > ORDER) {
            if (ORDER % p == 0) {
                for (int i = 1; i <= p; i++) {
                    cycle[size++] = (byte)('a' + a[i]);
                }
            }
            return;
        }
        a[t] = a[t - p];
        gen(t + 1, p);
        for (int j = a[t - p] + 1; j < LETTERS; j++) {
            a[t] = j;
            gen(t + 1, t);
        }
    }

    public static void main(String[] args) throws IOException {
        gen(1, 1);
        // repeating the cycle keeps every window of three letters a cyclic window
        // of it, so each triple, pair and letter appears almost equally often
        int remaining = LENGTH;
        while (remaining >= size) {
            System.out.write(cycle, 0, size);
            remaining -= size;
        }
        System.out.write(cycle, 0, remaining);
        System.out.write('\n');
        System.out.flush();
    }
}
