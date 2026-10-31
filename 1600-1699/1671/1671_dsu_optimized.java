import java.io.IOException;

public class Main {
    // refillable chunks handle any input length without retaining the whole input.
    private static final int BUFFER_SIZE = 8192;
    private static final byte[] input = new byte[BUFFER_SIZE];
    private static int position, length;
    private static int[] parent, from, to;
    private static int pieces;

    private static int readByte() throws IOException {
        if (position == length) {
            length = System.in.read(input);
            position = 0;
            if (length < 0)
                return -1;
        }
        return input[position++];
    }

    // parse positive decimal tokens directly to avoid scanner allocations.
    private static int nextInt() throws IOException {
        int c;
        do {
            c = readByte();
        } while (c <= ' ' && c != -1);
        int value = 0;
        while (c > ' ') {
            value = value * 10 + c - '0';
            c = readByte();
        }
        return value;
    }

    private static int find(int v) {
        int root = v;
        while (parent[root] >= 0)
            root = parent[root];
        while (v != root) {
            int next = parent[v];
            parent[v] = root;
            v = next;
        }
        return root;
    }

    private static void join(int edge) {
        int a = find(from[edge]), b = find(to[edge]);
        if (a == b)
            return;
        // roots store negative sizes, so the larger tree has the smaller value.
        if (parent[a] > parent[b]) {
            int temp = a;
            a = b;
            b = temp;
        }
        parent[a] += parent[b];
        parent[b] = a;
        pieces--;
    }

    public static void main(String[] args) throws IOException {
        int n = nextInt(), m = nextInt();
        from = new int[m];
        to = new int[m];
        for (int i = 0; i < m; i++) {
            from[i] = nextInt();
            to[i] = nextInt();
        }
        int q = nextInt();
        int[] cuts = new int[q];
        boolean[] cut = new boolean[m];
        for (int i = 0; i < q; i++) {
            cuts[i] = nextInt() - 1;
            cut[cuts[i]] = true;
        }
        parent = new int[n + 1];
        java.util.Arrays.fill(parent, -1);
        pieces = n;
        // run backwards: start from the web after all cuts and put the threads
        // back one by one, last cut first
        for (int i = 0; i < m; i++) {
            if (!cut[i])
                join(i);
        }
        for (int k = q - 1; k >= 0; k--) {
            int edge = cuts[k];
            // the processed cut index is no longer needed, so reuse its slot.
            cuts[k] = pieces;
            join(edge);
        }
        byte[] output = new byte[BUFFER_SIZE];
        // every output is a positive int, so ten decimal digits suffice.
        final int MAX_DIGITS = 10;
        byte[] digits = new byte[MAX_DIGITS];
        int used = 0;
        for (int k = 0; k < q; k++) {
            int value = cuts[k], count = 0;
            do {
                digits[count++] = (byte)('0' + value % 10);
                value /= 10;
            } while (value != 0);
            if (used + count + 1 > output.length) {
                System.out.write(output, 0, used);
                used = 0;
            }
            while (count > 0)
                output[used++] = digits[--count];
            output[used++] = (byte)(k + 1 == q ? '\n' : ' ');
        }
        System.out.write(output, 0, used);
        System.out.flush();
    }
}
