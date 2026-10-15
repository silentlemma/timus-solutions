import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.StreamTokenizer;
import java.util.Arrays;

public class Main {
    static final int TOLL = 1000;

    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        StreamTokenizer in = new StreamTokenizer(reader);
        in.nextToken();
        int n = (int) in.nval;
        int[] people = new int[n];
        for (int i = 0; i < n; i++) {
            in.nextToken();
            people[i] = (int) in.nval;
        }
        if (n == 2) {
            System.out.println("1 2");
            return;
        }
        Integer[] order = new Integer[n];
        for (int i = 0; i < n; i++) {
            order[i] = i;
        }
        Arrays.sort(order, (a, b) -> Integer.compare(people[a], people[b]));
        long[] p = new long[n];
        long[] q = new long[n];
        for (int i = 0; i < n; i++) {
            p[i] = people[order[i]];
            q[i] = TOLL / p[i];
        }
        // towns sorted by size: the best tour climbs to the last town on one path
        // and comes back on the other; up[j] costs a climb ending at the newest
        // town and a return ending at town j, down[j] the other way round
        long[] up = new long[n];
        long[] down = new long[n];
        int[] fromDown = new int[n];
        int[] fromUp = new int[n];
        up[0] = q[0] * p[1];
        down[0] = q[1] * p[0];
        long shiftUp = 0;
        long shiftDown = 0;
        for (int m = 1; m < n - 2; m++) {
            int nxt = m + 1;
            int bestUp = 0;
            int bestDown = 0;
            for (int j = 1; j < m; j++) {
                if (down[j] + q[j] * p[nxt] < down[bestUp] + q[bestUp] * p[nxt]) {
                    bestUp = j;
                }
                if (up[j] + q[nxt] * p[j] < up[bestDown] + q[nxt] * p[bestDown]) {
                    bestDown = j;
                }
            }
            long newUp = down[bestUp] + shiftDown + q[bestUp] * p[nxt];
            long newDown = up[bestDown] + shiftUp + q[nxt] * p[bestDown];
            shiftUp += q[m] * p[nxt];
            shiftDown += q[nxt] * p[m];
            up[m] = newUp - shiftUp;
            down[m] = newDown - shiftDown;
            fromDown[m + 1] = bestUp;
            fromUp[m + 1] = bestDown;
        }
        int last = n - 1;
        int m = n - 2;
        boolean climbing = true;
        int j = 0;
        long best = -1;
        for (int k = 0; k < m; k++) {
            long closeUp = up[k] + shiftUp + q[m] * p[last] + q[last] * p[k];
            long closeDown = down[k] + shiftDown + q[k] * p[last] + q[last] * p[m];
            if (best < 0 || closeUp < best) {
                best = closeUp;
                climbing = true;
                j = k;
            }
            if (closeDown < best) {
                best = closeDown;
                climbing = false;
                j = k;
            }
        }
        // walk back: town m is on the climbing path or not, the other path ends at j
        boolean[] onUp = new boolean[n];
        for (; m >= 1; m--) {
            onUp[m] = climbing;
            if (j == m - 1) {
                j = climbing ? fromDown[m] : fromUp[m];
                climbing = !climbing;
            }
        }
        int[] tour = new int[n];
        int size = 0;
        tour[size++] = 0;
        for (int k = 1; k < n - 1; k++) {
            if (onUp[k]) {
                tour[size++] = k;
            }
        }
        tour[size++] = n - 1;
        for (int k = n - 2; k >= 1; k--) {
            if (!onUp[k]) {
                tour[size++] = k;
            }
        }
        int start = 0;
        for (int i = 0; i < n; i++) {
            tour[i] = order[tour[i]];
            if (tour[i] == 0) {
                start = i;
            }
        }
        StringBuilder out = new StringBuilder();
        for (int i = 0; i < n; i++) {
            out.append(tour[(start + i) % n] + 1).append(i + 1 < n ? ' ' : '\n');
        }
        System.out.print(out);
    }
}
