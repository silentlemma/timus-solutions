import java.io.IOException;

public class Main {

    static final int BUFFER_SIZE = 4096, BYTE_MASK = 255;
    static final byte[] buffer = new byte[BUFFER_SIZE];
    static int position, available;

    static int read() throws java.io.IOException {
        if (position == available) {
            available = System.in.read(buffer);
            position = 0;
            if (available < 0)
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
            value = 10 * value + c - '0';
            c = read();
        }
        return value;
    }

    static final int MAX_NAME = 40, LOAD_FACTOR = 2, HASH_MULTIPLIER = 31;
    static final char[] token = new char[MAX_NAME];
    static int tokenLength, tokenHash;
    static char[][] names;
    static int[] ids;
    static int mask;

    static void next() throws IOException {
        int c = read();
        while (c >= 0 && c <= ' ')
            c = read();
        tokenLength = tokenHash = 0;
        while (c > ' ') {
            token[tokenLength++] = (char)c;
            tokenHash = HASH_MULTIPLIER * tokenHash + c;
            c = read();
        }
    }
    static int slot() {
        int index = tokenHash & mask;
        while (names[index] != null) {
            char[] name = names[index];
            int common = 0;
            if (name.length == tokenLength) {
                while (common < tokenLength && name[common] == token[common])
                    common++;
                if (common == tokenLength)
                    break;
            }
            index = (index + 1) & mask;
        }
        return index;
    }
    public static void main(String[] args) throws IOException {
        int n = (int)nextLong();
        int capacity = 1;
        while (capacity < n * LOAD_FACTOR)
            capacity <<= 1;
        names = new char[capacity][];
        ids = new int[capacity];
        mask = capacity - 1;
        int count = 0;
        for (int i = 0; i < n; i++) {
            next();
            int index = slot();
            if (names[index] == null) {
                names[index] = java.util.Arrays.copyOf(token, tokenLength);
                ids[index] = count++;
            }
        }
        int k = (int)nextLong();
        final int WORD_BITS = Long.SIZE;
        int words = (count + WORD_BITS - 1) / WORD_BITS;
        // Only menu products can occur in the meal; all other names are discarded.
        long[][] dangers = new long[k + 1][words];
        for (int i = 0; i <= k; i++) {
            int amount = (int)nextLong();
            for (int j = 0; j < amount; j++) {
                next();
                int index = slot();
                if (names[index] != null) {
                    int id = ids[index];
                    dangers[i][id / WORD_BITS] |= 1L << (id % WORD_BITS);
                }
            }
        }
        int m = (int)nextLong(), safeCount = 0;
        for (int i = 0; i < count; i++)
            if ((dangers[0][i / WORD_BITS] & (1L << (i % WORD_BITS))) == 0)
                safeCount++;
        StringBuilder output = new StringBuilder();
        for (int i = 1; i <= k; i++) {
            int risky = 0;
            for (int word = 0; word < words; word++)
                risky += Long.bitCount(dangers[i][word] & ~dangers[0][word]);
            output.append(m == 0 || risky == 0    ? "YES\n"
                          : safeCount - risky < m ? "NO\n"
                                                  : "MAYBE\n");
        }
        System.out.print(output);
    }
}
