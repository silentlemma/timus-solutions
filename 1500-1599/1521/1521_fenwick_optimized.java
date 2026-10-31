import java.io.BufferedOutputStream;
import java.io.IOException;

public class Main {
    // the output buffer is flushed repeatedly; n <= 100000 needs at most six digits.
    private static final int BUFFER_SIZE = 4096;
    private static final int MAX_DIGITS = 10;

    private static int readInt() throws IOException {
        // only n and k are parsed, without scanner allocation.
        int c;
        do {
            c = System.in.read();
        } while (c >= 0 && c <= ' ');
        int value = 0;
        while (c >= '0' && c <= '9') {
            value = value * 10 + c - '0';
            c = System.in.read();
        }
        return value;
    }

    public static void main(String[] args) throws IOException {
        int n = readInt(), k = readInt();
        // a fenwick tree over the circle: 1 for a soldier still marching
        // initially every interval is full, so its count is lowbit(i) <= n <= 100000.
        int[] tree = new int[n + 1];
        for (int i = 1; i <= n; i++) {
            tree[i] = i & -i;
        }
        int top = Integer.highestOneBit(n);
        BufferedOutputStream out = new BufferedOutputStream(System.out, BUFFER_SIZE);
        byte[] digits = new byte[MAX_DIGITS];
        for (int rank = 0, left = n; left > 0; left--) {
            // the soldier k places ahead, counting among those still marching
            rank = (rank + k - 1) % left;
            // descend to the (rank + 1)-th remaining soldier
            int pos = 0, need = rank + 1;
            for (int step = top; step > 0; step /= 2) {
                int next = pos + step;
                if (next <= n) {
                    if (tree[next] < need) {
                        need -= tree[next];
                        pos = next;
                    } else {
                        // this fenwick interval contains the soldier being removed.
                        tree[next]--;
                    }
                }
            }
            int value = pos + 1, start = digits.length;
            do {
                digits[--start] = (byte)('0' + value % 10);
                value /= 10;
            } while (value != 0);
            out.write(digits, start, digits.length - start);
            out.write(left > 1 ? ' ' : '\n');
        }
        out.flush();
    }
}
