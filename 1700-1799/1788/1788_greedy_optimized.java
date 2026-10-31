import java.util.Arrays;

public class Main {

    static final int INPUT_BUFFER = 4096;
    // refill instead of retaining the input; tokens may cross buffer boundaries.
    static final byte[] buffer = new byte[INPUT_BUFFER];
    static int position, size;
    static int read() throws java.io.IOException {
        if (position == size) {
            size = System.in.read(buffer);
            position = 0;
            if (size < 0)
                return -1;
        }
        return buffer[position++];
    }
    static int nextInt() throws java.io.IOException {
        int c = read();
        while (c >= 0 && c != '-' && (c < '0' || c > '9'))
            c = read();
        int sign = 1;
        if (c == '-') {
            sign = -1;
            c = read();
        }
        int value = 0;
        while (c >= '0' && c <= '9') {
            value = value * 10 + c - '0';
            c = read();
        }
        return value * sign;
    }

    static int sum(int[] values, int count) {
        int total = 0;
        for (int i = 0; i < count; i++)
            total += values[i];
        return total;
    }

    public static void main(String[] args) throws java.io.IOException {
        int n = nextInt(), m = nextInt();
        int[] girls = new int[n], boys = new int[m];
        for (int i = 0; i < n; i++)
            girls[i] = nextInt();
        for (int i = 0; i < m; i++)
            boys[i] = nextInt();
        // with k pairs the k most sensitive girls stay dry, and the k most
        // sensitive boys walk with them
        Arrays.sort(girls);
        Arrays.sort(boys);
        int best = Integer.MAX_VALUE;
        for (int k = 0; k <= Math.min(n, m); k++) {
            best = Math.min(best, sum(girls, n - k) + sum(boys, m - k) * k);
        }
        System.out.println(best);
    }
}
