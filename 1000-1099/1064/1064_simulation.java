import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Main {
    static final int MAX_N = 10000;

    // the number of comparisons after which the search over n elements reaches
    // index target, when every other element sends it towards the target
    static int steps(int n, int target) {
        int p = 0, q = n - 1;
        for (int count = 1; p <= q; count++) {
            int i = (p + q) / 2;
            if (i == target) {
                return count;
            }
            if (target < i) {
                q = i - 1;
            } else {
                p = i + 1;
            }
        }
        return 0;
    }

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int target = in.nextInt(), l = in.nextInt();
        // any array whose elements before the target are smaller and after it are
        // larger leads the search there, so only n decides the number of steps
        List<int[]> runs = new ArrayList<>();
        for (int n = target + 1; n <= MAX_N; n++) {
            if (steps(n, target) != l) {
                continue;
            }
            if (!runs.isEmpty() && runs.get(runs.size() - 1)[1] == n - 1) {
                runs.get(runs.size() - 1)[1] = n;
            } else {
                runs.add(new int[] {n, n});
            }
        }
        StringBuilder out = new StringBuilder();
        out.append(runs.size()).append('\n');
        for (int[] r : runs) {
            out.append(r[0]).append(' ').append(r[1]).append('\n');
        }
        System.out.print(out);
    }
}
