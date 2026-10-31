public class Main {

    static final int BUFFER_SIZE = 4096;
    static final int BYTE_MASK = 255;
    static final byte[] BUFFER = new byte[BUFFER_SIZE];
    static int position, available;
    // a refillable buffer keeps input memory constant for any number of records.
    static int read() throws java.io.IOException {
        if (position == available) {
            available = System.in.read(BUFFER);
            position = 0;
            if (available < 0)
                return -1;
        }
        return BUFFER[position++] & BYTE_MASK;
    }
    static int nextInt() throws java.io.IOException {
        int c;
        do {
            c = read();
        } while (c <= ' ' && c >= 0);
        int value = 0, sign = 1;
        if (c == '-') {
            sign = -1;
            c = read();
        }
        while (c >= '0' && c <= '9') {
            value = value * 10 + c - '0';
            c = read();
        }
        return sign * value;
    }

    public static void main(String[] args) throws java.io.IOException {
        int m = nextInt();
        int[] left = new int[m], right = new int[m];
        // starts at or below zero share bucket zero; only the farthest end matters.
        // m <= 5000 bounds the bucket count, regardless of the number of intervals.
        while (true) {
            int l = nextInt(), r = nextInt();
            if (l == 0 && r == 0)
                break;
            if (l >= m || r <= 0)
                continue;
            int at = Math.max(0, l);
            if (r > right[at] || (r == right[at] && l < left[at])) {
                left[at] = l;
                right[at] = r;
            }
        }
        int[] chosen = new int[m];
        int count = 0, covered = 0, at = 0;
        while (covered < m) {
            // among the segments that start inside the covered part, take the
            // one that reaches furthest; it is never worse than any other
            int best = -1;
            for (; at < m && at <= covered; ++at)
                if (best < 0 || right[at] > right[best])
                    best = at;
            if (best < 0 || right[best] <= covered) {
                System.out.println("No solution");
                return;
            }
            chosen[count++] = best;
            covered = right[best];
        }
        StringBuilder out = new StringBuilder();
        out.append(count).append('\n');
        for (int i = 0; i < count; ++i) {
            int best = chosen[i];
            out.append(left[best]).append(' ').append(right[best]).append('\n');
        }
        System.out.print(out);
    }
}
