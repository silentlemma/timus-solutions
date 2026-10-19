import java.io.IOException;

public class Main {
    private static final int WORD_BITS = Long.SIZE;
    private static final int BUFFER_SIZE = 65536;

    private static final class Input {
        private final byte[] buffer = new byte[BUFFER_SIZE];
        private int position;
        private int size;

        int read() throws IOException {
            if (position == size) {
                size = System.in.read(buffer);
                position = 0;
                if (size == -1) {
                    return -1;
                }
            }
            return buffer[position++];
        }

        int nextNonSpace() throws IOException {
            int value;
            do {
                value = read();
            } while (value <= ' ' && value != -1);
            return value;
        }

        int integer() throws IOException {
            int result = 0;
            int value = nextNonSpace();
            while (value > ' ') {
                result = result * 10 + value - '0';
                value = read();
            }
            return result;
        }

        long[] set(int n, int words) throws IOException {
            long[] mask = new long[words];
            int value = nextNonSpace();
            for (int i = 0; i < n; ++i) {
                if (value == '1') {
                    mask[i / WORD_BITS] |= 1L << (i % WORD_BITS);
                }
                value = read();
            }
            return mask;
        }
    }

    public static void main(String[] args) throws IOException {
        Input input = new Input();
        int n = input.integer();
        int m = input.integer();
        int words = (n + WORD_BITS - 1) / WORD_BITS;
        long[][] required = new long[m][];
        long[][] added = new long[m][];
        for (int rule = 0; rule < m; ++rule) {
            required[rule] = input.set(n, words);
            added[rule] = input.set(n, words);
        }
        long[] owned = input.set(n, words);

        boolean changed = true;
        while (changed) {
            changed = false;
            for (int rule = 0; rule < m; ++rule) {
                boolean ready = true;
                for (int word = 0; word < words; ++word) {
                    if ((required[rule][word] & ~owned[word]) != 0) {
                        ready = false;
                        break;
                    }
                }
                if (ready) {
                    for (int word = 0; word < words; ++word) {
                        long combined = owned[word] | added[rule][word];
                        if (combined != owned[word]) {
                            owned[word] = combined;
                            changed = true;
                        }
                    }
                }
            }
        }

        StringBuilder answer = new StringBuilder(n);
        for (int i = 0; i < n; ++i) {
            answer.append((owned[i / WORD_BITS] & (1L << (i % WORD_BITS))) == 0 ? '0' : '1');
        }
        System.out.println(answer);
    }
}
