import java.io.IOException;

public class Main {
    static final int BUFFER = 1 << 16;
    static byte[] buffer = new byte[BUFFER];
    static int length = 0, position = 0;
    static int[] likes, partner, chain;
    static boolean[] seen;

    static int read() throws IOException {
        if (position == length) {
            length = System.in.read(buffer, 0, BUFFER);
            position = 0;
            if (length <= 0)
                return -1;
        }
        return buffer[position++];
    }

    static int next() throws IOException {
        int c = read();
        while (c < '0' || c > '9') {
            if (c < 0)
                return 0;
            c = read();
        }
        int value = 0;
        while (c >= '0' && c <= '9') {
            value = value * 10 + (c - '0');
            c = read();
        }
        return value;
    }

    // pair the children along the likes from start, two by two; on an odd
    // path the last one, who likes nobody, stays free
    static void pairAlong(int start) {
        int size = 0;
        for (int v = start; v >= 0 && !seen[v]; v = likes[v]) {
            seen[v] = true;
            chain[size++] = v;
        }
        for (int i = 0; i + 1 < size; i += 2) {
            partner[chain[i]] = chain[i + 1];
            partner[chain[i + 1]] = chain[i];
        }
    }

    public static void main(String[] args) throws IOException {
        int k = next();
        // children 0..k-1 are boys and k..2k-1 girls; likes[v] is the child v
        // likes, or -1; nobody is liked by two, so the likes form paths and cycles
        likes = new int[2 * k];
        partner = new int[2 * k];
        chain = new int[2 * k];
        seen = new boolean[2 * k];
        boolean[] liked = new boolean[2 * k];
        for (int i = 0; i < 2 * k; i++) {
            int x = next();
            likes[i] = x == 0 ? -1 : i < k ? k + x - 1 : x - 1;
            partner[i] = -1;
            if (x != 0)
                liked[likes[i]] = true;
        }
        for (int v = 0; v < 2 * k; v++) {
            if (!liked[v])
                pairAlong(v);
        }
        for (int v = 0; v < 2 * k; v++) {
            if (!seen[v])
                pairAlong(v); // what is left are cycles, always of even length
        }
        // the free children like nobody and can be paired in any way
        int g = k;
        for (int b = 0; b < k; b++) {
            if (partner[b] >= 0)
                continue;
            while (partner[g] >= 0)
                g++;
            partner[b] = g;
            partner[g] = b;
        }
        StringBuilder out = new StringBuilder();
        for (int i = 0; i < k; i++)
            out.append(i > 0 ? " " : "").append(partner[i] - k + 1);
        System.out.println(out);
    }
}
