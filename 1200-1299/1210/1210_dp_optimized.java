import java.io.IOException;
import java.util.Arrays;

public class Main {

    static final int INPUT_BUFFER = 4096;
    // refill instead of retaining the input; tokens may cross buffer boundaries.
    static final byte[] buffer = new byte[INPUT_BUFFER];
    static int position, size;
    static int read() throws IOException {
        if (position == size) {
            size = System.in.read(buffer);
            position = 0;
            if (size < 0)
                return -1;
        }
        return buffer[position++];
    }
    static int nextInt() throws IOException {
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
    // at most 29 transitions of magnitude 32768 keep finite costs below this sentinel.
    static final int INF = 1000000;
    public static void main(String[] args) throws IOException {
        int levels = nextInt();
        // the cheapest cost of reaching each planet of the current level
        int[] cost = {0};
        for (int level = 0; level < levels; level++) {
            int k = nextInt();
            int[] nxt = new int[k];
            Arrays.fill(nxt, INF);
            for (int planet = 0; planet < k; planet++) {
                for (int src = nextInt(); src != 0; src = nextInt()) {
                    int price = nextInt();
                    if (cost[src - 1] < INF) {
                        nxt[planet] = Math.min(nxt[planet], cost[src - 1] + price);
                    }
                }
            }
            cost = nxt;
        }
        int best = INF;
        for (int value : cost)
            best = Math.min(best, value);
        System.out.println(best);
    }
}
