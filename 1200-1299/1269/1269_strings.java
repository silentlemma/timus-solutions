import java.io.DataInputStream;
import java.io.IOException;
import java.util.Arrays;

public class Main {
    static final int BUFFER = 1 << 16;
    static final int BYTE = 0xFF; // a byte read as 0 .. 255
    static final int WORDS = 102400; // all words together take at most 100 KB
    static DataInputStream in = new DataInputStream(System.in);
    static byte[] buf = new byte[BUFFER];
    static int bufLen = 0, bufPos = 0;

    // the next byte of the input, or -1 at its end
    static int read() throws IOException {
        if (bufPos == bufLen) {
            bufLen = in.read(buf, 0, BUFFER);
            bufPos = 0;
            if (bufLen <= 0)
                return -1;
        }
        return buf[bufPos++] & BYTE;
    }

    // a number on a line of its own
    static int readLineInt() throws IOException {
        int c = read(), x = 0;
        while (c == ' ')
            c = read();
        for (; c >= '0' && c <= '9'; c = read())
            x = x * 10 + c - '0';
        while (c != '\n' && c != -1)
            c = read();
        return x;
    }

    static int[] first, fail;
    static byte[] label;

    // the child of v along byte c, or -1
    static int walk(int v, int c) {
        for (int u = first[v]; u < first[v + 1]; u++)
            if (label[u] == (byte)c)
                return u;
        return -1;
    }

    public static void main(String[] args) throws IOException {
        int n = readLineInt();
        // build the trie as first-child / next-sibling lists, straight from the
        // bytes of the words; a word ends at a line break, a CR before it is dropped
        int[] child = new int[WORDS + 1], sibling = new int[WORDS + 1], ends = new int[WORDS + 1];
        byte[] chars = new byte[WORDS + 1];
        Arrays.fill(child, -1);
        Arrays.fill(sibling, -1);
        int nodes = 1;
        for (int i = 0; i < n; i++) {
            int v = 0, length = 0;
            for (int c = read(); c != '\n' && c != -1; c = read()) {
                if (c == '\r')
                    continue;
                int u = child[v];
                while (u >= 0 && chars[u] != (byte)c)
                    u = sibling[u];
                if (u < 0) {
                    u = nodes++;
                    chars[u] = (byte)c;
                    sibling[u] = child[v];
                    child[v] = u;
                }
                v = u;
                length++;
            }
            ends[v] = Math.max(ends[v], length);
        }
        // renumber in breadth-first order: the children of v then take the
        // numbers first[v] .. first[v + 1] - 1, and label[u] is the byte leading to u
        first = new int[nodes + 1];
        label = new byte[nodes];
        int[] longest = new int[nodes], old = new int[nodes];
        int size = 1;
        for (int v = 0; v < nodes; v++) {
            first[v] = size;
            for (int u = child[old[v]]; u >= 0; u = sibling[u]) {
                label[size] = chars[u];
                longest[size] = ends[u];
                old[size++] = u;
            }
        }
        first[nodes] = size;
        child = sibling = ends = old = null;
        chars = null;
        // failure links in the same order; a node also takes the longest word
        // of its failure node, which comes earlier
        fail = new int[nodes];
        int widest = 0;
        for (int v = 1; v < nodes; v++)
            for (int u = first[v]; u < first[v + 1]; u++) {
                int f = fail[v], g;
                while ((g = walk(f, label[u])) < 0 && f != 0)
                    f = fail[f];
                fail[u] = Math.max(g, 0);
                longest[u] = Math.max(longest[u], longest[fail[u]]);
                widest = Math.max(widest, longest[u]);
            }
        // the text is read byte by byte and never stored
        int m = readLineInt();
        for (int row = 1; row <= m; row++) {
            int v = 0, best = Integer.MAX_VALUE, i = 0;
            for (int c = read(); c != '\n' && c != -1; c = read()) {
                if (c == '\r')
                    continue;
                int g;
                while ((g = walk(v, c)) < 0 && v != 0)
                    v = fail[v];
                v = Math.max(g, 0);
                if (longest[v] > 0)
                    best = Math.min(best, i + 2 - longest[v]);
                else if (best < Integer.MAX_VALUE && i + 1 - widest >= best)
                    break; // no later match can start earlier
                i++;
            }
            if (best < Integer.MAX_VALUE) {
                System.out.println(row + " " + best);
                return;
            }
        }
        System.out.println("Passed");
    }
}
