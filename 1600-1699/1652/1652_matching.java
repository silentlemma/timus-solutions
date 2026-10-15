import java.io.*;
import java.util.*;

public class Main {
    static final int FIELDS = 3; // creditor, debtor, amount
    static long[][] debts;
    static int[] reach, holder, skip;
    static boolean[] seen;
    static Map<Integer, List<Integer>> own;

    static int unseen(int j) {
        int root = j;
        while (skip[root] != root)
            root = skip[root];
        while (skip[j] != root) {
            int next = skip[j];
            skip[j] = root;
            j = next;
        }
        return root;
    }

    static boolean tryDebt(int j, int b) {
        seen[j] = true;
        skip[j] = j + 1;
        if (holder[j] < 0 || augment(holder[j])) {
            holder[j] = b;
            return true;
        }
        return false;
    }

    static boolean augment(int b) {
        for (int j : own.get(b))
            if (!seen[j] && tryDebt(j, b))
                return true;
        for (int j = unseen(0); j < reach[b]; j = unseen(j + 1))
            if (debts[j][1] != b && tryDebt(j, b)) // a bank cannot hold its own debt
                return true;
        return false;
    }

    static void reset() {
        Arrays.fill(seen, false);
        for (int j = 0; j < skip.length; j++)
            skip[j] = j;
    }

    // a maximum matching of banks to debts of their own country: a bank
    // keeps a debt it already holds or buys one it can afford
    static int mostResponsible(List<Integer> banks, List<long[]> local, long[] money) {
        local.sort(Comparator.comparingLong(d -> d[2]));
        debts = local.toArray(new long[0][]);
        int nd = debts.length;
        own = new HashMap<>();
        for (int b : banks)
            own.put(b, new ArrayList<>());
        for (int j = 0; j < nd; j++) {
            List<Integer> mine = own.get((int)debts[j][0]);
            if (mine != null)
                mine.add(j);
        }
        for (int b : banks) { // the affordable prefix
            int lo = 0, hi = nd;
            while (lo < hi) {
                int mid = (lo + hi) / 2;
                if (debts[mid][2] <= money[b])
                    lo = mid + 1;
                else
                    hi = mid;
            }
            reach[b] = lo;
        }
        holder = new int[nd];
        Arrays.fill(holder, -1);
        seen = new boolean[nd];
        skip = new int[nd + 1];
        reset();
        List<Integer> order = new ArrayList<>(banks);
        // banks that hold a debt already go first, then the poorer ones
        order.sort((a, b) -> {
            boolean ha = !own.get(a).isEmpty(), hb = !own.get(b).isEmpty();
            if (ha != hb)
                return ha ? -1 : 1;
            return Integer.compare(reach[a], reach[b]);
        });
        int count = 0;
        for (int b : order)
            // marks are cleared only after a success: when a search fails the
            // matching stays as it was, so the debts it saw still lead nowhere
            if (augment(b)) {
                count++;
                reset();
            }
        return count;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        StreamTokenizer in = new StreamTokenizer(reader);
        in.nextToken();
        int n = (int)in.nval;
        int[] country = new int[n];
        long[] money = new long[n];
        Map<Integer, List<Integer>> banks = new TreeMap<>();
        for (int b = 0; b < n; b++) {
            in.nextToken();
            country[b] = (int)in.nval;
            in.nextToken();
            money[b] = (long)in.nval;
            banks.computeIfAbsent(country[b], c -> new ArrayList<>()).add(b);
        }
        in.nextToken();
        int m = (int)in.nval;
        Map<Integer, List<long[]>> byCountry = new HashMap<>();
        for (int i = 0; i < m; i++) {
            long[] d = new long[FIELDS];
            for (int f = 0; f < d.length; f++) {
                in.nextToken();
                d[f] = (long)in.nval;
            }
            d[0]--;
            d[1]--;
            byCountry.computeIfAbsent(country[(int)d[1]], c -> new ArrayList<>()).add(d);
        }
        reach = new int[n];
        int total = 0;
        for (Map.Entry<Integer, List<Integer>> e : banks.entrySet())
            total += mostResponsible(e.getValue(),
                byCountry.getOrDefault(e.getKey(), new ArrayList<>()), money);
        System.out.println(total);
    }
}
