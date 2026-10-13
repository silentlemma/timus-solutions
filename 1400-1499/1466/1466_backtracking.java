import java.util.ArrayList;
import java.util.HashMap;
import java.util.HashSet;
import java.util.List;
import java.util.Map;
import java.util.Scanner;
import java.util.Set;

public class Main {
    static int n;
    static List<int[][]> slots = new ArrayList<>(); // pi and sigma of one number
    static List<int[][]> chosen = new ArrayList<>();
    static List<List<int[][]>> found = new ArrayList<>();
    static List<List<Set<Integer>>> used = new ArrayList<>();

    static List<int[]> permutations(int k) {
        List<int[]> all = new ArrayList<>();
        if (k == 0) {
            all.add(new int[0]);
            return all;
        }
        for (int[] p : permutations(k - 1))
            for (int pos = 0; pos <= p.length; pos++) {
                int[] q = new int[k];
                for (int i = 0, from = 0; i < k; i++)
                    q[i] = i == pos ? k - 1 : p[from++];
                all.add(q);
            }
        return all;
    }

    // The square survives block swaps exactly when each number v sits in row pi_v(J) of
    // every block in column J and column sigma_v(I) of every block in row I, and each pair
    // (I, J) meets all positions (pi_v(J), sigma_v(I)) once; such sets are searched.
    static void grow(int start) {
        if (chosen.size() == n * n) {
            found.add(new ArrayList<>(chosen));
            return;
        }
        for (int k = start; k < slots.size(); k++) {
            int[] x = slots.get(k)[0], y = slots.get(k)[1];
            boolean free = true;
            for (int i = 0; i < n && free; i++)
                for (int j = 0; j < n && free; j++)
                    free = !used.get(i).get(j).contains(x[j] * n + y[i]);
            if (!free)
                continue;
            for (int i = 0; i < n; i++)
                for (int j = 0; j < n; j++)
                    used.get(i).get(j).add(x[j] * n + y[i]);
            chosen.add(slots.get(k));
            grow(k + 1);
            chosen.remove(chosen.size() - 1);
            for (int i = 0; i < n; i++)
                for (int j = 0; j < n; j++)
                    used.get(i).get(j).remove(x[j] * n + y[i]);
        }
    }

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        n = in.nextInt();
        int k = in.nextInt();
        List<int[]> given = new ArrayList<>();
        given.add(new int[] {0, 0, 0}); // the corner holds 0
        for (int i = 0; i < k; i++)
            given.add(new int[] {in.nextInt(), in.nextInt(), in.nextInt()});
        List<int[]> perms = permutations(n);
        for (int[] x : perms)
            for (int[] y : perms)
                slots.add(new int[][] {x, y});
        for (int i = 0; i < n; i++) {
            used.add(new ArrayList<>());
            for (int j = 0; j < n; j++)
                used.get(i).add(new HashSet<>());
        }
        grow(0);
        for (List<int[][]> structure : found) {
            // each given cell pins its number to the one slot that lands there
            Map<Integer, Integer> slotOf = new HashMap<>(), numberOf = new HashMap<>();
            boolean fine = true;
            for (int[] g : given) {
                int j = g[0] / n, c = g[0] % n, i = g[1] / n, r = g[1] % n, v = g[2];
                int s = 0;
                while (structure.get(s)[0][j] != r || structure.get(s)[1][i] != c)
                    s++;
                Integer t = slotOf.get(v), w = numberOf.get(s);
                if ((t != null && t != s) || (w != null && w != v)) {
                    fine = false;
                    break;
                }
                slotOf.put(v, s);
                numberOf.put(s, v);
            }
            if (fine) {
                System.out.println("YES");
                return;
            }
        }
        System.out.println("NO");
    }
}
