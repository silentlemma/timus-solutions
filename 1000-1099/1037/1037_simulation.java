import java.io.DataInputStream;
import java.io.IOException;
import java.util.Arrays;
import java.util.PriorityQueue;

public class Main {
    static final int BLOCKS = 30000, LIFETIME = 600;
    static final int BUFFER = 1 << 16;

    static DataInputStream in = new DataInputStream(System.in);
    static byte[] buf = new byte[BUFFER];
    static int len = 0, pos = 0;

    static int read() throws IOException {
        if (pos == len) {
            len = in.read(buf, 0, BUFFER);
            pos = 0;
            if (len <= 0) {
                return -1;
            }
        }
        return buf[pos++];
    }

    // the next non-blank character, or -1 at the end of the input
    static int skip() throws IOException {
        int c = read();
        while (c == ' ' || c == '\n' || c == '\r' || c == '\t') {
            c = read();
        }
        return c;
    }

    static int number(int c) throws IOException {
        int v = 0;
        while (c >= '0' && c <= '9') {
            v = v * 10 + (c - '0');
            c = read();
        }
        return v;
    }

    public static void main(String[] args) throws IOException {
        // expiry[b]: when block b becomes free, unless it is accessed again
        int[] expiry = new int[BLOCKS + 1];
        boolean[] busy = new boolean[BLOCKS + 1];
        // times never decrease, so the expiries are queued in order; an entry is
        // stale when the block was accessed again later
        int[] queueTime = new int[BUFFER];
        int[] queueBlock = new int[BUFFER];
        int head = 0, tail = 0;
        PriorityQueue<Integer> freed = new PriorityQueue<>();
        int fresh = 1;
        StringBuilder out = new StringBuilder();
        int c;
        while ((c = skip()) != -1) {
            int t = number(c);
            int op = skip();
            while (head < tail && queueTime[head] <= t) {
                int e = queueTime[head], b = queueBlock[head];
                head++;
                if (busy[b] && expiry[b] == e) {
                    busy[b] = false;
                    freed.add(b);
                }
            }
            int b;
            if (op == '+') {
                // freed blocks are all smaller than the never used ones
                b = freed.isEmpty() ? fresh++ : freed.poll();
                out.append(b);
            } else {
                b = number(skip());
                if (!busy[b]) {
                    out.append("-\n");
                    continue;
                }
                out.append('+');
            }
            out.append('\n');
            busy[b] = true;
            expiry[b] = t + LIFETIME;
            if (tail == queueTime.length) {
                queueTime = Arrays.copyOf(queueTime, 2 * tail);
                queueBlock = Arrays.copyOf(queueBlock, 2 * tail);
            }
            queueTime[tail] = expiry[b];
            queueBlock[tail] = b;
            tail++;
        }
        System.out.print(out);
    }
}
