public class Main {
    static final int CENTS = 100, DECIMAL_BASE = 10;
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

    static int number() throws Exception {
        int c = read();
        while (c >= 0 && c <= ' ')
            c = read();
        int value = 0;
        while (c > ' ') {
            if (c >= '0' && c <= '9')
                value = value * 10 + c - '0';
            c = read();
        }
        return value;
    }

    public static void main(String[] args) throws Exception {
        int n = number(), k = number(), longest = 0;
        long total = 0;
        int[] cables = new int[n];
        for (int i = 0; i < n; i++) {
            cables[i] = number();
            longest = Math.max(longest, cables[i]);
            total += cables[i];
        }
        int low = longest / k, high = (int)Math.min(longest, total / k);
        // Only whole centimetres are searched; decimal tokens lose their dot.
        while (low < high) {
            int mid = (low + high + 1) / 2;
            long pieces = 0;
            for (int length : cables) {
                pieces += length / mid;
                if (pieces >= k)
                    break;
            }
            if (pieces >= k)
                low = mid;
            else
                high = mid - 1;
        }
        int fraction = low % CENTS;
        System.out.println(low / CENTS + "." + (fraction < DECIMAL_BASE ? "0" : "") + fraction);
    }
}
