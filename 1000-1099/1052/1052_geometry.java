import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.StreamTokenizer;
import java.util.HashMap;
import java.util.Map;

public class Main {
    // a direction packed into one number; reduced components are below this in size
    static final long SHIFT = 1 << 13;

    static int gcd(int a, int b) {
        a = Math.abs(a);
        b = Math.abs(b);
        while (b != 0) {
            int t = a % b;
            a = b;
            b = t;
        }
        return a;
    }

    public static void main(String[] args) throws IOException {
        StreamTokenizer in =
            new StreamTokenizer(new BufferedReader(new InputStreamReader(System.in)));
        in.nextToken();
        int n = (int)in.nval;
        int[] x = new int[n], y = new int[n];
        for (int i = 0; i < n; i++) {
            in.nextToken();
            x[i] = (int)in.nval;
            in.nextToken();
            y[i] = (int)in.nval;
        }
        int best = Math.min(n, 2);
        for (int i = 0; i < n; i++) {
            // the points on one line through point i have the same reduced direction
            Map<Long, Integer> count = new HashMap<>();
            for (int j = i + 1; j < n; j++) {
                int dx = x[j] - x[i], dy = y[j] - y[i], g = gcd(dx, dy);
                dx /= g;
                dy /= g;
                // opposite directions are the same line
                if (dx < 0 || (dx == 0 && dy < 0)) {
                    dx = -dx;
                    dy = -dy;
                }
                int c = count.merge(dx * SHIFT + dy, 1, Integer::sum);
                best = Math.max(best, c + 1);
            }
        }
        System.out.println(best);
    }
}
