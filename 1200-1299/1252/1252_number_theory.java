import java.io.*;
import java.util.*;

public class Main {
    static int gcd(int a, int b) {
        while (b != 0) {
            int t = a % b;
            a = b;
            b = t;
        }
        return a;
    }

    public static void main(String[] args) throws IOException {
        StreamTokenizer st =
            new StreamTokenizer(new BufferedReader(new InputStreamReader(System.in)));
        st.nextToken();
        int n = (int)st.nval;
        // a stone's weight is at most 130000, so pack weight and position
        long[] keyed = new long[n];
        for (int i = 0; i < n; i++) {
            st.nextToken();
            keyed[i] = (long)st.nval * n + i;
        }
        Arrays.sort(keyed);
        // a swap moves a stone K + 1 places, so K + 1 must divide every stone's
        // distance to its place, in one order or the other; all weights differ
        int best = 0;
        for (int down = 0; down < 2; down++) {
            int g = 0;
            for (int place = 0; place < n; place++) {
                int target = down == 1 ? n - 1 - place : place;
                g = gcd(g, Math.abs(target - (int)(keyed[place] % n)));
            }
            best = Math.max(best, g > 0 ? g - 1 : n - 1);
        }
        System.out.println(best);
    }
}
