public class Main {
    static final int BYTES_PER_SHARE = 4;
    static long nextLong() throws java.io.IOException {
        int c = System.in.read();
        while (c >= 0 && c <= ' ')
            c = System.in.read();
        boolean negative = c == '-';
        if (negative || c == '+')
            c = System.in.read();
        long value = 0;
        while (c >= '0' && c <= '9') {
            value = value * 10 - (c - '0');
            c = System.in.read();
        }
        return negative ? value : -value;
    }
    static int nextInt() throws java.io.IOException { return (int)nextLong(); }
    static final int MONEY = 100;

    // buffered tokens avoid scanner regex initialization and temporary match objects.
    public static void main(String[] args) throws java.io.IOException {
        int n = (int)nextLong();
        int[] bought = new int[n];
        int total = 0;
        for (int i = 0; i < n; i++) {
            bought[i] = (int)nextLong();
            total += bought[i];
        }
        // everybody, Den too, drinks total / (n + 1); in units of 1 / (n + 1)
        // litre, friend i paid for bought[i] (n + 1) - total litres of others
        int all = 0;
        for (int i = 0; i < n; i++) {
            bought[i] = Math.max(0, bought[i] * (n + 1) - total);
            all += bought[i];
        }
        byte[] output = new byte[BYTES_PER_SHARE * n];
        int used = 0;
        for (int i = 0; i < n; i++) {
            int share = MONEY * bought[i] / all;
            if (share == MONEY) {
                output[used++] = '1';
                output[used++] = '0';
                output[used++] = '0';
            } else {
                if (share >= 10)
                    output[used++] = (byte)('0' + share / 10);
                output[used++] = (byte)('0' + share % 10);
            }
            output[used++] = (byte)(i + 1 == n ? '\n' : ' ');
        }
        System.out.write(output, 0, used);
    }
}
