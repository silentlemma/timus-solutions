public class Main {
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

    public static void main(String[] args) throws Exception {
        int n = nextInt(), m = nextInt();
        int firstV = nextInt(), lastV = firstV, maxV = firstV;
        for (int i = 1; i < n; i++) {
            lastV = nextInt();
            maxV = Math.max(maxV, lastV);
        }
        int firstH = nextInt(), lastH = firstH, maxH = firstH;
        for (int i = 1; i < m; i++) {
            lastH = nextInt();
            maxH = Math.max(maxH, lastH);
        }
        // Both street directions and an incident edge at each endpoint suffice.
        // Their qualifying cross-grid connects the two endpoints.
        System.out.println(Math.min(Math.min(maxV, maxH),
                                    Math.min(Math.max(firstV, firstH), Math.max(lastV, lastH))));
    }
}
