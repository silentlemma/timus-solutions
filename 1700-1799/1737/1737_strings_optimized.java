import java.io.BufferedOutputStream;

public class Main {
    static final int LIMIT = 100000;
    static final int PERIOD = 3;
    static final int BLOCK_REPEATS = 1024;
    static final int BLOCK_SIZE = PERIOD * BLOCK_REPEATS;
    static final int BUFFER_SIZE = 4096;
    static final byte[] LETTERS = {'a', 'b', 'c'};

    public static void main(String[] args) throws Exception {
        int n = 0, ch = System.in.read();
        while (ch <= ' ')
            ch = System.in.read();
        while (ch >= '0' && ch <= '9') {
            n = n * 10 + ch - '0';
            ch = System.in.read();
        }
        BufferedOutputStream out = new BufferedOutputStream(System.out, BUFFER_SIZE);
        if (n == 1) {
            for (byte letter : LETTERS) {
                out.write(letter);
                out.write('\n');
            }
            out.flush();
            return;
        }
        if (PERIOD * (PERIOD - 1) * n > LIMIT) {
            for (char letter : "TOO LONG\n".toCharArray())
                out.write(letter);
            out.flush();
            return;
        }
        byte[] block = new byte[BLOCK_SIZE];
        for (int first = 0; first < PERIOD; first++)
            for (int second = 0; second < PERIOD; second++)
                if (first != second) {
                    int third = 0;
                    while (third == first || third == second)
                        third++;
                    byte[] pattern = {LETTERS[first], LETTERS[second], LETTERS[third]};
                    for (int i = 0; i < BLOCK_SIZE; i++)
                        block[i] = pattern[i % PERIOD];
                    for (int left = n; left > 0;) {
                        int take = Math.min(left, BLOCK_SIZE);
                        out.write(block, 0, take);
                        left -= take;
                    }
                    out.write('\n');
                }
        out.flush();
    }
}
