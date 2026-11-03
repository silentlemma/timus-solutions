public class Main {
    static int[] parent, size;
    static byte[] parity;
    static final int BUFFER_SIZE = 4096;
    static final byte[] input = new byte[BUFFER_SIZE];
    static int position, available;

    static int read() throws java.io.IOException {
        if (position == available) {
            available = System.in.read(input);
            position = 0;
            if (available < 0)
                return -1;
        }
        return input[position++];
    }

    static int nextInt() throws java.io.IOException {
        int c = read();
        while (c <= ' ')
            c = read();
        int value = 0;
        while (c >= '0' && c <= '9') {
            value = value * 10 + c - '0';
            c = read();
        }
        return value;
    }

    static int find(int v) {
        if (parent[v] != v) {
            int old = parent[v];
            parent[v] = find(old);
            parity[v] ^= parity[old];
        }
        return parent[v];
    }

    public static void main(String[] args) throws Exception {
        int n = nextInt();
        parent = new int[n];
        size = new int[n];
        parity = new byte[n];
        for (int v = 0; v < n; v++) {
            parent[v] = v;
            size[v] = 1;
        }
        // Child/parent color XOR is stored; each edge requires opposite colors.
        for (int a = 0; a < n; a++) {
            int b;
            while ((b = nextInt()) != 0) {
                b--;
                int ra = find(a), rb = find(b);
                if (ra == rb) {
                    if (parity[a] == parity[b]) {
                        System.out.println(-1);
                        return;
                    }
                } else {
                    if (size[ra] < size[rb]) {
                        int tmp = ra;
                        ra = rb;
                        rb = tmp;
                    }
                    parent[rb] = ra;
                    parity[rb] = (byte)(parity[a] ^ parity[b] ^ 1);
                    size[ra] += size[rb];
                }
            }
        }
        find(0);
        int first = parity[0];
        StringBuilder answer = new StringBuilder(n);
        for (int v = 0; v < n; v++) {
            find(v);
            answer.append(parity[v] ^ first);
        }
        System.out.println(answer);
    }
}
