import java.io.*;

public class Main {
    static final int BASE = 10, DIGITS = 6, MAX_INPUT = 100000, WORD_BITS = 64;

    static final int INPUT_BLOCK = 4096;

    public static void main(String[] args) throws IOException {
        byte[] text = new byte[MAX_INPUT];
        byte[] block = new byte[INPUT_BLOCK];
        int n = 0;
        for (int amount; (amount = System.in.read(block)) > 0;)
            for (int i = 0; i < amount; i++)
                if (block[i] >= '0' && block[i] <= '9')
                    text[n++] = (byte)(block[i] - '0');
        int first = 1;
        // Try lengths in order; the first absent value is the global answer.
        for (int length = 1; length <= DIGITS; length++, first *= BASE) {
            int count = (BASE - 1) * first, modulus = first * BASE, value = 0;
            long[] seen = new long[(count + WORD_BITS - 1) / WORD_BITS];
            for (int i = 0; i < n; i++) {
                value = value * BASE + text[i];
                if (i >= length)
                    value -= text[i - length] * modulus;
                if (i + 1 >= length && value >= first) {
                    int offset = value - first;
                    seen[offset / WORD_BITS] |= 1L << (offset % WORD_BITS);
                }
            }
            for (int offset = 0; offset < count; offset++)
                if ((seen[offset / WORD_BITS] & (1L << (offset % WORD_BITS))) == 0) {
                    System.out.println(first + offset);
                    return;
                }
        }
    }
}
