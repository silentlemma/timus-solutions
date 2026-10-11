import java.io.BufferedOutputStream;
import java.io.IOException;
import java.io.OutputStream;

public class Main {
    static final int LETTERS = 26, ORDER = 3, LENGTH = 1000000;
    static int[] a = new int[LETTERS * ORDER];
    static int[] cycle = new int[LENGTH];
    static int size = 0;

    // A de Bruijn sequence: every word of ORDER letters once around the cycle.
    static void gen(int t, int p) {
        if (t > ORDER) {
            if (ORDER % p == 0) {
                for (int i = 1; i <= p; i++) {
                    cycle[size++] = a[i];
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
        byte[] out = new byte[LENGTH + 1];
        for (int i = 0; i < LENGTH; i++) {
            out[i] = (byte)('a' + cycle[i % size]);
        }
        out[LENGTH] = '\n';
        OutputStream w = new BufferedOutputStream(System.out);
        w.write(out);
        w.flush();
    }
}
